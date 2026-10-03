/**
 * Smart Workspace Controller - Fresher Interview Platform
 * Split Master-Detail & Smart Space Layout
 */

(function () {
  'use strict';

  const SUBJECTS = [
    'All',
    'HTML',
    'CSS',
    'JavaScript',
    'ES6',
    'DOM',
    'jQuery',
    'React',
    'Node.js',
    'Express',
    'SQL',
    'MongoDB',
    'Aptitude',
    'Problem Solving',
    'DSA',
    'Coding',
    'Projects',
    'HR'
  ];

  const state = {
    allQuestions: [],
    filteredQuestions: [],
    selectedQuestion: null,
    
    // Filters
    selectedSubject: 'All',
    selectedFilterTag: 'all', // 'all', 'saved', 'needs_practice', 'practiced'
    selectedDifficulty: 'All',
    selectedType: 'All',
    searchQuery: '',
    sortBy: 'default',
    
    // Persistent Sets
    practicedIds: new Set(),
    needPracticeIds: new Set(),
    savedIds: new Set(),
    
    // Modes
    hideAnswers: false,
    
    // Scratchpad notes per question
    notes: {}
  };

  let dom = {};

  function init() {
    loadStorage();
    cacheDom();
    bindEvents();

    if (window.FRESHER_QUESTIONS_DATA && Array.isArray(window.FRESHER_QUESTIONS_DATA)) {
      state.allQuestions = window.FRESHER_QUESTIONS_DATA;
    } else {
      console.error('Questions data missing!');
    }

    renderSidebarSubjects();
    applyFilters();
  }

  function loadStorage() {
    try {
      const data = JSON.parse(localStorage.getItem('fresher_smart_state') || '{}');
      if (Array.isArray(data.practiced)) state.practicedIds = new Set(data.practiced);
      if (Array.isArray(data.needPractice)) state.needPracticeIds = new Set(data.needPractice);
      if (Array.isArray(data.saved)) state.savedIds = new Set(data.saved);
      if (data.notes && typeof data.notes === 'object') state.notes = data.notes;

      const theme = localStorage.getItem('fresher_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', theme);
    } catch (e) {
      console.warn('Storage read error:', e);
    }
  }

  function saveStorage() {
    try {
      const payload = {
        practiced: [...state.practicedIds],
        needPractice: [...state.needPracticeIds],
        saved: [...state.savedIds],
        notes: state.notes
      };
      localStorage.setItem('fresher_smart_state', JSON.stringify(payload));
    } catch (e) {
      console.warn('Storage save error:', e);
    }
  }

  function cacheDom() {
    dom = {
      // Topbar
      searchInput: document.getElementById('smart-search-input'),
      btnStartDrill: document.getElementById('btn-top-drill'),
      btnPracticeWeak: document.getElementById('btn-top-weak'),
      btnToggleAnswers: document.getElementById('btn-top-hide'),
      themeToggle: document.getElementById('btn-top-theme'),
      
      // Sidebar
      sidebarSubjects: document.getElementById('sidebar-subjects'),
      sidebarFilterAll: document.getElementById('sidebar-filter-all'),
      sidebarFilterSaved: document.getElementById('sidebar-filter-saved'),
      sidebarFilterNeed: document.getElementById('sidebar-filter-need'),
      sidebarFilterPracticed: document.getElementById('sidebar-filter-practiced'),
      
      countAll: document.getElementById('count-all'),
      countSaved: document.getElementById('count-saved'),
      countNeed: document.getElementById('count-need'),
      countPracticed: document.getElementById('count-practiced'),
      
      // List Pane
      listCount: document.getElementById('list-count'),
      questionsList: document.getElementById('questions-list'),
      pillDiffs: document.querySelectorAll('.pill-diff'),
      pillTypes: document.querySelectorAll('.pill-type'),
      
      // Reader Pane
      readerPane: document.getElementById('reader-pane'),
      readerTitle: document.getElementById('reader-title'),
      badgeSubject: document.getElementById('badge-subject'),
      badgeTopic: document.getElementById('badge-topic'),
      badgeDiff: document.getElementById('badge-diff'),
      badgeType: document.getElementById('badge-type'),
      
      btnMarkPracticed: document.getElementById('btn-mark-practiced'),
      btnMarkNeed: document.getElementById('btn-mark-need'),
      btnMarkSaved: document.getElementById('btn-mark-saved'),
      btnCopyQ: document.getElementById('btn-copy-q'),
      
      readerAnswer: document.getElementById('reader-answer'),
      readerExplanation: document.getElementById('reader-explanation'),
      readerCodeWrapper: document.getElementById('reader-code-wrapper'),
      readerCode: document.getElementById('reader-code'),
      btnCopyCode: document.getElementById('btn-copy-code'),
      readerFollowup: document.getElementById('reader-followup'),
      readerFollowupBox: document.getElementById('reader-followup-box'),
      readerRef: document.getElementById('reader-ref'),
      revealShield: document.getElementById('reveal-shield'),
      
      scratchpadArea: document.getElementById('scratchpad-area'),
      
      btnPrevQ: document.getElementById('btn-prev-q'),
      btnNextQ: document.getElementById('btn-next-q'),
      
      // Drill Modal
      drillModal: document.getElementById('drill-modal')
    };
  }

  function bindEvents() {
    // Search input
    let searchTimeout;
    dom.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const val = e.target.value;
      searchTimeout = setTimeout(() => {
        state.searchQuery = val.trim().toLowerCase();
        applyFilters();
      }, 150);
    });

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
      // Don't intercept if focused on search or textarea
      if (document.activeElement === dom.searchInput || document.activeElement === dom.scratchpadArea) {
        if (e.key === 'Escape') document.activeElement.blur();
        return;
      }

      if (e.key === '/' || (e.ctrlKey && e.key === 'k')) {
        e.preventDefault();
        dom.searchInput.focus();
      } else if (e.key === 'ArrowDown' || e.key === 'j') {
        e.preventDefault();
        selectAdjacentQuestion(1);
      } else if (e.key === 'ArrowUp' || e.key === 'k') {
        e.preventDefault();
        selectAdjacentQuestion(-1);
      } else if (e.key === 'p') {
        togglePracticedCurrent();
      } else if (e.key === 'n') {
        toggleNeedCurrent();
      } else if (e.key === 's') {
        toggleSavedCurrent();
      }
    });

    // Sidebar Smart Filter items
    dom.sidebarFilterAll.addEventListener('click', () => setSmartFilter('all'));
    dom.sidebarFilterSaved.addEventListener('click', () => setSmartFilter('saved'));
    dom.sidebarFilterNeed.addEventListener('click', () => setSmartFilter('needs_practice'));
    dom.sidebarFilterPracticed.addEventListener('click', () => setSmartFilter('practiced'));

    // Difficulty Pills in List Header
    dom.pillDiffs.forEach(pill => {
      pill.addEventListener('click', () => {
        dom.pillDiffs.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedDifficulty = pill.getAttribute('data-diff');
        applyFilters();
      });
    });

    // Hide answers toggle
    dom.btnToggleAnswers.addEventListener('click', () => {
      state.hideAnswers = !state.hideAnswers;
      dom.readerPane.classList.toggle('answers-hidden', state.hideAnswers);
      dom.btnToggleAnswers.textContent = state.hideAnswers ? '👁️ Show Answers' : '🙈 Hide Answers';
    });

    dom.revealShield.addEventListener('click', () => {
      dom.readerPane.classList.remove('answers-hidden');
    });

    // Theme toggle
    dom.themeToggle.addEventListener('click', () => {
      const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('fresher_theme', next);
      dom.themeToggle.textContent = next === 'dark' ? '🌙 Dark' : '☀️ Light';
    });

    // Reader Action Buttons
    dom.btnMarkPracticed.addEventListener('click', togglePracticedCurrent);
    dom.btnMarkNeed.addEventListener('click', toggleNeedCurrent);
    dom.btnMarkSaved.addEventListener('click', toggleSavedCurrent);

    dom.btnCopyQ.addEventListener('click', () => {
      if (!state.selectedQuestion) return;
      const q = state.selectedQuestion;
      const text = `Q: ${q.question}\n\nAnswer: ${q.answer}\n\n${q.codeExample ? 'Code:\n' + q.codeExample : ''}`;
      navigator.clipboard.writeText(text);
      dom.btnCopyQ.textContent = '✓ Copied';
      setTimeout(() => dom.btnCopyQ.textContent = '📋 Copy', 1500);
    });

    dom.btnCopyCode.addEventListener('click', () => {
      if (!state.selectedQuestion || !state.selectedQuestion.codeExample) return;
      navigator.clipboard.writeText(state.selectedQuestion.codeExample);
      dom.btnCopyCode.textContent = '✓ Copied';
      setTimeout(() => dom.btnCopyCode.textContent = '📋 Copy', 1500);
    });

    // Scratchpad notes save
    dom.scratchpadArea.addEventListener('input', (e) => {
      if (!state.selectedQuestion) return;
      state.notes[state.selectedQuestion.id] = e.target.value;
      saveStorage();
    });

    // Prev / Next Question buttons
    dom.btnPrevQ.addEventListener('click', () => selectAdjacentQuestion(-1));
    dom.btnNextQ.addEventListener('click', () => selectAdjacentQuestion(1));

    // Weak area drill button
    dom.btnPracticeWeak.addEventListener('click', () => {
      setSmartFilter('needs_practice');
    });
  }

  function setSmartFilter(type) {
    state.selectedFilterTag = type;
    [dom.sidebarFilterAll, dom.sidebarFilterSaved, dom.sidebarFilterNeed, dom.sidebarFilterPracticed].forEach(el => el.classList.remove('active'));
    if (type === 'all') dom.sidebarFilterAll.classList.add('active');
    if (type === 'saved') dom.sidebarFilterSaved.classList.add('active');
    if (type === 'needs_practice') dom.sidebarFilterNeed.classList.add('active');
    if (type === 'practiced') dom.sidebarFilterPracticed.classList.add('active');
    applyFilters();
  }

  function renderSidebarSubjects() {
    dom.sidebarSubjects.innerHTML = '';
    SUBJECTS.forEach(sub => {
      const count = sub === 'All' 
        ? state.allQuestions.length 
        : state.allQuestions.filter(q => q.subject.toLowerCase() === sub.toLowerCase()).length;

      const item = document.createElement('button');
      item.className = `sidebar-nav-item ${sub === state.selectedSubject ? 'active' : ''} ${sub === 'DOM' ? 'dom-highlight' : ''}`;
      item.setAttribute('data-subject', sub);
      item.innerHTML = `
        <span>${sub === 'DOM' ? 'DOM ★' : sub}</span>
        <span class="sidebar-count">${count}</span>
      `;
      item.addEventListener('click', () => {
        state.selectedSubject = sub;
        dom.sidebarSubjects.querySelectorAll('.sidebar-nav-item').forEach(el => el.classList.remove('active'));
        item.classList.add('active');
        applyFilters();
      });
      dom.sidebarSubjects.appendChild(item);
    });
  }

  function updateSidebarCounts() {
    dom.countAll.textContent = state.allQuestions.length;
    dom.countSaved.textContent = state.savedIds.size;
    dom.countNeed.textContent = state.needPracticeIds.size;
    dom.countPracticed.textContent = state.practicedIds.size;
  }

  function applyFilters() {
    let list = state.allQuestions;

    // Subject filter
    if (state.selectedSubject !== 'All') {
      list = list.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }

    // Smart status filter
    if (state.selectedFilterTag === 'saved') {
      list = list.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedFilterTag === 'needs_practice') {
      list = list.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedFilterTag === 'practiced') {
      list = list.filter(q => state.practicedIds.has(q.id));
    }

    // Difficulty filter
    if (state.selectedDifficulty !== 'All') {
      list = list.filter(q => q.difficulty === state.selectedDifficulty);
    }

    // Search query
    if (state.searchQuery) {
      const q = state.searchQuery;
      list = list.filter(item => {
        return item.question.toLowerCase().includes(q) ||
               item.answer.toLowerCase().includes(q) ||
               item.subject.toLowerCase().includes(q) ||
               (item.topic && item.topic.toLowerCase().includes(q)) ||
               (item.codeExample && item.codeExample.toLowerCase().includes(q));
      });
    }

    state.filteredQuestions = list;
    updateSidebarCounts();
    renderQuestionsList();
  }

  function renderQuestionsList() {
    dom.listCount.textContent = `${state.filteredQuestions.length} Questions`;
    dom.questionsList.innerHTML = '';

    if (state.filteredQuestions.length === 0) {
      dom.questionsList.innerHTML = `
        <div style="padding:32px 16px; text-align:center; color:var(--text-muted); font-size:13px;">
          No matching questions in this view.<br>
          <button id="btn-reset-filters" class="btn-top" style="margin-top:10px;">Reset View</button>
        </div>
      `;
      const btn = document.getElementById('btn-reset-filters');
      if (btn) btn.addEventListener('click', () => {
        state.selectedSubject = 'All';
        setSmartFilter('all');
        renderSidebarSubjects();
      });
      clearReader();
      return;
    }

    const fragment = document.createDocumentFragment();

    state.filteredQuestions.forEach((q, idx) => {
      const isSelected = state.selectedQuestion && state.selectedQuestion.id === q.id;
      const isPracticed = state.practicedIds.has(q.id);
      const isNeed = state.needPracticeIds.has(q.id);
      const isSaved = state.savedIds.has(q.id);

      let statusDotClass = '';
      if (isPracticed) statusDotClass = 'dot-practiced';
      else if (isNeed) statusDotClass = 'dot-need';
      else if (isSaved) statusDotClass = 'dot-saved';

      let diffClass = 'diff-easy';
      if (q.difficulty === 'Medium') diffClass = 'diff-med';
      if (q.difficulty === 'Fresher Coding') diffClass = 'diff-code';

      const row = document.createElement('div');
      row.className = `q-row ${isSelected ? 'selected' : ''}`;
      row.setAttribute('data-id', q.id);
      row.innerHTML = `
        <div class="q-row-top">
          <div class="q-row-left">
            ${statusDotClass ? `<span class="q-row-status-dot ${statusDotClass}"></span>` : ''}
            <span class="q-row-num">#${String(idx + 1).padStart(2, '0')}</span>
            <span class="q-row-subject">${escapeHtml(q.subject)}</span>
          </div>
          <span class="q-row-diff ${diffClass}">${escapeHtml(q.difficulty)}</span>
        </div>
        <div class="q-row-title">${escapeHtml(q.question)}</div>
      `;

      row.addEventListener('click', () => {
        selectQuestion(q);
      });

      fragment.appendChild(row);
    });

    dom.questionsList.appendChild(fragment);

    // If current selected question is not in filtered list, select first one
    if (!state.selectedQuestion || !state.filteredQuestions.some(q => q.id === state.selectedQuestion.id)) {
      selectQuestion(state.filteredQuestions[0]);
    } else {
      highlightActiveRow();
    }
  }

  function selectQuestion(q) {
    state.selectedQuestion = q;
    highlightActiveRow();
    renderQuestionDetails(q);
  }

  function highlightActiveRow() {
    dom.questionsList.querySelectorAll('.q-row').forEach(row => {
      const qid = row.getAttribute('data-id');
      const isCurrent = state.selectedQuestion && state.selectedQuestion.id === qid;
      row.classList.toggle('selected', isCurrent);
      if (isCurrent) {
        row.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  function selectAdjacentQuestion(direction) {
    if (!state.selectedQuestion || state.filteredQuestions.length === 0) return;
    const curIdx = state.filteredQuestions.findIndex(q => q.id === state.selectedQuestion.id);
    let nextIdx = curIdx + direction;
    if (nextIdx < 0) nextIdx = 0;
    if (nextIdx >= state.filteredQuestions.length) nextIdx = state.filteredQuestions.length - 1;
    selectQuestion(state.filteredQuestions[nextIdx]);
  }

  function renderQuestionDetails(q) {
    dom.readerTitle.textContent = q.question;
    dom.badgeSubject.textContent = q.subject;
    dom.badgeTopic.textContent = q.topic || 'General';
    dom.badgeDiff.textContent = q.difficulty;
    dom.badgeType.textContent = q.questionType;

    // Status action buttons
    const isPracticed = state.practicedIds.has(q.id);
    const isNeed = state.needPracticeIds.has(q.id);
    const isSaved = state.savedIds.has(q.id);

    dom.btnMarkPracticed.className = `btn-action ${isPracticed ? 'active-practiced' : ''}`;
    dom.btnMarkPracticed.textContent = isPracticed ? '✓ Practiced' : 'Mark Practiced';

    dom.btnMarkNeed.className = `btn-action ${isNeed ? 'active-need' : ''}`;
    dom.btnMarkNeed.textContent = isNeed ? '⚠ Needs Practice' : 'Needs Practice';

    dom.btnMarkSaved.className = `btn-action ${isSaved ? 'active-saved' : ''}`;
    dom.btnMarkSaved.textContent = isSaved ? '★ Saved' : 'Save';

    // Content
    dom.readerAnswer.textContent = q.answer;

    if (q.shortExplanation && q.shortExplanation.trim()) {
      dom.readerExplanation.textContent = q.shortExplanation;
      dom.readerExplanation.style.display = 'block';
    } else {
      dom.readerExplanation.style.display = 'none';
    }

    if (q.codeExample && q.codeExample.trim()) {
      dom.readerCode.textContent = q.codeExample;
      dom.readerCodeWrapper.style.display = 'block';
    } else {
      dom.readerCodeWrapper.style.display = 'none';
    }

    if (q.followUpQuestions && q.followUpQuestions.trim()) {
      dom.readerFollowup.textContent = q.followUpQuestions;
      dom.readerFollowupBox.style.display = 'block';
    } else {
      dom.readerFollowupBox.style.display = 'none';
    }

    if (q.references && q.references.trim()) {
      dom.readerRef.textContent = `Reference: ${q.references}`;
      dom.readerRef.style.display = 'block';
    } else {
      dom.readerRef.style.display = 'none';
    }

    // Scratchpad notes
    dom.scratchpadArea.value = state.notes[q.id] || '';

    // If answers are hidden, reset shield
    if (state.hideAnswers) {
      dom.readerPane.classList.add('answers-hidden');
    }
  }

  function clearReader() {
    dom.readerTitle.textContent = 'Select a question from the list';
    dom.readerAnswer.textContent = '';
    dom.readerExplanation.style.display = 'none';
    dom.readerCodeWrapper.style.display = 'none';
    dom.readerFollowupBox.style.display = 'none';
    dom.readerRef.style.display = 'none';
    dom.scratchpadArea.value = '';
  }

  function togglePracticedCurrent() {
    if (!state.selectedQuestion) return;
    const qid = state.selectedQuestion.id;
    if (state.practicedIds.has(qid)) {
      state.practicedIds.delete(qid);
    } else {
      state.practicedIds.add(qid);
      state.needPracticeIds.delete(qid);
    }
    saveStorage();
    updateSidebarCounts();
    renderQuestionsList();
    renderQuestionDetails(state.selectedQuestion);
  }

  function toggleNeedCurrent() {
    if (!state.selectedQuestion) return;
    const qid = state.selectedQuestion.id;
    if (state.needPracticeIds.has(qid)) {
      state.needPracticeIds.delete(qid);
    } else {
      state.needPracticeIds.add(qid);
      state.practicedIds.delete(qid);
    }
    saveStorage();
    updateSidebarCounts();
    renderQuestionsList();
    renderQuestionDetails(state.selectedQuestion);
  }

  function toggleSavedCurrent() {
    if (!state.selectedQuestion) return;
    const qid = state.selectedQuestion.id;
    if (state.savedIds.has(qid)) {
      state.savedIds.delete(qid);
    } else {
      state.savedIds.add(qid);
    }
    saveStorage();
    updateSidebarCounts();
    renderQuestionsList();
    renderQuestionDetails(state.selectedQuestion);
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
