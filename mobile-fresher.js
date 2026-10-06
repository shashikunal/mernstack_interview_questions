/**
 * Mobile-First Fresher & AI Interview Reader Platform
 * Optimized for reading while traveling with quick Hamburger Menu and AI Masterclass
 */

(function () {
  'use strict';

  // Comprehensive curriculum subjects matching DevPrep Master Bank
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
    pageSize: 25,
    currentPage: 1
  };

  let dom = {};

  function init() {
    loadStorage();
    cacheDom();
    bindEvents();

    // 1. Combine AI & Fresher Master Question Banks
    const rawFresher = window.FRESHER_QUESTIONS_DATA || window.FRESHER_QUESTIONS || [];
    const rawAi = window.AI_GENAI_QUESTIONS_DATA || window.AI_GENAI_QUESTIONS || [];
    state.allQuestions = [...rawAi, ...rawFresher];

    console.log(`[DevPrep Mobile] Loaded ${state.allQuestions.length} total questions (${rawAi.length} AI + ${rawFresher.length} Full-Stack).`);

    renderSubjectStrip();
    renderDrawerSubjects();
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
      // Header & Navigation
      btnHamburger: document.getElementById('btn-hamburger'),
      drawer: document.getElementById('nav-drawer'),
      drawerOverlay: document.getElementById('drawer-overlay'),
      btnDrawerClose: document.getElementById('btn-drawer-close'),
      drawerCardAi: document.getElementById('drawer-card-ai'),
      drawerCardAll: document.getElementById('drawer-card-all'),
      drawerSubjectsList: document.getElementById('drawer-subjects-list'),
      drawerFilterChips: document.querySelectorAll('.drawer-filter-chip'),

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
      btnBottomMenu: document.getElementById('btn-bottom-menu'),
      btnScrollTop: document.getElementById('btn-scroll-top'),
      
      toast: document.getElementById('mobile-toast')
    };

    // Update active font button
    dom.fontBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-size') === state.fontSize);
    });
  }

  function openDrawer() {
    if (dom.drawer) dom.drawer.classList.add('open');
    if (dom.drawerOverlay) {
      dom.drawerOverlay.classList.add('open');
      dom.drawerOverlay.setAttribute('aria-hidden', 'false');
    }
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (dom.drawer) dom.drawer.classList.remove('open');
    if (dom.drawerOverlay) {
      dom.drawerOverlay.classList.remove('open');
      dom.drawerOverlay.setAttribute('aria-hidden', 'true');
    }
    document.body.style.overflow = '';
  }

  function bindEvents() {
    // 0. Hamburger Menu Drawer
    if (dom.btnHamburger) {
      dom.btnHamburger.addEventListener('click', openDrawer);
    }
    if (dom.btnDrawerClose) {
      dom.btnDrawerClose.addEventListener('click', closeDrawer);
    }
    if (dom.drawerOverlay) {
      dom.drawerOverlay.addEventListener('click', closeDrawer);
    }
    if (dom.btnBottomMenu) {
      dom.btnBottomMenu.addEventListener('click', openDrawer);
    }

    // Escape closes drawer
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && dom.drawer && dom.drawer.classList.contains('open')) {
        closeDrawer();
      }
    });

    // Drawer Curriculum Cards
    if (dom.drawerCardAi) {
      dom.drawerCardAi.addEventListener('click', () => {
        selectSubject('AI & Generative AI');
        showToast('🤖 AI & Vibe Coding Guide (249 Questions)');
      });
    }

    if (dom.drawerCardAll) {
      dom.drawerCardAll.addEventListener('click', () => {
        selectSubject('All');
        showToast('🌐 Master Question Bank (5,727 Questions)');
      });
    }

    // Drawer Filter Chips
    if (dom.drawerFilterChips) {
      dom.drawerFilterChips.forEach(chip => {
        chip.addEventListener('click', () => {
          const status = chip.getAttribute('data-status');
          setStatusFilter(status);
          closeDrawer();
        });
      });
    }

    // 1. Search input (debounced)
    let searchTimeout;
    if (dom.searchInput) {
      dom.searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const val = e.target.value;
        if (dom.searchClear) dom.searchClear.style.display = val ? 'block' : 'none';
        searchTimeout = setTimeout(() => {
          state.searchQuery = val.trim().toLowerCase();
          state.currentPage = 1;
          applyFilters();
        }, 180);
      });
    }

    if (dom.searchClear) {
      dom.searchClear.addEventListener('click', () => {
        if (dom.searchInput) {
          dom.searchInput.value = '';
          dom.searchInput.focus();
        }
        dom.searchClear.style.display = 'none';
        state.searchQuery = '';
        state.currentPage = 1;
        applyFilters();
      });
    }

    // 2. Font Sizing buttons
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

    // 3. Theme toggle
    if (dom.themeToggle) {
      dom.themeToggle.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
        const next = cur === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('fresher_theme', next);
        dom.themeToggle.textContent = next === 'dark' ? '🌙' : '☀️';
      });
    }

    // 4. Global Hide/Show answers
    if (dom.btnToggleHide) {
      dom.btnToggleHide.addEventListener('click', () => {
        state.hideAnswers = !state.hideAnswers;
        document.body.classList.toggle('hide-answers-active', state.hideAnswers);
        dom.btnToggleHide.textContent = state.hideAnswers ? '👁️ Show' : '🙈 Hide';
        showToast(state.hideAnswers ? 'Answers hidden for self-testing' : 'Answers visible');
      });
    }

    // 5. Quick Status Tabs
    if (dom.btnTabAll) dom.btnTabAll.addEventListener('click', () => setStatusFilter('all'));
    if (dom.btnTabNeed) dom.btnTabNeed.addEventListener('click', () => setStatusFilter('need'));
    if (dom.btnTabSaved) dom.btnTabSaved.addEventListener('click', () => setStatusFilter('saved'));
    if (dom.btnTabPracticed) dom.btnTabPracticed.addEventListener('click', () => setStatusFilter('practiced'));

    // 6. Bottom Bar Actions
    if (dom.btnBottomWeak) dom.btnBottomWeak.addEventListener('click', () => setStatusFilter('need'));
    if (dom.btnScrollTop) {
      dom.btnScrollTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // 7. Infinite scroll
    window.addEventListener('scroll', () => {
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 600) {
        if (state.currentPage * state.pageSize < state.filteredQuestions.length) {
          state.currentPage++;
          renderNextPage();
        }
      }
    });
  }

  function setStatusFilter(type) {
    state.selectedStatus = type;
    [dom.btnTabAll, dom.btnTabNeed, dom.btnTabSaved, dom.btnTabPracticed].forEach(btn => {
      if (btn) btn.classList.remove('active');
    });
    if (type === 'all' && dom.btnTabAll) dom.btnTabAll.classList.add('active');
    if (type === 'need' && dom.btnTabNeed) dom.btnTabNeed.classList.add('active');
    if (type === 'saved' && dom.btnTabSaved) dom.btnTabSaved.classList.add('active');
    if (type === 'practiced' && dom.btnTabPracticed) dom.btnTabPracticed.classList.add('active');
    state.currentPage = 1;
    applyFilters();
  }

  function selectSubject(sub) {
    state.selectedSubject = sub;
    state.currentPage = 1;

    // Update horizontal pills
    if (dom.subjectStrip) {
      dom.subjectStrip.querySelectorAll('.pill-subject').forEach(b => {
        const isMatch = (b.getAttribute('data-subject') === sub);
        b.classList.toggle('active', isMatch);
        if (isMatch) {
          b.scrollIntoView({ inline: 'center', behavior: 'smooth' });
        }
      });
    }

    // Update Drawer Curriculum cards
    if (dom.drawerCardAi) {
      dom.drawerCardAi.classList.toggle('active', sub === 'AI & Generative AI');
    }
    if (dom.drawerCardAll) {
      dom.drawerCardAll.classList.toggle('active', sub === 'All');
    }

    // Update Drawer Subjects list
    if (dom.drawerSubjectsList) {
      dom.drawerSubjectsList.querySelectorAll('.drawer-subj-item').forEach(item => {
        item.classList.toggle('active', item.getAttribute('data-subject') === sub);
      });
    }

    closeDrawer();
    applyFilters();
  }

  function renderSubjectStrip() {
    if (!dom.subjectStrip) return;
    dom.subjectStrip.innerHTML = '';

    SUBJECTS.forEach(sub => {
      const btn = document.createElement('button');
      const isAi = (sub === 'AI & Generative AI');
      const isAll = (sub === 'All');
      btn.className = `pill-subject ${sub === state.selectedSubject ? 'active' : ''} ${isAi ? 'pill-ai-featured' : ''} ${sub === 'DOM' ? 'dom-star' : ''}`;
      
      if (isAi) {
        btn.innerHTML = '🤖 AI & GenAI <span class="pill-badge-glow">249</span>';
      } else if (isAll) {
        btn.textContent = 'All Subjects';
      } else if (sub === 'DOM') {
        btn.textContent = 'DOM ★';
      } else {
        btn.textContent = sub;
      }

      btn.setAttribute('data-subject', sub);
      btn.addEventListener('click', () => {
        selectSubject(sub);
      });
      dom.subjectStrip.appendChild(btn);
    });
  }

  function renderDrawerSubjects() {
    if (!dom.drawerSubjectsList) return;
    dom.drawerSubjectsList.innerHTML = '';

    // Calculate count per subject
    const counts = {};
    state.allQuestions.forEach(q => {
      const s = q.subject || 'Other';
      counts[s] = (counts[s] || 0) + 1;
    });

    SUBJECTS.forEach(sub => {
      const count = sub === 'All' ? state.allQuestions.length : (counts[sub] || 0);
      const isAi = (sub === 'AI & Generative AI');

      const item = document.createElement('button');
      item.className = `drawer-subj-item ${sub === state.selectedSubject ? 'active' : ''} ${isAi ? 'drawer-subj-ai' : ''}`;
      item.setAttribute('data-subject', sub);

      let icon = '📄';
      if (isAi) icon = '🤖';
      else if (sub === 'All') icon = '🌐';
      else if (sub.includes('HTML')) icon = '🧱';
      else if (sub.includes('CSS')) icon = '🎨';
      else if (sub.includes('JavaScript') || sub.includes('ES6')) icon = '⚡';
      else if (sub.includes('DOM')) icon = '🌲';
      else if (sub.includes('jQuery')) icon = '💲';
      else if (sub.includes('React')) icon = '⚛️';
      else if (sub.includes('Node') || sub.includes('Express')) icon = '🟢';
      else if (sub.includes('SQL') || sub.includes('Mongo')) icon = '🗄️';
      else if (sub.includes('Aptitude') || sub.includes('Reasoning')) icon = '💡';
      else if (sub.includes('DSA') || sub.includes('Problem')) icon = '🧩';
      else if (sub.includes('Coding')) icon = '💻';
      else if (sub.includes('Git')) icon = '🌿';
      else if (sub.includes('Testing')) icon = '🧪';
      else if (sub.includes('Fundamentals')) icon = '🌐';
      else if (sub.includes('Project')) icon = '🚀';
      else if (sub.includes('HR')) icon = '👥';

      item.innerHTML = `
        <span class="drawer-subj-icon">${icon}</span>
        <span class="drawer-subj-name">${escapeHtml(sub)}</span>
        <span class="drawer-subj-count">${count.toLocaleString()}</span>
      `;

      item.addEventListener('click', () => {
        selectSubject(sub);
      });

      dom.drawerSubjectsList.appendChild(item);
    });
  }

  function applyFilters() {
    let list = state.allQuestions;

    // 1. Subject filter
    if (state.selectedSubject !== 'All') {
      const target = state.selectedSubject.toLowerCase();
      list = list.filter(q => {
        if (!q.subject) return false;
        const qSub = q.subject.toLowerCase();
        if (target === 'ai & generative ai') return qSub.includes('ai') || qSub.includes('generative');
        if (target === 'es6+' || target === 'es6') return qSub.includes('es6');
        if (target === 'express.js' || target === 'express') return qSub.includes('express');
        if (target === 'node.js' || target === 'node') return qSub.includes('node');
        if (target === 'git / github' || target === 'git') return qSub.includes('git');
        if (target === 'hr / communication' || target === 'hr') return qSub.includes('hr') || qSub.includes('communication');
        return qSub === target;
      });
    }

    // 2. Status filter
    if (state.selectedStatus === 'need') {
      list = list.filter(q => state.needPracticeIds.has(q.id));
    } else if (state.selectedStatus === 'saved') {
      list = list.filter(q => state.savedIds.has(q.id));
    } else if (state.selectedStatus === 'practiced') {
      list = list.filter(q => state.practicedIds.has(q.id));
    }

    // 3. Search query
    if (state.searchQuery) {
      const terms = state.searchQuery.toLowerCase().split(/\s+/);
      list = list.filter(item => {
        const full = [
          item.question,
          item.answer,
          item.subject,
          item.topic || '',
          item.codeExample || ''
        ].join(' ').toLowerCase();
        return terms.every(term => full.includes(term));
      });
    }

    state.filteredQuestions = list;
    if (dom.feedCount) {
      dom.feedCount.textContent = `${list.length.toLocaleString()} Questions (${state.selectedSubject})`;
    }
    if (dom.feedContainer) {
      dom.feedContainer.innerHTML = '';
      dom.feedContainer.removeAttribute('aria-busy');
    }

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
        selectSubject('All');
        setStatusFilter('all');
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
    if (q.difficulty === 'Fresher Coding' || q.difficulty === 'Advanced') diffClass = 'diff-code';

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

    const isAi = (q.subject === 'AI & Generative AI');

    card.innerHTML = `
      <div class="card-top">
        <div class="card-badges">
          <span class="badge-sub ${isAi ? 'badge-sub-ai' : ''}">${isAi ? '🤖 ' : ''}${escapeHtml(q.subject)}</span>
          <span class="badge-topic">${escapeHtml(q.topic || 'General')}</span>
          <span class="badge-diff ${diffClass}">• ${escapeHtml(q.difficulty || 'Easy')}</span>
        </div>
        <span class="card-qnum">#${String(index).padStart(2, '0')}</span>
      </div>

      <h2 class="card-question">${escapeHtml(q.question)}</h2>

      <div class="reveal-tap-box" data-action="reveal">
        👆 Tap to reveal answer (Self-Test Mode)
      </div>

      <div class="card-answer-wrap">
        <div class="answer-lead">
          <strong>Direct Answer:</strong>
          ${escapeHtml(q.answer)}
        </div>
        ${q.shortExplanation ? `<div class="answer-explanation">${escapeHtml(q.shortExplanation)}</div>` : ''}
      </div>

      ${codeHtml}
      ${followupHtml}

      <div class="card-actions">
        <button class="btn-card-action btn-act-practiced ${isPracticed ? 'active-practiced' : ''}" data-action="practiced">
          ${isPracticed ? '✓ Practiced' : 'Mark Done'}
        </button>
        <button class="btn-card-action btn-act-need ${isNeed ? 'active-need' : ''}" data-action="need">
          ${isNeed ? '⚠ Reviewing' : 'Needs Review'}
        </button>
        <button class="btn-card-action btn-act-saved ${isSaved ? 'active-saved' : ''}" data-action="save">
          ${isSaved ? '★ Saved' : 'Save'}
        </button>
        <button class="btn-card-action" data-action="copy-q" title="Copy question and answer">
          📋
        </button>
      </div>
    `;

    card.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-action]');
      if (!btn) return;
      const action = btn.getAttribute('data-action');

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
      const needBtn = card.querySelector('.btn-act-need');
      if (needBtn) needBtn.classList.remove('active-need');
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
      const pracBtn = card.querySelector('.btn-act-practiced');
      if (pracBtn) {
        pracBtn.classList.remove('active-practiced');
        pracBtn.textContent = 'Mark Done';
      }
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
    if (!dom.toast) return;
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
