/**
 * Fresher Interview Question & Answer Drill Platform
 * State Controller & Engine
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

  const DIFFICULTIES = ['Easy', 'Medium', 'Fresher Coding'];
  const QUESTION_TYPES = ['Concept', 'MCQ', 'Output', 'Coding', 'Debugging', 'Scenario', 'SQL Query', 'Aptitude', 'Logical Reasoning', 'Project', 'HR'];
  const ROUNDS = ['Aptitude Round', 'Online Test', 'Technical Round', 'Coding Round', 'Machine Coding', 'Project Discussion', 'HR Round'];
  const FREQUENCIES = ['High', 'Medium', 'Low'];
  const STATUSES = ['Not Practiced', 'Practiced', 'Needs Practice', 'Saved'];

  // State
  const state = {
    allQuestions: [],
    filteredQuestions: [],
    
    // Filters
    selectedSubject: 'All',
    selectedTopic: 'All',
    selectedDifficulty: 'All',
    selectedType: 'All',
    selectedRound: 'All',
    selectedFreq: 'All',
    selectedStatus: 'All',
    searchQuery: '',
    sortBy: 'recommended',
    
    // Practice Tracking (Persistent Sets)
    practicedIds: new Set(),
    needPracticeIds: new Set(),
    savedIds: new Set(),
    
    // Views
    hideAnswers: false,
    pageSize: 30,
    currentPage: 1,
    
    // Drill Mode State
    inDrill: false,
    drillQuestions: [],
    drillCurrentIndex: 0,
    drillAnswerRevealed: false
  };

  let dom = {};

  function init() {
    loadStorage();
    cacheDom();
    bindEvents();

    if (window.FRESHER_QUESTIONS_DATA && Array.isArray(window.FRESHER_QUESTIONS_DATA)) {
      state.allQuestions = window.FRESHER_QUESTIONS_DATA;
    } else {
      console.error('Fresher questions data not found!');
    }

    renderSubjectTabs();
    populateFilterDropdowns();
    applyFilters();
    updateStatCounts();
  }

  // Load from LocalStorage
  function loadStorage() {
    try {
      const data = JSON.parse(localStorage.getItem('fresher_practice_state') || '{}');
      if (Array.isArray(data.practiced)) state.practicedIds = new Set(data.practiced);
      if (Array.isArray(data.needPractice)) state.needPracticeIds = new Set(data.needPractice);
      if (Array.isArray(data.saved)) state.savedIds = new Set(data.saved);

      const theme = localStorage.getItem('fresher_theme');
      if (theme) document.documentElement.setAttribute('data-theme', theme);
    } catch (e) {
      console.warn('Storage read error:', e);
    }
  }

  function saveStorage() {
    try {
      const payload = {
        practiced: [...state.practicedIds],
        needPractice: [...state.needPracticeIds],
        saved: [...state.savedIds]
      };
      localStorage.setItem('fresher_practice_state', JSON.stringify(payload));
    } catch (e) {
      console.warn('Storage save error:', e);
    }
  }

  function cacheDom() {
    dom = {
      subjectNav: document.getElementById('subject-nav'),
      searchInput: document.getElementById('search-input'),
      searchClear: document.getElementById('search-clear'),
      
      // Filter dropdowns
      filterSubject: document.getElementById('filter-subject'),
      filterTopic: document.getElementById('filter-topic'),
      filterDifficulty: document.getElementById('filter-difficulty'),
      filterType: document.getElementById('filter-type'),
      filterRound: document.getElementById('filter-round'),
      filterFreq: document.getElementById('filter-freq'),
      filterStatus: document.getElementById('filter-status'),
      btnClearFilters: document.getElementById('btn-clear-filters'),
      filterToolbar: document.getElementById('filter-toolbar'),
      mobileFilterBtn: document.getElementById('mobile-filter-btn'),
      
      // Chips & Results
      chipsBar: document.getElementById('chips-bar'),
      resultsCount: document.getElementById('results-count'),
      sortSelect: document.getElementById('sort-select'),
      qList: document.getElementById('q-list'),
      paginationBar: document.getElementById('pagination-bar'),
      
      // Controls
      btnStartDrill: document.getElementById('btn-start-drill'),
      btnPracticeWeak: document.getElementById('btn-practice-weak'),
      btnToggleAnswers: document.getElementById('btn-toggle-answers'),
      themeToggle: document.getElementById('theme-toggle'),
      
      // Stats
      statPracticed: document.getElementById('stat-practiced'),
      statNeed: document.getElementById('stat-need'),
      statSaved: document.getElementById('stat-saved'),
      statTotal: document.getElementById('stat-total'),
      
      // Drill Modal
      drillModal: document.getElementById('drill-modal'),
      drillSetupView: document.getElementById('drill-setup-view'),
      drillRunnerView: document.getElementById('drill-runner-view'),
      drillCloseBtn: document.getElementById('drill-close-btn'),
      drillStartBtn: document.getElementById('drill-start-btn'),
      drillSubjectSelect: document.getElementById('drill-subject-select'),
      drillDiffSelect: document.getElementById('drill-diff-select'),
      drillTypeSelect: document.getElementById('drill-type-select'),
      drillCountSelect: document.getElementById('drill-count-select'),
      
      // Drill Runner fields
      drillProgress: document.getElementById('drill-progress'),
      drillSubjectBadge: document.getElementById('drill-subject-badge'),
      drillQTitle: document.getElementById('drill-q-title'),
      drillNotes: document.getElementById('drill-notes'),
      drillBtnReveal: document.getElementById('drill-btn-reveal'),
      drillAnsBox: document.getElementById('drill-ans-box'),
      drillAnsContent: document.getElementById('drill-ans-content'),
      drillBtnGotIt: document.getElementById('drill-btn-got-it'),
      drillBtnNeedPractice: document.getElementById('drill-btn-need-practice'),
      drillBtnNext: document.getElementById('drill-btn-next')
    };
  }

  function bindEvents() {
    // Search with debounce
    let searchTimeout;
    dom.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const val = e.target.value;
      dom.searchClear.style.display = val ? 'block' : 'none';
      searchTimeout = setTimeout(() => {
        state.searchQuery = val.trim().toLowerCase();
        state.currentPage = 1;
        applyFilters();
      }, 200);
    });

    dom.searchClear.addEventListener('click', () => {
      dom.searchInput.value = '';
      dom.searchClear.style.display = 'none';
      state.searchQuery = '';
      state.currentPage = 1;
      applyFilters();
      dom.searchInput.focus();
    });

    // Mobile filter toggle
    dom.mobileFilterBtn.addEventListener('click', () => {
      dom.filterToolbar.classList.toggle('mobile-open');
    });

    // Filter selects change
    dom.filterSubject.addEventListener('change', (e) => {
      setSubject(e.target.value);
    });
    dom.filterTopic.addEventListener('change', (e) => {
      state.selectedTopic = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });
    dom.filterDifficulty.addEventListener('change', (e) => {
      state.selectedDifficulty = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });
    dom.filterType.addEventListener('change', (e) => {
      state.selectedType = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });
    dom.filterRound.addEventListener('change', (e) => {
      state.selectedRound = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });
    dom.filterFreq.addEventListener('change', (e) => {
      state.selectedFreq = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });
    dom.filterStatus.addEventListener('change', (e) => {
      state.selectedStatus = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });

    // Clear filters
    dom.btnClearFilters.addEventListener('click', clearAllFilters);

    // Sorting
    dom.sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });

    // Hide/Show Answers toggle
    dom.btnToggleAnswers.addEventListener('click', () => {
      state.hideAnswers = !state.hideAnswers;
      document.body.classList.toggle('hide-answers-active', state.hideAnswers);
      dom.btnToggleAnswers.textContent = state.hideAnswers ? '👁️ Show Answers' : '🙈 Hide Answers';
    });

    // Theme toggle
    dom.themeToggle.addEventListener('click', () => {
      const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('fresher_theme', next);
      dom.themeToggle.textContent = next === 'dark' ? '🌙 Dark' : '☀️ Light';
    });

    // Drill Modal actions
    dom.btnStartDrill.addEventListener('click', openDrillSetup);
    dom.btnPracticeWeak.addEventListener('click', startWeakAreaDrill);
    dom.drillCloseBtn.addEventListener('click', closeDrillModal);
    dom.drillStartBtn.addEventListener('click', launchDrillSession);

    dom.drillBtnReveal.addEventListener('click', () => {
      state.drillAnswerRevealed = true;
      dom.drillAnsBox.classList.add('visible');
    });

    dom.drillBtnGotIt.addEventListener('click', () => {
      const currentQ = state.drillQuestions[state.drillCurrentIndex];
      if (currentQ) {
        state.practicedIds.add(currentQ.id);
        state.needPracticeIds.delete(currentQ.id);
        saveStorage();
        updateStatCounts();
      }
      advanceDrill();
    });

    dom.drillBtnNeedPractice.addEventListener('click', () => {
      const currentQ = state.drillQuestions[state.drillCurrentIndex];
      if (currentQ) {
        state.needPracticeIds.add(currentQ.id);
        state.practicedIds.delete(currentQ.id);
        saveStorage();
        updateStatCounts();
      }
      advanceDrill();
    });

    dom.drillBtnNext.addEventListener('click', advanceDrill);
  }

  // Render Horizontal Subject Navigation Tabs
  function renderSubjectTabs() {
    dom.subjectNav.innerHTML = '';
    SUBJECTS.forEach(sub => {
      const btn = document.createElement('button');
      btn.className = `nav-tab ${sub === state.selectedSubject ? 'active' : ''} ${sub === 'DOM' ? 'dom-highlight' : ''}`;
      btn.textContent = sub === 'DOM' ? 'DOM ★' : sub;
      btn.setAttribute('data-subject', sub);
      btn.addEventListener('click', () => {
        setSubject(sub);
      });
      dom.subjectNav.appendChild(btn);
    });
  }

  function setSubject(sub) {
    state.selectedSubject = sub;
    dom.filterSubject.value = sub;
    state.selectedTopic = 'All';
    state.currentPage = 1;
    
    // Update active tab class
    dom.subjectNav.querySelectorAll('.nav-tab').forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-subject') === sub);
    });

    populateTopicDropdown();
    applyFilters();
  }

  // Populate Filter Dropdowns
  function populateFilterDropdowns() {
    // Subject filter options
    dom.filterSubject.innerHTML = SUBJECTS.map(s => `<option value="${s}">${s === 'All' ? 'All Subjects' : s}</option>`).join('');
    dom.filterSubject.value = state.selectedSubject;

    // Difficulty
    dom.filterDifficulty.innerHTML = `<option value="All">All Difficulties</option>` +
      DIFFICULTIES.map(d => `<option value="${d}">${d}</option>`).join('');

    // Question Type
    dom.filterType.innerHTML = `<option value="All">All Types</option>` +
      QUESTION_TYPES.map(t => `<option value="${t}">${t}</option>`).join('');

    // Interview Round
    dom.filterRound.innerHTML = `<option value="All">All Rounds</option>` +
      ROUNDS.map(r => `<option value="${r}">${r}</option>`).join('');

    // Frequency
    dom.filterFreq.innerHTML = `<option value="All">All Frequencies</option>` +
      FREQUENCIES.map(f => `<option value="${f}">${f} Frequency</option>`).join('');

    // Status
    dom.filterStatus.innerHTML = `<option value="All">All Statuses</option>` +
      STATUSES.map(s => `<option value="${s}">${s}</option>`).join('');

    populateTopicDropdown();
  }

  function populateTopicDropdown() {
    let pool = state.allQuestions;
    if (state.selectedSubject !== 'All') {
      pool = pool.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }
    const topics = Array.from(new Set(pool.map(q => q.topic).filter(Boolean))).sort();
    dom.filterTopic.innerHTML = `<option value="All">All Topics</option>` +
      topics.map(t => `<option value="${t}">${t}</option>`).join('');
    dom.filterTopic.value = state.selectedTopic;
  }

  // Clear all filters
  function clearAllFilters() {
    state.selectedSubject = 'All';
    state.selectedTopic = 'All';
    state.selectedDifficulty = 'All';
    state.selectedType = 'All';
    state.selectedRound = 'All';
    state.selectedFreq = 'All';
    state.selectedStatus = 'All';
    state.searchQuery = '';
    state.currentPage = 1;
    dom.searchInput.value = '';
    dom.searchClear.style.display = 'none';

    dom.filterSubject.value = 'All';
    dom.filterTopic.value = 'All';
    dom.filterDifficulty.value = 'All';
    dom.filterType.value = 'All';
    dom.filterRound.value = 'All';
    dom.filterFreq.value = 'All';
    dom.filterStatus.value = 'All';

    dom.subjectNav.querySelectorAll('.nav-tab').forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-subject') === 'All');
    });

    populateTopicDropdown();
    applyFilters();
  }

  // Filter & Sort Logic
  function applyFilters() {
    let list = state.allQuestions;

    // 1. Subject
    if (state.selectedSubject !== 'All') {
      list = list.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }

    // 2. Topic
    if (state.selectedTopic !== 'All') {
      list = list.filter(q => q.topic === state.selectedTopic);
    }

    // 3. Difficulty
    if (state.selectedDifficulty !== 'All') {
      list = list.filter(q => q.difficulty === state.selectedDifficulty);
    }

    // 4. Type
    if (state.selectedType !== 'All') {
      list = list.filter(q => q.questionType === state.selectedType);
    }

    // 5. Round
    if (state.selectedRound !== 'All') {
      list = list.filter(q => q.interviewRound === state.selectedRound);
    }

    // 6. Frequency
    if (state.selectedFreq !== 'All') {
      list = list.filter(q => q.frequency === state.selectedFreq);
    }

    // 7. Practice Status
    if (state.selectedStatus === 'Practiced') {
      list = list.filter(q => state.practicedIds.has(q.id));
    } else if (state.selectedStatus === 'Needs Practice') {
      list = list.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedStatus === 'Saved') {
      list = list.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedStatus === 'Not Practiced') {
      list = list.filter(q => !state.practicedIds.has(q.id) && !state.needPracticeIds.has(q.id));
    }

    // 8. Search query across question, answer, subject, topic, subTopic, code
    if (state.searchQuery) {
      const q = state.searchQuery;
      list = list.filter(item => {
        return item.question.toLowerCase().includes(q) ||
               item.answer.toLowerCase().includes(q) ||
               item.subject.toLowerCase().includes(q) ||
               (item.topic && item.topic.toLowerCase().includes(q)) ||
               (item.subTopic && item.subTopic.toLowerCase().includes(q)) ||
               (item.codeExample && item.codeExample.toLowerCase().includes(q));
      });
    }

    // Sorting
    list = sortQuestions(list, state.sortBy);

    state.filteredQuestions = list;
    renderChipsBar();
    renderQuestionList();
  }

  function sortQuestions(arr, sortBy) {
    const sorted = [...arr];
    if (sortBy === 'frequently_asked') {
      const freqOrder = { High: 3, Medium: 2, Low: 1 };
      sorted.sort((a, b) => (freqOrder[b.frequency] || 0) - (freqOrder[a.frequency] || 0));
    } else if (sortBy === 'difficulty') {
      const diffOrder = { Easy: 1, Medium: 2, 'Fresher Coding': 3 };
      sorted.sort((a, b) => (diffOrder[a.difficulty] || 0) - (diffOrder[b.difficulty] || 0));
    } else if (sortBy === 'not_practiced') {
      sorted.sort((a, b) => {
        const aP = state.practicedIds.has(a.id) ? 1 : 0;
        const bP = state.practicedIds.has(b.id) ? 1 : 0;
        return aP - bP;
      });
    } else if (sortBy === 'needs_practice') {
      sorted.sort((a, b) => {
        const aN = state.needPracticeIds.has(a.id) ? 1 : 0;
        const bN = state.needPracticeIds.has(b.id) ? 1 : 0;
        return bN - aN;
      });
    } else if (sortBy === 'recently_added') {
      sorted.sort((a, b) => (b.addedAt || 0) - (a.addedAt || 0));
    }
    return sorted;
  }

  // Render Removable Chips
  function renderChipsBar() {
    const chips = [];

    if (state.selectedSubject !== 'All') {
      chips.push({ key: 'subject', label: `${state.selectedSubject}`, action: () => setSubject('All') });
    }
    if (state.selectedTopic !== 'All') {
      chips.push({ key: 'topic', label: `${state.selectedTopic}`, action: () => { state.selectedTopic = 'All'; dom.filterTopic.value = 'All'; applyFilters(); } });
    }
    if (state.selectedDifficulty !== 'All') {
      chips.push({ key: 'diff', label: `${state.selectedDifficulty}`, action: () => { state.selectedDifficulty = 'All'; dom.filterDifficulty.value = 'All'; applyFilters(); } });
    }
    if (state.selectedType !== 'All') {
      chips.push({ key: 'type', label: `${state.selectedType}`, action: () => { state.selectedType = 'All'; dom.filterType.value = 'All'; applyFilters(); } });
    }
    if (state.selectedRound !== 'All') {
      chips.push({ key: 'round', label: `${state.selectedRound}`, action: () => { state.selectedRound = 'All'; dom.filterRound.value = 'All'; applyFilters(); } });
    }
    if (state.selectedFreq !== 'All') {
      chips.push({ key: 'freq', label: `${state.selectedFreq} Frequency`, action: () => { state.selectedFreq = 'All'; dom.filterFreq.value = 'All'; applyFilters(); } });
    }
    if (state.selectedStatus !== 'All') {
      chips.push({ key: 'status', label: `${state.selectedStatus}`, action: () => { state.selectedStatus = 'All'; dom.filterStatus.value = 'All'; applyFilters(); } });
    }
    if (state.searchQuery) {
      chips.push({ key: 'search', label: `"${state.searchQuery}"`, action: () => { state.searchQuery = ''; dom.searchInput.value = ''; dom.searchClear.style.display = 'none'; applyFilters(); } });
    }

    if (chips.length === 0) {
      dom.chipsBar.innerHTML = '';
      return;
    }

    dom.chipsBar.innerHTML = chips.map((c, i) => `
      <span class="filter-chip" data-chip-idx="${i}">
        ${escapeHtml(c.label)} <span class="chip-remove" title="Remove filter">&times;</span>
      </span>
    `).join('') + `<button id="btn-chip-clear" class="btn btn-sm" style="font-size:11px; padding:1px 6px;">Clear all</button>`;

    dom.chipsBar.querySelectorAll('.filter-chip').forEach(el => {
      const idx = parseInt(el.getAttribute('data-chip-idx'), 10);
      el.querySelector('.chip-remove').addEventListener('click', () => {
        chips[idx].action();
      });
    });

    const clearBtn = document.getElementById('btn-chip-clear');
    if (clearBtn) clearBtn.addEventListener('click', clearAllFilters);
  }

  // Render Compact Vertical Question List
  function renderQuestionList() {
    const total = state.filteredQuestions.length;
    dom.resultsCount.textContent = `Showing ${Math.min(state.currentPage * state.pageSize, total)} of ${total} questions`;

    if (total === 0) {
      dom.qList.innerHTML = `
        <div class="empty-state">
          <p><strong>No questions found</strong> matching your selected filters.</p>
          <button id="btn-empty-clear" class="btn btn-sm" style="margin-top:8px;">Reset Filters</button>
        </div>
      `;
      const btn = document.getElementById('btn-empty-clear');
      if (btn) btn.addEventListener('click', clearAllFilters);
      dom.paginationBar.innerHTML = '';
      return;
    }

    const start = (state.currentPage - 1) * state.pageSize;
    const end = start + state.pageSize;
    const pageItems = state.filteredQuestions.slice(start, end);

    let html = '';
    pageItems.forEach((q, idx) => {
      const globalIndex = start + idx + 1;
      const isPracticed = state.practicedIds.has(q.id);
      const isNeed = state.needPracticeIds.has(q.id);
      const isSaved = state.savedIds.has(q.id);

      // Diff class
      let diffClass = 'badge-diff-easy';
      if (q.difficulty === 'Medium') diffClass = 'badge-diff-med';
      if (q.difficulty === 'Fresher Coding') diffClass = 'badge-diff-code';

      // Code snippet
      let codeHtml = '';
      if (q.codeExample && q.codeExample.trim()) {
        codeHtml = `<pre class="q-code"><code>${escapeHtml(q.codeExample)}</code></pre>`;
      }

      // Follow-up
      let followupHtml = '';
      if (q.followUpQuestions && q.followUpQuestions.trim()) {
        followupHtml = `<div class="q-followup"><strong>Follow-up:</strong> ${escapeHtml(q.followUpQuestions)}</div>`;
      }

      // Reference
      let refHtml = '';
      if (q.references && q.references.trim()) {
        refHtml = `<div class="q-ref">Reference: ${escapeHtml(q.references)}</div>`;
      }

      // Explanation
      let expHtml = '';
      if (q.shortExplanation && q.shortExplanation.trim()) {
        expHtml = `<div class="q-explanation">${escapeHtml(q.shortExplanation)}</div>`;
      }

      html += `
        <article class="q-item" data-qid="${q.id}">
          <div class="q-header">
            <div class="q-title-row">
              <h2 class="q-title"><span class="q-num">${String(globalIndex).padStart(2, '0')}.</span> ${escapeHtml(q.question)}</h2>
              <button class="btn-reveal-one" data-action="reveal">Show Answer</button>
            </div>
            <div class="q-meta">
              <span class="badge" style="font-weight:700;">${escapeHtml(q.subject)}</span>
              ${q.topic ? `<span class="badge">${escapeHtml(q.topic)}</span>` : ''}
              <span class="badge ${diffClass}">${escapeHtml(q.difficulty)}</span>
              <span class="badge">${escapeHtml(q.questionType)}</span>
              <span class="badge">${escapeHtml(q.interviewRound)}</span>
            </div>
          </div>

          <div class="q-content">
            <div class="q-answer-block">
              <strong class="ans-label">Answer:</strong>
              <span>${escapeHtml(q.answer)}</span>
            </div>
            ${expHtml}
            ${codeHtml}
            ${followupHtml}
            ${refHtml}
          </div>

          <div class="q-actions">
            <div class="action-group-left">
              <button class="btn-status ${isPracticed ? 'is-practiced' : ''}" data-action="toggle-practiced">
                ${isPracticed ? '✓ Practiced' : 'Mark Practiced'}
              </button>
              <button class="btn-status ${isNeed ? 'is-need' : ''}" data-action="toggle-need">
                ${isNeed ? '⚠ Needs Practice' : 'Need Practice'}
              </button>
              <button class="btn-status ${isSaved ? 'is-saved' : ''}" data-action="toggle-saved">
                ${isSaved ? '★ Saved' : 'Save'}
              </button>
            </div>
          </div>
        </article>
      `;
    });

    dom.qList.innerHTML = html;

    // Attach item events
    dom.qList.querySelectorAll('.q-item').forEach(itemEl => {
      const qid = itemEl.getAttribute('data-qid');
      
      itemEl.addEventListener('click', (e) => {
        const action = e.target.getAttribute('data-action');
        if (action === 'toggle-practiced') {
          togglePracticed(qid);
        } else if (action === 'toggle-need') {
          toggleNeedPractice(qid);
        } else if (action === 'toggle-saved') {
          toggleSaved(qid);
        } else if (action === 'reveal') {
          itemEl.classList.toggle('answer-revealed');
          e.target.textContent = itemEl.classList.contains('answer-revealed') ? 'Hide Answer' : 'Show Answer';
        }
      });
    });

    renderPagination(total);
  }

  // Status updates
  function togglePracticed(qid) {
    if (state.practicedIds.has(qid)) {
      state.practicedIds.delete(qid);
    } else {
      state.practicedIds.add(qid);
      state.needPracticeIds.delete(qid); // Clear need practice if marked practiced
    }
    saveStorage();
    updateStatCounts();
    renderQuestionList();
  }

  function toggleNeedPractice(qid) {
    if (state.needPracticeIds.has(qid)) {
      state.needPracticeIds.delete(qid);
    } else {
      state.needPracticeIds.add(qid);
      state.practicedIds.delete(qid);
    }
    saveStorage();
    updateStatCounts();
    renderQuestionList();
  }

  function toggleSaved(qid) {
    if (state.savedIds.has(qid)) {
      state.savedIds.delete(qid);
    } else {
      state.savedIds.add(qid);
    }
    saveStorage();
    updateStatCounts();
    renderQuestionList();
  }

  function updateStatCounts() {
    dom.statTotal.textContent = `${state.allQuestions.length} Questions`;
    dom.statPracticed.textContent = `${state.practicedIds.size} Practiced`;
    dom.statNeed.textContent = `${state.needPracticeIds.size} Needs Practice`;
    dom.statSaved.textContent = `${state.savedIds.size} Saved`;
  }

  // Pagination
  function renderPagination(total) {
    const totalPages = Math.ceil(total / state.pageSize);
    if (totalPages <= 1) {
      dom.paginationBar.innerHTML = '';
      return;
    }

    let html = '';
    if (state.currentPage > 1) {
      html += `<button class="btn btn-sm" id="pg-prev">&larr; Previous</button>`;
    }
    html += `<span style="font-size:12px; color:var(--text-dim); margin:0 8px;">Page ${state.currentPage} of ${totalPages}</span>`;
    if (state.currentPage < totalPages) {
      html += `<button class="btn btn-sm" id="pg-next">Next &rarr;</button>`;
    }

    dom.paginationBar.innerHTML = html;

    const prev = document.getElementById('pg-prev');
    if (prev) prev.addEventListener('click', () => {
      state.currentPage--;
      renderQuestionList();
      window.scrollTo({ top: dom.qList.offsetTop - 80, behavior: 'smooth' });
    });

    const next = document.getElementById('pg-next');
    if (next) next.addEventListener('click', () => {
      state.currentPage++;
      renderQuestionList();
      window.scrollTo({ top: dom.qList.offsetTop - 80, behavior: 'smooth' });
    });
  }

  // ==========================================
  // Practice / Drill Mode
  // ==========================================
  function openDrillSetup() {
    dom.drillSubjectSelect.innerHTML = SUBJECTS.map(s => `<option value="${s}">${s}</option>`).join('');
    dom.drillSubjectSelect.value = state.selectedSubject !== 'All' ? state.selectedSubject : 'All';

    dom.drillDiffSelect.innerHTML = `<option value="All">All Difficulties</option>` +
      DIFFICULTIES.map(d => `<option value="${d}">${d}</option>`).join('');

    dom.drillTypeSelect.innerHTML = `<option value="All">All Types</option>` +
      QUESTION_TYPES.map(t => `<option value="${t}">${t}</option>`).join('');

    dom.drillSetupView.style.display = 'block';
    dom.drillRunnerView.style.display = 'none';
    dom.drillModal.classList.add('open');
  }

  function launchDrillSession() {
    const sub = dom.drillSubjectSelect.value;
    const diff = dom.drillDiffSelect.value;
    const type = dom.drillTypeSelect.value;
    const count = parseInt(dom.drillCountSelect.value, 10) || 10;

    let pool = state.allQuestions;
    if (sub !== 'All') pool = pool.filter(q => q.subject.toLowerCase() === sub.toLowerCase());
    if (diff !== 'All') pool = pool.filter(q => q.difficulty === diff);
    if (type !== 'All') pool = pool.filter(q => q.questionType === type);

    if (pool.length === 0) {
      alert('No questions match your drill criteria. Please choose different options.');
      return;
    }

    // Shuffle and pick
    const shuffled = [...pool].sort(() => 0.5 - Math.random());
    state.drillQuestions = shuffled.slice(0, count);
    state.drillCurrentIndex = 0;
    state.drillAnswerRevealed = false;

    dom.drillSetupView.style.display = 'none';
    dom.drillRunnerView.style.display = 'block';
    renderDrillCard();
  }

  function startWeakAreaDrill() {
    const weakList = state.allQuestions.filter(q => state.needPracticeIds.has(q.id));
    if (weakList.length === 0) {
      alert('You have not marked any questions as "Needs Practice" yet.\n\nBrowse questions and click [Need Practice] on topics you want to reinforce!');
      return;
    }

    state.drillQuestions = [...weakList].sort(() => 0.5 - Math.random());
    state.drillCurrentIndex = 0;
    state.drillAnswerRevealed = false;

    dom.drillSetupView.style.display = 'none';
    dom.drillRunnerView.style.display = 'block';
    dom.drillModal.classList.add('open');
    renderDrillCard();
  }

  function renderDrillCard() {
    const q = state.drillQuestions[state.drillCurrentIndex];
    if (!q) {
      finishDrill();
      return;
    }

    dom.drillProgress.textContent = `Question ${state.drillCurrentIndex + 1} of ${state.drillQuestions.length}`;
    dom.drillSubjectBadge.textContent = `${q.subject} · ${q.difficulty}`;
    dom.drillQTitle.textContent = q.question;
    dom.drillNotes.value = '';

    dom.drillAnsBox.classList.remove('visible');
    state.drillAnswerRevealed = false;

    let ansHtml = `<div><strong>Answer:</strong> ${escapeHtml(q.answer)}</div>`;
    if (q.shortExplanation) ansHtml += `<div style="margin-top:6px; color:var(--text-muted);">${escapeHtml(q.shortExplanation)}</div>`;
    if (q.codeExample) ansHtml += `<pre class="q-code" style="margin-top:6px;"><code>${escapeHtml(q.codeExample)}</code></pre>`;
    if (q.followUpQuestions) ansHtml += `<div class="q-followup" style="margin-top:6px;"><strong>Follow-up:</strong> ${escapeHtml(q.followUpQuestions)}</div>`;
    if (q.references) ansHtml += `<div class="q-ref" style="margin-top:4px;">Reference: ${escapeHtml(q.references)}</div>`;

    dom.drillAnsContent.innerHTML = ansHtml;
  }

  function advanceDrill() {
    state.drillCurrentIndex++;
    if (state.drillCurrentIndex >= state.drillQuestions.length) {
      finishDrill();
    } else {
      renderDrillCard();
    }
  }

  function finishDrill() {
    alert(`Drill session completed!\n\nPracticed questions: ${state.drillQuestions.length}`);
    closeDrillModal();
    renderQuestionList();
  }

  function closeDrillModal() {
    dom.drillModal.classList.remove('open');
    state.drillQuestions = [];
    state.drillCurrentIndex = 0;
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

  // Boot up
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
