/**
 * DevPrep — Modern Split-Screen IDE Workspace Engine (Cursor / Raycast style)
 * High-Speed Question Explorer + Focus Reader + Interactive MCQ Assessment
 * 100% Real Authentic Data Preserved without alterations.
 */

(function () {
  'use strict';

  // 22 Curriculum Subjects
  const SUBJECTS = [
    'All',
    'HTML',
    'CSS',
    'JavaScript',
    'ES6+',
    'DOM',
    'jQuery',
    'React',
    'Node.js',
    'Express.js',
    'REST API / HTTP',
    'SQL',
    'MongoDB',
    'Aptitude',
    'Logical Reasoning',
    'Problem Solving',
    'DSA',
    'Coding',
    'Git / GitHub',
    'Testing',
    'Web Fundamentals',
    'Project Interview',
    'HR / Communication'
  ];

  // Core Application State
  const state = {
    allQuestions: [],
    filteredQuestions: [],
    selectedIndex: 0,

    // Filters
    selectedSubject: localStorage.getItem('devprep_subject') || 'All',
    selectedDifficulty: 'All',
    selectedStatus: 'All',
    searchQuery: '',

    // Active View Mode: 'solution' or 'quiz'
    viewMode: localStorage.getItem('devprep_mode') || 'solution',

    // Persistent User Assessment Activity
    userAnswers: JSON.parse(localStorage.getItem('fresher_user_answers') || '{}'),
    streak: parseInt(localStorage.getItem('fresher_streak') || '0', 10),
    practicedIds: new Set(JSON.parse(localStorage.getItem('fresher_practiced_ids') || '[]')),
    needPracticeIds: new Set(JSON.parse(localStorage.getItem('fresher_need_practice_ids') || '[]')),
    savedIds: new Set(JSON.parse(localStorage.getItem('fresher_saved_ids') || '[]')),

    // Command Palette
    cmdPaletteOpen: false,
    cmdResults: [],
    cmdHighlightedIdx: 0
  };

  // DOM Elements Cache
  const dom = {};

  function cacheDOMElements() {
    dom.brandReset = document.getElementById('brand-reset');
    dom.btnOpenCmd = document.getElementById('btn-open-cmd');
    dom.hudStreak = document.getElementById('hud-streak');
    dom.hudPracticed = document.getElementById('hud-practiced');
    dom.btnThemeToggle = document.getElementById('btn-theme-toggle');

    // Left Pane (Explorer)
    dom.explorerSearchInput = document.getElementById('explorer-search-input');
    dom.subjectCarouselTrack = document.getElementById('subject-carousel-track');
    dom.selectDifficulty = document.getElementById('select-difficulty');
    dom.selectStatus = document.getElementById('select-status');
    dom.explorerCountBadge = document.getElementById('explorer-count-badge');
    dom.explorerListContainer = document.getElementById('explorer-list-container');

    // Right Pane (Focus Reader)
    dom.focusPane = document.getElementById('focus-pane');
    dom.focusTagSubject = document.getElementById('focus-tag-subject');
    dom.focusTagTopic = document.getElementById('focus-tag-topic');
    dom.focusTagDifficulty = document.getElementById('focus-tag-difficulty');
    dom.focusTagRound = document.getElementById('focus-tag-round');
    dom.btnFocusPractice = document.getElementById('btn-focus-practice');
    dom.btnFocusWeak = document.getElementById('btn-focus-weak');
    dom.btnFocusSave = document.getElementById('btn-focus-save');
    dom.focusQNum = document.getElementById('focus-q-num');
    dom.focusQTitle = document.getElementById('focus-q-title');

    // View Mode Tabs
    dom.btnModeSolution = document.getElementById('btn-mode-solution');
    dom.btnModeQuiz = document.getElementById('btn-mode-quiz');
    dom.solutionViewPanel = document.getElementById('solution-view-panel');
    dom.quizViewPanel = document.getElementById('quiz-view-panel');

    // Solution Elements
    dom.focusAnswerText = document.getElementById('focus-answer-text');
    dom.focusExplWrap = document.getElementById('focus-expl-wrap');
    dom.focusExplText = document.getElementById('focus-expl-text');
    dom.focusCodeWrap = document.getElementById('focus-code-wrap');
    dom.focusCodeText = document.getElementById('focus-code-text');
    dom.btnCodeCopy = document.getElementById('btn-code-copy');
    dom.focusFollowupWrap = document.getElementById('focus-followup-wrap');
    dom.focusFollowupText = document.getElementById('focus-followup-text');
    dom.focusRefWrap = document.getElementById('focus-ref-wrap');
    dom.focusRefText = document.getElementById('focus-ref-text');

    // Quiz Elements
    dom.focusMcqOptions = document.getElementById('focus-mcq-options');
    dom.quizSolutionDrawer = document.getElementById('quiz-solution-drawer');
    dom.quizKeyPill = document.getElementById('quiz-key-pill');
    dom.quizDrawerAnswer = document.getElementById('quiz-drawer-answer');
    dom.quizDrawerExplWrap = document.getElementById('quiz-drawer-expl-wrap');
    dom.quizDrawerExpl = document.getElementById('quiz-drawer-expl');

    // Navigation Buttons
    dom.btnNavPrev = document.getElementById('btn-nav-prev');
    dom.btnNavNext = document.getElementById('btn-nav-next');

    // Command Palette Modal
    dom.cmdModalOverlay = document.getElementById('cmd-modal-overlay');
    dom.cmdPaletteInput = document.getElementById('cmd-palette-input');
    dom.cmdResultsList = document.getElementById('cmd-results-list');

    // Toast
    dom.workspaceToast = document.getElementById('workspace-toast');
  }

  // Toast Notification
  let toastTimer = null;
  function showToast(msg) {
    if (!dom.workspaceToast) return;
    dom.workspaceToast.textContent = msg;
    dom.workspaceToast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      dom.workspaceToast.classList.remove('show');
    }, 2000);
  }

  // Fast String Hash for deterministic options
  function stringHash(str) {
    let hash = 0;
    const s = String(str || '');
    for (let i = 0; i < s.length; i++) {
      hash = ((hash << 5) - hash) + s.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  function getAnswerSummary(text) {
    if (!text) return 'Standard industry convention and best practice.';
    let clean = text.replace(/```[\s\S]*?```/g, '').replace(/`([^`]+)`/g, '$1').trim();
    clean = clean.replace(/^(?:Correct\s+Answer:\s*[A-D]\s*[\r\n]+)/i, '');
    const firstSentence = clean.split(/(?<=[.!?])\s+/)[0].trim();
    if (firstSentence.length > 130) {
      return firstSentence.substring(0, 127) + '...';
    }
    if (firstSentence.length < 15 && clean.length > 20) {
      return clean.substring(0, 120) + '...';
    }
    return firstSentence || clean.substring(0, 100);
  }

  // MCQ Parser & Synthesizer
  const mcqCache = new Map();

  function getMCQData(q) {
    if (mcqCache.has(q.id)) {
      return mcqCache.get(q.id);
    }

    const fullText = (q.question || '') + '\n' + (q.answer || '');

    // Check for explicit options in question or answer
    const corrMatch = fullText.match(/Correct\s*Answer\s*:\s*([A-D])/i) ||
                      fullText.match(/(?:Answer|Option)\s*:\s*([A-D])/i);
    const optsPattern = /A[.)]\s*(.*?)\s*\n\s*B[.)]\s*(.*?)\s*\n\s*C[.)]\s*(.*?)\s*\n\s*D[.)]\s*(.*?)(?=\n\s*(?:Explanation|Source|Note|Key|Correct|$))/s;
    const optsMatch = fullText.match(optsPattern);

    if (optsMatch) {
      const correctLetter = corrMatch ? corrMatch[1].toUpperCase() : 'A';
      const cleanQ = (q.question || '').replace(/A[.)]\s*[\s\S]*$/, '').trim();
      const mcqObj = {
        isExplicit: true,
        displayQuestion: cleanQ || q.question,
        options: {
          A: optsMatch[1].trim(),
          B: optsMatch[2].trim(),
          C: optsMatch[3].trim(),
          D: optsMatch[4].trim()
        },
        correct: correctLetter
      };
      mcqCache.set(q.id, mcqObj);
      return mcqObj;
    }

    // Synthesize 4 plausible options deterministically from questions in same subject
    const subjectPool = state.allQuestions.filter(item => item.subject === q.subject && item.id !== q.id);
    const pool = subjectPool.length >= 6 ? subjectPool : state.allQuestions.filter(item => item.id !== q.id);

    const qHash = stringHash(q.id);
    const letters = ['A', 'B', 'C', 'D'];
    const correctLetter = letters[qHash % 4];

    const distractors = [];
    for (let i = 0; i < pool.length && distractors.length < 3; i++) {
      const candidateIndex = (qHash + (i + 1) * 7) % pool.length;
      const candidate = pool[candidateIndex];
      const summary = getAnswerSummary(candidate.answer);
      if (summary && !distractors.includes(summary) && summary !== getAnswerSummary(q.answer)) {
        distractors.push(summary);
      }
    }

    const fallbacks = [
      'It executes synchronously on the main UI thread without caching.',
      'It creates a mutable singleton reference across all execution contexts.',
      'It is deprecated in the latest ECMAScript / Web standard specifications.',
      'It resets internal pointer state and throws a runtime evaluation error.'
    ];
    while (distractors.length < 3) {
      distractors.push(fallbacks[distractors.length]);
    }

    const options = {};
    let distIdx = 0;
    letters.forEach(letter => {
      if (letter === correctLetter) {
        options[letter] = getAnswerSummary(q.answer);
      } else {
        options[letter] = distractors[distIdx++] || fallbacks[0];
      }
    });

    const mcqObj = {
      isExplicit: false,
      displayQuestion: q.question,
      options: options,
      correct: correctLetter
    };

    mcqCache.set(q.id, mcqObj);
    return mcqObj;
  }

  // Filter Pipeline
  function applyFilters() {
    let result = state.allQuestions.slice();

    // 1. Subject Filter
    if (state.selectedSubject !== 'All') {
      result = result.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }

    // 2. Difficulty Filter
    if (state.selectedDifficulty !== 'All') {
      result = result.filter(q => q.difficulty.toLowerCase() === state.selectedDifficulty.toLowerCase());
    }

    // 3. Status Filter
    if (state.selectedStatus === 'practiced') {
      result = result.filter(q => state.practicedIds.has(q.id));
    } else if (state.selectedStatus === 'weak') {
      result = result.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedStatus === 'saved') {
      result = result.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedStatus === 'unanswered') {
      result = result.filter(q => !state.userAnswers[q.id]);
    }

    // 4. Search Filter
    if (state.searchQuery.trim()) {
      const terms = state.searchQuery.toLowerCase().trim().split(/\s+/);
      result = result.filter(q => {
        const fullContent = [
          q.question,
          q.answer,
          q.shortExplanation || '',
          q.subject,
          q.topic,
          q.subTopic || '',
          q.codeExample || ''
        ].join(' ').toLowerCase();
        return terms.every(term => fullContent.includes(term));
      });
    }

    state.filteredQuestions = result;

    // Reset selected index if out of range
    if (state.selectedIndex >= state.filteredQuestions.length) {
      state.selectedIndex = 0;
    }

    renderExplorerList();
    renderFocusPane();
    updateHUD();
  }

  // Render Left Pane (Question Explorer List)
  function renderExplorerList() {
    if (!dom.explorerListContainer) return;
    dom.explorerListContainer.innerHTML = '';

    const total = state.filteredQuestions.length;
    if (dom.explorerCountBadge) {
      dom.explorerCountBadge.textContent = `${total.toLocaleString()} Qs`;
    }

    if (total === 0) {
      dom.explorerListContainer.innerHTML = `
        <div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 13px;">
          No matching questions.<br>Try relaxing active filters.
        </div>
      `;
      return;
    }

    // Render items
    state.filteredQuestions.forEach((q, idx) => {
      const isSelected = (idx === state.selectedIndex);
      const isPracticed = state.practicedIds.has(q.id);
      const isWeak = state.needPracticeIds.has(q.id);
      const isSaved = state.savedIds.has(q.id);
      const answer = state.userAnswers[q.id];

      const item = document.createElement('div');
      item.className = `explorer-item ${isSelected ? 'active' : ''}`;
      item.setAttribute('data-index', idx);

      let statusIconHtml = '';
      if (answer) {
        statusIconHtml = answer.isCorrect 
          ? '<span class="status-indicator correct" title="Answered correctly">✓</span>' 
          : '<span class="status-indicator incorrect" title="Answered incorrectly">✕</span>';
      } else if (isPracticed) {
        statusIconHtml = '<span class="status-indicator correct" title="Practiced">✓</span>';
      } else if (isWeak) {
        statusIconHtml = '<span class="status-indicator weak" title="Needs Practice">⚠</span>';
      }

      item.innerHTML = `
        <span class="explorer-item-num">${String(idx + 1).padStart(2, '0')}</span>
        <div class="explorer-item-content">
          <div class="explorer-item-title">${escapeHtml(q.question)}</div>
          <div class="explorer-item-meta">
            <span class="mini-badge mini-badge-subject">${escapeHtml(q.subject)}</span>
            <span class="mini-badge">${escapeHtml(q.difficulty)}</span>
            ${isSaved ? '<span style="color:var(--color-purple); font-size:11px;">★</span>' : ''}
            ${statusIconHtml}
          </div>
        </div>
      `;

      item.addEventListener('click', () => {
        state.selectedIndex = idx;
        renderFocusPane();
        updateExplorerActiveState();
      });

      dom.explorerListContainer.appendChild(item);
    });

    scrollActiveItemIntoView();
  }

  function updateExplorerActiveState() {
    if (!dom.explorerListContainer) return;
    const items = dom.explorerListContainer.querySelectorAll('.explorer-item');
    items.forEach((item, idx) => {
      item.classList.toggle('active', idx === state.selectedIndex);
    });
    scrollActiveItemIntoView();
  }

  function scrollActiveItemIntoView() {
    if (!dom.explorerListContainer) return;
    const activeItem = dom.explorerListContainer.querySelector('.explorer-item.active');
    if (activeItem) {
      activeItem.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
  }

  // Render Right Pane (Focus Reader & Quiz Pane)
  function renderFocusPane() {
    if (state.filteredQuestions.length === 0) {
      if (dom.focusQTitle) dom.focusQTitle.textContent = 'No questions match this filter combination.';
      if (dom.focusAnswerText) dom.focusAnswerText.textContent = '';
      return;
    }

    const q = state.filteredQuestions[state.selectedIndex];
    const mcq = getMCQData(q);
    const globalNum = state.selectedIndex + 1;
    const isPracticed = state.practicedIds.has(q.id);
    const isWeak = state.needPracticeIds.has(q.id);
    const isSaved = state.savedIds.has(q.id);

    // 1. Meta Badges
    if (dom.focusTagSubject) dom.focusTagSubject.textContent = q.subject;
    if (dom.focusTagTopic) dom.focusTagTopic.textContent = q.topic;
    if (dom.focusTagDifficulty) {
      dom.focusTagDifficulty.textContent = q.difficulty;
      dom.focusTagDifficulty.className = `badge badge-${q.difficulty.toLowerCase().replace(' ', '-')}`;
    }
    if (dom.focusTagRound) dom.focusTagRound.textContent = q.interviewRound || 'Technical Round';

    // 2. Action Buttons
    if (dom.btnFocusPractice) {
      dom.btnFocusPractice.className = `btn-focus-action ${isPracticed ? 'active-practiced' : ''}`;
      dom.btnFocusPractice.textContent = isPracticed ? '✓ Practiced' : '✓ Mark Practiced';
    }

    if (dom.btnFocusWeak) {
      dom.btnFocusWeak.className = `btn-focus-action ${isWeak ? 'active-weak' : ''}`;
      dom.btnFocusWeak.textContent = isWeak ? '⚠ Flagged Weak' : '⚠ Flag Weak';
    }

    if (dom.btnFocusSave) {
      dom.btnFocusSave.className = `btn-focus-action ${isSaved ? 'active-saved' : ''}`;
      dom.btnFocusSave.textContent = isSaved ? '★ Bookmarked' : '★ Bookmark';
    }

    // 3. Question Title
    if (dom.focusQNum) dom.focusQNum.textContent = `Q${globalNum}.`;
    if (dom.focusQTitle) dom.focusQTitle.textContent = q.question;

    // 4. View Mode Switcher
    if (dom.btnModeSolution && dom.btnModeQuiz) {
      dom.btnModeSolution.classList.toggle('active', state.viewMode === 'solution');
      dom.btnModeQuiz.classList.toggle('active', state.viewMode === 'quiz');
      dom.solutionViewPanel.style.display = (state.viewMode === 'solution') ? 'block' : 'none';
      dom.quizViewPanel.style.display = (state.viewMode === 'quiz') ? 'block' : 'none';
    }

    // 5. Populate Solution View (100% Real Question/Answer Data)
    if (dom.focusAnswerText) dom.focusAnswerText.textContent = q.answer;

    if (q.shortExplanation) {
      dom.focusExplWrap.style.display = 'block';
      dom.focusExplText.textContent = q.shortExplanation;
    } else {
      dom.focusExplWrap.style.display = 'none';
    }

    if (q.codeExample) {
      dom.focusCodeWrap.style.display = 'block';
      dom.focusCodeText.textContent = q.codeExample;
    } else {
      dom.focusCodeWrap.style.display = 'none';
    }

    if (q.followUpQuestions) {
      dom.focusFollowupWrap.style.display = 'block';
      dom.focusFollowupText.textContent = q.followUpQuestions;
    } else {
      dom.focusFollowupWrap.style.display = 'none';
    }

    if (q.references) {
      dom.focusRefWrap.style.display = 'block';
      dom.focusRefText.textContent = q.references;
    } else {
      dom.focusRefWrap.style.display = 'none';
    }

    // 6. Populate Interactive Quiz View
    renderQuizOptions(q, mcq);

    // 7. Navigation Buttons
    if (dom.btnNavPrev) dom.btnNavPrev.disabled = (state.selectedIndex === 0);
    if (dom.btnNavNext) dom.btnNavNext.disabled = (state.selectedIndex === state.filteredQuestions.length - 1);
  }

  // Render MCQ Options for Quiz Mode
  function renderQuizOptions(q, mcq) {
    if (!dom.focusMcqOptions) return;
    dom.focusMcqOptions.innerHTML = '';

    const userAnswer = state.userAnswers[q.id];
    const letters = ['A', 'B', 'C', 'D'];

    letters.forEach(letter => {
      const btn = document.createElement('button');
      btn.className = 'mcq-option-item';
      btn.type = 'button';
      btn.setAttribute('data-option', letter);

      if (userAnswer) {
        if (userAnswer.selected === letter) {
          btn.className += userAnswer.isCorrect ? ' selected-correct' : ' selected-wrong';
        } else if (!userAnswer.isCorrect && letter === mcq.correct) {
          btn.className += ' reveal-correct';
        }
      }

      btn.innerHTML = `
        <span class="mcq-letter-badge">${letter}</span>
        <span class="mcq-option-text">${escapeHtml(mcq.options[letter])}</span>
      `;

      btn.addEventListener('click', () => {
        handleOptionSelect(q, letter);
      });

      dom.focusMcqOptions.appendChild(btn);
    });

    // Quiz Solution Drawer
    if (dom.quizSolutionDrawer) {
      if (userAnswer) {
        dom.quizSolutionDrawer.style.display = 'block';
        if (dom.quizKeyPill) dom.quizKeyPill.textContent = `🔑 Verified Answer Key: Option ${mcq.correct}`;
        if (dom.quizDrawerAnswer) dom.quizDrawerAnswer.textContent = q.answer;
        if (q.shortExplanation) {
          dom.quizDrawerExplWrap.style.display = 'block';
          dom.quizDrawerExpl.textContent = q.shortExplanation;
        } else {
          dom.quizDrawerExplWrap.style.display = 'none';
        }
      } else {
        dom.quizSolutionDrawer.style.display = 'none';
      }
    }
  }

  // Handle MCQ Option Selection
  function handleOptionSelect(q, chosenLetter) {
    const mcq = getMCQData(q);
    const isCorrect = (chosenLetter === mcq.correct);

    state.userAnswers[q.id] = {
      selected: chosenLetter,
      isCorrect: isCorrect,
      timestamp: Date.now()
    };
    localStorage.setItem('fresher_user_answers', JSON.stringify(state.userAnswers));

    if (isCorrect) {
      state.streak++;
      state.practicedIds.add(q.id);
      state.needPracticeIds.delete(q.id);
      showToast(`✓ Correct! Streak: 🔥 ${state.streak}`);
    } else {
      state.streak = 0;
      state.needPracticeIds.add(q.id);
      state.practicedIds.delete(q.id);
      showToast(`✕ Incorrect. Correct answer is Option ${mcq.correct}`);
    }

    localStorage.setItem('fresher_streak', state.streak);
    localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
    localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));

    renderFocusPane();
    renderExplorerList();
    updateHUD();
  }

  // Next / Previous Navigation
  function nextQuestion() {
    if (state.selectedIndex < state.filteredQuestions.length - 1) {
      state.selectedIndex++;
      renderFocusPane();
      updateExplorerActiveState();
    } else {
      showToast('You are on the last question in this list.');
    }
  }

  function prevQuestion() {
    if (state.selectedIndex > 0) {
      state.selectedIndex--;
      renderFocusPane();
      updateExplorerActiveState();
    }
  }

  // Update Top Bar HUD Counters
  function updateHUD() {
    if (dom.hudStreak) dom.hudStreak.textContent = `🔥 ${state.streak}`;
    if (dom.hudPracticed) dom.hudPracticed.textContent = state.practicedIds.size.toLocaleString();
  }

  // Render 22 Subject Carousel Track in Explorer Header
  function renderSubjectCarousel() {
    if (!dom.subjectCarouselTrack) return;
    dom.subjectCarouselTrack.innerHTML = '';

    SUBJECTS.forEach(sub => {
      const count = (sub === 'All') 
        ? state.allQuestions.length 
        : state.allQuestions.filter(q => q.subject === sub).length;

      const chip = document.createElement('button');
      chip.className = `subject-chip ${sub === state.selectedSubject ? 'active' : ''}`;
      chip.type = 'button';
      chip.textContent = `${sub} (${count})`;

      chip.addEventListener('click', () => {
        state.selectedSubject = sub;
        localStorage.setItem('devprep_subject', sub);

        // Update active chip classes
        dom.subjectCarouselTrack.querySelectorAll('.subject-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');

        state.selectedIndex = 0;
        applyFilters();
      });

      dom.subjectCarouselTrack.appendChild(chip);
    });
  }

  // Command Palette (Ctrl+K)
  function openCmdPalette() {
    if (!dom.cmdModalOverlay) return;
    state.cmdPaletteOpen = true;
    dom.cmdModalOverlay.classList.add('open');
    if (dom.cmdPaletteInput) {
      dom.cmdPaletteInput.value = '';
      dom.cmdPaletteInput.focus();
    }
    renderCmdResults('');
  }

  function closeCmdPalette() {
    if (!dom.cmdModalOverlay) return;
    state.cmdPaletteOpen = false;
    dom.cmdModalOverlay.classList.remove('open');
  }

  function renderCmdResults(query) {
    if (!dom.cmdResultsList) return;
    dom.cmdResultsList.innerHTML = '';

    const clean = query.toLowerCase().trim();
    let matches = [];

    if (!clean) {
      // Default: show current 20 questions
      matches = state.allQuestions.slice(0, 20);
    } else {
      const terms = clean.split(/\s+/);
      matches = state.allQuestions.filter(q => {
        const str = `${q.question} ${q.subject} ${q.topic} ${q.answer}`.toLowerCase();
        return terms.every(term => str.includes(term));
      }).slice(0, 30);
    }

    state.cmdResults = matches;
    state.cmdHighlightedIdx = 0;

    if (matches.length === 0) {
      dom.cmdResultsList.innerHTML = '<div style="padding: 16px; text-align: center; color: var(--text-muted); font-size: 13.5px;">No questions found matching your search.</div>';
      return;
    }

    matches.forEach((q, idx) => {
      const item = document.createElement('div');
      item.className = `cmd-result-item ${idx === 0 ? 'highlighted' : ''}`;
      item.setAttribute('data-index', idx);

      item.innerHTML = `
        <div style="flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; margin-right:12px;">
          <strong>Q${q.num || idx + 1}.</strong> ${escapeHtml(q.question)}
        </div>
        <span class="mini-badge mini-badge-subject">${escapeHtml(q.subject)}</span>
      `;

      item.addEventListener('click', () => {
        jumpToQuestionFromCmd(q);
      });

      dom.cmdResultsList.appendChild(item);
    });
  }

  function jumpToQuestionFromCmd(q) {
    closeCmdPalette();

    // Reset subject filter if question is outside current subject
    if (state.selectedSubject !== 'All' && q.subject !== state.selectedSubject) {
      state.selectedSubject = 'All';
      if (dom.subjectCarouselTrack) {
        dom.subjectCarouselTrack.querySelectorAll('.subject-chip').forEach(c => {
          c.classList.toggle('active', c.textContent.startsWith('All'));
        });
      }
    }

    state.searchQuery = '';
    if (dom.explorerSearchInput) dom.explorerSearchInput.value = '';

    applyFilters();

    const targetIdx = state.filteredQuestions.findIndex(item => item.id === q.id);
    if (targetIdx !== -1) {
      state.selectedIndex = targetIdx;
      renderFocusPane();
      updateExplorerActiveState();
    }
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // 1. Search with Debounce
    let searchTimer = null;
    if (dom.explorerSearchInput) {
      dom.explorerSearchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => {
          state.searchQuery = e.target.value;
          state.selectedIndex = 0;
          applyFilters();
        }, 120);
      });
    }

    // 2. Select Filters
    if (dom.selectDifficulty) {
      dom.selectDifficulty.addEventListener('change', (e) => {
        state.selectedDifficulty = e.target.value;
        state.selectedIndex = 0;
        applyFilters();
      });
    }

    if (dom.selectStatus) {
      dom.selectStatus.addEventListener('change', (e) => {
        state.selectedStatus = e.target.value;
        state.selectedIndex = 0;
        applyFilters();
      });
    }

    // 3. View Mode Switcher
    if (dom.btnModeSolution) {
      dom.btnModeSolution.addEventListener('click', () => {
        state.viewMode = 'solution';
        localStorage.setItem('devprep_mode', 'solution');
        renderFocusPane();
      });
    }

    if (dom.btnModeQuiz) {
      dom.btnModeQuiz.addEventListener('click', () => {
        state.viewMode = 'quiz';
        localStorage.setItem('devprep_mode', 'quiz');
        renderFocusPane();
      });
    }

    // 4. Action Buttons (Practiced, Weak, Save)
    if (dom.btnFocusPractice) {
      dom.btnFocusPractice.addEventListener('click', () => {
        const q = state.filteredQuestions[state.selectedIndex];
        if (!q) return;
        if (state.practicedIds.has(q.id)) {
          state.practicedIds.delete(q.id);
          showToast('Unmarked question');
        } else {
          state.practicedIds.add(q.id);
          state.needPracticeIds.delete(q.id);
          showToast('✓ Marked Practiced');
        }
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        renderFocusPane();
        renderExplorerList();
        updateHUD();
      });
    }

    if (dom.btnFocusWeak) {
      dom.btnFocusWeak.addEventListener('click', () => {
        const q = state.filteredQuestions[state.selectedIndex];
        if (!q) return;
        if (state.needPracticeIds.has(q.id)) {
          state.needPracticeIds.delete(q.id);
          showToast('Removed from Weak Areas');
        } else {
          state.needPracticeIds.add(q.id);
          state.practicedIds.delete(q.id);
          showToast('⚠ Flagged as Weak Area');
        }
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        renderFocusPane();
        renderExplorerList();
        updateHUD();
      });
    }

    if (dom.btnFocusSave) {
      dom.btnFocusSave.addEventListener('click', () => {
        const q = state.filteredQuestions[state.selectedIndex];
        if (!q) return;
        if (state.savedIds.has(q.id)) {
          state.savedIds.delete(q.id);
          showToast('Removed from Bookmarks');
        } else {
          state.savedIds.add(q.id);
          showToast('★ Saved to Bookmarks');
        }
        localStorage.setItem('fresher_saved_ids', JSON.stringify(Array.from(state.savedIds)));
        renderFocusPane();
        renderExplorerList();
      });
    }

    // 5. Copy Code
    if (dom.btnCodeCopy) {
      dom.btnCodeCopy.addEventListener('click', () => {
        const q = state.filteredQuestions[state.selectedIndex];
        if (q?.codeExample) {
          navigator.clipboard.writeText(q.codeExample).then(() => {
            dom.btnCodeCopy.textContent = '✓ Copied';
            setTimeout(() => { dom.btnCodeCopy.textContent = 'Copy'; }, 1500);
          });
        }
      });
    }

    // 6. Navigation Buttons
    if (dom.btnNavPrev) dom.btnNavPrev.addEventListener('click', prevQuestion);
    if (dom.btnNavNext) dom.btnNavNext.addEventListener('click', nextQuestion);

    // 7. Command Palette Open / Close
    if (dom.btnOpenCmd) dom.btnOpenCmd.addEventListener('click', openCmdPalette);

    if (dom.cmdModalOverlay) {
      dom.cmdModalOverlay.addEventListener('click', (e) => {
        if (e.target === dom.cmdModalOverlay) closeCmdPalette();
      });
    }

    if (dom.cmdPaletteInput) {
      let cmdTimer = null;
      dom.cmdPaletteInput.addEventListener('input', (e) => {
        clearTimeout(cmdTimer);
        cmdTimer = setTimeout(() => {
          renderCmdResults(e.target.value);
        }, 100);
      });

      dom.cmdPaletteInput.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (state.cmdHighlightedIdx < state.cmdResults.length - 1) {
            state.cmdHighlightedIdx++;
            updateCmdHighlighted();
          }
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (state.cmdHighlightedIdx > 0) {
            state.cmdHighlightedIdx--;
            updateCmdHighlighted();
          }
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (state.cmdResults[state.cmdHighlightedIdx]) {
            jumpToQuestionFromCmd(state.cmdResults[state.cmdHighlightedIdx]);
          }
        }
      });
    }

    function updateCmdHighlighted() {
      if (!dom.cmdResultsList) return;
      const items = dom.cmdResultsList.querySelectorAll('.cmd-result-item');
      items.forEach((item, idx) => {
        item.classList.toggle('highlighted', idx === state.cmdHighlightedIdx);
        if (idx === state.cmdHighlightedIdx) {
          item.scrollIntoView({ block: 'nearest' });
        }
      });
    }

    // 8. Theme Switcher
    if (dom.btnThemeToggle) {
      dom.btnThemeToggle.addEventListener('click', () => {
        const curr = document.documentElement.getAttribute('data-theme') || 'light';
        const next = curr === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', next);
        dom.btnThemeToggle.textContent = next === 'light' ? '🌙' : '☀️';
        localStorage.setItem('fresher_theme', next);
      });
    }

    if (dom.brandReset) {
      dom.brandReset.addEventListener('click', (e) => {
        e.preventDefault();
        state.selectedSubject = 'All';
        state.searchQuery = '';
        state.selectedIndex = 0;
        if (dom.explorerSearchInput) dom.explorerSearchInput.value = '';
        renderSubjectCarousel();
        applyFilters();
      });
    }

    // 9. Keyboard Shortcuts: J / K, 1-4, Ctrl+K
    window.addEventListener('keydown', (e) => {
      // Command Palette Trigger: Ctrl+K or Cmd+K
      if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        if (state.cmdPaletteOpen) closeCmdPalette();
        else openCmdPalette();
        return;
      }

      // Escape key closes modals
      if (e.key === 'Escape') {
        if (state.cmdPaletteOpen) {
          closeCmdPalette();
          return;
        }
      }

      // If typing in input, ignore single-letter shortcuts
      if (document.activeElement === dom.explorerSearchInput || document.activeElement === dom.cmdPaletteInput) {
        return;
      }

      // J / Down: Next question
      if (e.key === 'j' || e.key === 'J' || e.key === 'ArrowDown') {
        e.preventDefault();
        nextQuestion();
        return;
      }

      // K / Up: Previous question
      if (e.key === 'k' || e.key === 'K' || e.key === 'ArrowUp') {
        e.preventDefault();
        prevQuestion();
        return;
      }

      // M: Toggle Solution View vs Quiz View
      if (e.key === 'm' || e.key === 'M') {
        state.viewMode = state.viewMode === 'solution' ? 'quiz' : 'solution';
        localStorage.setItem('devprep_mode', state.viewMode);
        renderFocusPane();
        showToast(`Switched to ${state.viewMode === 'quiz' ? 'Quiz Assessment View' : 'Solution View'}`);
        return;
      }

      // S: Toggle Bookmark
      if (e.key === 's' || e.key === 'S') {
        if (dom.btnFocusSave) dom.btnFocusSave.click();
        return;
      }

      // W: Toggle Weak Flag
      if (e.key === 'w' || e.key === 'W') {
        if (dom.btnFocusWeak) dom.btnFocusWeak.click();
        return;
      }

      // Option selection in Quiz Mode: 1/A, 2/B, 3/C, 4/D
      if (state.viewMode === 'quiz') {
        const q = state.filteredQuestions[state.selectedIndex];
        if (q) {
          if (e.key === '1' || e.key === 'a' || e.key === 'A') handleOptionSelect(q, 'A');
          else if (e.key === '2' || e.key === 'b' || e.key === 'B') handleOptionSelect(q, 'B');
          else if (e.key === '3' || e.key === 'c' || e.key === 'C') handleOptionSelect(q, 'C');
          else if (e.key === '4' || e.key === 'd' || e.key === 'D') handleOptionSelect(q, 'D');
        }
      }
    });
  }

  // HTML Escape Utility
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Initialization
  function init() {
    cacheDOMElements();

    const rawData = window.FRESHER_QUESTIONS_DATA || window.FRESHER_QUESTIONS;
    if (rawData && Array.isArray(rawData)) {
      state.allQuestions = rawData;
    } else {
      console.error('FRESHER_QUESTIONS_DATA not loaded.');
      return;
    }

    // Apply stored theme
    const storedTheme = localStorage.getItem('fresher_theme') || 'light';
    document.documentElement.setAttribute('data-theme', storedTheme);
    if (dom.btnThemeToggle) {
      dom.btnThemeToggle.textContent = storedTheme === 'light' ? '🌙' : '☀️';
    }

    renderSubjectCarousel();
    setupEventListeners();
    applyFilters();
    updateHUD();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
