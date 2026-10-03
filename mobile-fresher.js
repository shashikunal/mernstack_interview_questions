/**
 * Mobile-First Fresher Interview Reader Platform
 * Optimized for reading while traveling
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
    
    // Filters
    selectedSubject: 'All',
    selectedStatus: 'all', // 'all', 'need', 'saved', 'practiced'
    searchQuery: '',
    
    // Persistent Status
    practicedIds: new Set(),
    needPracticeIds: new Set(),
    savedIds: new Set(),
    
    // Reading settings
    fontSize: 'md', // 'sm', 'md', 'lg', 'xl'
    hideAnswers: false,
    
    // Pagination for butter-smooth mobile scroll
    pageSize: 20,
    currentPage: 1
  };

  let dom = {};

  function init() {
    loadStorage();
    cacheDom();
    bindEvents();

    if (window.FRESHER_QUESTIONS_DATA && Array.isArray(window.FRESHER_QUESTIONS_DATA)) {
      state.allQuestions = window.FRESHER_QUESTIONS_DATA;
    }

    renderSubjectStrip();
    applyFilters();
  }

  function loadStorage() {
    try {
      const data = JSON.parse(localStorage.getItem('fresher_mobile_state') || '{}');
      if (Array.isArray(data.practiced)) state.practicedIds = new Set(data.practiced);
      if (Array.isArray(data.needPractice)) state.needPracticeIds = new Set(data.needPractice);
      if (Array.isArray(data.saved)) state.savedIds = new Set(data.saved);

      state.fontSize = localStorage.getItem('fresher_font_size') || 'md';
      document.body.className = `font-${state.fontSize}`;

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
        saved: [...state.savedIds]
      };
      localStorage.setItem('fresher_mobile_state', JSON.stringify(payload));
    } catch (e) {
      console.warn('Storage save error:', e);
    }
  }

  function cacheDom() {
    dom = {
      subjectStrip: document.getElementById('subject-strip'),
      searchInput: document.getElementById('search-input'),
      searchClear: document.getElementById('search-clear'),
      
      feedContainer: document.getElementById('mobile-feed'),
      feedCount: document.getElementById('feed-count'),
      
      // Quick Status Buttons
      btnTabAll: document.getElementById('tab-status-all'),
      btnTabNeed: document.getElementById('tab-status-need'),
      btnTabSaved: document.getElementById('tab-status-saved'),
      btnTabPracticed: document.getElementById('tab-status-practiced'),
      
      // Controls
      btnToggleHide: document.getElementById('btn-toggle-hide'),
      themeToggle: document.getElementById('btn-toggle-theme'),
      fontBtns: document.querySelectorAll('.btn-font'),
      
      // Bottom Bar
      btnBottomWeak: document.getElementById('btn-bottom-weak'),
      btnScrollTop: document.getElementById('btn-scroll-top'),
      
      toast: document.getElementById('mobile-toast')
    };

    // Update active font button
    dom.fontBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-size') === state.fontSize);
    });
  }

  function bindEvents() {
    // Search input (debounced)
    let searchTimeout;
    dom.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const val = e.target.value;
      dom.searchClear.style.display = val ? 'block' : 'none';
      searchTimeout = setTimeout(() => {
        state.searchQuery = val.trim().toLowerCase();
        state.currentPage = 1;
        applyFilters();
      }, 180);
    });

    dom.searchClear.addEventListener('click', () => {
      dom.searchInput.value = '';
      dom.searchClear.style.display = 'none';
      state.searchQuery = '';
      state.currentPage = 1;
      applyFilters();
      dom.searchInput.focus();
    });

    // Font Sizing buttons
    dom.fontBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const size = btn.getAttribute('data-size');
        state.fontSize = size;
        document.body.className = `font-${size}`;
        localStorage.setItem('fresher_font_size', size);
        dom.fontBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        showToast(`Text Size: ${size.toUpperCase()}`);
      });
    });

    // Theme toggle
    dom.themeToggle.addEventListener('click', () => {
      const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('fresher_theme', next);
      dom.themeToggle.textContent = next === 'dark' ? '🌙' : '☀️';
    });

    // Global Hide/Show answers
    dom.btnToggleHide.addEventListener('click', () => {
      state.hideAnswers = !state.hideAnswers;
      document.body.classList.toggle('hide-answers-active', state.hideAnswers);
      dom.btnToggleHide.textContent = state.hideAnswers ? '👁️ Show' : '🙈 Hide';
      showToast(state.hideAnswers ? 'Answers hidden for self-test' : 'Answers visible');
    });

    // Quick Status Tabs
    dom.btnTabAll.addEventListener('click', () => setStatusFilter('all'));
    dom.btnTabNeed.addEventListener('click', () => setStatusFilter('need'));
    dom.btnTabSaved.addEventListener('click', () => setStatusFilter('saved'));
    dom.btnTabPracticed.addEventListener('click', () => setStatusFilter('practiced'));

    // Bottom Bar Actions
    dom.btnBottomWeak.addEventListener('click', () => setStatusFilter('need'));
    dom.btnScrollTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Infinite scroll
    window.addEventListener('scroll', () => {
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
        if (state.currentPage * state.pageSize < state.filteredQuestions.length) {
          state.currentPage++;
          renderNextPage();
        }
      }
    });
  }

  function setStatusFilter(type) {
    state.selectedStatus = type;
    [dom.btnTabAll, dom.btnTabNeed, dom.btnTabSaved, dom.btnTabPracticed].forEach(btn => btn.classList.remove('active'));
    if (type === 'all') dom.btnTabAll.classList.add('active');
    if (type === 'need') dom.btnTabNeed.classList.add('active');
    if (type === 'saved') dom.btnTabSaved.classList.add('active');
    if (type === 'practiced') dom.btnTabPracticed.classList.add('active');
    state.currentPage = 1;
    applyFilters();
  }

  function renderSubjectStrip() {
    dom.subjectStrip.innerHTML = '';
    SUBJECTS.forEach(sub => {
      const btn = document.createElement('button');
      btn.className = `pill-subject ${sub === state.selectedSubject ? 'active' : ''} ${sub === 'DOM' ? 'dom-star' : ''}`;
      btn.textContent = sub === 'DOM' ? 'DOM ★' : sub;
      btn.setAttribute('data-subject', sub);
      btn.addEventListener('click', () => {
        state.selectedSubject = sub;
        dom.subjectStrip.querySelectorAll('.pill-subject').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.currentPage = 1;
        applyFilters();
        btn.scrollIntoView({ inline: 'center', behavior: 'smooth' });
      });
      dom.subjectStrip.appendChild(btn);
    });
  }

  function applyFilters() {
    let list = state.allQuestions;

    // Subject filter
    if (state.selectedSubject !== 'All') {
      list = list.filter(q => q.subject.toLowerCase() === state.selectedSubject.toLowerCase());
    }

    // Status filter
    if (state.selectedStatus === 'need') {
      list = list.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedStatus === 'saved') {
      list = list.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedStatus === 'practiced') {
      list = list.filter(q => state.practicedIds.has(q.id));
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
    dom.feedCount.textContent = `${list.length} Questions`;
    dom.feedContainer.innerHTML = '';

    if (list.length === 0) {
      dom.feedContainer.innerHTML = `
        <div class="feed-empty">
          <p style="font-size:16px; font-weight:700; margin-bottom:6px;">No questions found</p>
          <p style="font-size:13px; color:var(--text-dim); margin-bottom:12px;">Try adjusting your subject or status filter</p>
          <button id="btn-feed-reset" class="btn-tool" style="padding:8px 16px;">View All Questions</button>
        </div>
      `;
      const resetBtn = document.getElementById('btn-feed-reset');
      if (resetBtn) resetBtn.addEventListener('click', () => {
        state.selectedSubject = 'All';
        setStatusFilter('all');
        renderSubjectStrip();
      });
      return;
    }

    renderNextPage();
  }

  function renderNextPage() {
    const start = (state.currentPage - 1) * state.pageSize;
    const end = start + state.pageSize;
    const slice = state.filteredQuestions.slice(start, end);

    const fragment = document.createDocumentFragment();

    slice.forEach((q, idx) => {
      const card = createQuestionCard(q, start + idx + 1);
      fragment.appendChild(card);
    });

    dom.feedContainer.appendChild(fragment);
  }

  function createQuestionCard(q, index) {
    const card = document.createElement('article');
    card.className = 'read-card';
    card.setAttribute('data-id', q.id);

    const isPracticed = state.practicedIds.has(q.id);
    const isNeed = state.needPracticeIds.has(q.id);
    const isSaved = state.savedIds.has(q.id);

    if (isPracticed) card.classList.add('status-practiced');
    if (isNeed) card.classList.add('status-need');
    if (isSaved) card.classList.add('status-saved');

    let diffClass = 'diff-easy';
    if (q.difficulty === 'Medium') diffClass = 'diff-med';
    if (q.difficulty === 'Fresher Coding') diffClass = 'diff-code';

    // Code snippet
    let codeHtml = '';
    if (q.codeExample && q.codeExample.trim()) {
      codeHtml = `
        <div class="card-code-wrap">
          <div class="card-code-top">
            <span>Code Example</span>
            <button class="btn-copy-code" data-action="copy-code">Copy</button>
          </div>
          <pre class="code-scroll"><code>${escapeHtml(q.codeExample)}</code></pre>
        </div>
      `;
    }

    // Follow-up
    let followupHtml = '';
    if (q.followUpQuestions && q.followUpQuestions.trim()) {
      followupHtml = `
        <div class="card-followup">
          <strong>Follow-up:</strong>
          <span>${escapeHtml(q.followUpQuestions)}</span>
        </div>
      `;
    }

    card.innerHTML = `
      <div class="card-top">
        <div class="card-badges">
          <span class="badge-sub">${escapeHtml(q.subject)}</span>
          <span class="badge-topic">${escapeHtml(q.topic || 'General')}</span>
          <span class="badge-diff ${diffClass}">• ${escapeHtml(q.difficulty)}</span>
        </div>
        <span class="card-qnum">#${String(index).padStart(2, '0')}</span>
      </div>

      <h2 class="card-question">${escapeHtml(q.question)}</h2>

      <div class="reveal-tap-box" data-action="reveal">
        🔒 Tap to Reveal Answer & Test Yourself
      </div>

      <div class="card-answer-wrap">
        <div class="answer-lead">
          <strong>Answer:</strong>
          <span>${escapeHtml(q.answer)}</span>
        </div>
        ${q.shortExplanation ? `<div class="answer-explanation">${escapeHtml(q.shortExplanation)}</div>` : ''}
      </div>

      ${codeHtml}
      ${followupHtml}

      ${q.references ? `<div class="card-ref">Reference: ${escapeHtml(q.references)}</div>` : ''}

      <div class="card-actions">
        <button class="btn-card-action btn-act-practiced ${isPracticed ? 'active-practiced' : ''}" data-action="practiced">
          ${isPracticed ? '✓ Practiced' : 'Mark Done'}
        </button>
        <button class="btn-card-action btn-act-need ${isNeed ? 'active-need' : ''}" data-action="need">
          ${isNeed ? '⚠ Need Review' : 'Need Review'}
        </button>
        <button class="btn-card-action btn-act-saved ${isSaved ? 'active-saved' : ''}" data-action="save">
          ${isSaved ? '★ Saved' : 'Save'}
        </button>
        <button class="btn-card-action" data-action="copy-q" style="flex:0 0 auto; padding:8px 10px;" title="Copy">
          📋
        </button>
      </div>
    `;

    // Card Event delegation
    card.addEventListener('click', (e) => {
      const action = e.target.closest('[data-action]')?.getAttribute('data-action');
      if (!action) return;

      if (action === 'practiced') {
        togglePracticed(q.id, card);
      } else if (action === 'need') {
        toggleNeed(q.id, card);
      } else if (action === 'save') {
        toggleSave(q.id, card);
      } else if (action === 'copy-code') {
        copyText(q.codeExample, 'Code copied to clipboard');
      } else if (action === 'copy-q') {
        const fullText = `Q: ${q.question}\n\nAnswer: ${q.answer}\n\n${q.codeExample || ''}`;
        copyText(fullText, 'Question & Answer copied');
      } else if (action === 'reveal') {
        card.classList.add('revealed');
      }
    });

    return card;
  }

  function togglePracticed(qid, card) {
    const btn = card.querySelector('.btn-act-practiced');
    if (state.practicedIds.has(qid)) {
      state.practicedIds.delete(qid);
      btn.classList.remove('active-practiced');
      btn.textContent = 'Mark Done';
      card.classList.remove('status-practiced');
      showToast('Removed from practiced');
    } else {
      state.practicedIds.add(qid);
      state.needPracticeIds.delete(qid);
      btn.classList.add('active-practiced');
      btn.textContent = '✓ Practiced';
      card.classList.add('status-practiced');
      card.classList.remove('status-need');
      card.querySelector('.btn-act-need').classList.remove('active-need');
      showToast('Marked as Practiced ✓');
    }
    saveStorage();
  }

  function toggleNeed(qid, card) {
    const btn = card.querySelector('.btn-act-need');
    if (state.needPracticeIds.has(qid)) {
      state.needPracticeIds.delete(qid);
      btn.classList.remove('active-need');
      card.classList.remove('status-need');
      showToast('Removed from review');
    } else {
      state.needPracticeIds.add(qid);
      state.practicedIds.delete(qid);
      btn.classList.add('active-need');
      card.classList.add('status-need');
      card.classList.remove('status-practiced');
      card.querySelector('.btn-act-practiced').classList.remove('active-practiced');
      card.querySelector('.btn-act-practiced').textContent = 'Mark Done';
      showToast('Saved for Weak Area Review ⚠');
    }
    saveStorage();
  }

  function toggleSave(qid, card) {
    const btn = card.querySelector('.btn-act-saved');
    if (state.savedIds.has(qid)) {
      state.savedIds.delete(qid);
      btn.classList.remove('active-saved');
      btn.textContent = 'Save';
      card.classList.remove('status-saved');
      showToast('Removed from saved');
    } else {
      state.savedIds.add(qid);
      btn.classList.add('active-saved');
      btn.textContent = '★ Saved';
      card.classList.add('status-saved');
      showToast('Question Bookmarked ★');
    }
    saveStorage();
  }

  function copyText(text, msg) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(() => showToast(msg));
    }
  }

  let toastTimer;
  function showToast(msg) {
    clearTimeout(toastTimer);
    dom.toast.textContent = msg;
    dom.toast.classList.add('show');
    toastTimer = setTimeout(() => {
      dom.toast.classList.remove('show');
    }, 2000);
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
