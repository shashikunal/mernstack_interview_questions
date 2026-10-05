/**
 * DevPrep — Modern Split-Screen IDE Workspace Engine (Cursor / Raycast style)
 * High-Speed Question Explorer + Focus Reader + Interactive MCQ Assessment
 * 100% Real Authentic Data Preserved without alterations.
 */

(function () {
  'use strict';

  // Curriculum Subjects (Featured AI Module + 22 Full-Stack Subjects)
  const SUBJECTS = [
    'All',
    'AI & Generative AI',
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

    // Filters (Default to AI & Generative AI Module)
    selectedSubject: localStorage.getItem('devprep_subject') || 'AI & Generative AI',
    selectedTopic: 'All',
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

    // Curriculum Module Switcher Tabs (AI vs Full-Stack)
    dom.tabCurriculumAi = document.getElementById('tab-curriculum-ai');
    dom.tabCurriculumFullstack = document.getElementById('tab-curriculum-fullstack');

    // Left Pane (Explorer)
    dom.selectSubject = document.getElementById('select-subject');
    dom.selectTopic = document.getElementById('select-topic');
    dom.explorerSearchInput = document.getElementById('explorer-search-input');
    dom.explorerSearchClear = document.getElementById('explorer-search-clear');
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
    dom.btnModeCourse = document.getElementById('btn-mode-course');
    dom.btnModeVideos = document.getElementById('btn-mode-videos');
    dom.btnModePrompts = document.getElementById('btn-mode-prompts');
    dom.solutionViewPanel = document.getElementById('solution-view-panel');
    dom.quizViewPanel = document.getElementById('quiz-view-panel');
    dom.courseViewPanel = document.getElementById('course-view-panel');
    dom.videosViewPanel = document.getElementById('videos-view-panel');
    dom.promptsViewPanel = document.getElementById('prompts-view-panel');

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

    // 2. Topic Filter
    if (state.selectedTopic !== 'All') {
      const targetTopic = state.selectedTopic.toLowerCase();
      result = result.filter(q => {
        const t = (q.topic || '').toLowerCase();
        const st = (q.subTopic || '').toLowerCase();
        return t === targetTopic || st === targetTopic;
      });
    }

    // 3. Difficulty Filter
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
    const isSolution = (state.viewMode === 'solution');
    const isQuiz = (state.viewMode === 'quiz');
    const isCourse = (state.viewMode === 'course');
    const isVideos = (state.viewMode === 'videos');
    const isPrompts = (state.viewMode === 'prompts');

    if (dom.btnModeSolution) dom.btnModeSolution.classList.toggle('active', isSolution);
    if (dom.btnModeQuiz) dom.btnModeQuiz.classList.toggle('active', isQuiz);
    if (dom.btnModeCourse) dom.btnModeCourse.classList.toggle('active', isCourse);
    if (dom.btnModeVideos) dom.btnModeVideos.classList.toggle('active', isVideos);
    if (dom.btnModePrompts) dom.btnModePrompts.classList.toggle('active', isPrompts);

    if (dom.solutionViewPanel) dom.solutionViewPanel.style.display = isSolution ? 'block' : 'none';
    if (dom.quizViewPanel) dom.quizViewPanel.style.display = isQuiz ? 'block' : 'none';
    if (dom.courseViewPanel) dom.courseViewPanel.style.display = isCourse ? 'flex' : 'none';
    if (dom.videosViewPanel) dom.videosViewPanel.style.display = isVideos ? 'flex' : 'none';
    if (dom.promptsViewPanel) dom.promptsViewPanel.style.display = isPrompts ? 'flex' : 'none';

    if (isCourse) {
      renderCoursePanel();
      return;
    }
    if (isVideos) {
      renderVideosPanel();
      return;
    }
    if (isPrompts) {
      renderPromptsPanel();
      return;
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
        if (dom.quizKeyPill) dom.quizKeyPill.textContent = `✅ Correct Answer: Option ${mcq.correct}`;
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

  // =========================================================================
  // VIBE CODING STUDIO: 28-Step Course, 14 Videos, 12 Prompt Exercises
  // =========================================================================

  let activeCourseStepFilter = 'All';

  function renderCoursePanel() {
    if (!dom.courseViewPanel) return;
    const courseData = window.AI_VIBE_COURSE_DATA;
    if (!courseData || !courseData.steps) {
      dom.courseViewPanel.innerHTML = '<div style="padding:20px; color:var(--text-muted);">Course data loading...</div>';
      return;
    }

    const steps = courseData.steps;
    let filteredSteps = steps;
    if (activeCourseStepFilter === 'fund') {
      filteredSteps = steps.filter(s => s.stepNumber >= 1 && s.stepNumber <= 3);
    } else if (activeCourseStepFilter === 'vibe') {
      filteredSteps = steps.filter(s => s.stepNumber >= 4 && s.stepNumber <= 9);
    } else if (activeCourseStepFilter === 'stack') {
      filteredSteps = steps.filter(s => s.stepNumber >= 10 && s.stepNumber <= 13);
    } else if (activeCourseStepFilter === 'rag') {
      filteredSteps = steps.filter(s => s.stepNumber >= 14 && s.stepNumber <= 19);
    } else if (activeCourseStepFilter === 'projects') {
      filteredSteps = steps.filter(s => s.stepNumber >= 20 && s.stepNumber <= 26);
    } else if (activeCourseStepFilter === 'practice') {
      filteredSteps = steps.filter(s => s.stepNumber >= 27 && s.stepNumber <= 28);
    }

    let html = `
      <div class="vibe-hero-banner">
        <div class="vibe-hero-badge">🗺️ STEP-BY-STEP ROADMAP</div>
        <div class="vibe-hero-title">28-Step Guide to Modern AI Coding</div>
        <p style="color:var(--text-secondary); font-size:13.5px; line-height:1.6; margin-bottom:12px;">
          A simple, easy-to-follow path from basic concepts to building real web projects with AI tools.
        </p>
        <div class="vibe-hero-philosophy">
          <span>Your Simple Learning Flow:</span>
          <span class="philosophy-step">1. Learn Concept</span> <span class="philosophy-arrow">→</span>
          <span class="philosophy-step">2. Try with AI</span> <span class="philosophy-arrow">→</span>
          <span class="philosophy-step">3. Build Project</span> <span class="philosophy-arrow">→</span>
          <span class="philosophy-step">4. Test Code</span> <span class="philosophy-arrow">→</span>
          <span class="philosophy-step">5. Ace Interview</span>
        </div>
      </div>

      <div class="vibe-filter-bar">
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'All' ? 'active' : ''}" data-stepfilter="All">All 28 Steps</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'fund' ? 'active' : ''}" data-stepfilter="fund">Steps 1–3: Basics &amp; Tools</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'vibe' ? 'active' : ''}" data-stepfilter="vibe">Steps 4–9: AI Coding &amp; Prompts</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'stack' ? 'active' : ''}" data-stepfilter="stack">Steps 10–13: Connecting Full-Stack</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'rag' ? 'active' : ''}" data-stepfilter="rag">Steps 14–19: RAG &amp; AI Agents</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'projects' ? 'active' : ''}" data-stepfilter="projects">Steps 20–26: Real Projects &amp; Security</button>
        <button class="vibe-filter-pill ${activeCourseStepFilter === 'practice' ? 'active' : ''}" data-stepfilter="practice">Steps 27–28: Videos &amp; Exercises</button>
      </div>

      <div class="vibe-steps-container" style="display:flex; flex-direction:column; gap:22px;">
    `;

    filteredSteps.forEach(step => {
      let workflowHtml = '';
      if (step.workflow) {
        workflowHtml = `
          <div class="vibe-workflow-box">
            <div style="font-size:11px; text-transform:uppercase; color:#94a3b8; margin-bottom:6px; font-weight:700;">Workflow Diagram:</div>
            <pre><code>${escapeHtml(step.workflow)}</code></pre>
          </div>
        `;
      }

      let activityHtml = '';
      if (step.studentActivity) {
        activityHtml = `
          <div class="vibe-activity-box">
            <div class="vibe-activity-title">🛠️ Student Hands-On Activity: ${escapeHtml(step.studentActivity.title)}</div>
            <p style="font-size:13.5px; margin-bottom:10px;">${escapeHtml(step.studentActivity.task)}</p>
            <button class="vibe-model-solution-toggle" type="button" data-step-id="${step.id}">💡 Show Model Solution &amp; Checklist</button>
            <div class="vibe-model-solution-content" id="solution-${step.id}">
              <div style="font-weight:600; color:var(--accent-primary); margin-bottom:6px;">Model Approach:</div>
              <p style="margin-bottom:8px;">${escapeHtml(step.studentActivity.modelSolution || '')}</p>
              ${step.studentActivity.checklist ? `
                <div style="font-weight:600; color:var(--text-primary); margin-top:8px; margin-bottom:4px;">Verification Checklist:</div>
                <ul style="padding-left:18px; margin:0;">
                  ${step.studentActivity.checklist.map(c => `<li>✓ ${escapeHtml(c)}</li>`).join('')}
                </ul>
              ` : ''}
            </div>
          </div>
        `;
      }

      let projectRulesHtml = '';
      if (step.projectRules) {
        projectRulesHtml = `
          <div class="vibe-workflow-box" style="margin-top:14px;">
            <div style="font-size:11px; text-transform:uppercase; color:#38bdf8; margin-bottom:6px; font-weight:700;">Enterprise PROJECT_RULES.md Blueprint:</div>
            <pre><code>${escapeHtml(step.projectRules)}</code></pre>
          </div>
        `;
      }

      let architectureHtml = '';
      if (step.architecture) {
        architectureHtml = `
          <div class="vibe-workflow-box" style="margin-top:14px;">
            <div style="font-size:11px; text-transform:uppercase; color:#a78bfa; margin-bottom:6px; font-weight:700;">System Architecture Blueprint:</div>
            <pre><code>${escapeHtml(step.architecture)}</code></pre>
          </div>
        `;
      }

      let itemsHtml = '';
      if (step.items && step.items.length) {
        itemsHtml = `
          <ul style="padding-left:20px; margin:12px 0;">
            ${step.items.map(it => `<li>${escapeHtml(it)}</li>`).join('')}
          </ul>
        `;
      }

      html += `
        <article class="vibe-step-card" id="step-card-${step.stepNumber}">
          <div class="vibe-step-header">
            <div>
              <span class="vibe-step-num-pill">STEP ${step.stepNumber} OF 28</span>
              <h2 class="vibe-step-title">${escapeHtml(step.title)}</h2>
            </div>
            <span class="badge badge-subject">Practical Module</span>
          </div>

          <div class="vibe-step-body">
            <p>${escapeHtml(step.description || '')}</p>
            ${itemsHtml}
            ${workflowHtml}
            ${projectRulesHtml}
            ${architectureHtml}
            ${activityHtml}
          </div>
        </article>
      `;
    });

    html += `</div>`;
    dom.courseViewPanel.innerHTML = html;

    // Attach event listeners for step category filter pills
    dom.courseViewPanel.querySelectorAll('.vibe-filter-pill').forEach(btn => {
      btn.addEventListener('click', (e) => {
        activeCourseStepFilter = e.target.getAttribute('data-stepfilter');
        renderCoursePanel();
      });
    });

    // Attach toggle listeners for student activity model solutions
    dom.courseViewPanel.querySelectorAll('.vibe-model-solution-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const stepId = btn.getAttribute('data-step-id');
        const content = dom.courseViewPanel.querySelector(`#solution-${stepId}`);
        if (content) {
          const isOpen = content.classList.toggle('open');
          btn.textContent = isOpen ? '✕ Hide Model Solution' : '💡 Show Model Solution & Checklist';
        }
      });
    });
  }

  function renderVideosPanel() {
    if (!dom.videosViewPanel) return;
    const courseData = window.AI_VIBE_COURSE_DATA;
    if (!courseData || !courseData.videos) {
      dom.videosViewPanel.innerHTML = '<div style="padding:20px; color:var(--text-muted);">Video lessons loading...</div>';
      return;
    }

    let html = `
      <div class="vibe-hero-banner">
        <div class="vibe-hero-badge">🎬 14 VIDEO LESSONS</div>
        <div class="vibe-hero-title">Watch &amp; Learn: AI Coding Videos</div>
        <p style="color:var(--text-secondary); font-size:13.5px; line-height:1.6; margin-bottom:0;">
          Simple, step-by-step video lessons showing how to code with Cursor, Copilot, and Claude. Click any lesson to watch inline or in theater view.
        </p>
      </div>

      <div class="vibe-video-grid">
    `;

    courseData.videos.forEach(vid => {
      const ytId = vid.youtubeId || '68H2u-rT1_k';
      const thumbUrl = vid.thumbnailUrl || `https://img.youtube.com/vi/${ytId}/hqdefault.jpg`;
      const watchUrl = vid.videoUrl || `https://www.youtube.com/watch?v=${ytId}`;
      const questions = Array.isArray(vid.interviewQuestions)
        ? vid.interviewQuestions
        : (vid.interviewQuestion ? [vid.interviewQuestion] : []);

      html += `
        <div class="vibe-video-card" id="card-${escapeHtml(vid.id)}">
          <!-- Video Player Container (Thumbnail or Live Iframe) -->
          <div class="vibe-video-player-container" id="player-container-${escapeHtml(vid.id)}" data-ytid="${escapeHtml(ytId)}" data-title="${escapeHtml(vid.title)}">
            <div class="vibe-video-thumb-screen" data-vid-id="${escapeHtml(vid.id)}" style="background-image: linear-gradient(180deg, rgba(15,23,42,0.35) 0%, rgba(15,23,42,0.85) 100%), url('${thumbUrl}');">
              <div class="vibe-video-badge-pill">${escapeHtml(vid.duration || '15 mins')} • ${escapeHtml(vid.difficulty || 'All Levels')}</div>
              <button class="vibe-video-play-btn" aria-label="Play ${escapeHtml(vid.title)}" title="Play Video Lesson">
                <span class="vibe-play-icon">▶</span>
              </button>
              <div class="vibe-play-hint">Click to Play Lesson</div>
            </div>
          </div>

          <!-- Video Action Bar -->
          <div class="vibe-video-action-bar">
            <button class="btn-video-act btn-video-play-inline" data-vid-id="${escapeHtml(vid.id)}" title="Play video right here">
              ▶ Play Inline
            </button>
            <button class="btn-video-act btn-video-theater" data-vid-id="${escapeHtml(vid.id)}" title="Open large theater studio player">
              ⛶ Theater View
            </button>
            <a href="${escapeHtml(watchUrl)}" target="_blank" rel="noopener noreferrer" class="btn-video-act btn-video-yt" title="Open directly on YouTube">
              ↗ YouTube
            </a>
          </div>

          <h3 class="vibe-video-title">${escapeHtml(vid.title)}</h3>
          <p class="vibe-video-desc">${escapeHtml(vid.objective || '')}</p>

          <div style="margin-bottom:12px;">
            <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); margin-bottom:4px;">Demonstration:</div>
            <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.5;">${escapeHtml(vid.demonstration || '')}</div>
          </div>

          ${vid.promptUsed ? `
            <div class="vibe-video-prompt-box">
              <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap; margin-right:8px;" title="${escapeHtml(vid.promptUsed)}">${escapeHtml(vid.promptUsed)}</span>
              <button class="btn-copy-prompt" style="background:var(--accent-primary); color:#ffffff; border:none; padding:4px 8px; border-radius:4px; font-size:11px; cursor:pointer;" data-prompt="${escapeHtml(vid.promptUsed)}">Copy Prompt</button>
            </div>
          ` : ''}

          ${vid.exercise ? `
            <div class="vibe-video-exercise-box">
              <strong>Student Exercise:</strong> ${escapeHtml(vid.exercise)}
            </div>
          ` : ''}

          ${questions.length > 0 ? `
            <div class="vibe-video-questions-box">
              <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); margin-bottom:6px;">Target Interview Questions:</div>
              <ul style="margin:0; padding-left:18px; font-size:12.5px; color:var(--text-secondary);">
                ${questions.map(q => `<li style="margin-bottom:4px;">${escapeHtml(q)}</li>`).join('')}
              </ul>
            </div>
          ` : ''}
        </div>
      `;
    });

    html += `</div>`;
    dom.videosViewPanel.innerHTML = html;

    // Attach click handlers
    attachVideoPanelEvents(courseData.videos);
  }

  function attachVideoPanelEvents(videos) {
    if (!dom.videosViewPanel) return;

    // 1. Copy Prompt buttons
    dom.videosViewPanel.querySelectorAll('.btn-copy-prompt').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const text = btn.getAttribute('data-prompt');
        if (text && navigator.clipboard) {
          navigator.clipboard.writeText(text);
          showToast('Prompt copied to clipboard!');
        }
      });
    });

    // 2. Play Inline via thumbnail click
    dom.videosViewPanel.querySelectorAll('.vibe-video-thumb-screen').forEach(thumb => {
      thumb.addEventListener('click', () => {
        const vidId = thumb.getAttribute('data-vid-id');
        const videoObj = videos.find(v => v.id === vidId);
        if (videoObj) playVideoInline(videoObj, videos);
      });
    });

    // 3. Play Inline via button
    dom.videosViewPanel.querySelectorAll('.btn-video-play-inline').forEach(btn => {
      btn.addEventListener('click', () => {
        const vidId = btn.getAttribute('data-vid-id');
        const videoObj = videos.find(v => v.id === vidId);
        if (videoObj) playVideoInline(videoObj, videos);
      });
    });

    // 4. Theater modal view
    dom.videosViewPanel.querySelectorAll('.btn-video-theater').forEach(btn => {
      btn.addEventListener('click', () => {
        const vidId = btn.getAttribute('data-vid-id');
        const videoObj = videos.find(v => v.id === vidId);
        if (videoObj) openVideoTheaterModal(videoObj);
      });
    });
  }

  function playVideoInline(videoObj, allVideos) {
    const container = document.getElementById(`player-container-${videoObj.id}`);
    if (!container) return;
    const ytId = videoObj.youtubeId || '68H2u-rT1_k';
    const watchUrl = videoObj.videoUrl || `https://www.youtube.com/watch?v=${ytId}`;

    container.innerHTML = `
      <div class="vibe-inline-player-wrapper">
        <div class="vibe-inline-top-bar">
          <span class="vibe-inline-title" title="${escapeHtml(videoObj.title)}">▶ ${escapeHtml(videoObj.title)}</span>
          <div style="display:flex; gap:6px; align-items:center;">
            <button class="btn-inline-theater" data-vid-id="${escapeHtml(videoObj.id)}" title="Switch to theater modal">⛶ Theater</button>
            <a href="${escapeHtml(watchUrl)}" target="_blank" rel="noopener noreferrer" class="btn-inline-yt" title="Open directly on YouTube">↗ YouTube</a>
            <button class="btn-inline-close" data-vid-id="${escapeHtml(videoObj.id)}" title="Close video player">✕ Close</button>
          </div>
        </div>
        <div class="vibe-inline-iframe-box">
          <iframe 
            class="vibe-video-iframe"
            src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(ytId)}?autoplay=1&rel=0&enablejsapi=1" 
            title="${escapeHtml(videoObj.title)}"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        </div>
      </div>
    `;

    container.querySelector('.btn-inline-close')?.addEventListener('click', (e) => {
      e.stopPropagation();
      restoreVideoThumbnail(videoObj, allVideos);
    });

    container.querySelector('.btn-inline-theater')?.addEventListener('click', (e) => {
      e.stopPropagation();
      openVideoTheaterModal(videoObj);
    });
  }

  function restoreVideoThumbnail(videoObj, allVideos) {
    const container = document.getElementById(`player-container-${videoObj.id}`);
    if (!container) return;
    const ytId = videoObj.youtubeId || '68H2u-rT1_k';
    const thumbUrl = videoObj.thumbnailUrl || `https://img.youtube.com/vi/${ytId}/hqdefault.jpg`;

    container.innerHTML = `
      <div class="vibe-video-thumb-screen" data-vid-id="${escapeHtml(videoObj.id)}" style="background-image: linear-gradient(180deg, rgba(15,23,42,0.35) 0%, rgba(15,23,42,0.85) 100%), url('${thumbUrl}');">
        <div class="vibe-video-badge-pill">${escapeHtml(videoObj.duration || '15 mins')} • ${escapeHtml(videoObj.difficulty || 'All Levels')}</div>
        <button class="vibe-video-play-btn" aria-label="Play ${escapeHtml(videoObj.title)}" title="Play Video Lesson">
          <span class="vibe-play-icon">▶</span>
        </button>
        <div class="vibe-play-hint">Click to Play Lesson</div>
      </div>
    `;

    container.querySelector('.vibe-video-thumb-screen')?.addEventListener('click', () => {
      playVideoInline(videoObj, allVideos);
    });
  }

  function openVideoTheaterModal(videoObj) {
    let modalOverlay = document.getElementById('video-theater-overlay');
    if (!modalOverlay) {
      modalOverlay = document.createElement('div');
      modalOverlay.id = 'video-theater-overlay';
      modalOverlay.className = 'vibe-theater-overlay';
      document.body.appendChild(modalOverlay);
    }

    const ytId = videoObj.youtubeId || '68H2u-rT1_k';
    const watchUrl = videoObj.videoUrl || `https://www.youtube.com/watch?v=${ytId}`;
    const questions = Array.isArray(videoObj.interviewQuestions)
      ? videoObj.interviewQuestions
      : (videoObj.interviewQuestion ? [videoObj.interviewQuestion] : []);

    modalOverlay.innerHTML = `
      <div class="vibe-theater-box" role="dialog" aria-modal="true" aria-labelledby="theater-title">
        <div class="vibe-theater-header">
          <div style="display:flex; align-items:center; gap:10px;">
            <span class="vibe-hero-badge" style="margin-bottom:0;">🎬 VIDEO MASTERCLASS</span>
            <span style="font-size:12px; color:var(--text-muted);">${escapeHtml(videoObj.duration || '15 mins')} • ${escapeHtml(videoObj.difficulty || 'All Levels')}</span>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <a href="${escapeHtml(watchUrl)}" target="_blank" rel="noopener noreferrer" class="btn-theater-yt" title="Open directly on YouTube">
              ↗ Watch on YouTube
            </a>
            <button id="btn-close-theater" class="btn-theater-close" title="Close theater (Esc)">✕</button>
          </div>
        </div>

        <div class="vibe-theater-player-wrap">
          <iframe 
            class="vibe-theater-iframe"
            src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(ytId)}?autoplay=1&rel=0&enablejsapi=1" 
            title="${escapeHtml(videoObj.title)}"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        </div>

        <div class="vibe-theater-info">
          <h2 id="theater-title" class="vibe-theater-title">${escapeHtml(videoObj.title)}</h2>
          <p class="vibe-theater-desc">${escapeHtml(videoObj.objective || '')}</p>

          <div class="vibe-theater-section">
            <h4 style="margin:0 0 6px 0; font-size:12.5px; text-transform:uppercase; color:var(--accent-primary); letter-spacing:0.5px;">Demonstration Walkthrough</h4>
            <p style="font-size:13.5px; color:var(--text-secondary); line-height:1.6; margin:0;">${escapeHtml(videoObj.demonstration || '')}</p>
          </div>

          ${videoObj.promptUsed ? `
            <div class="vibe-theater-section">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h4 style="margin:0; font-size:12.5px; text-transform:uppercase; color:var(--accent-primary); letter-spacing:0.5px;">Production Prompt</h4>
                <button id="theater-copy-prompt" class="btn-copy-prompt" style="background:var(--accent-primary); color:#ffffff; border:none; padding:4px 10px; border-radius:4px; font-size:11.5px; cursor:pointer;" data-prompt="${escapeHtml(videoObj.promptUsed)}">📋 Copy Prompt</button>
              </div>
              <div style="background:var(--bg-hover); padding:10px 14px; border-radius:6px; font-family:var(--font-mono); font-size:12px; border:1px solid var(--border-color); color:var(--text-primary); line-height:1.5;">
                ${escapeHtml(videoObj.promptUsed)}
              </div>
            </div>
          ` : ''}

          ${videoObj.exercise ? `
            <div class="vibe-theater-section">
              <h4 style="margin:0 0 6px 0; font-size:12.5px; text-transform:uppercase; color:var(--accent-primary); letter-spacing:0.5px;">Hands-On Exercise</h4>
              <div style="background:rgba(37,99,235,0.05); border:1px dashed var(--accent-border); border-radius:6px; padding:10px 14px; font-size:13px; color:var(--text-primary); line-height:1.5;">
                ${escapeHtml(videoObj.exercise)}
              </div>
            </div>
          ` : ''}

          ${questions.length > 0 ? `
            <div class="vibe-theater-section">
              <h4 style="margin:0 0 8px 0; font-size:12.5px; text-transform:uppercase; color:var(--accent-primary); letter-spacing:0.5px;">Target Interview Questions</h4>
              <ul style="margin:0; padding-left:20px; font-size:13px; color:var(--text-secondary); line-height:1.6;">
                ${questions.map(q => `<li style="margin-bottom:6px;"><strong>${escapeHtml(q)}</strong></li>`).join('')}
              </ul>
            </div>
          ` : ''}
        </div>
      </div>
    `;

    modalOverlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    // Close Handler
    const closeHandler = () => {
      modalOverlay.style.display = 'none';
      modalOverlay.innerHTML = '';
      document.body.style.overflow = '';
      document.removeEventListener('keydown', escHandler);
    };

    const escHandler = (e) => {
      if (e.key === 'Escape') closeHandler();
    };

    document.getElementById('btn-close-theater')?.addEventListener('click', closeHandler);
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeHandler();
    });
    document.addEventListener('keydown', escHandler);

    document.getElementById('theater-copy-prompt')?.addEventListener('click', () => {
      if (videoObj.promptUsed && navigator.clipboard) {
        navigator.clipboard.writeText(videoObj.promptUsed);
        showToast('Prompt copied to clipboard!');
      }
    });
  }

  function renderPromptsPanel() {
    if (!dom.promptsViewPanel) return;
    const courseData = window.AI_VIBE_COURSE_DATA;
    if (!courseData || !courseData.promptExercises) {
      dom.promptsViewPanel.innerHTML = '<div style="padding:20px; color:var(--text-muted);">Prompt exercises loading...</div>';
      return;
    }

    let html = `
      <div class="vibe-hero-banner">
        <div class="vibe-hero-badge">💡 PRACTICE PROMPTS</div>
        <div class="vibe-hero-title">12 Simple Examples: How to Write Better Prompts</div>
        <p style="color:var(--text-secondary); font-size:13.5px; line-height:1.6; margin-bottom:0;">
          Side-by-side examples of weak prompts vs. clear, effective prompts, with simple explanations of why they work better.
        </p>
      </div>

      <div class="vibe-prompt-grid">
    `;

    courseData.promptExercises.forEach(pe => {
      html += `
        <article class="vibe-prompt-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
            <div>
              <span class="mini-badge mini-badge-subject">Example ${pe.id}</span>
              <h3 style="font-size:17px; font-weight:700; color:var(--text-primary); margin-top:4px;">${escapeHtml(pe.title)}</h3>
            </div>
            <button class="btn-copy-prompt" style="background:var(--color-success); color:#ffffff; border:none; padding:6px 12px; border-radius:var(--radius-sm); font-size:12px; font-weight:600; cursor:pointer;" data-prompt="${escapeHtml(pe.improvedPrompt)}">📋 Copy Better Prompt</button>
          </div>

          <div class="vibe-prompt-compare-cols">
            <div class="vibe-prompt-col bad">
              <span class="vibe-prompt-tag bad">✕ Weak Prompt</span>
              <div class="vibe-prompt-text">${escapeHtml(pe.badPrompt)}</div>
              <div style="font-size:12px; color:var(--color-error); line-height:1.5;">
                <strong>Why this is weak:</strong> ${escapeHtml(pe.whyBad)}
              </div>
            </div>

            <div class="vibe-prompt-col improved">
              <span class="vibe-prompt-tag improved">✓ Better Prompt (Clear &amp; Specific)</span>
              <div class="vibe-prompt-text">${escapeHtml(pe.improvedPrompt)}</div>
              <div style="font-size:12px; color:var(--color-success); line-height:1.5;">
                <strong>What you get:</strong> ${escapeHtml(pe.expectedOutput)}
              </div>
            </div>
          </div>

          <div class="token-metric-strip">
            <div>
              <strong>Token Metrics:</strong> ${escapeHtml(pe.tokenComparison || 'Significant token savings with constrained generation')}
            </div>
            <span class="token-savings-pill">70%+ Token Efficiency</span>
          </div>
        </article>
      `;
    });

    html += `</div>`;
    dom.promptsViewPanel.innerHTML = html;

    dom.promptsViewPanel.querySelectorAll('.btn-copy-prompt').forEach(btn => {
      btn.addEventListener('click', () => {
        const text = btn.getAttribute('data-prompt');
        if (text && navigator.clipboard) {
          navigator.clipboard.writeText(text);
          showToast('Improved prompt copied to clipboard!');
        }
      });
    });
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

  // Populate Subject Select Dropdown
  function populateSubjectDropdown() {
    if (!dom.selectSubject) return;
    const totalCount = state.allQuestions.length;
    let html = `<option value="All">All Full-Stack & AI Bank (${totalCount.toLocaleString()})</option>`;

    SUBJECTS.filter(s => s !== 'All').forEach(sub => {
      const cnt = state.allQuestions.filter(q => q.subject.toLowerCase() === sub.toLowerCase()).length;
      const isAi = (sub === 'AI & Generative AI');
      const label = isAi ? `⭐ [MOST IMPORTANT] AI & Generative AI (${cnt.toLocaleString()})` : `${sub} (${cnt.toLocaleString()})`;
      html += `<option value="${escapeHtml(sub)}">${escapeHtml(label)}</option>`;
    });

    dom.selectSubject.innerHTML = html;
    dom.selectSubject.value = state.selectedSubject;
  }

  // Populate & Update Topic Select Dropdown dynamically based on selected subject
  function updateTopicDropdown() {
    if (!dom.selectTopic) return;

    // Filter questions by current subject
    const subjectQuestions = (state.selectedSubject === 'All')
      ? state.allQuestions
      : state.allQuestions.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());

    // Gather distinct topics with counts
    const topicCounts = new Map();
    subjectQuestions.forEach(q => {
      if (q.topic && q.topic.trim()) {
        const t = q.topic.trim();
        topicCounts.set(t, (topicCounts.get(t) || 0) + 1);
      }
    });

    // Sort topics: by question count descending, then alphabetical
    const sortedTopics = Array.from(topicCounts.entries()).sort((a, b) => {
      if (b[1] !== a[1]) return b[1] - a[1];
      return a[0].localeCompare(b[0]);
    });

    const prefix = state.selectedSubject === 'All' ? 'All Topics' : `All ${state.selectedSubject} Topics`;
    let html = `<option value="All">${prefix} (${subjectQuestions.length.toLocaleString()})</option>`;

    sortedTopics.forEach(([topicName, count]) => {
      html += `<option value="${escapeHtml(topicName)}">${escapeHtml(topicName)} (${count.toLocaleString()})</option>`;
    });

    dom.selectTopic.innerHTML = html;

    // Reset selectedTopic to 'All' if it's not in the new subject pool
    if (state.selectedTopic !== 'All' && !topicCounts.has(state.selectedTopic)) {
      state.selectedTopic = 'All';
    }
    dom.selectTopic.value = state.selectedTopic;
  }

  // Synchronize Curriculum Switcher Tabs with Current State
  function syncCurriculumTabs() {
    const isAi = (state.selectedSubject === 'AI & Generative AI');
    if (dom.tabCurriculumAi) {
      dom.tabCurriculumAi.classList.toggle('active-important', isAi);
      dom.tabCurriculumAi.setAttribute('aria-selected', isAi ? 'true' : 'false');
    }
    if (dom.tabCurriculumFullstack) {
      dom.tabCurriculumFullstack.classList.toggle('active-fullstack', !isAi);
      dom.tabCurriculumFullstack.setAttribute('aria-selected', !isAi ? 'true' : 'false');
    }
  }

  // Synchronize Subject Carousel Active Pill with Selected Subject
  function syncSubjectCarousel() {
    syncCurriculumTabs();
    if (!dom.subjectCarouselTrack) return;
    const chips = dom.subjectCarouselTrack.querySelectorAll('.subject-chip');
    chips.forEach(c => {
      const sub = c.getAttribute('data-subject');
      const isAct = (sub === state.selectedSubject);
      c.classList.toggle('active', isAct);
      if (isAct) {
        c.scrollIntoView({ behavior: 'smooth', inline: 'nearest', block: 'nearest' });
      }
    });
  }

  // Render 22 Subject Carousel Track in Explorer Header
  function renderSubjectCarousel() {
    if (!dom.subjectCarouselTrack) return;
    dom.subjectCarouselTrack.innerHTML = '';

    SUBJECTS.forEach(sub => {
      const count = (sub === 'All') 
        ? state.allQuestions.length 
        : state.allQuestions.filter(q => q.subject === sub).length;

      const isAi = (sub === 'AI & Generative AI');
      const chip = document.createElement('button');
      chip.className = `subject-chip ${sub === state.selectedSubject ? 'active' : ''} ${isAi ? 'chip-ai-featured' : ''}`;
      chip.type = 'button';
      chip.setAttribute('data-subject', sub);
      chip.textContent = isAi ? `⭐ AI & GenAI (${count})` : `${sub} (${count})`;

      chip.addEventListener('click', () => {
        state.selectedSubject = sub;
        localStorage.setItem('devprep_subject', sub);
        if (dom.selectSubject) dom.selectSubject.value = sub;

        state.selectedTopic = 'All';
        updateTopicDropdown();
        syncSubjectCarousel();

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

    // Reset subject/topic filter if question is outside current selection
    if (state.selectedSubject !== 'All' && q.subject.toLowerCase() !== state.selectedSubject.toLowerCase()) {
      state.selectedSubject = 'All';
      if (dom.selectSubject) dom.selectSubject.value = 'All';
      syncSubjectCarousel();
    }
    state.selectedTopic = 'All';
    updateTopicDropdown();

    state.searchQuery = '';
    if (dom.explorerSearchInput) dom.explorerSearchInput.value = '';
    if (dom.explorerSearchClear) dom.explorerSearchClear.style.display = 'none';

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
    // Top Curriculum Module Switcher (AI vs Full-Stack)
    if (dom.tabCurriculumAi) {
      dom.tabCurriculumAi.addEventListener('click', () => {
        state.selectedSubject = 'AI & Generative AI';
        localStorage.setItem('devprep_subject', 'AI & Generative AI');
        state.selectedTopic = 'All';
        if (dom.selectSubject) dom.selectSubject.value = 'AI & Generative AI';
        updateTopicDropdown();
        syncSubjectCarousel();
        state.selectedIndex = 0;
        applyFilters();
        showToast('⭐ Active: AI + Generative AI + Prompt Engineering Masterclass');
      });
    }

    if (dom.tabCurriculumFullstack) {
      dom.tabCurriculumFullstack.addEventListener('click', () => {
        state.selectedSubject = 'All';
        localStorage.setItem('devprep_subject', 'All');
        state.selectedTopic = 'All';
        if (dom.selectSubject) dom.selectSubject.value = 'All';
        updateTopicDropdown();
        syncSubjectCarousel();
        state.selectedIndex = 0;
        applyFilters();
        showToast('💻 Active: Full-Stack MERN Question Bank (5,478 Qs)');
      });
    }

    // 0. Subject & Topic Top Navigation Selects
    if (dom.selectSubject) {
      dom.selectSubject.addEventListener('change', (e) => {
        state.selectedSubject = e.target.value;
        localStorage.setItem('devprep_subject', state.selectedSubject);
        state.selectedTopic = 'All';
        updateTopicDropdown();
        syncSubjectCarousel();
        state.selectedIndex = 0;
        applyFilters();
      });
    }

    if (dom.selectTopic) {
      dom.selectTopic.addEventListener('change', (e) => {
        state.selectedTopic = e.target.value;
        state.selectedIndex = 0;
        applyFilters();
      });
    }

    // 1. Search with Debounce & Clear Button
    let searchTimer = null;
    if (dom.explorerSearchInput) {
      dom.explorerSearchInput.addEventListener('input', (e) => {
        if (dom.explorerSearchClear) {
          dom.explorerSearchClear.style.display = e.target.value ? 'flex' : 'none';
        }
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => {
          state.searchQuery = e.target.value;
          state.selectedIndex = 0;
          applyFilters();
        }, 120);
      });
    }

    if (dom.explorerSearchClear) {
      dom.explorerSearchClear.addEventListener('click', () => {
        if (dom.explorerSearchInput) dom.explorerSearchInput.value = '';
        dom.explorerSearchClear.style.display = 'none';
        state.searchQuery = '';
        state.selectedIndex = 0;
        applyFilters();
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

    if (dom.btnModeCourse) {
      dom.btnModeCourse.addEventListener('click', () => {
        state.viewMode = 'course';
        renderFocusPane();
      });
    }

    if (dom.btnModeVideos) {
      dom.btnModeVideos.addEventListener('click', () => {
        state.viewMode = 'videos';
        renderFocusPane();
      });
    }

    if (dom.btnModePrompts) {
      dom.btnModePrompts.addEventListener('click', () => {
        state.viewMode = 'prompts';
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
        state.selectedTopic = 'All';
        state.searchQuery = '';
        state.selectedDifficulty = 'All';
        state.selectedStatus = 'All';
        state.selectedIndex = 0;
        if (dom.explorerSearchInput) dom.explorerSearchInput.value = '';
        if (dom.explorerSearchClear) dom.explorerSearchClear.style.display = 'none';
        if (dom.selectSubject) dom.selectSubject.value = 'All';
        if (dom.selectDifficulty) dom.selectDifficulty.value = 'All';
        if (dom.selectStatus) dom.selectStatus.value = 'All';
        updateTopicDropdown();
        syncSubjectCarousel();
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

    const rawData = window.FRESHER_QUESTIONS_DATA || window.FRESHER_QUESTIONS || [];
    const rawAiData = window.AI_GENAI_QUESTIONS_DATA || window.AI_GENAI_QUESTIONS || [];
    state.allQuestions = [...rawAiData, ...rawData];

    if (state.allQuestions.length === 0) {
      console.error('Questions data not loaded.');
      return;
    }

    // Apply stored theme
    const storedTheme = localStorage.getItem('fresher_theme') || 'light';
    document.documentElement.setAttribute('data-theme', storedTheme);
    if (dom.btnThemeToggle) {
      dom.btnThemeToggle.textContent = storedTheme === 'light' ? '🌙' : '☀️';
    }

    populateSubjectDropdown();
    updateTopicDropdown();
    renderSubjectCarousel();
    syncCurriculumTabs();
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
