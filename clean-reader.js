/**
 * DevPrep — Modern Technical Interview Preparation Platform
 * UI/UX Redesign Engine inspired by crackedin.io
 * Strictly consumes existing data without modifying any question or answer text.
 */

(function () {
  'use strict';

  // 22 Curriculum Subjects from existing data
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
    currentTab: 'dashboard', // 'dashboard', 'questions', 'theory', 'mcq', 'coding', 'progress', 'weak', 'saved'

    // Filters
    selectedSubject: 'All',
    selectedTopic: 'All',
    selectedDifficulty: 'All',
    selectedType: 'All',
    selectedStatus: 'All',
    selectedSort: 'default',
    searchQuery: '',

    // Pagination
    currentPage: 1,
    pageSize: 50,

    // MCQ Tab Pagination
    mcqPage: 1,
    mcqPageSize: 20,

    // Persistent User Practice & Assessment Data
    userAnswers: JSON.parse(localStorage.getItem('fresher_user_answers') || '{}'),
    streak: parseInt(localStorage.getItem('fresher_streak') || '0', 10),
    practicedIds: new Set(JSON.parse(localStorage.getItem('fresher_practiced_ids') || '[]')),
    needPracticeIds: new Set(JSON.parse(localStorage.getItem('fresher_need_practice_ids') || '[]')),
    savedIds: new Set(JSON.parse(localStorage.getItem('fresher_saved_ids') || '[]')),
    lastSubject: localStorage.getItem('fresher_last_subject') || 'JavaScript',
    lastTopic: localStorage.getItem('fresher_last_topic') || 'Core Concepts',
    expandedAnswerIds: new Set(),

    // Drill Session
    drillSession: {
      isActive: false,
      questions: [],
      currentIndex: 0,
      answerRevealed: false,
      practicedCount: 0,
      weakCount: 0
    }
  };

  // DOM Elements Cache
  const dom = {};

  function cacheDOMElements() {
    dom.body = document.body;
    dom.appSidebar = document.getElementById('app-sidebar');
    dom.btnMobileMenu = document.getElementById('btn-mobile-menu');
    dom.brandLink = document.getElementById('brand-link');
    dom.globalSearchInput = document.getElementById('global-search-input');
    dom.searchClearBtn = document.getElementById('search-clear-btn');
    dom.headerStreakCount = document.getElementById('header-streak-count');
    dom.headerPracticedCount = document.getElementById('header-practiced-count');
    dom.btnThemeToggle = document.getElementById('btn-theme-toggle');

    // Sidebar
    dom.navButtons = document.querySelectorAll('.nav-item-btn[data-tab]');
    dom.badgeTotalQuestions = document.getElementById('badge-total-questions');
    dom.badgeWeakCount = document.getElementById('badge-weak-count');
    dom.badgeSavedCount = document.getElementById('badge-saved-count');
    dom.sidebarSubjectSelect = document.getElementById('sidebar-subject-select');
    dom.btnSidebarMockTest = document.getElementById('btn-sidebar-mock-test');

    // Views
    dom.viewPanels = document.querySelectorAll('.view-panel');
    dom.viewDashboard = document.getElementById('view-dashboard');
    dom.viewQuestions = document.getElementById('view-questions');
    dom.viewTheory = document.getElementById('view-theory');
    dom.viewMcq = document.getElementById('view-mcq');
    dom.viewCoding = document.getElementById('view-coding');
    dom.viewProgress = document.getElementById('view-progress');

    // Dashboard Elements
    dom.continueSubjectTitle = document.getElementById('continue-subject-title');
    dom.btnContinueLearning = document.getElementById('btn-continue-learning');
    dom.dashTheoryCount = document.getElementById('dash-theory-count');
    dom.dashMcqCount = document.getElementById('dash-mcq-count');
    dom.dashInterviewCount = document.getElementById('dash-interview-count');
    dom.dashCodingCount = document.getElementById('dash-coding-count');
    dom.dashboardSubjectGrid = document.getElementById('dashboard-subject-grid');

    // Questions View Elements
    dom.questionsViewTitle = document.getElementById('questions-view-title');
    dom.questionsCountMeta = document.getElementById('questions-count-meta');
    dom.filterSubject = document.getElementById('filter-subject');
    dom.filterTopic = document.getElementById('filter-topic');
    dom.filterDifficulty = document.getElementById('filter-difficulty');
    dom.filterType = document.getElementById('filter-type');
    dom.filterStatus = document.getElementById('filter-status');
    dom.filterSort = document.getElementById('filter-sort');
    dom.topicChipsContainer = document.getElementById('topic-chips-container');
    dom.topicChipsTrack = document.getElementById('topic-chips-track');
    dom.questionsStreamContainer = document.getElementById('questions-stream-container');
    dom.paginationInfoText = document.getElementById('pagination-info-text');
    dom.btnPagePrev = document.getElementById('btn-page-prev');
    dom.btnPageNext = document.getElementById('btn-page-next');
    dom.selectPerPage = document.getElementById('select-per-page');

    // MCQ View Elements
    dom.mcqScoreDisplay = document.getElementById('mcq-score-display');
    dom.mcqAccuracyDisplay = document.getElementById('mcq-accuracy-display');
    dom.btnResetMcqScore = document.getElementById('btn-reset-mcq-score');
    dom.mcqFilterSubject = document.getElementById('mcq-filter-subject');
    dom.mcqFilterDifficulty = document.getElementById('mcq-filter-difficulty');
    dom.mcqFilterStatus = document.getElementById('mcq-filter-status');
    dom.mcqStreamContainer = document.getElementById('mcq-stream-container');
    dom.mcqPaginationInfo = document.getElementById('mcq-pagination-info');
    dom.btnMcqPrev = document.getElementById('btn-mcq-prev');
    dom.btnMcqNext = document.getElementById('btn-mcq-next');

    // Theory & Coding View Elements
    dom.theoryCountMeta = document.getElementById('theory-count-meta');
    dom.theoryFilterSubject = document.getElementById('theory-filter-subject');
    dom.theoryFilterTopic = document.getElementById('theory-filter-topic');
    dom.theoryStreamContainer = document.getElementById('theory-stream-container');
    dom.codingCountMeta = document.getElementById('coding-count-meta');
    dom.codingFilterSubject = document.getElementById('coding-filter-subject');
    dom.codingFilterDifficulty = document.getElementById('coding-filter-difficulty');
    dom.codingStreamContainer = document.getElementById('coding-stream-container');

    // Progress View Elements
    dom.progTotalPracticed = document.getElementById('prog-total-practiced');
    dom.progPracticedPct = document.getElementById('prog-practiced-pct');
    dom.progAccuracy = document.getElementById('prog-accuracy');
    dom.progAnsweredStats = document.getElementById('prog-answered-stats');
    dom.progWeakCount = document.getElementById('prog-weak-count');
    dom.progSavedCount = document.getElementById('prog-saved-count');
    dom.progressSubjectsList = document.getElementById('progress-subjects-list');
    dom.btnPracticeWeakNow = document.getElementById('btn-practice-weak-now');

    // Drill Modal Elements
    dom.drillModal = document.getElementById('drill-modal');
    dom.btnCloseDrillModal = document.getElementById('btn-close-drill-modal');
    dom.drillProgressBar = document.getElementById('drill-progress-bar');
    dom.drillPanelSetup = document.getElementById('drill-panel-setup');
    dom.drillPanelRunner = document.getElementById('drill-panel-runner');
    dom.drillPanelSummary = document.getElementById('drill-panel-summary');
    dom.drillRunnerFooter = document.getElementById('drill-runner-footer');
    dom.drillSelectSubject = document.getElementById('drill-select-subject');
    dom.drillSelectDifficulty = document.getElementById('drill-select-difficulty');
    dom.drillSelectCount = document.getElementById('drill-select-count');
    dom.btnStartDrillSession = document.getElementById('btn-start-drill-session');
    dom.btnDrillWeakSession = document.getElementById('btn-drill-weak-session');
    dom.drillQMeta = document.getElementById('drill-q-meta');
    dom.drillCounterText = document.getElementById('drill-counter-text');
    dom.drillQTitle = document.getElementById('drill-q-title');
    dom.drillOptionsContainer = document.getElementById('drill-options-container');
    dom.btnDrillRevealAnswer = document.getElementById('btn-drill-reveal-answer');
    dom.drillAnswerDrawer = document.getElementById('drill-answer-drawer');
    dom.drillAnswerKeyPill = document.getElementById('drill-answer-key-pill');
    dom.drillAnswerText = document.getElementById('drill-answer-text');
    dom.drillExplWrap = document.getElementById('drill-expl-wrap');
    dom.drillExplText = document.getElementById('drill-expl-text');
    dom.drillCodeWrap = document.getElementById('drill-code-wrap');
    dom.drillCodeText = document.getElementById('drill-code-text');
    dom.drillGotit = document.getElementById('btn-drill-gotit');
    dom.drillNeed = document.getElementById('btn-drill-need');
    dom.drillPrevQ = document.getElementById('btn-drill-prev-q');
    dom.drillNextQ = document.getElementById('btn-drill-next-q');
    dom.drillSummaryText = document.getElementById('drill-summary-text');
    dom.btnDrillAgain = document.getElementById('btn-drill-again');
    dom.btnCloseDrillSummary = document.getElementById('btn-close-drill-summary');

    // Toast
    dom.toastNotice = document.getElementById('toast-notice');
  }

  // Toast Helper
  let toastTimer = null;
  function showToast(msg) {
    if (!dom.toastNotice) return;
    dom.toastNotice.textContent = msg;
    dom.toastNotice.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      dom.toastNotice.classList.remove('show');
    }, 2200);
  }

  // Fast String Hash for deterministic distractor assignment
  function stringHash(str) {
    let hash = 0;
    const s = String(str || '');
    for (let i = 0; i < s.length; i++) {
      hash = ((hash << 5) - hash) + s.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  // Extract clean thesis sentence from an answer without altering original text
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

  // MCQ Data Engine (Preserves questions and answers, synthesizes 4 options deterministically)
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

    // Synthesize 4 domain-relevant options from existing questions in same subject
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

  // Switch Tab / View
  function switchTab(tabName) {
    state.currentTab = tabName;

    // Update active nav button
    dom.navButtons.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabName);
    });

    // Update active view panel
    dom.viewPanels.forEach(panel => {
      panel.classList.toggle('active', panel.id === `view-${tabName}`);
    });

    // Handle special views (e.g., weak areas filter or saved filter)
    if (tabName === 'weak') {
      state.currentTab = 'questions';
      state.selectedStatus = 'weak';
      if (dom.filterStatus) dom.filterStatus.value = 'weak';
      // Switch view to questions with weak filter
      dom.viewPanels.forEach(p => p.classList.toggle('active', p.id === 'view-questions'));
      dom.navButtons.forEach(b => b.classList.toggle('active', b.getAttribute('data-tab') === 'weak'));
      state.currentPage = 1;
      applyFilters();
      return;
    }

    if (tabName === 'saved') {
      state.currentTab = 'questions';
      state.selectedStatus = 'saved';
      if (dom.filterStatus) dom.filterStatus.value = 'saved';
      dom.viewPanels.forEach(p => p.classList.toggle('active', p.id === 'view-questions'));
      dom.navButtons.forEach(b => b.classList.toggle('active', b.getAttribute('data-tab') === 'saved'));
      state.currentPage = 1;
      applyFilters();
      return;
    }

    if (tabName === 'questions') {
      applyFilters();
    } else if (tabName === 'mcq') {
      renderMcqView();
    } else if (tabName === 'theory') {
      renderTheoryView();
    } else if (tabName === 'coding') {
      renderCodingView();
    } else if (tabName === 'progress') {
      renderProgressView();
    } else if (tabName === 'dashboard') {
      renderDashboard();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Close mobile sidebar if open
    if (dom.appSidebar) {
      dom.appSidebar.classList.remove('open');
    }
  }

  // Render Dashboard
  function renderDashboard() {
    if (!dom.viewDashboard) return;

    // 1. Calculate Real Preparation Stats directly from existing data
    const totalQuestions = state.allQuestions.length;
    const theoryQuestions = state.allQuestions.filter(q => q.questionType === 'Concept' || q.shortExplanation);
    const codingQuestions = state.allQuestions.filter(q => q.questionType === 'Coding' || q.difficulty === 'Fresher Coding' || q.codeExample);
    const interviewQuestions = state.allQuestions.filter(q => q.interviewRound && q.interviewRound.includes('Round'));

    if (dom.dashTheoryCount) dom.dashTheoryCount.textContent = theoryQuestions.length.toLocaleString();
    if (dom.dashMcqCount) dom.dashMcqCount.textContent = totalQuestions.toLocaleString();
    if (dom.dashInterviewCount) dom.dashInterviewCount.textContent = interviewQuestions.length.toLocaleString();
    if (dom.dashCodingCount) dom.dashCodingCount.textContent = codingQuestions.length.toLocaleString();

    // 2. Continue Learning
    if (dom.continueSubjectTitle) {
      dom.continueSubjectTitle.textContent = `${state.lastSubject} · ${state.lastTopic}`;
    }

    // 3. Render 22 Subject Curriculum Cards
    if (dom.dashboardSubjectGrid) {
      dom.dashboardSubjectGrid.innerHTML = '';
      SUBJECTS.filter(s => s !== 'All').forEach(sub => {
        const subQuestions = state.allQuestions.filter(q => q.subject === sub);
        const subCoding = subQuestions.filter(q => q.questionType === 'Coding' || q.difficulty === 'Fresher Coding' || q.codeExample).length;
        const subTheory = subQuestions.filter(q => q.questionType === 'Concept').length;

        const card = document.createElement('div');
        card.className = 'subject-card';
        card.innerHTML = `
          <div class="subject-card-title">
            <span>${escapeHtml(sub)}</span>
            <span style="font-size:12px; font-weight:600; color:var(--accent-primary); font-family:var(--font-mono);">${subQuestions.length} Qs</span>
          </div>
          <div class="subject-card-stats">
            <span class="subject-tag-pill">${subTheory} Theory</span>
            <span class="subject-tag-pill">${subQuestions.length} MCQ</span>
            ${subCoding > 0 ? `<span class="subject-tag-pill">${subCoding} Coding</span>` : ''}
          </div>
        `;

        card.addEventListener('click', () => {
          state.selectedSubject = sub;
          state.selectedTopic = 'All';
          state.lastSubject = sub;
          localStorage.setItem('fresher_last_subject', sub);
          if (dom.filterSubject) dom.filterSubject.value = sub;
          switchTab('questions');
        });

        dom.dashboardSubjectGrid.appendChild(card);
      });
    }

    updateHeaderBadges();
  }

  // Filter & Search Engine
  function applyFilters() {
    let result = state.allQuestions.slice();

    // Subject
    if (state.selectedSubject !== 'All') {
      result = result.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }

    // Topic
    if (state.selectedTopic !== 'All') {
      const topNorm = state.selectedTopic.toLowerCase();
      result = result.filter(q => (q.topic || '').toLowerCase() === topNorm || (q.subTopic || '').toLowerCase() === topNorm);
    }

    // Difficulty
    if (state.selectedDifficulty !== 'All') {
      result = result.filter(q => q.difficulty.toLowerCase() === state.selectedDifficulty.toLowerCase());
    }

    // Question Type
    if (state.selectedType !== 'All') {
      result = result.filter(q => q.questionType.toLowerCase() === state.selectedType.toLowerCase());
    }

    // Status Filter
    if (state.selectedStatus === 'practiced') {
      result = result.filter(q => state.practicedIds.has(q.id));
    } else if (state.selectedStatus === 'weak') {
      result = result.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedStatus === 'saved') {
      result = result.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedStatus === 'unpracticed') {
      result = result.filter(q => !state.practicedIds.has(q.id) && !state.needPracticeIds.has(q.id));
    }

    // Global Search (across questions, answers, topics, and code)
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

    // Sorting
    if (state.selectedSort === 'freq') {
      const freqMap = { High: 3, Medium: 2, Low: 1 };
      result.sort((a, b) => (freqMap[b.frequency] || 0) - (freqMap[a.frequency] || 0));
    } else if (state.selectedSort === 'diff_asc') {
      const diffMap = { Easy: 1, Medium: 2, 'Fresher Coding': 3 };
      result.sort((a, b) => (diffMap[a.difficulty] || 2) - (diffMap[b.difficulty] || 2));
    } else if (state.selectedSort === 'diff_desc') {
      const diffMap = { Easy: 1, Medium: 2, 'Fresher Coding': 3 };
      result.sort((a, b) => (diffMap[b.difficulty] || 2) - (diffMap[a.difficulty] || 2));
    } else if (state.selectedSort === 'weak_first') {
      result.sort((a, b) => (state.needPracticeIds.has(b.id) ? 1 : 0) - (state.needPracticeIds.has(a.id) ? 1 : 0));
    } else {
      result.sort((a, b) => (a.num || 0) - (b.num || 0));
    }

    state.filteredQuestions = result;

    // Reset pagination
    const maxPages = Math.max(1, Math.ceil(result.length / state.pageSize));
    if (state.currentPage > maxPages) state.currentPage = 1;

    renderQuestionsView();
    updateTopicPills();
  }

  // Update Topic Pills
  function updateTopicPills() {
    if (!dom.topicChipsContainer || !dom.topicChipsTrack) return;

    if (state.selectedSubject === 'All') {
      dom.topicChipsContainer.style.display = 'none';
      return;
    }

    dom.topicChipsContainer.style.display = 'block';
    dom.topicChipsTrack.innerHTML = '';

    const subjectQs = state.allQuestions.filter(q => q.subject === state.selectedSubject);
    const topics = Array.from(new Set(subjectQs.map(q => q.topic).filter(Boolean))).sort();

    // 'All Topics' Chip
    const allChip = document.createElement('button');
    allChip.className = `topic-chip ${state.selectedTopic === 'All' ? 'active' : ''}`;
    allChip.textContent = `All ${state.selectedSubject} (${subjectQs.length})`;
    allChip.addEventListener('click', () => {
      state.selectedTopic = 'All';
      if (dom.filterTopic) dom.filterTopic.value = 'All';
      state.currentPage = 1;
      applyFilters();
    });
    dom.topicChipsTrack.appendChild(allChip);

    topics.forEach(top => {
      const cnt = subjectQs.filter(q => q.topic === top).length;
      const chip = document.createElement('button');
      chip.className = `topic-chip ${state.selectedTopic === top ? 'active' : ''}`;
      chip.textContent = `${top} (${cnt})`;
      chip.addEventListener('click', () => {
        state.selectedTopic = top;
        state.lastTopic = top;
        localStorage.setItem('fresher_last_topic', top);
        if (dom.filterTopic) dom.filterTopic.value = top;
        state.currentPage = 1;
        applyFilters();
      });
      dom.topicChipsTrack.appendChild(chip);
    });
  }

  // Render Interview Questions View
  function renderQuestionsView() {
    if (!dom.questionsStreamContainer) return;
    dom.questionsStreamContainer.innerHTML = '';

    if (dom.questionsCountMeta) {
      dom.questionsCountMeta.textContent = `Showing ${state.filteredQuestions.length.toLocaleString()} of ${state.allQuestions.length.toLocaleString()} questions`;
    }

    if (dom.questionsViewTitle) {
      dom.questionsViewTitle.textContent = state.selectedSubject === 'All' ? 'Technical Interview Questions' : `${state.selectedSubject} Interview Questions`;
    }

    if (state.filteredQuestions.length === 0) {
      dom.questionsStreamContainer.innerHTML = `
        <div style="padding:40px; text-align:center; background:var(--bg-surface); border:1px solid var(--border-card); border-radius:var(--radius-md);">
          <div style="font-size:18px; font-weight:600; margin-bottom:6px;">No questions match this filter</div>
          <p style="font-size:13.5px; color:var(--text-muted); margin-bottom:16px;">Try clearing search keywords or resetting your active difficulty/topic filters.</p>
          <button id="btn-reset-filters" class="btn-primary" style="margin:0 auto;">Reset Filters</button>
        </div>
      `;
      const btnReset = document.getElementById('btn-reset-filters');
      if (btnReset) {
        btnReset.addEventListener('click', () => {
          state.selectedSubject = 'All';
          state.selectedTopic = 'All';
          state.selectedDifficulty = 'All';
          state.selectedType = 'All';
          state.selectedStatus = 'All';
          state.searchQuery = '';
          if (dom.globalSearchInput) dom.globalSearchInput.value = '';
          if (dom.filterSubject) dom.filterSubject.value = 'All';
          if (dom.filterTopic) dom.filterTopic.value = 'All';
          if (dom.filterDifficulty) dom.filterDifficulty.value = 'All';
          if (dom.filterStatus) dom.filterStatus.value = 'All';
          applyFilters();
        });
      }
      if (dom.paginationControls) dom.paginationControls.style.display = 'none';
      return;
    }

    if (dom.paginationControls) dom.paginationControls.style.display = 'flex';

    // Pagination slice
    const startIndex = (state.currentPage - 1) * state.pageSize;
    const paged = state.pageSize === Infinity 
      ? state.filteredQuestions 
      : state.filteredQuestions.slice(startIndex, startIndex + state.pageSize);

    paged.forEach((q, idx) => {
      const globalIndex = startIndex + idx + 1;
      const isExpanded = state.expandedAnswerIds.has(q.id);
      const isPracticed = state.practicedIds.has(q.id);
      const isWeak = state.needPracticeIds.has(q.id);
      const isSaved = state.savedIds.has(q.id);

      let diffBadgeClass = 'badge-easy';
      if (q.difficulty === 'Medium') diffBadgeClass = 'badge-medium';
      if (q.difficulty === 'Fresher Coding') diffBadgeClass = 'badge-hard';

      const card = document.createElement('article');
      card.className = 'question-card';
      card.setAttribute('data-id', q.id);

      card.innerHTML = `
        <div class="question-card-header">
          <span class="question-index">Q${String(globalIndex).padStart(2, '0')}</span>
          <h3 class="question-title">${escapeHtml(q.question)}</h3>
        </div>

        <div class="card-meta-row">
          <span class="badge badge-subject">${escapeHtml(q.subject)}</span>
          <span class="badge">${escapeHtml(q.topic)}</span>
          <span class="badge ${diffBadgeClass}">${escapeHtml(q.difficulty)}</span>
          <span class="badge">${escapeHtml(q.questionType)}</span>
          ${isPracticed ? '<span class="badge" style="color:var(--color-success); border-color:var(--color-success-border);">✓ Practiced</span>' : ''}
          ${isWeak ? '<span class="badge" style="color:var(--color-warning); border-color:var(--color-warning-border);">⚠ Needs Practice</span>' : ''}
          ${isSaved ? '<span class="badge" style="color:var(--color-purple); border-color:var(--color-purple-border);">★ Saved</span>' : ''}
        </div>

        <div class="card-actions">
          <button class="btn-card-action btn-toggle-answer" data-id="${q.id}">
            ${isExpanded ? 'Hide Answer ↑' : 'View Answer →'}
          </button>
          <button class="btn-card-action ${isPracticed ? 'active-practiced' : ''}" data-action="practice" data-id="${q.id}">
            ${isPracticed ? '✓ Practiced' : 'Mark Practiced'}
          </button>
          <button class="btn-card-action ${isWeak ? 'active-weak' : ''}" data-action="weak" data-id="${q.id}">
            ${isWeak ? '⚠ Needs Practice' : 'Flag Weak Area'}
          </button>
          <button class="btn-card-action ${isSaved ? 'active-saved' : ''}" data-action="save" data-id="${q.id}">
            ${isSaved ? '★ Bookmarked' : '☆ Bookmark'}
          </button>
        </div>

        <!-- Collapsible Answer View (Untouched Existing Content) -->
        <div class="answer-drawer ${isExpanded ? 'expanded' : ''}" id="answer-${q.id}">
          <div class="answer-section">
            <div class="answer-section-label">Answer</div>
            <div class="answer-content">${escapeHtml(q.answer)}</div>
          </div>

          ${q.shortExplanation ? `
            <div class="answer-section">
              <div class="answer-section-label">Important Points &amp; Explanation</div>
              <div class="explanation-content">${escapeHtml(q.shortExplanation)}</div>
            </div>
          ` : ''}

          ${q.codeExample ? `
            <div class="answer-section">
              <div class="answer-section-label">Example Code</div>
              <div class="code-box">
                <div class="code-box-header">
                  <span class="code-box-title">Snippet</span>
                  <button class="btn-copy-code" data-code="${escapeHtml(q.codeExample)}">Copy</button>
                </div>
                <pre><code>${escapeHtml(q.codeExample)}</code></pre>
              </div>
            </div>
          ` : ''}

          ${q.followUpQuestions ? `
            <div class="followup-box">
              <strong>Follow-Up:</strong> ${escapeHtml(q.followUpQuestions)}
            </div>
          ` : ''}

          ${q.references ? `
            <div class="reference-line">
              <strong>Reference:</strong> ${escapeHtml(q.references)}
            </div>
          ` : ''}
        </div>
      `;

      // Event Listeners on Card
      const btnToggle = card.querySelector('.btn-toggle-answer');
      const drawer = card.querySelector('.answer-drawer');
      btnToggle.addEventListener('click', () => {
        if (state.expandedAnswerIds.has(q.id)) {
          state.expandedAnswerIds.delete(q.id);
          drawer.classList.remove('expanded');
          btnToggle.textContent = 'View Answer →';
        } else {
          state.expandedAnswerIds.add(q.id);
          drawer.classList.add('expanded');
          btnToggle.textContent = 'Hide Answer ↑';
        }
      });

      // Actions: Practiced, Weak, Save
      const btnPractice = card.querySelector('[data-action="practice"]');
      btnPractice.addEventListener('click', () => {
        if (state.practicedIds.has(q.id)) {
          state.practicedIds.delete(q.id);
          showToast(`Unmarked Question #${globalIndex}`);
        } else {
          state.practicedIds.add(q.id);
          state.needPracticeIds.delete(q.id);
          showToast(`Marked Question #${globalIndex} as Practiced!`);
        }
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        updateHeaderBadges();
        applyFilters();
      });

      const btnWeak = card.querySelector('[data-action="weak"]');
      btnWeak.addEventListener('click', () => {
        if (state.needPracticeIds.has(q.id)) {
          state.needPracticeIds.delete(q.id);
          showToast(`Removed #${globalIndex} from Weak Areas`);
        } else {
          state.needPracticeIds.add(q.id);
          state.practicedIds.delete(q.id);
          showToast(`Added #${globalIndex} to Weak Areas for drill`);
        }
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        updateHeaderBadges();
        applyFilters();
      });

      const btnSave = card.querySelector('[data-action="save"]');
      btnSave.addEventListener('click', () => {
        if (state.savedIds.has(q.id)) {
          state.savedIds.delete(q.id);
          showToast(`Removed #${globalIndex} from Bookmarks`);
        } else {
          state.savedIds.add(q.id);
          showToast(`Saved #${globalIndex} to Bookmarks`);
        }
        localStorage.setItem('fresher_saved_ids', JSON.stringify(Array.from(state.savedIds)));
        updateHeaderBadges();
        applyFilters();
      });

      // Copy Code
      const btnCopy = card.querySelector('.btn-copy-code');
      if (btnCopy) {
        btnCopy.addEventListener('click', () => {
          navigator.clipboard.writeText(q.codeExample || '').then(() => {
            btnCopy.textContent = '✓ Copied';
            setTimeout(() => { btnCopy.textContent = 'Copy'; }, 1500);
          });
        });
      }

      dom.questionsStreamContainer.appendChild(card);
    });

    renderPagination();
  }

  // Render Pagination Info & Buttons
  function renderPagination() {
    if (!dom.paginationInfoText || !dom.btnPagePrev || !dom.btnPageNext) return;

    const totalPages = Math.max(1, Math.ceil(state.filteredQuestions.length / state.pageSize));
    dom.paginationInfoText.textContent = `Page ${state.currentPage} of ${totalPages} (${state.filteredQuestions.length.toLocaleString()} questions)`;

    dom.btnPagePrev.disabled = state.currentPage <= 1;
    dom.btnPageNext.disabled = state.currentPage >= totalPages;
  }

  // Render Interactive MCQ View
  function renderMcqView() {
    if (!dom.mcqStreamContainer) return;
    dom.mcqStreamContainer.innerHTML = '';

    let mcqPool = state.allQuestions.slice();

    const sub = dom.mcqFilterSubject ? dom.mcqFilterSubject.value : 'All';
    const diff = dom.mcqFilterDifficulty ? dom.mcqFilterDifficulty.value : 'All';
    const stat = dom.mcqFilterStatus ? dom.mcqFilterStatus.value : 'All';

    if (sub !== 'All') mcqPool = mcqPool.filter(q => q.subject === sub);
    if (diff !== 'All') mcqPool = mcqPool.filter(q => q.difficulty === diff);
    if (stat === 'unanswered') mcqPool = mcqPool.filter(q => !state.userAnswers[q.id]);
    if (stat === 'correct') mcqPool = mcqPool.filter(q => state.userAnswers[q.id]?.isCorrect === true);
    if (stat === 'incorrect') mcqPool = mcqPool.filter(q => state.userAnswers[q.id]?.isCorrect === false);

    const total = mcqPool.length;
    const start = (state.mcqPage - 1) * state.mcqPageSize;
    const paged = mcqPool.slice(start, start + state.mcqPageSize);

    if (dom.mcqPaginationInfo) {
      const totalPages = Math.max(1, Math.ceil(total / state.mcqPageSize));
      dom.mcqPaginationInfo.textContent = `Page ${state.mcqPage} of ${totalPages} (${total} assessment questions)`;
      if (dom.btnMcqPrev) dom.btnMcqPrev.disabled = state.mcqPage <= 1;
      if (dom.btnMcqNext) dom.btnMcqNext.disabled = state.mcqPage >= totalPages;
    }

    paged.forEach((q, idx) => {
      const globalIndex = start + idx + 1;
      const mcq = getMCQData(q);
      const userAnswer = state.userAnswers[q.id];
      const isExpanded = !!userAnswer;

      const card = document.createElement('article');
      card.className = 'question-card';
      card.setAttribute('data-id', q.id);

      const letters = ['A', 'B', 'C', 'D'];
      const optionsHtml = letters.map(letter => {
        let optClass = '';
        if (userAnswer) {
          if (userAnswer.selected === letter) {
            optClass = userAnswer.isCorrect ? 'selected-correct' : 'selected-wrong';
          } else if (!userAnswer.isCorrect && letter === mcq.correct) {
            optClass = 'reveal-correct';
          }
        }
        return `
          <button class="mcq-option-btn ${optClass}" data-option="${letter}" type="button">
            <span class="mcq-letter">${letter}</span>
            <span class="mcq-text">${escapeHtml(mcq.options[letter])}</span>
          </button>
        `;
      }).join('');

      card.innerHTML = `
        <div class="question-card-header">
          <span class="question-index">Q${String(globalIndex).padStart(2, '0')}</span>
          <h3 class="question-title">${escapeHtml(mcq.displayQuestion)}</h3>
        </div>

        <div class="card-meta-row">
          <span class="badge badge-subject">${escapeHtml(q.subject)}</span>
          <span class="badge">${escapeHtml(q.topic)}</span>
          <span class="badge">${escapeHtml(q.difficulty)}</span>
          ${userAnswer ? (userAnswer.isCorrect ? '<span class="badge" style="color:var(--color-success); border-color:var(--color-success-border);">✓ Correct</span>' : '<span class="badge" style="color:var(--color-error); border-color:var(--color-error-border);">✕ Incorrect</span>') : ''}
        </div>

        <div class="mcq-options-list">
          ${optionsHtml}
        </div>

        <div class="answer-drawer ${isExpanded ? 'expanded' : ''}" id="mcq-drawer-${q.id}">
          <div class="answer-key-pill">🔑 Answer Key: Option ${mcq.correct}</div>
          <div class="answer-section">
            <div class="answer-section-label">Verified Answer</div>
            <div class="answer-content">${escapeHtml(q.answer)}</div>
          </div>
          ${q.shortExplanation ? `
            <div class="answer-section">
              <div class="answer-section-label">Explanation</div>
              <div class="explanation-content">${escapeHtml(q.shortExplanation)}</div>
            </div>
          ` : ''}
        </div>
      `;

      // Bind Option Click
      const optionButtons = card.querySelectorAll('.mcq-option-btn');
      optionButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          const chosen = btn.getAttribute('data-option');
          const isCorrect = (chosen === mcq.correct);

          // Save answer
          state.userAnswers[q.id] = {
            selected: chosen,
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
            showToast(`✕ Incorrect. Option ${mcq.correct} is correct.`);
          }
          localStorage.setItem('fresher_streak', state.streak);
          localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
          localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));

          // Update UI
          updateMcqScorecard();
          renderMcqView();
        });
      });

      dom.mcqStreamContainer.appendChild(card);
    });

    updateMcqScorecard();
  }

  function updateMcqScorecard() {
    const answeredIds = Object.keys(state.userAnswers);
    const totalAnswered = answeredIds.length;
    let correctCount = 0;
    answeredIds.forEach(id => {
      if (state.userAnswers[id]?.isCorrect) correctCount++;
    });

    if (dom.mcqScoreDisplay) dom.mcqScoreDisplay.textContent = `${correctCount} / ${totalAnswered}`;
    if (dom.mcqAccuracyDisplay) {
      const acc = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
      dom.mcqAccuracyDisplay.textContent = `${acc}%`;
    }
    updateHeaderBadges();
  }

  // Render Theory & Concepts View
  function renderTheoryView() {
    if (!dom.theoryStreamContainer) return;
    dom.theoryStreamContainer.innerHTML = '';

    const sub = dom.theoryFilterSubject ? dom.theoryFilterSubject.value : 'All';
    const top = dom.theoryFilterTopic ? dom.theoryFilterTopic.value : 'All';

    let pool = state.allQuestions.filter(q => q.questionType === 'Concept' || q.shortExplanation);
    if (sub !== 'All') pool = pool.filter(q => q.subject === sub);
    if (top !== 'All') pool = pool.filter(q => q.topic === top);

    if (dom.theoryCountMeta) {
      dom.theoryCountMeta.textContent = `${pool.length} concept notes`;
    }

    pool.slice(0, 40).forEach((q, idx) => {
      const card = document.createElement('article');
      card.className = 'question-card';
      card.innerHTML = `
        <div class="question-card-header">
          <span class="question-index">#${idx + 1}</span>
          <h3 class="question-title">${escapeHtml(q.question)}</h3>
        </div>
        <div class="card-meta-row">
          <span class="badge badge-subject">${escapeHtml(q.subject)}</span>
          <span class="badge">${escapeHtml(q.topic)}</span>
        </div>
        <div class="answer-section">
          <div class="answer-content">${escapeHtml(q.answer)}</div>
        </div>
        ${q.shortExplanation ? `
          <div class="explanation-content" style="margin-top:12px;">${escapeHtml(q.shortExplanation)}</div>
        ` : ''}
        ${q.codeExample ? `
          <div class="code-box" style="margin-top:12px;">
            <div class="code-box-header">
              <span class="code-box-title">Code Demonstration</span>
              <button class="btn-copy-code" data-code="${escapeHtml(q.codeExample)}">Copy</button>
            </div>
            <pre><code>${escapeHtml(q.codeExample)}</code></pre>
          </div>
        ` : ''}
      `;

      const btnCopy = card.querySelector('.btn-copy-code');
      if (btnCopy) {
        btnCopy.addEventListener('click', () => {
          navigator.clipboard.writeText(q.codeExample || '').then(() => {
            btnCopy.textContent = '✓ Copied';
            setTimeout(() => { btnCopy.textContent = 'Copy'; }, 1500);
          });
        });
      }

      dom.theoryStreamContainer.appendChild(card);
    });
  }

  // Render Coding Problems View
  function renderCodingView() {
    if (!dom.codingStreamContainer) return;
    dom.codingStreamContainer.innerHTML = '';

    const sub = dom.codingFilterSubject ? dom.codingFilterSubject.value : 'All';
    const diff = dom.codingFilterDifficulty ? dom.codingFilterDifficulty.value : 'All';

    let pool = state.allQuestions.filter(q => q.questionType === 'Coding' || q.difficulty === 'Fresher Coding' || q.codeExample);
    if (sub !== 'All') pool = pool.filter(q => q.subject === sub);
    if (diff !== 'All') pool = pool.filter(q => q.difficulty === diff);

    if (dom.codingCountMeta) {
      dom.codingCountMeta.textContent = `${pool.length} coding problems`;
    }

    pool.slice(0, 30).forEach((q, idx) => {
      const card = document.createElement('article');
      card.className = 'question-card';
      card.innerHTML = `
        <div class="question-card-header">
          <span class="question-index">P${idx + 1}</span>
          <h3 class="question-title">${escapeHtml(q.question)}</h3>
        </div>
        <div class="card-meta-row">
          <span class="badge badge-subject">${escapeHtml(q.subject)}</span>
          <span class="badge">${escapeHtml(q.topic)}</span>
          <span class="badge badge-hard">${escapeHtml(q.difficulty)}</span>
        </div>
        <div class="answer-section">
          <div class="answer-section-label">Solution Approach</div>
          <div class="answer-content">${escapeHtml(q.answer)}</div>
        </div>
        ${q.codeExample ? `
          <div class="code-box">
            <div class="code-box-header">
              <span class="code-box-title">Solution Implementation (JetBrains Mono)</span>
              <button class="btn-copy-code" data-code="${escapeHtml(q.codeExample)}">Copy</button>
            </div>
            <pre><code>${escapeHtml(q.codeExample)}</code></pre>
          </div>
        ` : ''}
      `;

      const btnCopy = card.querySelector('.btn-copy-code');
      if (btnCopy) {
        btnCopy.addEventListener('click', () => {
          navigator.clipboard.writeText(q.codeExample || '').then(() => {
            btnCopy.textContent = '✓ Copied';
            setTimeout(() => { btnCopy.textContent = 'Copy'; }, 1500);
          });
        });
      }

      dom.codingStreamContainer.appendChild(card);
    });
  }

  // Render Progress & Weak Areas View
  function renderProgressView() {
    if (!dom.viewProgress) return;

    const totalQuestions = state.allQuestions.length;
    const practicedCount = state.practicedIds.size;
    const weakCount = state.needPracticeIds.size;
    const savedCount = state.savedIds.size;

    const answeredIds = Object.keys(state.userAnswers);
    let correctCount = 0;
    answeredIds.forEach(id => {
      if (state.userAnswers[id]?.isCorrect) correctCount++;
    });
    const acc = answeredIds.length > 0 ? Math.round((correctCount / answeredIds.length) * 100) : 0;

    if (dom.progTotalPracticed) dom.progTotalPracticed.textContent = practicedCount.toLocaleString();
    if (dom.progPracticedPct) {
      const pct = Math.round((practicedCount / totalQuestions) * 100);
      dom.progPracticedPct.textContent = `${pct}% of ${totalQuestions.toLocaleString()} total questions`;
    }
    if (dom.progAccuracy) dom.progAccuracy.textContent = `${acc}%`;
    if (dom.progAnsweredStats) dom.progAnsweredStats.textContent = `${correctCount} of ${answeredIds.length} answered correctly`;
    if (dom.progWeakCount) dom.progWeakCount.textContent = weakCount;
    if (dom.progSavedCount) dom.progSavedCount.textContent = savedCount;

    // Render Subject Progress Bars
    if (dom.progressSubjectsList) {
      dom.progressSubjectsList.innerHTML = '';
      SUBJECTS.filter(s => s !== 'All').forEach(sub => {
        const subQuestions = state.allQuestions.filter(q => q.subject === sub);
        const subPracticed = subQuestions.filter(q => state.practicedIds.has(q.id)).length;
        const subPct = subQuestions.length > 0 ? Math.round((subPracticed / subQuestions.length) * 100) : 0;

        const row = document.createElement('div');
        row.style.background = 'var(--bg-surface)';
        row.style.border = '1px solid var(--border-card)';
        row.style.borderRadius = 'var(--radius-md)';
        row.style.padding = '12px 16px';

        row.innerHTML = `
          <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:13.5px;">
            <strong>${escapeHtml(sub)}</strong>
            <span style="color:var(--text-muted); font-size:12.5px;">${subPracticed} / ${subQuestions.length} (${subPct}%)</span>
          </div>
          <div style="height:6px; background:var(--bg-subtle); border-radius:var(--radius-full); overflow:hidden;">
            <div style="width:${subPct}%; height:100%; background:var(--accent-primary); border-radius:var(--radius-full);"></div>
          </div>
        `;

        dom.progressSubjectsList.appendChild(row);
      });
    }
  }

  // Update Header Badges
  function updateHeaderBadges() {
    if (dom.headerStreakCount) dom.headerStreakCount.textContent = `🔥 ${state.streak}`;
    if (dom.headerPracticedCount) dom.headerPracticedCount.textContent = state.practicedIds.size.toLocaleString();
    if (dom.badgeTotalQuestions && state.allQuestions.length > 0) {
      dom.badgeTotalQuestions.textContent = state.allQuestions.length.toLocaleString();
    }
    if (dom.badgeWeakCount) dom.badgeWeakCount.textContent = state.needPracticeIds.size;
    if (dom.badgeSavedCount) dom.badgeSavedCount.textContent = state.savedIds.size;
  }

  // Populate Dropdown Selects
  function populateDropdowns() {
    // Subject Dropdowns
    const subjectOptions = '<option value="All">All Subjects</option>' +
      SUBJECTS.filter(s => s !== 'All').map(s => {
        const cnt = state.allQuestions.filter(q => q.subject === s).length;
        return `<option value="${escapeHtml(s)}">${escapeHtml(s)} (${cnt})</option>`;
      }).join('');

    if (dom.filterSubject) dom.filterSubject.innerHTML = subjectOptions;
    if (dom.sidebarSubjectSelect) dom.sidebarSubjectSelect.innerHTML = `<option value="All">All Subjects (${state.allQuestions.length.toLocaleString()} Qs)</option>` +
      SUBJECTS.filter(s => s !== 'All').map(s => {
        const cnt = state.allQuestions.filter(q => q.subject === s).length;
        return `<option value="${escapeHtml(s)}">${escapeHtml(s)} (${cnt})</option>`;
      }).join('');
    if (dom.mcqFilterSubject) dom.mcqFilterSubject.innerHTML = subjectOptions;
    if (dom.theoryFilterSubject) dom.theoryFilterSubject.innerHTML = subjectOptions;
    if (dom.codingFilterSubject) dom.codingFilterSubject.innerHTML = subjectOptions;
    if (dom.drillSelectSubject) dom.drillSelectSubject.innerHTML = dom.sidebarSubjectSelect.innerHTML;

    updateTopicsDropdown();
  }

  function updateTopicsDropdown() {
    if (!dom.filterTopic) return;
    const pool = state.selectedSubject === 'All' 
      ? state.allQuestions 
      : state.allQuestions.filter(q => q.subject === state.selectedSubject);

    const topics = Array.from(new Set(pool.map(q => q.topic).filter(Boolean))).sort();
    dom.filterTopic.innerHTML = '<option value="All">All Topics</option>' +
      topics.map(t => `<option value="${escapeHtml(t)}">${escapeHtml(t)}</option>`).join('');

    if (dom.theoryFilterTopic) dom.theoryFilterTopic.innerHTML = dom.filterTopic.innerHTML;
  }

  // Mock Test / Drill Modal Runner
  function openDrillModal() {
    if (!dom.drillModal) return;
    dom.drillPanelSetup.style.display = 'block';
    dom.drillPanelRunner.style.display = 'none';
    dom.drillPanelSummary.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'none';
    dom.drillProgressBar.style.width = '0%';
    dom.drillModal.classList.add('active');
  }

  function startDrill(questionsList) {
    if (questionsList.length === 0) {
      showToast('No questions match drill criteria. Try broader filters.');
      return;
    }

    state.drillSession.questions = questionsList.slice().sort(() => Math.random() - 0.5);
    state.drillSession.currentIndex = 0;
    state.drillSession.answerRevealed = false;
    state.drillSession.practicedCount = 0;
    state.drillSession.weakCount = 0;

    dom.drillPanelSetup.style.display = 'none';
    dom.drillPanelRunner.style.display = 'block';
    dom.drillPanelSummary.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'flex';

    renderCurrentDrillQuestion();
  }

  function renderCurrentDrillQuestion() {
    const session = state.drillSession;
    const q = session.questions[session.currentIndex];
    const total = session.questions.length;
    const currentNum = session.currentIndex + 1;
    const mcq = getMCQData(q);

    dom.drillProgressBar.style.width = `${(currentNum / total) * 100}%`;
    dom.drillCounterText.textContent = `Q ${currentNum} / ${total}`;
    dom.drillQTitle.textContent = mcq.displayQuestion;

    dom.drillQMeta.innerHTML = `
      <span class="badge badge-subject">${escapeHtml(q.subject)}</span>
      <span class="badge">${escapeHtml(q.topic)}</span>
      <span class="badge">${escapeHtml(q.difficulty)}</span>
    `;

    // Render 4 clickable drill options
    dom.drillOptionsContainer.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];
    letters.forEach(letter => {
      const btn = document.createElement('button');
      btn.className = 'mcq-option-btn';
      btn.type = 'button';
      btn.setAttribute('data-option', letter);
      btn.innerHTML = `
        <span class="mcq-letter">${letter}</span>
        <span class="mcq-text">${escapeHtml(mcq.options[letter])}</span>
      `;

      btn.addEventListener('click', () => {
        const isCorrect = (letter === mcq.correct);
        dom.drillOptionsContainer.querySelectorAll('.mcq-option-btn').forEach(b => {
          const bLet = b.getAttribute('data-option');
          b.classList.remove('selected-correct', 'selected-wrong', 'reveal-correct');
          if (bLet === letter) {
            b.classList.add(isCorrect ? 'selected-correct' : 'selected-wrong');
          } else if (!isCorrect && bLet === mcq.correct) {
            b.classList.add('reveal-correct');
          }
        });

        // Reveal answer drawer
        session.answerRevealed = true;
        dom.drillAnswerDrawer.classList.add('expanded');
        dom.btnDrillRevealAnswer.style.display = 'none';

        if (isCorrect) {
          session.practicedCount++;
          state.practicedIds.add(q.id);
          state.needPracticeIds.delete(q.id);
        } else {
          session.weakCount++;
          state.needPracticeIds.add(q.id);
          state.practicedIds.delete(q.id);
        }
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        updateHeaderBadges();
      });

      dom.drillOptionsContainer.appendChild(btn);
    });

    // Reset answer drawer
    session.answerRevealed = false;
    dom.drillAnswerDrawer.classList.remove('expanded');
    dom.btnDrillRevealAnswer.style.display = 'inline-flex';
    dom.drillAnswerKeyPill.textContent = `🔑 Answer Key: Option ${mcq.correct}`;
    dom.drillAnswerText.textContent = q.answer;

    if (q.shortExplanation) {
      dom.drillExplWrap.style.display = 'block';
      dom.drillExplText.textContent = q.shortExplanation;
    } else {
      dom.drillExplWrap.style.display = 'none';
    }

    if (q.codeExample) {
      dom.drillCodeWrap.style.display = 'block';
      dom.drillCodeText.textContent = q.codeExample;
    } else {
      dom.drillCodeWrap.style.display = 'none';
    }

    dom.drillPrevQ.disabled = session.currentIndex === 0;
    dom.drillNextQ.textContent = session.currentIndex === total - 1 ? 'Finish Drill ✓' : 'Next →';
  }

  function advanceDrill() {
    const session = state.drillSession;
    if (session.currentIndex < session.questions.length - 1) {
      session.currentIndex++;
      renderCurrentDrillQuestion();
    } else {
      finishDrill();
    }
  }

  function finishDrill() {
    const session = state.drillSession;
    dom.drillPanelRunner.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'none';
    dom.drillPanelSummary.style.display = 'block';
    dom.drillProgressBar.style.width = '100%';

    dom.drillSummaryText.innerHTML = `
      You completed <strong>${session.questions.length} questions</strong>.<br>
      <span style="color:var(--color-success); font-weight:600;">✓ Correct: ${session.practicedCount}</span> &nbsp;|&nbsp; 
      <span style="color:var(--color-warning); font-weight:600;">⚠ Flagged for Practice: ${session.weakCount}</span>
    `;
  }

  // Event Listeners Setup
  function setupEventListeners() {
    // 1. Navigation Buttons (Tabs)
    dom.navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.getAttribute('data-tab');
        switchTab(tab);
      });
    });

    if (dom.btnSidebarMockTest) {
      dom.btnSidebarMockTest.addEventListener('click', openDrillModal);
    }

    if (dom.brandLink) {
      dom.brandLink.addEventListener('click', (e) => {
        e.preventDefault();
        switchTab('dashboard');
      });
    }

    if (dom.btnContinueLearning) {
      dom.btnContinueLearning.addEventListener('click', () => {
        state.selectedSubject = state.lastSubject || 'JavaScript';
        if (dom.filterSubject) dom.filterSubject.value = state.selectedSubject;
        switchTab('questions');
      });
    }

    // 2. Mobile Menu Toggle
    if (dom.btnMobileMenu && dom.appSidebar) {
      dom.btnMobileMenu.addEventListener('click', () => {
        dom.appSidebar.classList.toggle('open');
      });
    }

    // 3. Search with Debounce
    let searchDebounce = null;
    if (dom.globalSearchInput) {
      dom.globalSearchInput.addEventListener('input', (e) => {
        clearTimeout(searchDebounce);
        const val = e.target.value;
        if (dom.searchClearBtn) dom.searchClearBtn.style.display = val ? 'block' : 'none';
        searchDebounce = setTimeout(() => {
          state.searchQuery = val;
          state.currentPage = 1;
          if (state.currentTab !== 'questions') {
            switchTab('questions');
          } else {
            applyFilters();
          }
        }, 150);
      });
    }

    if (dom.searchClearBtn) {
      dom.searchClearBtn.addEventListener('click', () => {
        if (dom.globalSearchInput) dom.globalSearchInput.value = '';
        dom.searchClearBtn.style.display = 'none';
        state.searchQuery = '';
        state.currentPage = 1;
        applyFilters();
      });
    }

    // 4. Filter Selects
    if (dom.filterSubject) {
      dom.filterSubject.addEventListener('change', (e) => {
        state.selectedSubject = e.target.value;
        state.selectedTopic = 'All';
        state.currentPage = 1;
        updateTopicsDropdown();
        applyFilters();
      });
    }

    if (dom.sidebarSubjectSelect) {
      dom.sidebarSubjectSelect.addEventListener('change', (e) => {
        state.selectedSubject = e.target.value;
        state.selectedTopic = 'All';
        if (dom.filterSubject) dom.filterSubject.value = e.target.value;
        state.currentPage = 1;
        updateTopicsDropdown();
        switchTab('questions');
      });
    }

    if (dom.filterTopic) {
      dom.filterTopic.addEventListener('change', (e) => {
        state.selectedTopic = e.target.value;
        state.currentPage = 1;
        applyFilters();
      });
    }

    if (dom.filterDifficulty) {
      dom.filterDifficulty.addEventListener('change', (e) => {
        state.selectedDifficulty = e.target.value;
        state.currentPage = 1;
        applyFilters();
      });
    }

    if (dom.filterType) {
      dom.filterType.addEventListener('change', (e) => {
        state.selectedType = e.target.value;
        state.currentPage = 1;
        applyFilters();
      });
    }

    if (dom.filterStatus) {
      dom.filterStatus.addEventListener('change', (e) => {
        state.selectedStatus = e.target.value;
        state.currentPage = 1;
        applyFilters();
      });
    }

    if (dom.filterSort) {
      dom.filterSort.addEventListener('change', (e) => {
        state.selectedSort = e.target.value;
        applyFilters();
      });
    }

    if (dom.selectPerPage) {
      dom.selectPerPage.addEventListener('change', (e) => {
        state.pageSize = e.target.value === 'all' ? Infinity : parseInt(e.target.value, 10);
        state.currentPage = 1;
        applyFilters();
      });
    }

    // 5. Pagination Buttons
    if (dom.btnPagePrev) {
      dom.btnPagePrev.addEventListener('click', () => {
        if (state.currentPage > 1) {
          state.currentPage--;
          renderQuestionsView();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    if (dom.btnPageNext) {
      dom.btnPageNext.addEventListener('click', () => {
        const totalPages = Math.ceil(state.filteredQuestions.length / state.pageSize);
        if (state.currentPage < totalPages) {
          state.currentPage++;
          renderQuestionsView();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    // 6. MCQ Filters & Controls
    if (dom.mcqFilterSubject) dom.mcqFilterSubject.addEventListener('change', () => { state.mcqPage = 1; renderMcqView(); });
    if (dom.mcqFilterDifficulty) dom.mcqFilterDifficulty.addEventListener('change', () => { state.mcqPage = 1; renderMcqView(); });
    if (dom.mcqFilterStatus) dom.mcqFilterStatus.addEventListener('change', () => { state.mcqPage = 1; renderMcqView(); });

    if (dom.btnMcqPrev) {
      dom.btnMcqPrev.addEventListener('click', () => {
        if (state.mcqPage > 1) {
          state.mcqPage--;
          renderMcqView();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    if (dom.btnMcqNext) {
      dom.btnMcqNext.addEventListener('click', () => {
        state.mcqPage++;
        renderMcqView();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    if (dom.btnResetMcqScore) {
      dom.btnResetMcqScore.addEventListener('click', () => {
        if (confirm('Reset your assessment scorecard stats?')) {
          state.userAnswers = {};
          state.streak = 0;
          localStorage.removeItem('fresher_user_answers');
          localStorage.removeItem('fresher_streak');
          renderMcqView();
          showToast('Scorecard reset.');
        }
      });
    }

    // 7. Theory & Coding Filters
    if (dom.theoryFilterSubject) dom.theoryFilterSubject.addEventListener('change', renderTheoryView);
    if (dom.theoryFilterTopic) dom.theoryFilterTopic.addEventListener('change', renderTheoryView);
    if (dom.codingFilterSubject) dom.codingFilterSubject.addEventListener('change', renderCodingView);
    if (dom.codingFilterDifficulty) dom.codingFilterDifficulty.addEventListener('change', renderCodingView);

    // 8. Progress View Action
    if (dom.btnPracticeWeakNow) {
      dom.btnPracticeWeakNow.addEventListener('click', () => {
        const weakList = state.allQuestions.filter(q => state.needPracticeIds.has(q.id));
        if (weakList.length > 0) {
          openDrillModal();
          startDrill(weakList);
        } else {
          showToast('No weak areas marked yet. Flag questions as "Needs Practice" to drill them!');
        }
      });
    }

    // 9. Theme Switcher (Smooth Light/Dark toggle)
    if (dom.btnThemeToggle) {
      dom.btnThemeToggle.addEventListener('click', () => {
        const curr = document.documentElement.getAttribute('data-theme') || 'light';
        const next = curr === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', next);
        dom.btnThemeToggle.textContent = next === 'light' ? '🌙' : '☀️';
        localStorage.setItem('fresher_theme', next);
      });
    }

    // 10. Drill Modal Handlers
    if (dom.btnCloseDrillModal) {
      dom.btnCloseDrillModal.addEventListener('click', () => {
        dom.drillModal.classList.remove('active');
        state.drillSession.isActive = false;
        renderDashboard();
      });
    }

    if (dom.btnStartDrillSession) {
      dom.btnStartDrillSession.addEventListener('click', () => {
        const selSub = dom.drillSelectSubject ? dom.drillSelectSubject.value : 'All';
        const selDiff = dom.drillSelectDifficulty ? dom.drillSelectDifficulty.value : 'All';
        const countVal = dom.drillSelectCount ? dom.drillSelectCount.value : '20';

        let pool = state.allQuestions.slice();
        if (selSub !== 'All') pool = pool.filter(q => q.subject === selSub);
        if (selDiff !== 'All') pool = pool.filter(q => q.difficulty === selDiff);

        const limit = countVal === 'all' ? pool.length : parseInt(countVal, 10);
        startDrill(pool.slice(0, limit));
      });
    }

    if (dom.btnDrillWeakSession) {
      dom.btnDrillWeakSession.addEventListener('click', () => {
        const weakList = state.allQuestions.filter(q => state.needPracticeIds.has(q.id));
        if (weakList.length === 0) {
          showToast('No weak areas marked yet.');
          return;
        }
        startDrill(weakList);
      });
    }

    if (dom.btnDrillRevealAnswer) {
      dom.btnDrillRevealAnswer.addEventListener('click', () => {
        state.drillSession.answerRevealed = true;
        dom.drillAnswerDrawer.classList.add('expanded');
        dom.btnDrillRevealAnswer.style.display = 'none';
      });
    }

    if (dom.drillGotit) {
      dom.drillGotit.addEventListener('click', () => {
        const q = state.drillSession.questions[state.drillSession.currentIndex];
        state.drillSession.practicedCount++;
        state.practicedIds.add(q.id);
        state.needPracticeIds.delete(q.id);
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        showToast('✓ Marked Practiced');
        advanceDrill();
      });
    }

    if (dom.drillNeed) {
      dom.drillNeed.addEventListener('click', () => {
        const q = state.drillSession.questions[state.drillSession.currentIndex];
        state.drillSession.weakCount++;
        state.needPracticeIds.add(q.id);
        state.practicedIds.delete(q.id);
        localStorage.setItem('fresher_practiced_ids', JSON.stringify(Array.from(state.practicedIds)));
        localStorage.setItem('fresher_need_practice_ids', JSON.stringify(Array.from(state.needPracticeIds)));
        showToast('⚠ Flagged for Practice');
        advanceDrill();
      });
    }

    if (dom.drillPrevQ) {
      dom.drillPrevQ.addEventListener('click', () => {
        if (state.drillSession.currentIndex > 0) {
          state.drillSession.currentIndex--;
          renderCurrentDrillQuestion();
        }
      });
    }

    if (dom.drillNextQ) {
      dom.drillNextQ.addEventListener('click', advanceDrill);
    }

    if (dom.btnDrillAgain) {
      dom.btnDrillAgain.addEventListener('click', openDrillModal);
    }

    if (dom.btnCloseDrillSummary) {
      dom.btnCloseDrillSummary.addEventListener('click', () => {
        dom.drillModal.classList.remove('active');
        switchTab('dashboard');
      });
    }

    // 11. Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== dom.globalSearchInput) {
        e.preventDefault();
        if (dom.globalSearchInput) dom.globalSearchInput.focus();
      }
      if (e.key === 'Escape') {
        if (dom.drillModal && dom.drillModal.classList.contains('active')) {
          dom.drillModal.classList.remove('active');
        }
        if (dom.appSidebar && dom.appSidebar.classList.contains('open')) {
          dom.appSidebar.classList.remove('open');
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

  // App Initialization
  function init() {
    cacheDOMElements();

    // Load authentic dataset from global window object
    const rawData = window.FRESHER_QUESTIONS_DATA || window.FRESHER_QUESTIONS;
    if (rawData && Array.isArray(rawData)) {
      state.allQuestions = rawData;
    } else {
      console.error('FRESHER_QUESTIONS_DATA not loaded.');
      return;
    }

    // Apply stored theme (default light, matching crackedin developer aesthetic)
    const storedTheme = localStorage.getItem('fresher_theme') || 'light';
    document.documentElement.setAttribute('data-theme', storedTheme);
    if (dom.btnThemeToggle) {
      dom.btnThemeToggle.textContent = storedTheme === 'light' ? '🌙' : '☀️';
    }

    populateDropdowns();
    setupEventListeners();
    renderDashboard();
    updateHeaderBadges();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
