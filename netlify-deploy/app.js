/**
 * MERN Stack Interview Pro - Advanced Controller & State Engine
 */

(function () {
  'use strict';

  // State Management
  const state = {
    allQuestions: [],
    categories: [],
    tags: [],
    
    // Filters
    searchQuery: '',
    selectedCategory: 'all',
    selectedTag: 'all',
    filterCode: false,
    filterMetric: false,
    filterTip: false,
    filterStarred: false,
    filterUnmastered: false,
    sortBy: 'default',
    
    // View mode: 'study', 'flashcard', 'compact'
    viewMode: 'study',
    
    // Pagination
    pageSize: 30,
    currentPage: 1,
    
    // LocalStorage sets
    starredIds: new Set(),
    masteredIds: new Set(),
    
    // Filtered result cache
    filteredQuestions: []
  };

  // DOM Elements cache
  let dom = {};

  // Initialize
  function init() {
    loadStoredData();
    cacheDom();
    bindEvents();
    
    // Ensure dataset loaded
    if (window.INTERVIEW_DATA) {
      state.allQuestions = window.INTERVIEW_DATA.questions || [];
      state.categories = window.INTERVIEW_DATA.categories || [];
      state.tags = window.INTERVIEW_DATA.tags || [];
      
      renderCategoryTabs();
      renderPopularTags();
      applyFilters();
      updateGlobalStats();
    } else {
      console.error('Interview data not found on window.INTERVIEW_DATA');
    }
  }

  // LocalStorage handling
  function loadStoredData() {
    try {
      const savedTheme = localStorage.getItem('mern_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      
      const savedStarred = JSON.parse(localStorage.getItem('mern_starred') || '[]');
      state.starredIds = new Set(savedStarred);
      
      const savedMastered = JSON.parse(localStorage.getItem('mern_mastered') || '[]');
      state.masteredIds = new Set(savedMastered);
      
      state.viewMode = localStorage.getItem('mern_view_mode') || 'study';
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
  }

  function saveStoredData() {
    try {
      localStorage.setItem('mern_starred', JSON.stringify([...state.starredIds]));
      localStorage.setItem('mern_mastered', JSON.stringify([...state.masteredIds]));
      localStorage.setItem('mern_view_mode', state.viewMode);
    } catch (e) {
      console.warn('Failed saving to LocalStorage', e);
    }
  }

  // Cache DOM elements
  function cacheDom() {
    dom = {
      themeToggle: document.getElementById('theme-toggle'),
      searchInput: document.getElementById('search-input'),
      searchClear: document.getElementById('search-clear'),
      categoryTabs: document.getElementById('category-tabs'),
      tagFilterRow: document.getElementById('tag-filter-row'),
      chipFilters: document.querySelectorAll('.filter-chip'),
      sortSelect: document.getElementById('sort-select'),
      questionsContainer: document.getElementById('questions-container'),
      loadMoreContainer: document.getElementById('load-more-container'),
      loadMoreBtn: document.getElementById('btn-load-more'),
      resultsCount: document.getElementById('results-count'),
      
      // Mode buttons
      btnModeStudy: document.getElementById('btn-mode-study'),
      btnModeFlashcard: document.getElementById('btn-mode-flashcard'),
      btnModeCompact: document.getElementById('btn-mode-compact'),
      btnRandom: document.getElementById('btn-random'),
      btnExpandAll: document.getElementById('btn-expand-all'),
      btnResetProgress: document.getElementById('btn-reset-progress'),
      
      // Stats
      statTotal: document.getElementById('stat-total'),
      statMastered: document.getElementById('stat-mastered'),
      statStarred: document.getElementById('stat-starred'),
      progressFill: document.getElementById('progress-bar-fill'),
      
      // Toast & Scroll
      toast: document.getElementById('toast-msg'),
      backToTop: document.getElementById('back-to-top')
    };

    updateModeButtonStyles();
  }

  // Bind Listeners
  function bindEvents() {
    // Theme toggle
    dom.themeToggle.addEventListener('click', toggleTheme);

    // Search input (debounced)
    let searchTimeout;
    dom.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const val = e.target.value.trim();
      dom.searchClear.style.display = val ? 'block' : 'none';
      const kbd = document.querySelector('.keyboard-shortcut');
      if (kbd) kbd.style.display = val ? 'none' : 'block';

      searchTimeout = setTimeout(() => {
        state.searchQuery = val.toLowerCase();
        state.currentPage = 1;
        applyFilters();
      }, 250);
    });

    dom.searchClear.addEventListener('click', () => {
      dom.searchInput.value = '';
      dom.searchClear.style.display = 'none';
      const kbd = document.querySelector('.keyboard-shortcut');
      if (kbd) kbd.style.display = 'block';
      state.searchQuery = '';
      state.currentPage = 1;
      applyFilters();
      dom.searchInput.focus();
    });

    // Keyboard shortcut '/' or Ctrl+K to search
    window.addEventListener('keydown', (e) => {
      if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement !== dom.searchInput) {
        e.preventDefault();
        dom.searchInput.focus();
      }
      if (e.key === 'Escape' && document.activeElement === dom.searchInput) {
        dom.searchInput.value = '';
        dom.searchClear.style.display = 'none';
        state.searchQuery = '';
        applyFilters();
        dom.searchInput.blur();
      }
    });

    // Sort select
    dom.sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      state.currentPage = 1;
      applyFilters();
    });

    // Chip filters
    dom.chipFilters.forEach(chip => {
      chip.addEventListener('click', () => {
        const filterType = chip.dataset.filter;
        chip.classList.toggle('active');
        const isActive = chip.classList.contains('active');

        if (filterType === 'code') state.filterCode = isActive;
        if (filterType === 'metric') state.filterMetric = isActive;
        if (filterType === 'tip') state.filterTip = isActive;
        if (filterType === 'starred') state.filterStarred = isActive;
        if (filterType === 'unmastered') state.filterUnmastered = isActive;

        state.currentPage = 1;
        applyFilters();
      });
    });

    // Mode Buttons
    dom.btnModeStudy.addEventListener('click', () => switchViewMode('study'));
    dom.btnModeFlashcard.addEventListener('click', () => switchViewMode('flashcard'));
    dom.btnModeCompact.addEventListener('click', () => switchViewMode('compact'));

    // Load More button
    dom.loadMoreBtn.addEventListener('click', () => {
      state.currentPage++;
      renderQuestionsPage();
    });

    // Random Question Drill
    dom.btnRandom.addEventListener('click', pickRandomQuestion);

    // Expand / Collapse All
    dom.btnExpandAll.addEventListener('click', toggleExpandAll);

    // Reset Progress
    dom.btnResetProgress.addEventListener('click', resetProgress);

    // Back to top
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        dom.backToTop.style.display = 'flex';
      } else {
        dom.backToTop.style.display = 'none';
      }
    });

    dom.backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Theme switch
  function toggleTheme() {
    const cur = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('mern_theme', next);
    dom.themeToggle.innerHTML = next === 'dark' ? '🌙 Dark' : '☀️ Light';
  }

  // Switch View Mode
  function switchViewMode(mode) {
    state.viewMode = mode;
    saveStoredData();
    updateModeButtonStyles();
    document.body.className = `mode-${mode}`;
    renderQuestionsList();
  }

  function updateModeButtonStyles() {
    [dom.btnModeStudy, dom.btnModeFlashcard, dom.btnModeCompact].forEach(btn => btn.classList.remove('active'));
    if (state.viewMode === 'study') dom.btnModeStudy.classList.add('active');
    if (state.viewMode === 'flashcard') dom.btnModeFlashcard.classList.add('active');
    if (state.viewMode === 'compact') dom.btnModeCompact.classList.add('active');
    document.body.className = `mode-${state.viewMode}`;
  }

  // Render Category Tabs
  function renderCategoryTabs() {
    const totalCount = state.allQuestions.length;
    let html = `
      <button class="cat-tab active" data-cat="all">
        <span>🌟 All Categories</span>
        <span class="cat-count">${totalCount}</span>
      </button>
    `;

    state.categories.forEach(cat => {
      const count = state.allQuestions.filter(q => q.category === cat.id).length;
      html += `
        <button class="cat-tab" data-cat="${cat.id}">
          <span>${cat.icon} ${escapeHtml(cat.name)}</span>
          <span class="cat-count">${count}</span>
        </button>
      `;
    });

    dom.categoryTabs.innerHTML = html;

    dom.categoryTabs.querySelectorAll('.cat-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        dom.categoryTabs.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        state.selectedCategory = tab.dataset.cat;
        state.currentPage = 1;
        renderPopularTags();
        applyFilters();
      });
    });
  }

  // Render Sub-topic Tag Pills based on category
  function renderPopularTags() {
    let pool = state.allQuestions;
    if (state.selectedCategory !== 'all') {
      pool = pool.filter(q => q.category === state.selectedCategory);
    }

    const tagCounts = {};
    pool.forEach(q => {
      q.tags.forEach(t => {
        tagCounts[t] = (tagCounts[t] || 0) + 1;
      });
    });

    const sortedTags = Object.keys(tagCounts).sort((a, b) => tagCounts[b] - tagCounts[a]).slice(0, 16);

    let html = `<span class="tag-label">TOPICS:</span>`;
    html += `<span class="tag-pill ${state.selectedTag === 'all' ? 'active' : ''}" data-tag="all">All Topics</span>`;

    sortedTags.forEach(t => {
      const activeClass = state.selectedTag === t ? 'active' : '';
      html += `<span class="tag-pill ${activeClass}" data-tag="${escapeHtml(t)}">${escapeHtml(t)} (${tagCounts[t]})</span>`;
    });

    dom.tagFilterRow.innerHTML = html;

    dom.tagFilterRow.querySelectorAll('.tag-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        dom.tagFilterRow.querySelectorAll('.tag-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedTag = pill.dataset.tag;
        state.currentPage = 1;
        applyFilters();
      });
    });
  }

  // Filter Algorithm
  function applyFilters() {
    let list = state.allQuestions;

    // 1. Category Filter
    if (state.selectedCategory !== 'all') {
      list = list.filter(q => q.category === state.selectedCategory);
    }

    // 2. Tag Filter
    if (state.selectedTag !== 'all') {
      list = list.filter(q => q.tags.includes(state.selectedTag));
    }

    // 3. Search Query
    if (state.searchQuery) {
      const q = state.searchQuery;
      list = list.filter(item => {
        return item.searchIndex.includes(q) ||
               item.title.toLowerCase().includes(q) ||
               (item.code && item.code.toLowerCase().includes(q)) ||
               (item.useCase && item.useCase.toLowerCase().includes(q)) ||
               (item.tip && item.tip.toLowerCase().includes(q));
      });
    }

    // 4. Feature Toggles
    if (state.filterCode) {
      list = list.filter(q => q.code && q.code.trim().length > 0);
    }
    if (state.filterMetric) {
      list = list.filter(q => q.useCase && q.useCase.trim().length > 0);
    }
    if (state.filterTip) {
      list = list.filter(q => q.tip && q.tip.trim().length > 0);
    }
    if (state.filterStarred) {
      list = list.filter(q => state.starredIds.has(q.id));
    }
    if (state.filterUnmastered) {
      list = list.filter(q => !state.masteredIds.has(q.id));
    }

    // 5. Sorting
    if (state.sortBy === 'num-asc') {
      list = [...list].sort((a, b) => a.num - b.num);
    } else if (state.sortBy === 'num-desc') {
      list = [...list].sort((a, b) => b.num - a.num);
    } else if (state.sortBy === 'title-asc') {
      list = [...list].sort((a, b) => a.title.localeCompare(b.title));
    }

    state.filteredQuestions = list;
    state.currentPage = 1;
    renderQuestionsList();
  }

  // Render question cards list
  function renderQuestionsList() {
    dom.resultsCount.innerHTML = `Showing <strong>${Math.min(state.pageSize * state.currentPage, state.filteredQuestions.length)}</strong> of <strong>${state.filteredQuestions.length}</strong> questions`;

    if (state.filteredQuestions.length === 0) {
      dom.questionsContainer.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">🔍</div>
          <div class="empty-title">No matching questions found</div>
          <div class="empty-desc">Try loosening your search terms or unchecking some active filters.</div>
        </div>
      `;
      dom.loadMoreContainer.style.display = 'none';
      return;
    }

    dom.questionsContainer.innerHTML = '';
    renderQuestionsPage();
  }

  function renderQuestionsPage() {
    const start = (state.currentPage - 1) * state.pageSize;
    const end = start + state.pageSize;
    const slice = state.filteredQuestions.slice(start, end);

    const fragment = document.createDocumentFragment();

    slice.forEach(q => {
      const cardEl = createQuestionCard(q);
      fragment.appendChild(cardEl);
    });

    dom.questionsContainer.appendChild(fragment);

    // Update results count label
    const displayedCount = Math.min(state.currentPage * state.pageSize, state.filteredQuestions.length);
    dom.resultsCount.innerHTML = `Showing <strong>${displayedCount}</strong> of <strong>${state.filteredQuestions.length}</strong> questions`;

    // Toggle Load More button
    if (displayedCount < state.filteredQuestions.length) {
      dom.loadMoreContainer.style.display = 'flex';
      const remaining = state.filteredQuestions.length - displayedCount;
      dom.loadMoreBtn.innerText = `Load More Questions (${remaining} remaining)`;
    } else {
      dom.loadMoreContainer.style.display = 'none';
    }
  }

  // Create single question card element
  function createQuestionCard(q) {
    const card = document.createElement('article');
    card.className = `q-card ${state.masteredIds.has(q.id) ? 'is-mastered' : ''}`;
    card.id = `card-${q.id}`;
    card.setAttribute('data-id', q.id);
    card.setAttribute('data-cat', q.category);

    const isStarred = state.starredIds.has(q.id);
    const isMastered = state.masteredIds.has(q.id);

    // Category label formatting
    const catObj = state.categories.find(c => c.id === q.category);
    const catName = catObj ? `${catObj.icon} ${catObj.name}` : q.category;

    // Highlight search match in title
    let highlightedTitle = escapeHtml(q.title);
    if (state.searchQuery && state.searchQuery.length >= 2) {
      const regex = new RegExp(`(${escapeRegExp(state.searchQuery)})`, 'gi');
      highlightedTitle = highlightedTitle.replace(regex, '<span class="highlight-match">$1</span>');
    }

    // Mini tags
    const tagsHtml = q.tags.map(t => `<span class="mini-tag" data-tag="${escapeHtml(t)}">#${escapeHtml(t)}</span>`).join('');

    // Code container
    let codeHtml = '';
    if (q.code && q.code.trim()) {
      codeHtml = `
        <div class="code-container">
          <div class="code-header">
            <span>JavaScript / Snippet</span>
            <button class="copy-code-btn" data-action="copy-code">📋 Copy Code</button>
          </div>
          <pre class="code-pre"><code>${escapeHtml(q.code)}</code></pre>
        </div>
      `;
    }

    // Project Metric Box
    let metricHtml = '';
    if (q.useCase && q.useCase.trim()) {
      metricHtml = `
        <div class="insight-box usecase-box">
          <strong>📈 1 YOE Project Story / Metric:</strong>
          <span>${escapeHtml(q.useCase)}</span>
        </div>
      `;
    }

    // Tip Box
    let tipHtml = '';
    if (q.tip && q.tip.trim()) {
      tipHtml = `
        <div class="insight-box tip-box">
          <strong>💡 Interviewer Tip / Watch-out:</strong>
          <span>${escapeHtml(q.tip)}</span>
        </div>
      `;
    }

    card.innerHTML = `
      <div class="card-header">
        <div class="card-meta-left">
          <span class="badge-cat">${catName} #${q.num}</span>
          <div class="card-tags">${tagsHtml}</div>
        </div>
        <div class="card-actions">
          <button class="action-btn copy-card-btn" title="Copy Question & Answer" data-action="copy-card">📋</button>
          <button class="action-btn star-btn ${isStarred ? 'active' : ''}" title="Star Question" data-action="star">⭐</button>
          <button class="action-btn master-btn ${isMastered ? 'active' : ''}" title="Mark as Mastered" data-action="master">✔️</button>
        </div>
      </div>

      <h2 class="card-title">${highlightedTitle}</h2>

      <div class="flashcard-overlay">
        <div style="font-size:24px;">🔒</div>
        <p>Click to Reveal Answer & Test Yourself</p>
      </div>

      <div class="card-body">
        ${q.explanation}
      </div>

      ${codeHtml}
      ${metricHtml}
      ${tipHtml}

      <div class="self-test-actions">
        <button class="btn-eval-ok" data-action="eval-master">✔️ Got It Right</button>
        <button class="btn-eval-fail" data-action="eval-review">⏳ Review Again</button>
      </div>
    `;

    // Event delegation on card
    card.addEventListener('click', (e) => {
      const action = e.target.closest('[data-action]')?.dataset.action;
      const tagTarget = e.target.closest('.mini-tag');
      const flashcardOverlay = e.target.closest('.flashcard-overlay');
      const cardTitle = e.target.closest('.card-title');

      if (action === 'star') {
        toggleStar(q.id, card);
      } else if (action === 'master') {
        toggleMaster(q.id, card);
      } else if (action === 'copy-code') {
        copyText(q.code, 'Code snippet copied to clipboard!');
      } else if (action === 'copy-card') {
        const fullText = `Q: ${q.title}\n\n${card.querySelector('.card-body')?.innerText || ''}\n\nCode:\n${q.code || 'N/A'}\n\nProject Metric:\n${q.useCase || 'N/A'}\n\nTip:\n${q.tip || 'N/A'}`;
        copyText(fullText, 'Question & Answer copied!');
      } else if (action === 'eval-master') {
        if (!state.masteredIds.has(q.id)) {
          toggleMaster(q.id, card);
        }
        showToast('Great job! Marked as Mastered ✔️');
      } else if (action === 'eval-review') {
        if (state.masteredIds.has(q.id)) {
          toggleMaster(q.id, card);
        }
        showToast('Added to review queue!');
      } else if (flashcardOverlay) {
        card.classList.add('revealed');
      } else if (tagTarget) {
        const selectedTag = tagTarget.dataset.tag;
        state.selectedTag = selectedTag;
        state.currentPage = 1;
        renderPopularTags();
        applyFilters();
      } else if (cardTitle && state.viewMode === 'compact') {
        card.classList.toggle('expanded');
      }
    });

    return card;
  }

  // Star toggle
  function toggleStar(id, cardEl) {
    const starBtn = cardEl.querySelector('.star-btn');
    if (state.starredIds.has(id)) {
      state.starredIds.delete(id);
      starBtn.classList.remove('active');
      showToast('Removed from saved questions');
    } else {
      state.starredIds.add(id);
      starBtn.classList.add('active');
      showToast('Question saved to bookmarks ⭐');
    }
    saveStoredData();
    updateGlobalStats();
  }

  // Mastered toggle
  function toggleMaster(id, cardEl) {
    const masterBtn = cardEl.querySelector('.master-btn');
    if (state.masteredIds.has(id)) {
      state.masteredIds.delete(id);
      masterBtn.classList.remove('active');
      cardEl.classList.remove('is-mastered');
      showToast('Marked for review ⏳');
    } else {
      state.masteredIds.add(id);
      masterBtn.classList.add('active');
      cardEl.classList.add('is-mastered');
      showToast('Question mastered! 🎉');
    }
    saveStoredData();
    updateGlobalStats();
  }

  // Copy helper
  function copyText(str, msg) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(str).then(() => showToast(msg));
    } else {
      const textarea = document.createElement('textarea');
      textarea.value = str;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      try {
        document.execCommand('copy');
        showToast(msg);
      } catch (err) {
        console.error('Copy failed', err);
      }
      document.body.removeChild(textarea);
    }
  }

  // Toast
  let toastTimer;
  function showToast(msg) {
    clearTimeout(toastTimer);
    dom.toast.innerText = msg;
    dom.toast.classList.add('show');
    toastTimer = setTimeout(() => {
      dom.toast.classList.remove('show');
    }, 2400);
  }

  // Update Global Stats & Progress Bar
  function updateGlobalStats() {
    const total = state.allQuestions.length;
    const mastered = state.masteredIds.size;
    const starred = state.starredIds.size;
    const pct = total > 0 ? Math.round((mastered / total) * 100) : 0;

    dom.statTotal.innerText = `${total.toLocaleString()} Questions`;
    dom.statMastered.innerText = `${mastered.toLocaleString()} / ${total.toLocaleString()} (${pct}%)`;
    dom.statStarred.innerText = `${starred.toLocaleString()} Saved`;
    dom.progressFill.style.width = `${pct}%`;
  }

  // Pick Random Question (Drill Mode)
  function pickRandomQuestion() {
    if (state.filteredQuestions.length === 0) return;
    const randomIdx = Math.floor(Math.random() * state.filteredQuestions.length);
    const targetQ = state.filteredQuestions[randomIdx];

    // Find in DOM or re-render to page containing it
    const existingCard = document.getElementById(`card-${targetQ.id}`);
    if (existingCard) {
      existingCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
      existingCard.style.outline = '2px solid var(--accent-sky)';
      setTimeout(() => existingCard.style.outline = '', 2000);
      showToast(`Jumped to: ${targetQ.title.slice(0, 35)}...`);
    } else {
      // Just filter to this question
      dom.searchInput.value = targetQ.title;
      state.searchQuery = targetQ.title.toLowerCase();
      applyFilters();
      showToast(`Drilling: ${targetQ.title.slice(0, 35)}...`);
    }
  }

  // Expand / Collapse All (in compact or flashcard mode)
  let isAllExpanded = false;
  function toggleExpandAll() {
    isAllExpanded = !isAllExpanded;
    const cards = document.querySelectorAll('.q-card');
    cards.forEach(c => {
      if (isAllExpanded) {
        c.classList.add('expanded');
        c.classList.add('revealed');
      } else {
        c.classList.remove('expanded');
        c.classList.remove('revealed');
      }
    });
    dom.btnExpandAll.innerHTML = isAllExpanded ? '📂 Collapse All' : '📖 Expand All';
  }

  // Reset Progress Confirmation
  function resetProgress() {
    if (confirm('Reset your study progress? This will clear all mastered checks and saved bookmarks.')) {
      state.masteredIds.clear();
      state.starredIds.clear();
      saveStoredData();
      updateGlobalStats();
      renderQuestionsList();
      showToast('Progress has been reset');
    }
  }

  // Escape HTML helper
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Escape RegExp helper
  function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Boot up
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
