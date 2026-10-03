/**
 * Fresher Interview Practice — Modern Compact Q&A Drill Platform
 * Serious developer tool for freshers: Search, Filter, Practice, Drill, Master.
 */

(function () {
  'use strict';

  // Complete 22-Subject Curriculum
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

  // Application State
  const state = {
    allQuestions: [],
    filteredQuestions: [],

    // Filters
    selectedSubject: 'All',
    selectedTopic: 'All',
    selectedSubtopic: 'All',
    selectedDifficulty: 'All',
    selectedType: 'All',
    selectedRound: 'All',
    selectedFrequency: 'All',
    selectedStatus: 'All', // 'All', 'not_practiced', 'practiced', 'need_practice', 'saved'
    selectedSort: 'default',
    searchQuery: '',

    // Pagination
    currentPage: 1,
    pageSize: 50,

    // UI state
    allAnswersHidden: false,
    expandedAnswerIds: new Set(),
    fontSize: localStorage.getItem('fresher_font_size') || 'md',
    theme: localStorage.getItem('fresher_theme') || 'dark',

    // Real Persistent Practice State
    practicedIds: new Set(JSON.parse(localStorage.getItem('fresher_practiced_ids') || '[]')),
    needPracticeIds: new Set(JSON.parse(localStorage.getItem('fresher_need_practice_ids') || '[]')),
    savedIds: new Set(JSON.parse(localStorage.getItem('fresher_saved_ids') || '[]')),

    // Drill Mode State
    drillSession: {
      isActive: false,
      questions: [],
      currentIndex: 0,
      answerRevealed: false,
      practicedThisSession: new Set(),
      needPracticeThisSession: new Set()
    }
  };

  // DOM Elements Cache
  const dom = {};

  function cacheDOMElements() {
    dom.body = document.body;
    dom.searchInput = document.getElementById('search-input');
    dom.searchClear = document.getElementById('search-clear');
    dom.subjectScrollTrack = document.getElementById('subject-scroll-track');
    dom.topicSubtopicContainer = document.getElementById('topic-subtopic-container');
    dom.topicScrollTrack = document.getElementById('topic-scroll-track');
    dom.breadcrumbBar = document.getElementById('breadcrumb-bar');
    
    // Selects
    dom.selectTopic = document.getElementById('select-topic');
    dom.selectSubtopic = document.getElementById('select-subtopic');
    dom.selectDifficulty = document.getElementById('select-difficulty');
    dom.selectType = document.getElementById('select-type');
    dom.selectRound = document.getElementById('select-round');
    dom.selectFrequency = document.getElementById('select-frequency');
    dom.selectStatus = document.getElementById('select-status');
    dom.selectSort = document.getElementById('select-sort');
    dom.selectPageSize = document.getElementById('select-page-size');

    // Counts & Badges
    dom.resultsCountBadge = document.getElementById('results-count-badge');
    dom.weakCountHeader = document.getElementById('weak-count-header');
    dom.mobileFilterBadge = document.getElementById('mobile-filter-badge');
    dom.activeChipsBar = document.getElementById('active-chips-bar');
    dom.questionsList = document.getElementById('questions-list-container');

    // Buttons
    dom.btnStartDrill = document.getElementById('btn-start-drill');
    dom.btnQuickWeak = document.getElementById('btn-quick-weak');
    dom.btnToggleAllAnswers = document.getElementById('btn-toggle-all-answers');
    dom.btnToggleTheme = document.getElementById('btn-toggle-theme');
    dom.btnOpenDrawer = document.getElementById('btn-open-drawer');
    dom.btnCloseDrawer = document.getElementById('btn-close-drawer');
    dom.mobileDrawer = document.getElementById('mobile-drawer');
    dom.btnDrawerApply = document.getElementById('btn-drawer-apply');
    dom.btnDrawerClear = document.getElementById('btn-drawer-clear');

    // Drawer Inputs
    dom.drawerTopic = document.getElementById('drawer-topic');
    dom.drawerDifficulty = document.getElementById('drawer-difficulty');
    dom.drawerType = document.getElementById('drawer-type');
    dom.drawerRound = document.getElementById('drawer-round');
    dom.drawerStatus = document.getElementById('drawer-status');

    // Pagination
    dom.paginationBar = document.getElementById('pagination-bar');
    dom.btnPrevPage = document.getElementById('btn-prev-page');
    dom.btnNextPage = document.getElementById('btn-next-page');
    dom.pageIndicator = document.getElementById('page-indicator');

    // Drill Modal Elements
    dom.drillModal = document.getElementById('drill-modal');
    dom.btnCloseDrill = document.getElementById('btn-close-drill');
    dom.drillProgressText = document.getElementById('drill-progress-text');
    dom.drillProgressBarFill = document.getElementById('drill-progress-bar-fill');
    dom.drillSetupPanel = document.getElementById('drill-setup-panel');
    dom.drillRunnerPanel = document.getElementById('drill-runner-panel');
    dom.drillSummaryPanel = document.getElementById('drill-summary-panel');
    dom.drillRunnerFooter = document.getElementById('drill-runner-footer');
    dom.drillSubjectSelect = document.getElementById('drill-subject-select');
    dom.drillTopicSelect = document.getElementById('drill-topic-select');
    dom.drillDifficultySelect = document.getElementById('drill-difficulty-select');
    dom.drillTypeSelect = document.getElementById('drill-type-select');
    dom.drillCountSelect = document.getElementById('drill-count-select');
    dom.btnBeginDrill = document.getElementById('btn-begin-drill');
    dom.btnDrillWeakOnly = document.getElementById('btn-drill-weak-only');
    dom.drillQTitle = document.getElementById('drill-q-title');
    dom.drillQMeta = document.getElementById('drill-q-meta');
    dom.btnDrillRevealAnswer = document.getElementById('btn-drill-reveal-answer');
    dom.drillAnswerBox = document.getElementById('drill-answer-box');
    dom.drillAnswerText = document.getElementById('drill-answer-text');
    dom.drillExplanationWrap = document.getElementById('drill-explanation-wrap');
    dom.drillExplanationText = document.getElementById('drill-explanation-text');
    dom.drillCodeWrap = document.getElementById('drill-code-wrap');
    dom.drillCodeText = document.getElementById('drill-code-text');
    dom.drillFollowupWrap = document.getElementById('drill-followup-wrap');
    dom.drillFollowupText = document.getElementById('drill-followup-text');
    dom.btnDrillMarkGotit = document.getElementById('btn-drill-mark-gotit');
    dom.btnDrillMarkNeed = document.getElementById('btn-drill-mark-need');
    dom.btnDrillPrev = document.getElementById('btn-drill-prev');
    dom.btnDrillNext = document.getElementById('btn-drill-next');
    dom.drillSummaryStats = document.getElementById('drill-summary-stats');
    dom.drillWeakTopicsWrap = document.getElementById('drill-weak-topics-wrap');
    dom.drillWeakTopicsList = document.getElementById('drill-weak-topics-list');
    dom.btnDrillAgain = document.getElementById('btn-drill-again');
    dom.btnDrillPracticeWeakNow = document.getElementById('btn-drill-practice-weak-now');

    // Toast
    dom.toastMsg = document.getElementById('toast-msg');
  }

  // Toast Notice Helper
  let toastTimer = null;
  function showToast(message) {
    if (!dom.toastMsg) return;
    dom.toastMsg.textContent = message;
    dom.toastMsg.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      dom.toastMsg.classList.remove('show');
    }, 2200);
  }

  // Save Persistence
  function persistUserAction(key, set) {
    localStorage.setItem(key, JSON.stringify(Array.from(set)));
    updateWeakCountHeader();
  }

  function updateWeakCountHeader() {
    if (dom.weakCountHeader) {
      dom.weakCountHeader.textContent = state.needPracticeIds.size;
    }
  }

  // Canonical lookups for resilient URL normalization
  const CANONICAL_DIFFICULTIES = {
    'easy': 'Easy',
    'medium': 'Medium',
    'med': 'Medium',
    'fresher coding': 'Fresher Coding',
    'coding': 'Fresher Coding',
    'fresher-coding': 'Fresher Coding'
  };

  const CANONICAL_TYPES = {
    'concept': 'Concept',
    'coding': 'Coding',
    'scenario': 'Scenario',
    'output': 'Output',
    'sql query': 'SQL Query',
    'sql': 'SQL Query',
    'aptitude': 'Aptitude',
    'logical reasoning': 'Logical Reasoning',
    'logical': 'Logical Reasoning',
    'debugging': 'Debugging',
    'project': 'Project',
    'hr': 'HR'
  };

  const CANONICAL_ROUNDS = {
    'technical': 'Technical Round',
    'technical round': 'Technical Round',
    'online': 'Online Test',
    'online test': 'Online Test',
    'coding': 'Coding Round',
    'coding round': 'Coding Round',
    'project': 'Project Discussion',
    'project discussion': 'Project Discussion',
    'hr': 'HR Round',
    'hr round': 'HR Round'
  };

  const CANONICAL_STATUSES = {
    'not_practiced': 'not_practiced',
    'unpracticed': 'not_practiced',
    'practiced': 'practiced',
    'done': 'practiced',
    'need_practice': 'need_practice',
    'needs_practice': 'need_practice',
    'needs-practice': 'need_practice',
    'weak': 'need_practice',
    'saved': 'saved',
    'bookmarked': 'saved'
  };

  function normalizeSubject(val) {
    if (!val) return 'All';
    const clean = val.trim().toLowerCase();
    if (clean === 'all') return 'All';
    const found = SUBJECTS.find(s => s.toLowerCase() === clean);
    if (found) return found;
    if (clean === 'js' || clean === 'javascript') return 'JavaScript';
    if (clean === 'es6' || clean === 'es6+') return 'ES6+';
    if (clean === 'node' || clean === 'nodejs') return 'Node.js';
    if (clean === 'express' || clean === 'expressjs') return 'Express.js';
    if (clean === 'mongo' || clean === 'mongodb') return 'MongoDB';
    if (clean === 'react' || clean === 'reactjs') return 'React';
    if (clean === 'rest' || clean === 'http' || clean === 'rest-api' || clean === 'api' || clean === 'rest / http' || clean === 'rest api / http') return 'REST API / HTTP';
    if (clean === 'git' || clean === 'github' || clean === 'git / github') return 'Git / GitHub';
    if (clean === 'testing') return 'Testing';
    if (clean === 'web' || clean === 'web fundamentals') return 'Web Fundamentals';
    if (clean === 'projects' || clean === 'project' || clean === 'project interview') return 'Project Interview';
    if (clean === 'hr' || clean === 'communication' || clean === 'hr / communication') return 'HR / Communication';
    if (clean === 'reasoning' || clean === 'logical reasoning') return 'Logical Reasoning';
    return 'All';
  }

  // URL State Management (Sync query parameters)
  function readURLState() {
    const params = new URLSearchParams(window.location.search);
    if (params.has('subject')) {
      state.selectedSubject = normalizeSubject(params.get('subject'));
    }
    if (params.has('topic')) {
      state.selectedTopic = params.get('topic').trim();
    }
    if (params.has('subtopic')) {
      state.selectedSubtopic = params.get('subtopic').trim();
    }
    if (params.has('difficulty')) {
      const diffKey = params.get('difficulty').trim().toLowerCase();
      state.selectedDifficulty = CANONICAL_DIFFICULTIES[diffKey] || 'All';
    }
    if (params.has('type')) {
      const typeKey = params.get('type').trim().toLowerCase();
      state.selectedType = CANONICAL_TYPES[typeKey] || 'All';
    }
    if (params.has('round')) {
      const roundKey = params.get('round').trim().toLowerCase();
      state.selectedRound = CANONICAL_ROUNDS[roundKey] || 'All';
    }
    if (params.has('status')) {
      const statKey = params.get('status').trim().toLowerCase();
      state.selectedStatus = CANONICAL_STATUSES[statKey] || 'All';
    }
    if (params.has('sort')) {
      state.selectedSort = params.get('sort');
    }
    if (params.has('q')) {
      state.searchQuery = params.get('q');
      if (dom.searchInput) dom.searchInput.value = state.searchQuery;
    }
    if (params.has('page')) {
      state.currentPage = parseInt(params.get('page'), 10) || 1;
    }
  }

  function syncURLState() {
    const params = new URLSearchParams();
    if (state.selectedSubject !== 'All') params.set('subject', state.selectedSubject);
    if (state.selectedTopic !== 'All') params.set('topic', state.selectedTopic);
    if (state.selectedSubtopic !== 'All') params.set('subtopic', state.selectedSubtopic);
    if (state.selectedDifficulty !== 'All') params.set('difficulty', state.selectedDifficulty);
    if (state.selectedType !== 'All') params.set('type', state.selectedType);
    if (state.selectedRound !== 'All') params.set('round', state.selectedRound);
    if (state.selectedStatus !== 'All') params.set('status', state.selectedStatus);
    if (state.selectedSort !== 'default') params.set('sort', state.selectedSort);
    if (state.searchQuery) params.set('q', state.searchQuery);
    if (state.currentPage > 1) params.set('page', state.currentPage);

    const queryString = params.toString();
    const newRelativePathQuery = window.location.pathname + (queryString ? '?' + queryString : '');
    history.replaceState(null, '', newRelativePathQuery);
  }

  // Data Filtering Engine
  function applyFiltersAndSort() {
    let result = state.allQuestions.slice();

    // 1. Subject Filter (case-insensitive)
    if (state.selectedSubject !== 'All') {
      const normSub = state.selectedSubject.toLowerCase();
      result = result.filter(q => q.subject.toLowerCase() === normSub);
    }

    // 2. Topic Filter (flexible: matches topic or subtopic, case-insensitive)
    if (state.selectedTopic !== 'All') {
      const normTopic = state.selectedTopic.toLowerCase().trim();
      result = result.filter(q => {
        const qTop = (q.topic || '').toLowerCase();
        const qSub = (q.subTopic || '').toLowerCase();
        return qTop === normTopic || qTop.includes(normTopic) || qSub.includes(normTopic);
      });
    }

    // 3. Subtopic Filter (flexible: matches subtopic, case-insensitive)
    if (state.selectedSubtopic !== 'All') {
      const normSubtopic = state.selectedSubtopic.toLowerCase().trim();
      result = result.filter(q => {
        const qSub = (q.subTopic || '').toLowerCase();
        return qSub === normSubtopic || qSub.includes(normSubtopic);
      });
    }

    // 4. Difficulty Filter (case-insensitive)
    if (state.selectedDifficulty !== 'All') {
      const normDiff = state.selectedDifficulty.toLowerCase();
      result = result.filter(q => q.difficulty.toLowerCase() === normDiff);
    }

    // 5. Question Type Filter (case-insensitive)
    if (state.selectedType !== 'All') {
      const normType = state.selectedType.toLowerCase();
      result = result.filter(q => q.questionType.toLowerCase() === normType);
    }

    // 6. Interview Round Filter (case-insensitive)
    if (state.selectedRound !== 'All') {
      const normRound = state.selectedRound.toLowerCase();
      result = result.filter(q => q.interviewRound.toLowerCase() === normRound);
    }

    // 7. Frequency Filter (case-insensitive)
    if (state.selectedFrequency !== 'All') {
      const normFreq = state.selectedFrequency.toLowerCase();
      result = result.filter(q => q.frequency.toLowerCase() === normFreq);
    }

    // 8. Practice Status Filter
    if (state.selectedStatus !== 'All') {
      if (state.selectedStatus === 'practiced') {
        result = result.filter(q => state.practicedIds.has(q.id));
      } else if (state.selectedStatus === 'need_practice') {
        result = result.filter(q => state.needPracticeIds.has(q.id));
      } else if (state.selectedStatus === 'saved') {
        result = result.filter(q => state.savedIds.has(q.id));
      } else if (state.selectedStatus === 'not_practiced') {
        result = result.filter(q => !state.practicedIds.has(q.id) && !state.needPracticeIds.has(q.id));
      }
    }

    // 9. Search Query Filter (Normalized multi-term across all fields)
    if (state.searchQuery.trim()) {
      const rawQuery = state.searchQuery.toLowerCase().trim();
      const terms = rawQuery.split(/\s+/).filter(Boolean);
      result = result.filter(q => {
        const searchableContent = [
          q.question,
          q.answer,
          q.shortExplanation || '',
          q.subject,
          q.topic,
          q.subTopic || '',
          q.codeExample || '',
          q.followUpQuestions || '',
          q.references || ''
        ].join(' ').toLowerCase();
        return terms.every(term => searchableContent.includes(term));
      });
    }

    // 10. Sorting
    if (state.selectedSort === 'freq') {
      const freqOrder = { High: 3, Medium: 2, Low: 1 };
      result.sort((a, b) => (freqOrder[b.frequency] || 0) - (freqOrder[a.frequency] || 0));
    } else if (state.selectedSort === 'diff_asc') {
      const diffOrder = { Easy: 1, Medium: 2, 'Fresher Coding': 3 };
      result.sort((a, b) => (diffOrder[a.difficulty] || 2) - (diffOrder[b.difficulty] || 2));
    } else if (state.selectedSort === 'diff_desc') {
      const diffOrder = { Easy: 1, Medium: 2, 'Fresher Coding': 3 };
      result.sort((a, b) => (diffOrder[b.difficulty] || 2) - (diffOrder[a.difficulty] || 2));
    } else if (state.selectedSort === 'need_first') {
      result.sort((a, b) => (state.needPracticeIds.has(b.id) ? 1 : 0) - (state.needPracticeIds.has(a.id) ? 1 : 0));
    } else if (state.selectedSort === 'saved_first') {
      result.sort((a, b) => (state.savedIds.has(b.id) ? 1 : 0) - (state.savedIds.has(a.id) ? 1 : 0));
    } else {
      // Default natural order by question number
      result.sort((a, b) => (a.num || 0) - (b.num || 0));
    }

    state.filteredQuestions = result;

    // Reset pagination if out of range
    const maxPages = Math.max(1, Math.ceil(result.length / state.pageSize));
    if (state.currentPage > maxPages) {
      state.currentPage = 1;
    }

    syncURLState();
    renderAllViews();
  }

  // Render Master
  function renderAllViews() {
    renderSubjectBar();
    renderTopicBar();
    renderBreadcrumbs();
    renderFilterDropdowns();
    renderActiveChips();
    renderQuestionList();
    renderPagination();
    updateWeakCountHeader();
  }

  // Render Subject Navigation Strip
  function renderSubjectBar() {
    if (!dom.subjectScrollTrack) return;
    dom.subjectScrollTrack.innerHTML = '';

    SUBJECTS.forEach(sub => {
      const btn = document.createElement('button');
      btn.className = `subject-pill ${sub === state.selectedSubject ? 'active' : ''}`;
      
      // Calculate real count for subject
      let count = 0;
      if (sub === 'All') {
        count = state.allQuestions.length;
      } else {
        count = state.allQuestions.filter(q => q.subject === sub).length;
      }

      btn.innerHTML = `${sub} <span class="subject-count-badge">(${count})</span>`;
      btn.addEventListener('click', () => {
        state.selectedSubject = sub;
        state.selectedTopic = 'All';
        state.selectedSubtopic = 'All';
        state.currentPage = 1;
        applyFiltersAndSort();
      });

      dom.subjectScrollTrack.appendChild(btn);
    });
  }

  // Render Topic Navigation Bar
  function renderTopicBar() {
    if (!dom.topicSubtopicContainer || !dom.topicScrollTrack) return;

    if (state.selectedSubject === 'All') {
      dom.topicSubtopicContainer.classList.remove('visible');
      return;
    }

    dom.topicSubtopicContainer.classList.add('visible');
    dom.topicScrollTrack.innerHTML = '';

    // Collect topics for current subject
    const subjectQuestions = state.allQuestions.filter(q => q.subject === state.selectedSubject);
    const topics = Array.from(new Set(subjectQuestions.map(q => q.topic))).sort();

    // 'All Topics' pill
    const allBtn = document.createElement('button');
    allBtn.className = `topic-pill ${state.selectedTopic === 'All' ? 'active' : ''}`;
    allBtn.textContent = `All ${state.selectedSubject} Topics (${subjectQuestions.length})`;
    allBtn.addEventListener('click', () => {
      state.selectedTopic = 'All';
      state.selectedSubtopic = 'All';
      state.currentPage = 1;
      applyFiltersAndSort();
    });
    dom.topicScrollTrack.appendChild(allBtn);

    topics.forEach(t => {
      const tCount = subjectQuestions.filter(q => q.topic === t).length;
      const tBtn = document.createElement('button');
      tBtn.className = `topic-pill ${state.selectedTopic === t ? 'active' : ''}`;
      tBtn.textContent = `${t} (${tCount})`;
      tBtn.addEventListener('click', () => {
        state.selectedTopic = t;
        state.selectedSubtopic = 'All';
        state.currentPage = 1;
        applyFiltersAndSort();
      });
      dom.topicScrollTrack.appendChild(tBtn);
    });
  }

  // Render Breadcrumb Trail
  function renderBreadcrumbs() {
    if (!dom.breadcrumbBar) return;
    const parts = [
      `<a href="#" id="bc-home">Interview Questions</a>`
    ];

    if (state.selectedSubject !== 'All') {
      parts.push(`<span class="breadcrumb-separator">/</span>`);
      parts.push(`<a href="#" id="bc-subject">${escapeHtml(state.selectedSubject)}</a>`);
    }

    if (state.selectedTopic !== 'All') {
      parts.push(`<span class="breadcrumb-separator">/</span>`);
      parts.push(`<span class="breadcrumb-current">${escapeHtml(state.selectedTopic)}</span>`);
    }

    if (state.selectedSubtopic !== 'All') {
      parts.push(`<span class="breadcrumb-separator">/</span>`);
      parts.push(`<span class="breadcrumb-current">${escapeHtml(state.selectedSubtopic)}</span>`);
    }

    dom.breadcrumbBar.innerHTML = parts.join(' ');

    const bcHome = document.getElementById('bc-home');
    if (bcHome) {
      bcHome.addEventListener('click', (e) => {
        e.preventDefault();
        state.selectedSubject = 'All';
        state.selectedTopic = 'All';
        state.selectedSubtopic = 'All';
        applyFiltersAndSort();
      });
    }

    const bcSubject = document.getElementById('bc-subject');
    if (bcSubject) {
      bcSubject.addEventListener('click', (e) => {
        e.preventDefault();
        state.selectedTopic = 'All';
        state.selectedSubtopic = 'All';
        applyFiltersAndSort();
      });
    }
  }

  // Populate Filter Dropdowns dynamically
  function renderFilterDropdowns() {
    // 1. Populate Topics based on current subject
    if (dom.selectTopic) {
      const currentSubjectQuestions = state.selectedSubject === 'All' 
        ? state.allQuestions 
        : state.allQuestions.filter(q => q.subject === state.selectedSubject);
      
      const topics = Array.from(new Set(currentSubjectQuestions.map(q => q.topic))).sort();
      
      dom.selectTopic.innerHTML = '<option value="All">All Topics</option>' +
        topics.map(t => `<option value="${escapeHtml(t)}" ${t === state.selectedTopic ? 'selected' : ''}>${escapeHtml(t)}</option>`).join('');

      if (dom.drawerTopic) {
        dom.drawerTopic.innerHTML = dom.selectTopic.innerHTML;
      }
    }

    // 2. Populate Subtopics based on current topic
    if (dom.selectSubtopic) {
      let filteredSubtopicsPool = state.allQuestions;
      if (state.selectedSubject !== 'All') filteredSubtopicsPool = filteredSubtopicsPool.filter(q => q.subject === state.selectedSubject);
      if (state.selectedTopic !== 'All') filteredSubtopicsPool = filteredSubtopicsPool.filter(q => q.topic === state.selectedTopic);

      const subtopics = Array.from(new Set(filteredSubtopicsPool.map(q => q.subTopic))).sort();
      dom.selectSubtopic.innerHTML = '<option value="All">All Subtopics</option>' +
        subtopics.map(st => `<option value="${escapeHtml(st)}" ${st === state.selectedSubtopic ? 'selected' : ''}>${escapeHtml(st)}</option>`).join('');
    }

    // 3. Sync control values
    if (dom.selectDifficulty) dom.selectDifficulty.value = state.selectedDifficulty;
    if (dom.selectType) dom.selectType.value = state.selectedType;
    if (dom.selectRound) dom.selectRound.value = state.selectedRound;
    if (dom.selectFrequency) dom.selectFrequency.value = state.selectedFrequency;
    if (dom.selectStatus) dom.selectStatus.value = state.selectedStatus;
    if (dom.selectSort) dom.selectSort.value = state.selectedSort;

    // 4. Update Result indicator
    if (dom.resultsCountBadge) {
      dom.resultsCountBadge.textContent = `Showing ${state.filteredQuestions.length} of ${state.allQuestions.length} questions`;
    }

    // 5. Update mobile filter badge count
    let activeFilterCount = 0;
    if (state.selectedSubject !== 'All') activeFilterCount++;
    if (state.selectedTopic !== 'All') activeFilterCount++;
    if (state.selectedDifficulty !== 'All') activeFilterCount++;
    if (state.selectedType !== 'All') activeFilterCount++;
    if (state.selectedStatus !== 'All') activeFilterCount++;
    if (state.searchQuery.trim()) activeFilterCount++;

    if (dom.mobileFilterBadge) {
      dom.mobileFilterBadge.textContent = activeFilterCount > 0 ? `(${activeFilterCount})` : '';
    }
  }

  // Render Active Filter Chips
  function renderActiveChips() {
    if (!dom.activeChipsBar) return;
    const chips = [];

    if (state.selectedSubject !== 'All') {
      chips.push({ label: `Subject: ${state.selectedSubject}`, clear: () => state.selectedSubject = 'All' });
    }
    if (state.selectedTopic !== 'All') {
      chips.push({ label: `Topic: ${state.selectedTopic}`, clear: () => state.selectedTopic = 'All' });
    }
    if (state.selectedSubtopic !== 'All') {
      chips.push({ label: `Subtopic: ${state.selectedSubtopic}`, clear: () => state.selectedSubtopic = 'All' });
    }
    if (state.selectedDifficulty !== 'All') {
      chips.push({ label: `Difficulty: ${state.selectedDifficulty}`, clear: () => state.selectedDifficulty = 'All' });
    }
    if (state.selectedType !== 'All') {
      chips.push({ label: `Type: ${state.selectedType}`, clear: () => state.selectedType = 'All' });
    }
    if (state.selectedStatus !== 'All') {
      const statusLabels = { practiced: 'Practiced', need_practice: 'Needs Practice', saved: 'Saved', not_practiced: 'Not Practiced' };
      chips.push({ label: `Status: ${statusLabels[state.selectedStatus] || state.selectedStatus}`, clear: () => state.selectedStatus = 'All' });
    }
    if (state.searchQuery.trim()) {
      chips.push({ label: `Search: "${state.searchQuery}"`, clear: () => { state.searchQuery = ''; if (dom.searchInput) dom.searchInput.value = ''; } });
    }

    if (chips.length === 0) {
      dom.activeChipsBar.style.display = 'none';
      dom.activeChipsBar.innerHTML = '';
      return;
    }

    dom.activeChipsBar.style.display = 'flex';
    dom.activeChipsBar.innerHTML = '';

    chips.forEach(chip => {
      const el = document.createElement('span');
      el.className = 'filter-chip';
      el.innerHTML = `${escapeHtml(chip.label)} <button class="filter-chip-remove" aria-label="Remove filter">&times;</button>`;
      el.querySelector('.filter-chip-remove').addEventListener('click', () => {
        chip.clear();
        state.currentPage = 1;
        applyFiltersAndSort();
      });
      dom.activeChipsBar.appendChild(el);
    });

    const clearAllBtn = document.createElement('button');
    clearAllBtn.className = 'btn-clear-all-chips';
    clearAllBtn.textContent = 'Clear all filters';
    clearAllBtn.addEventListener('click', () => {
      state.selectedSubject = 'All';
      state.selectedTopic = 'All';
      state.selectedSubtopic = 'All';
      state.selectedDifficulty = 'All';
      state.selectedType = 'All';
      state.selectedRound = 'All';
      state.selectedFrequency = 'All';
      state.selectedStatus = 'All';
      state.searchQuery = '';
      if (dom.searchInput) dom.searchInput.value = '';
      state.currentPage = 1;
      applyFiltersAndSort();
    });
    dom.activeChipsBar.appendChild(clearAllBtn);
  }

  // Render Compact Question List
  function renderQuestionList() {
    if (!dom.questionsList) return;
    dom.questionsList.innerHTML = '';

    if (state.filteredQuestions.length === 0) {
      dom.questionsList.innerHTML = `
        <div class="empty-state-card">
          <div class="empty-state-title">No questions found</div>
          <p class="empty-state-desc">Try clearing your search keyword or relaxing active filters to see more results.</p>
          <button id="btn-empty-clear" class="btn-header-action btn-header-primary">Reset Filters</button>
        </div>
      `;
      const btnClear = document.getElementById('btn-empty-clear');
      if (btnClear) {
        btnClear.addEventListener('click', () => {
          state.selectedSubject = 'All';
          state.selectedTopic = 'All';
          state.selectedSubtopic = 'All';
          state.selectedDifficulty = 'All';
          state.selectedType = 'All';
          state.selectedStatus = 'All';
          state.searchQuery = '';
          if (dom.searchInput) dom.searchInput.value = '';
          state.currentPage = 1;
          applyFiltersAndSort();
        });
      }
      return;
    }

    // Pagination slice
    const startIndex = (state.currentPage - 1) * state.pageSize;
    const pagedQuestions = state.pageSize === Infinity 
      ? state.filteredQuestions 
      : state.filteredQuestions.slice(startIndex, startIndex + state.pageSize);

    pagedQuestions.forEach((q, idx) => {
      const globalIndex = startIndex + idx + 1;
      const isExpanded = !state.allAnswersHidden && state.expandedAnswerIds.has(q.id);

      const isPracticed = state.practicedIds.has(q.id);
      const isNeedPractice = state.needPracticeIds.has(q.id);
      const isSaved = state.savedIds.has(q.id);

      let diffClass = 'tag-diff-easy';
      if (q.difficulty === 'Medium') diffClass = 'tag-diff-medium';
      if (q.difficulty === 'Fresher Coding') diffClass = 'tag-diff-coding';

      const row = document.createElement('article');
      row.className = 'question-row';
      row.setAttribute('data-id', q.id);

      row.innerHTML = `
        <div class="question-header-line">
          <div class="question-title-area">
            <span class="q-index-num">${String(globalIndex).padStart(2, '0')}.</span>
            <h2 class="q-text-title">${escapeHtml(q.question)}</h2>
          </div>
        </div>

        <div class="q-meta-tags">
          <span class="tag-badge tag-subject">${escapeHtml(q.subject)}</span>
          <span class="tag-badge">${escapeHtml(q.topic)}</span>
          <span class="tag-badge">${escapeHtml(q.subTopic)}</span>
          <span class="tag-badge ${diffClass}">${escapeHtml(q.difficulty)}</span>
          <span class="tag-badge">${escapeHtml(q.questionType)}</span>
          <span class="tag-badge">${escapeHtml(q.interviewRound)}</span>
          ${isPracticed ? '<span class="tag-badge tag-status-practiced">✓ Practiced</span>' : ''}
          ${isNeedPractice ? '<span class="tag-badge tag-status-need">⚠ Needs Practice</span>' : ''}
          ${isSaved ? '<span class="tag-badge tag-status-saved">★ Saved</span>' : ''}
        </div>

        <div class="q-action-bar">
          <button class="btn-q-action btn-q-toggle-answer" data-id="${q.id}">
            ${isExpanded ? '▲ Hide Answer' : '▼ Show Answer'}
          </button>
          <button class="btn-q-action btn-act-practice ${isPracticed ? 'active-practiced' : ''}" data-id="${q.id}" title="Toggle practiced status">
            ${isPracticed ? '✓ Practiced' : 'Mark Practiced'}
          </button>
          <button class="btn-q-action btn-act-need ${isNeedPractice ? 'active-need' : ''}" data-id="${q.id}" title="Flag as needing further practice">
            ${isNeedPractice ? '⚠ Needs Practice' : 'Needs Practice'}
          </button>
          <button class="btn-q-action btn-act-save ${isSaved ? 'active-saved' : ''}" data-id="${q.id}" title="Bookmark question">
            ${isSaved ? '★ Saved' : '☆ Save'}
          </button>
        </div>

        <!-- Collapsible Answer Drawer -->
        <div class="q-answer-details ${isExpanded ? 'expanded' : ''}" id="answer-${q.id}">
          <div class="answer-section-label">Interview Answer</div>
          <div class="answer-text-content">${escapeHtml(q.answer)}</div>

          ${q.shortExplanation ? `
            <div class="answer-section-label">Key Explanation</div>
            <div class="answer-explanation">${escapeHtml(q.shortExplanation)}</div>
          ` : ''}

          ${q.codeExample ? `
            <div class="answer-section-label">Code Example</div>
            <div class="code-snippet-box">
              <div class="code-header">
                <span>Code snippet</span>
                <button class="btn-copy-code" data-code="${escapeHtml(q.codeExample)}">Copy</button>
              </div>
              <pre><code>${escapeHtml(q.codeExample)}</code></pre>
            </div>
          ` : ''}

          ${q.followUpQuestions ? `
            <div class="q-followup-box">
              <strong>Follow-Up:</strong> ${escapeHtml(q.followUpQuestions)}
            </div>
          ` : ''}

          ${q.references ? `
            <div class="q-reference-line">
              <strong>Reference:</strong> ${escapeHtml(q.references)}
            </div>
          ` : ''}
        </div>
      `;

      // Event Listeners for Row Actions
      const titleEl = row.querySelector('.q-text-title');
      const toggleBtn = row.querySelector('.btn-q-toggle-answer');
      const detailsEl = row.querySelector('.q-answer-details');

      const toggleAction = () => {
        if (state.expandedAnswerIds.has(q.id)) {
          state.expandedAnswerIds.delete(q.id);
          detailsEl.classList.remove('expanded');
          toggleBtn.textContent = '▼ Show Answer';
        } else {
          state.expandedAnswerIds.add(q.id);
          detailsEl.classList.add('expanded');
          toggleBtn.textContent = '▲ Hide Answer';
        }
      };

      titleEl.addEventListener('click', toggleAction);
      toggleBtn.addEventListener('click', toggleAction);

      // Practice status toggle
      const btnPractice = row.querySelector('.btn-act-practice');
      btnPractice.addEventListener('click', () => {
        if (state.practicedIds.has(q.id)) {
          state.practicedIds.delete(q.id);
          showToast(`Unmarked question #${globalIndex}`);
        } else {
          state.practicedIds.add(q.id);
          state.needPracticeIds.delete(q.id); // Mutually exclusive
          showToast(`Marked #${globalIndex} as Practiced!`);
        }
        persistUserAction('fresher_practiced_ids', state.practicedIds);
        persistUserAction('fresher_need_practice_ids', state.needPracticeIds);
        applyFiltersAndSort();
      });

      // Needs Practice toggle
      const btnNeed = row.querySelector('.btn-act-need');
      btnNeed.addEventListener('click', () => {
        if (state.needPracticeIds.has(q.id)) {
          state.needPracticeIds.delete(q.id);
          showToast(`Removed #${globalIndex} from Weak Areas`);
        } else {
          state.needPracticeIds.add(q.id);
          state.practicedIds.delete(q.id);
          showToast(`Added #${globalIndex} to Weak Areas for drill`);
        }
        persistUserAction('fresher_practiced_ids', state.practicedIds);
        persistUserAction('fresher_need_practice_ids', state.needPracticeIds);
        applyFiltersAndSort();
      });

      // Save toggle
      const btnSave = row.querySelector('.btn-act-save');
      btnSave.addEventListener('click', () => {
        if (state.savedIds.has(q.id)) {
          state.savedIds.delete(q.id);
          showToast(`Removed #${globalIndex} from Saved`);
        } else {
          state.savedIds.add(q.id);
          showToast(`Saved #${globalIndex} to Bookmarks`);
        }
        persistUserAction('fresher_saved_ids', state.savedIds);
        applyFiltersAndSort();
      });

      // Copy Code Button
      const copyBtn = row.querySelector('.btn-copy-code');
      if (copyBtn) {
        copyBtn.addEventListener('click', () => {
          const rawCode = q.codeExample || '';
          navigator.clipboard.writeText(rawCode).then(() => {
            copyBtn.classList.add('copied');
            copyBtn.textContent = '✓ Copied!';
            setTimeout(() => {
              copyBtn.classList.remove('copied');
              copyBtn.textContent = 'Copy';
            }, 1500);
          });
        });
      }

      dom.questionsList.appendChild(row);
    });
  }

  // Render Pagination Bar
  function renderPagination() {
    if (!dom.paginationBar) return;

    if (state.pageSize === Infinity || state.filteredQuestions.length <= state.pageSize) {
      dom.paginationBar.style.display = 'none';
      return;
    }

    dom.paginationBar.style.display = 'flex';
    const totalPages = Math.ceil(state.filteredQuestions.length / state.pageSize);

    if (dom.pageIndicator) {
      dom.pageIndicator.textContent = `Page ${state.currentPage} of ${totalPages}`;
    }

    if (dom.btnPrevPage) {
      dom.btnPrevPage.disabled = state.currentPage <= 1;
    }

    if (dom.btnNextPage) {
      dom.btnNextPage.disabled = state.currentPage >= totalPages;
    }
  }

  // Dynamic Drill Topics Helper
  function updateDrillTopics(sub) {
    if (!dom.drillTopicSelect) return;
    const pool = sub === 'All' ? state.allQuestions : state.allQuestions.filter(q => q.subject === sub);
    const topics = Array.from(new Set(pool.map(q => q.topic).filter(Boolean))).sort();
    dom.drillTopicSelect.innerHTML = '<option value="All">All Topics</option>' +
      topics.map(t => `<option value="${escapeHtml(t)}">${escapeHtml(t)}</option>`).join('');
  }

  // Drill Mode Engine
  function openDrillSetup() {
    if (!dom.drillModal) return;
    state.drillSession.isActive = true;

    // Prepopulate drill subject select
    if (dom.drillSubjectSelect) {
      dom.drillSubjectSelect.innerHTML = `<option value="All">All Subjects (${state.allQuestions.length} Qs)</option>` +
        SUBJECTS.filter(s => s !== 'All').map(s => {
          const cnt = state.allQuestions.filter(q => q.subject === s).length;
          return `<option value="${s}" ${s === state.selectedSubject ? 'selected' : ''}>${s} (${cnt} Qs)</option>`;
        }).join('');

      updateDrillTopics(dom.drillSubjectSelect.value);
    }

    // Reset views
    dom.drillSetupPanel.style.display = 'block';
    dom.drillRunnerPanel.style.display = 'none';
    dom.drillSummaryPanel.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'none';
    dom.drillProgressText.textContent = 'Drill Setup';
    dom.drillProgressBarFill.style.width = '0%';

    dom.drillModal.classList.add('active');
  }

  function startDrillSession(questionsList) {
    if (questionsList.length === 0) {
      showToast('No questions match drill criteria. Try broader filters.');
      return;
    }

    // Shuffle questions lightly for active drill variety
    const shuffled = questionsList.slice().sort(() => Math.random() - 0.5);

    state.drillSession.questions = shuffled;
    state.drillSession.currentIndex = 0;
    state.drillSession.answerRevealed = false;
    state.drillSession.practicedThisSession.clear();
    state.drillSession.needPracticeThisSession.clear();

    dom.drillSetupPanel.style.display = 'none';
    dom.drillRunnerPanel.style.display = 'block';
    dom.drillSummaryPanel.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'flex';

    renderCurrentDrillQuestion();
  }

  function renderCurrentDrillQuestion() {
    const session = state.drillSession;
    const q = session.questions[session.currentIndex];
    const total = session.questions.length;
    const currentNum = session.currentIndex + 1;

    dom.drillProgressText.textContent = `Question ${currentNum} of ${total}`;
    dom.drillProgressBarFill.style.width = `${(currentNum / total) * 100}%`;

    dom.drillQTitle.textContent = q.question;
    dom.drillQMeta.innerHTML = `
      <span class="tag-badge tag-subject">${escapeHtml(q.subject)}</span>
      <span class="tag-badge">${escapeHtml(q.topic)}</span>
      <span class="tag-badge tag-diff-${q.difficulty.toLowerCase().replace(' ', '-')}">${escapeHtml(q.difficulty)}</span>
    `;

    // Reset answer reveal
    session.answerRevealed = false;
    dom.drillAnswerBox.classList.remove('revealed');
    dom.btnDrillRevealAnswer.style.display = 'inline-flex';

    // Populate answer data
    dom.drillAnswerText.textContent = q.answer;

    if (q.shortExplanation) {
      dom.drillExplanationWrap.style.display = 'block';
      dom.drillExplanationText.textContent = q.shortExplanation;
    } else {
      dom.drillExplanationWrap.style.display = 'none';
    }

    if (q.codeExample) {
      dom.drillCodeWrap.style.display = 'block';
      dom.drillCodeText.textContent = q.codeExample;
    } else {
      dom.drillCodeWrap.style.display = 'none';
    }

    if (q.followUpQuestions) {
      dom.drillFollowupWrap.style.display = 'block';
      dom.drillFollowupText.textContent = q.followUpQuestions;
    } else {
      dom.drillFollowupWrap.style.display = 'none';
    }

    // Pagination buttons
    dom.btnDrillPrev.disabled = session.currentIndex === 0;
    dom.btnDrillNext.textContent = session.currentIndex === total - 1 ? 'Finish Drill ✓' : 'Next →';
  }

  function completeDrillSession() {
    const session = state.drillSession;
    dom.drillRunnerPanel.style.display = 'none';
    dom.drillRunnerFooter.style.display = 'none';
    dom.drillSummaryPanel.style.display = 'block';

    dom.drillProgressText.textContent = 'Drill Complete';
    dom.drillProgressBarFill.style.width = '100%';

    const total = session.questions.length;
    const practicedCount = session.practicedThisSession.size;
    const needPracticeCount = session.needPracticeThisSession.size;

    dom.drillSummaryStats.innerHTML = `
      <strong>${total} questions practiced</strong><br>
      <span style="color:var(--accent-green);">✓ Mastered: ${practicedCount}</span> &nbsp;|&nbsp; 
      <span style="color:var(--accent-rose);">⚠ Needs More Practice: ${needPracticeCount}</span>
    `;

    // Derive real weak topics
    if (needPracticeCount > 0) {
      dom.drillWeakTopicsWrap.style.display = 'block';
      dom.drillWeakTopicsList.innerHTML = '';
      const weakTopics = new Set();
      session.questions.forEach(q => {
        if (session.needPracticeThisSession.has(q.id)) {
          weakTopics.add(`${q.subject} → ${q.topic}`);
        }
      });
      weakTopics.forEach(wt => {
        const li = document.createElement('li');
        li.textContent = wt;
        dom.drillWeakTopicsList.appendChild(li);
      });
    } else {
      dom.drillWeakTopicsWrap.style.display = 'none';
    }
  }

  function closeDrillModal() {
    if (!dom.drillModal) return;
    dom.drillModal.classList.remove('active');
    state.drillSession.isActive = false;
    applyFiltersAndSort(); // refresh main view with any drill status updates
  }

  // Event Listeners Setup
  function setupEventListeners() {
    // 1. Search with Debounce
    let searchDebounceTimer = null;
    if (dom.searchInput) {
      dom.searchInput.addEventListener('input', (e) => {
        clearTimeout(searchDebounceTimer);
        const val = e.target.value;
        if (dom.searchClear) {
          dom.searchClear.style.display = val ? 'block' : 'none';
        }
        searchDebounceTimer = setTimeout(() => {
          state.searchQuery = val;
          state.currentPage = 1;
          applyFiltersAndSort();
        }, 150);
      });
    }

    if (dom.searchClear) {
      dom.searchClear.addEventListener('click', () => {
        if (dom.searchInput) dom.searchInput.value = '';
        dom.searchClear.style.display = 'none';
        state.searchQuery = '';
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    // 2. Selects
    if (dom.selectTopic) {
      dom.selectTopic.addEventListener('change', (e) => {
        state.selectedTopic = e.target.value;
        state.selectedSubtopic = 'All';
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectSubtopic) {
      dom.selectSubtopic.addEventListener('change', (e) => {
        state.selectedSubtopic = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectDifficulty) {
      dom.selectDifficulty.addEventListener('change', (e) => {
        state.selectedDifficulty = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectType) {
      dom.selectType.addEventListener('change', (e) => {
        state.selectedType = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectRound) {
      dom.selectRound.addEventListener('change', (e) => {
        state.selectedRound = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectFrequency) {
      dom.selectFrequency.addEventListener('change', (e) => {
        state.selectedFrequency = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectStatus) {
      dom.selectStatus.addEventListener('change', (e) => {
        state.selectedStatus = e.target.value;
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    if (dom.selectSort) {
      dom.selectSort.addEventListener('change', (e) => {
        state.selectedSort = e.target.value;
        applyFiltersAndSort();
      });
    }

    if (dom.selectPageSize) {
      dom.selectPageSize.addEventListener('change', (e) => {
        state.pageSize = e.target.value === 'all' ? Infinity : parseInt(e.target.value, 10);
        state.currentPage = 1;
        applyFiltersAndSort();
      });
    }

    // 3. Quick Weak Areas Button
    if (dom.btnQuickWeak) {
      dom.btnQuickWeak.addEventListener('click', () => {
        state.selectedStatus = 'need_practice';
        state.currentPage = 1;
        applyFiltersAndSort();
        showToast('Filtering to questions marked as Needs Practice');
      });
    }

    // 4. Toggle Show / Hide All Answers
    if (dom.btnToggleAllAnswers) {
      dom.btnToggleAllAnswers.addEventListener('click', () => {
        state.allAnswersHidden = !state.allAnswersHidden;
        if (state.allAnswersHidden) {
          state.expandedAnswerIds.clear();
          dom.btnToggleAllAnswers.textContent = '👁 Show Answers';
          showToast('All answers hidden for self-testing');
        } else {
          state.filteredQuestions.forEach(q => state.expandedAnswerIds.add(q.id));
          dom.btnToggleAllAnswers.textContent = '🙈 Hide All Answers';
          showToast('All answers revealed');
        }
        renderQuestionList();
      });
    }

    // 5. Typography Font Scaler
    document.querySelectorAll('.btn-font-scale').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.btn-font-scale').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const size = btn.getAttribute('data-size');
        dom.body.className = `font-${size}`;
        localStorage.setItem('fresher_font_size', size);
      });
    });

    // 6. Theme Switcher
    if (dom.btnToggleTheme) {
      dom.btnToggleTheme.addEventListener('click', () => {
        const curr = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = curr === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        dom.btnToggleTheme.textContent = next === 'dark' ? '🌙' : '☀️';
        localStorage.setItem('fresher_theme', next);
      });
    }

    // 7. Mobile Drawer
    if (dom.btnOpenDrawer && dom.mobileDrawer) {
      dom.btnOpenDrawer.addEventListener('click', () => {
        dom.mobileDrawer.classList.add('open');
      });
    }

    if (dom.btnCloseDrawer && dom.mobileDrawer) {
      dom.btnCloseDrawer.addEventListener('click', () => {
        dom.mobileDrawer.classList.remove('open');
      });
    }

    if (dom.btnDrawerApply && dom.mobileDrawer) {
      dom.btnDrawerApply.addEventListener('click', () => {
        if (dom.drawerTopic) state.selectedTopic = dom.drawerTopic.value;
        if (dom.drawerDifficulty) state.selectedDifficulty = dom.drawerDifficulty.value;
        if (dom.drawerType) state.selectedType = dom.drawerType.value;
        if (dom.drawerRound) state.selectedRound = dom.drawerRound.value;
        if (dom.drawerStatus) state.selectedStatus = dom.drawerStatus.value;
        state.currentPage = 1;
        dom.mobileDrawer.classList.remove('open');
        applyFiltersAndSort();
      });
    }

    if (dom.btnDrawerClear && dom.mobileDrawer) {
      dom.btnDrawerClear.addEventListener('click', () => {
        state.selectedTopic = 'All';
        state.selectedDifficulty = 'All';
        state.selectedType = 'All';
        state.selectedRound = 'All';
        state.selectedStatus = 'All';
        state.currentPage = 1;
        dom.mobileDrawer.classList.remove('open');
        applyFiltersAndSort();
      });
    }

    // 8. Pagination Navigation
    if (dom.btnPrevPage) {
      dom.btnPrevPage.addEventListener('click', () => {
        if (state.currentPage > 1) {
          state.currentPage--;
          applyFiltersAndSort();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    if (dom.btnNextPage) {
      dom.btnNextPage.addEventListener('click', () => {
        const totalPages = Math.ceil(state.filteredQuestions.length / state.pageSize);
        if (state.currentPage < totalPages) {
          state.currentPage++;
          applyFiltersAndSort();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    // 9. Drill Mode Handlers
    if (dom.btnStartDrill) {
      dom.btnStartDrill.addEventListener('click', openDrillSetup);
    }

    if (dom.btnCloseDrill) {
      dom.btnCloseDrill.addEventListener('click', closeDrillModal);
    }

    if (dom.drillSubjectSelect) {
      dom.drillSubjectSelect.addEventListener('change', (e) => {
        updateDrillTopics(e.target.value);
      });
    }

    if (dom.btnBeginDrill) {
      dom.btnBeginDrill.addEventListener('click', () => {
        const selSub = dom.drillSubjectSelect ? dom.drillSubjectSelect.value : 'All';
        const selTop = dom.drillTopicSelect ? dom.drillTopicSelect.value : 'All';
        const selDiff = dom.drillDifficultySelect ? dom.drillDifficultySelect.value : 'All';
        const selType = dom.drillTypeSelect ? dom.drillTypeSelect.value : 'All';
        const countVal = dom.drillCountSelect ? dom.drillCountSelect.value : '20';

        let pool = state.allQuestions.slice();
        if (selSub !== 'All') pool = pool.filter(q => q.subject === selSub);
        if (selTop !== 'All') pool = pool.filter(q => q.topic === selTop || (q.subTopic && q.subTopic === selTop));
        if (selDiff !== 'All') pool = pool.filter(q => q.difficulty === selDiff);
        if (selType !== 'All') pool = pool.filter(q => q.questionType === selType);

        if (pool.length === 0) {
          showToast('No questions match this filter combination. Try broader filters.');
          return;
        }

        const limit = countVal === 'all' ? pool.length : parseInt(countVal, 10);
        if (pool.length < limit && countVal !== 'all') {
          showToast(`Found ${pool.length} matching questions. Starting drill with all ${pool.length}.`);
        }
        startDrillSession(pool.slice(0, limit));
      });
    }

    if (dom.btnDrillWeakOnly) {
      dom.btnDrillWeakOnly.addEventListener('click', () => {
        const weakPool = state.allQuestions.filter(q => state.needPracticeIds.has(q.id));
        if (weakPool.length === 0) {
          showToast('No weak areas marked yet. Tap "Needs Practice" on questions you want to drill!');
          return;
        }
        startDrillSession(weakPool);
      });
    }

    if (dom.btnDrillRevealAnswer) {
      dom.btnDrillRevealAnswer.addEventListener('click', () => {
        state.drillSession.answerRevealed = true;
        dom.drillAnswerBox.classList.add('revealed');
        dom.btnDrillRevealAnswer.style.display = 'none';
      });
    }

    if (dom.btnDrillMarkGotit) {
      dom.btnDrillMarkGotit.addEventListener('click', () => {
        const q = state.drillSession.questions[state.drillSession.currentIndex];
        state.drillSession.practicedThisSession.add(q.id);
        state.drillSession.needPracticeThisSession.delete(q.id);
        state.practicedIds.add(q.id);
        state.needPracticeIds.delete(q.id);
        persistUserAction('fresher_practiced_ids', state.practicedIds);
        persistUserAction('fresher_need_practice_ids', state.needPracticeIds);
        showToast('✓ Marked as Practiced!');
        advanceDrill();
      });
    }

    if (dom.btnDrillMarkNeed) {
      dom.btnDrillMarkNeed.addEventListener('click', () => {
        const q = state.drillSession.questions[state.drillSession.currentIndex];
        state.drillSession.needPracticeThisSession.add(q.id);
        state.drillSession.practicedThisSession.delete(q.id);
        state.needPracticeIds.add(q.id);
        state.practicedIds.delete(q.id);
        persistUserAction('fresher_practiced_ids', state.practicedIds);
        persistUserAction('fresher_need_practice_ids', state.needPracticeIds);
        showToast('⚠ Added to Weak Areas');
        advanceDrill();
      });
    }

    function advanceDrill() {
      const session = state.drillSession;
      if (session.currentIndex < session.questions.length - 1) {
        session.currentIndex++;
        renderCurrentDrillQuestion();
      } else {
        completeDrillSession();
      }
    }

    if (dom.btnDrillPrev) {
      dom.btnDrillPrev.addEventListener('click', () => {
        if (state.drillSession.currentIndex > 0) {
          state.drillSession.currentIndex--;
          renderCurrentDrillQuestion();
        }
      });
    }

    if (dom.btnDrillNext) {
      dom.btnDrillNext.addEventListener('click', advanceDrill);
    }

    if (dom.btnDrillAgain) {
      dom.btnDrillAgain.addEventListener('click', openDrillSetup);
    }

    if (dom.btnDrillPracticeWeakNow) {
      dom.btnDrillPracticeWeakNow.addEventListener('click', () => {
        const weakPool = state.allQuestions.filter(q => state.needPracticeIds.has(q.id));
        if (weakPool.length > 0) {
          startDrillSession(weakPool);
        } else {
          closeDrillModal();
        }
      });
    }

    // Keyboard navigation shortcuts
    window.addEventListener('keydown', (e) => {
      // Active Drill keyboard shortcuts
      if (state.drillSession.isActive) {
        if (e.key === 'Escape') {
          closeDrillModal();
          return;
        }
        if ((e.key === ' ' || e.key === 'Enter') && !state.drillSession.answerRevealed) {
          e.preventDefault();
          if (dom.btnDrillRevealAnswer) dom.btnDrillRevealAnswer.click();
          return;
        }
        if (state.drillSession.answerRevealed) {
          if (e.key === 'g' || e.key === 'G' || e.key === '1') {
            e.preventDefault();
            if (dom.btnDrillMarkGotit) dom.btnDrillMarkGotit.click();
            return;
          }
          if (e.key === 'p' || e.key === 'P' || e.key === 'w' || e.key === 'W' || e.key === '2') {
            e.preventDefault();
            if (dom.btnDrillMarkNeed) dom.btnDrillMarkNeed.click();
            return;
          }
        }
        if (e.key === 'ArrowRight') {
          e.preventDefault();
          if (dom.btnDrillNext) dom.btnDrillNext.click();
          return;
        }
        if (e.key === 'ArrowLeft') {
          e.preventDefault();
          if (dom.btnDrillPrev) dom.btnDrillPrev.click();
          return;
        }
      }

      // Global shortcuts
      if (e.key === '/' && document.activeElement !== dom.searchInput) {
        e.preventDefault();
        dom.searchInput.focus();
      }
      if (e.key === 'Escape') {
        if (dom.mobileDrawer && dom.mobileDrawer.classList.contains('open')) {
          dom.mobileDrawer.classList.remove('open');
        }
      }
    });

    // Browser back/forward sync
    window.addEventListener('popstate', () => {
      readURLState();
      applyFiltersAndSort();
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

    // Load data from global window object
    const rawData = window.FRESHER_QUESTIONS_DATA || window.FRESHER_QUESTIONS;
    if (rawData && Array.isArray(rawData)) {
      state.allQuestions = rawData;
    } else {
      console.error('FRESHER_QUESTIONS_DATA not found on window object.');
      return;
    }

    // Apply stored font size & theme
    if (state.fontSize && dom.body) {
      dom.body.className = `font-${state.fontSize}`;
      document.querySelectorAll('.btn-font-scale').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-size') === state.fontSize);
      });
    }

    if (state.theme) {
      document.documentElement.setAttribute('data-theme', state.theme);
      if (dom.btnToggleTheme) {
        dom.btnToggleTheme.textContent = state.theme === 'dark' ? '🌙' : '☀️';
      }
    }

    readURLState();
    setupEventListeners();
    applyFiltersAndSort();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
