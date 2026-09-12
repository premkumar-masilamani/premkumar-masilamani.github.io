---
layout: post
lang: english
type: blog
permalink: /english/blog/:title/

date: 2026-09-09
title: Japanese Candlestick Patterns
---
<style>
    .csp-wrapper {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: inherit;
      line-height: 1.5;
      box-sizing: border-box;
      width: 100%;
      max-width: 1060px;
      margin: 0 auto;
      padding: 16px 8px 40px 8px;
    }
    .csp-wrapper *, .csp-wrapper *::before, .csp-wrapper *::after {
      box-sizing: border-box;
    }

    /* Header */
    .csp-header {
      text-align: center;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    }
    .csp-title {
      font-size: 1.9rem;
      font-weight: 700;
      margin: 0 0 10px 0;
      letter-spacing: -0.5px;
      color: inherit;
    }
    .csp-subtitle {
      opacity: 0.8;
      font-size: 0.95rem;
      max-width: 760px;
      margin: 0 auto 16px auto;
      line-height: 1.6;
    }
    .csp-legend-bar {
      display: inline-flex;
      gap: 18px;
      padding: 8px 18px;
      border-radius: 20px;
      border: 1px solid rgba(128, 128, 128, 0.3);
      font-size: 0.85rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    .csp-legend-item {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Controls */
    .csp-controls {
      margin-bottom: 28px;
      padding-bottom: 18px;
      border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    }
    .csp-search-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
    }
    .csp-search-wrapper {
      position: relative;
      flex: 1;
    }
    .csp-search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      opacity: 0.6;
      pointer-events: none;
      font-size: 1rem;
    }
    .csp-search-input {
      width: 100%;
      padding: 10px 38px 10px 40px;
      border: 1px solid rgba(128, 128, 128, 0.35);
      border-radius: 8px;
      color: inherit;
      font-size: 0.95rem;
      background: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .csp-search-input:focus {
      outline: none;
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }
    .csp-search-input::placeholder {
      opacity: 0.6;
    }
    .csp-clear-btn {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      border: none;
      color: inherit;
      opacity: 0.6;
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
      padding: 2px 6px;
      border-radius: 4px;
      display: none;
      background: none;
    }
    .csp-clear-btn:hover {
      opacity: 1;
    }
    .csp-counter-badge {
      font-size: 0.85rem;
      opacity: 0.85;
      white-space: nowrap;
      padding: 8px 14px;
      border: 1px solid rgba(128, 128, 128, 0.3);
      border-radius: 6px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* Filter Pills */
    .csp-filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }
    .csp-filter-btn {
      border: 1px solid rgba(128, 128, 128, 0.3);
      color: inherit;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: none;
      transition: all 0.15s ease;
    }
    .csp-filter-btn:hover {
      border-color: rgba(128, 128, 128, 0.6);
      opacity: 0.9;
    }
    .csp-filter-btn.active {
      border-color: #3b82f6;
      color: #3b82f6;
      font-weight: 700;
      box-shadow: 0 0 0 1px #3b82f6;
    }
    .csp-pill-count {
      display: inline-block;
      padding: 1px 6px;
      border-radius: 10px;
      border: 1px solid rgba(128, 128, 128, 0.25);
      font-size: 0.75rem;
      font-weight: 600;
    }
    .csp-filter-btn.active .csp-pill-count {
      border-color: #3b82f6;
    }

    /* Empty State */
    .csp-no-results {
      text-align: center;
      padding: 50px 20px;
      border: 1px dashed rgba(128, 128, 128, 0.3);
      border-radius: 8px;
      margin: 30px 0;
    }
    .csp-no-results-icon {
      font-size: 2.2rem;
      margin-bottom: 10px;
      opacity: 0.5;
    }
    .csp-no-results h3 {
      font-size: 1.2rem;
      margin: 0 0 6px 0;
      color: inherit;
    }
    .csp-no-results p {
      opacity: 0.75;
      font-size: 0.9rem;
      margin: 0 0 16px 0;
    }
    .csp-reset-btn {
      border: 1px solid #3b82f6;
      color: #3b82f6;
      padding: 8px 18px;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      background: none;
      transition: opacity 0.15s;
    }
    .csp-reset-btn:hover {
      opacity: 0.8;
    }

    /* Category Sections */
    .csp-category-section {
      margin-bottom: 40px;
    }
    .csp-category-header {
      margin-bottom: 12px;
    }
    .csp-category-header h2 {
      font-size: 1.3rem;
      font-weight: 700;
      margin: 0 0 4px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      color: inherit;
    }
    .csp-category-header .csp-subtitle {
      margin: 0;
      font-size: 0.88rem;
      font-style: italic;
      opacity: 0.75;
    }

    /* Pattern Table */
    .csp-table-wrapper {
      overflow-x: auto;
      border: 1px solid rgba(128, 128, 128, 0.25);
      border-radius: 8px;
      margin-top: 8px;
    }
    .csp-pattern-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .csp-pattern-table thead {
      border-bottom: 2px solid rgba(128, 128, 128, 0.25);
    }
    .csp-pattern-table th {
      padding: 12px 16px;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      opacity: 0.8;
      font-weight: 700;
      border-bottom: 1px solid rgba(128, 128, 128, 0.25);
    }
    .csp-pattern-table th.csp-col-visual {
      width: 170px;
      text-align: center;
    }
    .csp-pattern-table th.csp-col-desc {
      text-align: left;
    }
    .csp-pattern-table td {
      padding: 14px 16px;
      border-bottom: 1px solid rgba(128, 128, 128, 0.15);
      vertical-align: top;
    }
    .csp-pattern-table tr:last-child td {
      border-bottom: none;
    }
    .csp-cell-visual {
      text-align: center;
      vertical-align: middle !important;
      padding: 12px !important;
      width: 170px;
    }
    .csp-pattern-svg {
      width: 150px;
      height: 130px;
      border-radius: 6px;
      display: block;
      margin: 0 auto;
      border: 1px solid rgba(128, 128, 128, 0.25);
    }
    .csp-cell-desc {
      padding-left: 18px !important;
    }
    .csp-pattern-header-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 8px;
    }
    .csp-pattern-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin: 0;
      color: inherit;
    }
    .csp-badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .csp-badge-bull {
      color: #16a34a;
      border: 1px solid #16a34a;
    }
    .csp-badge-bear {
      color: #dc2626;
      border: 1px solid #dc2626;
    }
    .csp-badge-cont-bull {
      color: #2563eb;
      border: 1px solid #2563eb;
    }
    .csp-badge-cont-bear {
      color: #d97706;
      border: 1px solid #d97706;
    }
    .csp-badge-bars {
      opacity: 0.85;
      border: 1px solid rgba(128, 128, 128, 0.35);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    .csp-pattern-body {
      font-size: 0.88rem;
      line-height: 1.6;
    }
    .csp-label {
      font-weight: 600;
      opacity: 0.95;
      display: inline-block;
      margin-right: 4px;
    }
    .csp-desc-text {
      opacity: 0.82;
    }

    /* Mobile responsiveness */
    @media (max-width: 720px) {
      .csp-pattern-table th.csp-col-visual { width: 130px; }
      .csp-cell-visual { width: 130px; padding: 8px !important; }
      .csp-pattern-svg { width: 120px; height: 104px; }
      .csp-search-row { flex-direction: column; align-items: stretch; }
      .csp-counter-badge { text-align: center; }
      .csp-cell-desc { padding-left: 10px !important; }
    }
</style>

<script>
  (function() {
    function normalize(str) {
      return (str || '')
        .toLowerCase()
        .replace(/[—–\-]/g, ' ')
        .replace(/[^\w\s]/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
    }

    function initCandlestickSearch() {
      const searchInput = document.getElementById('csp-search-input');
      const clearSearchBtn = document.getElementById('csp-clear-search');
      const counterBadge = document.getElementById('csp-counter-badge');
      const filterButtons = document.querySelectorAll('.csp-filter-btn');
      const categorySections = document.querySelectorAll('.csp-category-section');
      const patternRows = document.querySelectorAll('.csp-pattern-row');
      const noResultsEl = document.getElementById('csp-no-results');
      const resetBtn = document.getElementById('csp-reset-filters');
      const totalCount = patternRows.length || 68;

      if (!searchInput) return;

      // Pre-compute normalized and enriched searchable text for each row
      const rowData = Array.from(patternRows).map(function(row) {
        const rawSearchable = (row.dataset.searchable || '') + ' ' + (row.textContent || '');
        const norm = normalize(rawSearchable);
        // Include common synonyms and number variants
        const enriched = norm + ' ' +
          norm.replace(/\bshadow\b/g, 'wick')
              .replace(/\bwick\b/g, 'shadow')
              .replace(/\bone\b/g, '1')
              .replace(/\btwo\b/g, '2')
              .replace(/\bthree\b/g, '3')
              .replace(/\bfour\b/g, '4')
              .replace(/\bfive\b/g, '5');
        return {
          element: row,
          group: row.dataset.group,
          searchable: enriched,
          matchesSearch: true
        };
      });

      let currentGroup = 'all';

      function updateFilters(options) {
        options = options || {};
        const rawQuery = (searchInput.value || '').trim();
        const query = normalize(rawQuery);
        const terms = query.split(/\s+/).filter(Boolean);

        let totalVisible = 0;
        const groupCounts = {
          'all': 0,
          'bullish-reversals': 0,
          'bearish-reversals': 0,
          'bullish-continuations': 0,
          'bearish-continuations': 0
        };

        // First pass: evaluate search matches across all rows
        rowData.forEach(function(item) {
          const matches = terms.length === 0 || terms.every(function(term) {
            return item.searchable.indexOf(term) !== -1;
          });
          item.matchesSearch = matches;
          if (matches) {
            groupCounts['all']++;
            if (groupCounts[item.group] !== undefined) {
              groupCounts[item.group]++;
            }
          }
        });

        // If user is searching and the previously active category has 0 matches,
        // automatically switch to 'all' so matching patterns from other categories are shown
        if (options.fromInput && currentGroup !== 'all' && terms.length > 0) {
          if (groupCounts[currentGroup] === 0 && groupCounts['all'] > 0) {
            currentGroup = 'all';
            filterButtons.forEach(function(btn) {
              btn.classList.toggle('active', btn.dataset.group === 'all');
            });
          }
        }

        // Second pass: apply row visibility
        rowData.forEach(function(item) {
          const matchesGroup = (currentGroup === 'all' || currentGroup === item.group);
          if (item.matchesSearch && matchesGroup) {
            item.element.style.display = '';
            totalVisible++;
          } else {
            item.element.style.display = 'none';
          }
        });

        // Category section visibility based on group counts
        categorySections.forEach(function(section) {
          const sGroup = section.dataset.group;
          if (currentGroup !== 'all' && currentGroup !== sGroup) {
            section.style.display = 'none';
          } else {
            section.style.display = (groupCounts[sGroup] > 0) ? '' : 'none';
          }
        });

        // Pill counts
        filterButtons.forEach(function(btn) {
          const grp = btn.dataset.group;
          const countSpan = btn.querySelector('.csp-pill-count');
          if (countSpan && groupCounts[grp] !== undefined) {
            countSpan.textContent = groupCounts[grp];
          }
        });

        // Counter badge & clear button
        if (counterBadge) {
          counterBadge.textContent = 'Showing ' + totalVisible + ' of ' + totalCount + ' patterns';
        }
        if (clearSearchBtn) {
          clearSearchBtn.style.display = rawQuery.length > 0 ? 'block' : 'none';
        }

        // Empty state
        if (noResultsEl) {
          noResultsEl.style.display = (totalVisible === 0) ? 'block' : 'none';
        }
      }

      // Input event listeners (cover typing, autocomplete, keyup, change, paste)
      function handleInputChange() {
        updateFilters({ fromInput: true });
      }
      searchInput.addEventListener('input', handleInputChange);
      searchInput.addEventListener('keyup', handleInputChange);
      searchInput.addEventListener('change', handleInputChange);
      searchInput.addEventListener('search', handleInputChange);

      searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
          searchInput.value = '';
          updateFilters({ fromInput: true });
        } else if (e.key === 'Enter') {
          e.preventDefault();
          const firstVisible = document.querySelector('.csp-pattern-row:not([style*="display: none"])');
          if (firstVisible) {
            firstVisible.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      });

      // Clear search button
      if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', function() {
          searchInput.value = '';
          searchInput.focus();
          updateFilters({ fromInput: true });
        });
      }

      // Category filter buttons
      filterButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
          filterButtons.forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          currentGroup = this.dataset.group;
          updateFilters({ fromInput: false });
        });
      });

      // Reset filters button
      if (resetBtn) {
        resetBtn.addEventListener('click', function() {
          searchInput.value = '';
          currentGroup = 'all';
          filterButtons.forEach(function(b) {
            b.classList.toggle('active', b.dataset.group === 'all');
          });
          updateFilters({ fromInput: false });
          searchInput.focus();
        });
      }

      // Check URL hash on initial load
      if (window.location.hash) {
        const targetId = window.location.hash.replace('#', '');
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          setTimeout(function() {
            targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }, 200);
        }
      }

      // Initial filter run
      updateFilters({ fromInput: false });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initCandlestickSearch);
    } else {
      initCandlestickSearch();
    }
  })();
</script>

<div class="csp-wrapper">
    <!-- Controls -->
    <div class="csp-controls">
      <div class="csp-search-row">
        <div class="csp-search-wrapper">
          <span class="csp-search-icon">&#128269;</span>
          <input type="text" id="csp-search-input" class="csp-search-input" placeholder="Search 68 patterns by name, structure, psychology, outcome, or bars (e.g. Hammer, Doji, Reversal, Gap)..." autocomplete="off" spellcheck="false">
          <button type="button" id="csp-clear-search" class="csp-clear-btn" title="Clear search">&times;</button>
        </div>
        <div id="csp-counter-badge" class="csp-counter-badge">Showing 68 of 68 patterns</div>
      </div>

      <div class="csp-filter-pills" role="tablist" aria-label="Category filters">
        <button type="button" class="csp-filter-btn active" data-group="all">
          All <span class="csp-pill-count">68</span>
        </button>
        <button type="button" class="csp-filter-btn" data-group="bullish-reversals">
          Bullish Reversals <span class="csp-pill-count">26</span>
        </button>
        <button type="button" class="csp-filter-btn" data-group="bearish-reversals">
          Bearish Reversals <span class="csp-pill-count">26</span>
        </button>
        <button type="button" class="csp-filter-btn" data-group="bullish-continuations">
          Bullish Continuations <span class="csp-pill-count">8</span>
        </button>
        <button type="button" class="csp-filter-btn" data-group="bearish-continuations">
          Bearish Continuations <span class="csp-pill-count">8</span>
        </button>
      </div>
    </div>

    <!-- Empty State -->
    <div id="csp-no-results" class="csp-no-results" style="display: none;">
      <div class="csp-no-results-icon">&#128269;</div>
      <h3>No matching candlestick patterns found</h3>
      <p>Try adjusting your search keywords or resetting category filters.</p>
      <button type="button" id="csp-reset-filters" class="csp-reset-btn">Reset All Filters</button>
    </div>

    <!-- Category Sections -->
    <section id="section-bullish-reversals" class="csp-category-section" data-group="bullish-reversals">
      <div class="csp-category-header">
        <h2>
          <span>Part I: Bullish Reversals</span>
          <span class="csp-badge csp-badge-bull">26 Patterns</span>
        </h2>
        <p class="csp-subtitle">Appears at the bottom of a downtrend; signals sellers are exhausted and buyers are taking control.</p>
      </div>
      <div class="csp-table-wrapper">
        <table class="csp-pattern-table">
          <thead>
            <tr>
              <th class="csp-col-visual">Visual Pattern</th>
              <th class="csp-col-desc">Pattern Name &amp; Market Dynamics</th>
            </tr>
          </thead>
          <tbody>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="long-white-body" data-searchable="long white body (1) long-white-body bullish reversal 1 bar bars structure: single tall green candle with a large body appearing after a decline. psychology: relentless buying pressure dominates the session from opening to close. outcome: strong buying pressure; may signal continuation or, when appearing after a decline, a potential bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Long White Body (1)">
                <line x1="75" y1="20" x2="75" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="63" y="35" width="24" height="60" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Long White Body (1)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Single tall green candle with a large body appearing after a decline.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Relentless buying pressure dominates the session from opening to close.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Strong buying pressure; may signal continuation or, when appearing after a decline, a potential bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="hammer" data-searchable="hammer (1) hammer bullish reversal 1 bar bars structure: small body near the top of the range after a decline, with a long lower shadow (&gt;= 2x body) and minimal upper shadow. psychology: intraday sell-off is firmly rejected by buyers pushing price back near the session high. outcome: potential bullish reversal; confirmation above the hammer's high strengthens the signal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Hammer (1)">
                <line x1="75" y1="35" x2="75" y2="115" stroke="#2ecc71" stroke-width="2"/> <rect x="64" y="38" width="22" height="12" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Hammer (1)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body near the top of the range after a decline, with a long lower shadow (&gt;= 2x body) and minimal upper shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Intraday sell-off is firmly rejected by buyers pushing price back near the session high.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Potential bullish reversal; confirmation above the hammer&#39;s high strengthens the signal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="inverted-hammer" data-searchable="inverted hammer (1) inverted-hammer bullish reversal 1 bar bars structure: small body near the bottom of the range after a decline, with a long upper shadow (&gt;= 2x body) and minimal lower shadow. psychology: buyers attempt an intraday counter-attack; while rejected from highs, emerging demand is demonstrated. outcome: early sign of potential bullish reversal; a strong bullish candle above the pattern confirms improving demand.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Inverted Hammer (1)">
                <line x1="75" y1="25" x2="75" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="64" y="88" width="22" height="12" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Inverted Hammer (1)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body near the bottom of the range after a decline, with a long upper shadow (&gt;= 2x body) and minimal lower shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buyers attempt an intraday counter-attack; while rejected from highs, emerging demand is demonstrated.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Early sign of potential bullish reversal; a strong bullish candle above the pattern confirms improving demand.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-belt-hold" data-searchable="belt hold (1) bullish-belt-hold bullish reversal 1 bar bars structure: tall green candle opening at or near its low after a decline and rallying to close near its high with little to no lower shadow. psychology: buyers take control from the open without conceding ground, sustaining upward pressure. outcome: strong buying from the open may mark a bullish reversal; follow-through above the candle high strengthens the signal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Belt Hold (1)">
                <line x1="75" y1="25" x2="75" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="63" y="30" width="24" height="75" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Belt Hold (1)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Tall green candle opening at or near its low after a decline and rallying to close near its high with little to no lower shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buyers take control from the open without conceding ground, sustaining upward pressure.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Strong buying from the open may mark a bullish reversal; follow-through above the candle high strengthens the signal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-engulfing" data-searchable="engulfing pattern (2) bullish-engulfing bullish reversal 2 bar bars structure: a small red body engulfed completely by a subsequent taller green body appearing after a downtrend. psychology: a lower open attracts strong demand, overwhelming prior selling pressure. outcome: sellers lose control as buyers overwhelm the prior session's body; a move above the engulfing candle's high confirms the reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Engulfing Pattern (2)">
                <line x1="55" y1="45" x2="55" y2="90" stroke="#e74c3c" stroke-width="2"/> <rect x="45" y="55" width="20" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="25" x2="95" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="83" y="35" width="24" height="53" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Engulfing Pattern (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A small red body engulfed completely by a subsequent taller green body appearing after a downtrend.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A lower open attracts strong demand, overwhelming prior selling pressure.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sellers lose control as buyers overwhelm the prior session&#39;s body; a move above the engulfing candle&#39;s high confirms the reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-harami" data-searchable="harami (2) bullish-harami bullish reversal 2 bar bars structure: large red candle followed by a smaller green candle whose body is contained entirely inside day 1's body. psychology: downward momentum stalls abruptly as sellers fail to expand the range. outcome: selling momentum weakens; a subsequent break above the pattern strengthens the bullish reversal signal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Harami (2)">
                <line x1="55" y1="25" x2="55" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="43" y="35" width="24" height="60" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="50" x2="95" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="86" y="60" width="18" height="20" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Harami (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Large red candle followed by a smaller green candle whose body is contained entirely inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downward momentum stalls abruptly as sellers fail to expand the range.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Selling momentum weakens; a subsequent break above the pattern strengthens the bullish reversal signal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-harami-cross" data-searchable="harami cross (2) bullish-harami-cross bullish reversal 2 bar bars structure: long red candle followed by a doji whose body is contained within the boundaries of day 1's body. psychology: selling pressure dissipates into balance and indecision following an extended decline. outcome: stronger form of the bullish harami, indicating indecision after a decline; bullish follow-through is needed for confirmation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Harami Cross (2)">
                <line x1="55" y1="25" x2="55" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="43" y="35" width="24" height="60" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="50" x2="95" y2="80" stroke="#f1c40f" stroke-width="2"/> <line x1="86" y1="65" x2="104" y2="65" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Harami Cross (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a Doji whose body is contained within the boundaries of Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling pressure dissipates into balance and indecision following an extended decline.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Stronger form of the bullish Harami, indicating indecision after a decline; bullish follow-through is needed for confirmation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="piercing-line" data-searchable="piercing line (2) piercing-line bullish reversal 2 bar bars structure: long red candle followed by a green candle that opens below day 1's low and closes above the 50% midpoint of day 1 (but below day 1's open). psychology: an initial gap-down is rejected as buyers recover more than half of the prior session's losses. outcome: sellers lose control after a gap-down; recovery above the midpoint signals a potential bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Piercing Line (2)">
                <line x1="55" y1="25" x2="55" y2="95" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="50" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="40" x2="95" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="55" width="22" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Piercing Line (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a green candle that opens below Day 1&#39;s low and closes above the 50% midpoint of Day 1 (but below Day 1&#39;s open).</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An initial gap-down is rejected as buyers recover more than half of the prior session&#39;s losses.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sellers lose control after a gap-down; recovery above the midpoint signals a potential bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-doji-star" data-searchable="doji star (2) bullish-doji-star bullish reversal 2 bar bars structure: long red candle followed by a doji that gaps down beneath day 1's body. psychology: sellers force a gap lower but fail to generate follow-through, leading to market balance. outcome: selling momentum stalls after a gap-down; a bullish confirmation candle increases the likelihood of a reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Doji Star (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="40" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="88" x2="95" y2="115" stroke="#f1c40f" stroke-width="2"/> <line x1="86" y1="100" x2="104" y2="100" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Doji Star (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a Doji that gaps down beneath Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers force a gap lower but fail to generate follow-through, leading to market balance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Selling momentum stalls after a gap-down; a bullish confirmation candle increases the likelihood of a reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-meeting-lines" data-searchable="meeting lines (2) bullish-meeting-lines bullish reversal 2 bar bars structure: long red candle followed by a green candle opening sharply lower and closing at the same price as day 1's close. psychology: bulls counter-attack the gap-down with equal force to close level with day 1. outcome: selling pressure is met by strong buying, producing matching closes; subsequent upside confirmation supports a bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Meeting Lines (2)">
                <line x1="55" y1="30" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="40" width="22" height="40" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="75" x2="95" y2="115" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="80" width="22" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Meeting Lines (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a green candle opening sharply lower and closing at the same price as Day 1&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bulls counter-attack the gap-down with equal force to close level with Day 1.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Selling pressure is met by strong buying, producing matching closes; subsequent upside confirmation supports a bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-white-soldiers" data-searchable="three white soldiers (3) three-white-soldiers bullish reversal 3 bar bars structure: three consecutive long green candles after a decline, each opening within the prior body and closing near its high. psychology: consistent buying pressure dominates consecutive sessions without significant pullbacks. outcome: sustained buying pressure across three sessions signals a strong shift toward bullish control.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three White Soldiers (3)">
                <line x1="40" y1="65" x2="40" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="70" width="18" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="40" x2="75" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="45" width="18" height="33" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="18" x2="110" y2="60" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="22" width="18" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three White Soldiers (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive long green candles after a decline, each opening within the prior body and closing near its high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Consistent buying pressure dominates consecutive sessions without significant pullbacks.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sustained buying pressure across three sessions signals a strong shift toward bullish control.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="morning-star" data-searchable="morning star (3) morning-star bullish reversal 3 bar bars structure: long red candle, a downward-gapping small body, and a long green candle closing well into day 1's body (typically above its midpoint). psychology: selling pressure gives way to indecision, followed by decisive buyer dominance. outcome: selling pressure gives way to indecision and then strong buying; a close well into the first candle's body supports a bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Morning Star (3)">
                <line x1="40" y1="25" x2="40" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="88" x2="75" y2="115" stroke="#2ecc71" stroke-width="2"/> <rect x="67" y="95" width="16" height="10" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="30" x2="110" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="100" y="40" width="20" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Morning Star (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, a downward-gapping small body, and a long green candle closing well into Day 1&#39;s body (typically above its midpoint).</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling pressure gives way to indecision, followed by decisive buyer dominance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Selling pressure gives way to indecision and then strong buying; a close well into the first candle&#39;s body supports a bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="morning-doji-star" data-searchable="morning doji star (3) morning-doji-star bullish reversal 3 bar bars structure: long red candle, a downward-gapping isolated doji, and a long green candle closing deeply into day 1's body. psychology: a sharp decline transitions into acute market indecision, which buyers then resolve upward. outcome: a doji after a sharp decline signals strong indecision; bullish follow-through can confirm a reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Morning Doji Star (3)">
                <line x1="40" y1="25" x2="40" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="90" x2="75" y2="115" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="102" x2="83" y2="102" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="30" x2="110" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="100" y="40" width="20" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Morning Doji Star (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, a downward-gapping isolated Doji, and a long green candle closing deeply into Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A sharp decline transitions into acute market indecision, which buyers then resolve upward.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A Doji after a sharp decline signals strong indecision; bullish follow-through can confirm a reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-abandoned-baby" data-searchable="abandoned baby (3) bullish-abandoned-baby bullish reversal 3 bar bars structure: long red candle, an isolated doji gapping below both neighboring candles' shadows, and a green candle gapping up. psychology: an island formation occurs where selling exhausts on a gap-down, followed by an immediate upward gap. outcome: an isolated doji after a gap-down signals exhaustion; a gap-up reversal candle confirms a potential bullish turn.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Abandoned Baby (3)">
                <line x1="40" y1="25" x2="40" y2="75" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="92" x2="75" y2="112" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="102" x2="83" y2="102" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="25" x2="110" y2="75" stroke="#2ecc71" stroke-width="2"/> <rect x="100" y="35" width="20" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Abandoned Baby (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, an isolated Doji gapping below both neighboring candles&#39; shadows, and a green candle gapping up.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An island formation occurs where selling exhausts on a gap-down, followed by an immediate upward gap.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">An isolated Doji after a gap-down signals exhaustion; a gap-up reversal candle confirms a potential bullish turn.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-tri-star" data-searchable="tri-star (3) bullish-tri-star bullish reversal 3 bar bars structure: three consecutive dojis appearing after a decline, with the middle doji gapping below the other two. psychology: selling momentum dissipates into extreme, sustained indecision across three sessions. outcome: rare sequence showing extreme indecision after a decline; upside follow-through may signal a bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Tri-Star (3)">
                <line x1="40" y1="40" x2="40" y2="70" stroke="#f1c40f" stroke-width="2"/> <line x1="32" y1="55" x2="48" y2="55" stroke="#f1c40f" stroke-width="3"/> <line x1="75" y1="75" x2="75" y2="105" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="90" x2="83" y2="90" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="40" x2="110" y2="70" stroke="#f1c40f" stroke-width="2"/> <line x1="102" y1="55" x2="118" y2="55" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Tri-Star (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive Dojis appearing after a decline, with the middle Doji gapping below the other two.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling momentum dissipates into extreme, sustained indecision across three sessions.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Rare sequence showing extreme indecision after a decline; upside follow-through may signal a bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-breakaway" data-searchable="breakaway (5) bullish-breakaway bullish reversal 5 bar bars structure: long red candle, downside gap to a red candle, three smaller declining bodies, followed by a strong green candle closing within the initial gap. psychology: downward momentum gradually weakens after an initial gap before buyers drive price back into the gap. outcome: downward momentum gradually weakens before a strong bullish candle breaks back into the gap, signaling a potential reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Breakaway (5)">
                <line x1="28" y1="20" x2="28" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="21" y="25" width="14" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="50" y1="65" x2="50" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="70" width="12" height="12" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="72" y1="80" x2="72" y2="98" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="83" width="12" height="11" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="94" y1="90" x2="94" y2="108" stroke="#e74c3c" stroke-width="2"/> <rect x="88" y="93" width="12" height="11" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="122" y1="45" x2="122" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="114" y="50" width="16" height="50" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Breakaway (5)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, downside gap to a red candle, three smaller declining bodies, followed by a strong green candle closing within the initial gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downward momentum gradually weakens after an initial gap before buyers drive price back into the gap.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Downward momentum gradually weakens before a strong bullish candle breaks back into the gap, signaling a potential reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-inside-up" data-searchable="three inside up (3) three-inside-up bullish reversal 3 bar bars structure: a bullish harami followed by a third green candle that closes above the second candle's high. psychology: selling pressure halts within the prior candle, and follow-through buying confirms buyers are gaining control. outcome: the harami signals weakening selling pressure; the third candle confirms that buyers are gaining control.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Inside Up (3)">
                <line x1="40" y1="25" x2="40" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="55" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="50" x2="75" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="67" y="60" width="16" height="20" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="20" x2="110" y2="70" stroke="#2ecc71" stroke-width="2"/> <rect x="100" y="28" width="20" height="37" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Inside Up (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A Bullish Harami followed by a third green candle that closes above the second candle&#39;s high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling pressure halts within the prior candle, and follow-through buying confirms buyers are gaining control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The Harami signals weakening selling pressure; the third candle confirms that buyers are gaining control.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-outside-up" data-searchable="three outside up (3) three-outside-up bullish reversal 3 bar bars structure: a bullish engulfing pattern followed by a third green candle closing higher than day 2. psychology: momentum shifts toward buyers during the engulfing session, with follow-through confirming demand. outcome: the engulfing pattern shifts momentum toward buyers, and the third candle provides bullish confirmation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Outside Up (3)">
                <line x1="40" y1="50" x2="40" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="32" y="55" width="16" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="30" x2="75" y2="100" stroke="#2ecc71" stroke-width="2"/> <rect x="64" y="40" width="22" height="48" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="15" x2="110" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="100" y="20" width="20" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Outside Up (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A Bullish Engulfing pattern followed by a third green candle closing higher than Day 2.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Momentum shifts toward buyers during the engulfing session, with follow-through confirming demand.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The engulfing pattern shifts momentum toward buyers, and the third candle provides bullish confirmation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-kicking" data-searchable="kicking (2) bullish-kicking bullish reversal 2 bar bars structure: red marubozu followed by a green marubozu that gaps up above day 1's open. psychology: an immediate gap above the previous open reflects an abrupt shift in market balance. outcome: a sharp gap in the opposite direction shows an abrupt shift in market control and can produce a strong bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Kicking (2)">
                <line x1="55" y1="60" x2="55" y2="110" stroke="#e74c3c" stroke-width="2"/> <rect x="43" y="60" width="24" height="50" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="50" stroke="#2ecc71" stroke-width="2"/> <rect x="83" y="15" width="24" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Kicking (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red Marubozu followed by a green Marubozu that gaps up above Day 1&#39;s open.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An immediate gap above the previous open reflects an abrupt shift in market balance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A sharp gap in the opposite direction shows an abrupt shift in market control and can produce a strong bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="unique-three-rivers-bottom" data-searchable="unique three rivers bottom (3) unique-three-rivers-bottom bullish reversal 3 bar bars structure: long red candle, followed by a smaller red candle within day 1's body making a new low with a long lower shadow, then a small green candle whose low remains above day 2's low. psychology: a new downside extreme is rejected intraday, and subsequent stabilization indicates selling exhaustion. outcome: a new downside extreme is rejected, followed by stabilization; a bullish third candle signals a potential bottom.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Unique Three Rivers Bottom (3)">
                <line x1="40" y1="30" x2="40" y2="90" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="50" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="55" x2="75" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="67" y="60" width="16" height="15" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="70" x2="110" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="102" y="78" width="16" height="12" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Unique Three Rivers Bottom (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, followed by a smaller red candle within Day 1&#39;s body making a new low with a long lower shadow, then a small green candle whose low remains above Day 2&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A new downside extreme is rejected intraday, and subsequent stabilization indicates selling exhaustion.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A new downside extreme is rejected, followed by stabilization; a bullish third candle signals a potential bottom.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-stars-in-the-south" data-searchable="three stars in the south (3) three-stars-in-the-south bullish reversal 3 bar bars structure: three declining red candles: day 1 has a long lower shadow; day 2 has a smaller body and a higher low; day 3 is a small red body contained within day 2's range. psychology: sellers make progressively less downward progress each session, unable to force lower lows. outcome: successively weaker bearish candles show selling momentum fading; the pattern warns of a potential bullish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Stars in the South (3)">
                <line x1="40" y1="30" x2="40" y2="110" stroke="#e74c3c" stroke-width="2"/> <rect x="30" y="35" width="20" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="45" x2="75" y2="95" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="50" width="18" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="55" x2="110" y2="75" stroke="#e74c3c" stroke-width="2"/> <rect x="102" y="58" width="16" height="14" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Stars in the South (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three declining red candles: Day 1 has a long lower shadow; Day 2 has a smaller body and a higher low; Day 3 is a small red body contained within Day 2&#39;s range.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers make progressively less downward progress each session, unable to force lower lows.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Successively weaker bearish candles show selling momentum fading; the pattern warns of a potential bullish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="concealing-swallow" data-searchable="concealing swallow (4) concealing-swallow bullish reversal 4 bar bars structure: four red candles: two falling marubozus, an inverted-hammer-like red candle gapping down, engulfed by a fourth red engulfing candle. psychology: intense selling reaches an extreme climax as an attempted extension fails and the final candle consumes day 3's range. outcome: persistent selling becomes vulnerable after the third candle's failed downside extension; the fourth candle's engulfing action signals potential exhaustion and reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Concealing Swallow (4)">
                <line x1="35" y1="25" x2="35" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="27" y="25" width="16" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="60" y1="50" x2="60" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="52" y="50" width="16" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="85" y1="60" x2="85" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="78" y="95" width="14" height="10" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="115" y1="45" x2="115" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="106" y="50" width="18" height="60" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Concealing Swallow (4)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">4 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Four red candles: two falling Marubozus, an inverted-hammer-like red candle gapping down, engulfed by a fourth red engulfing candle.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Intense selling reaches an extreme climax as an attempted extension fails and the final candle consumes Day 3&#39;s range.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Persistent selling becomes vulnerable after the third candle&#39;s failed downside extension; the fourth candle&#39;s engulfing action signals potential exhaustion and reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-stick-sandwich" data-searchable="stick sandwich (3) bullish-stick-sandwich bullish reversal 3 bar bars structure: two red candles with matching closing prices sandwiching a green candle in a downtrend. psychology: support is tested twice at the same price level with an interim bounce showing buying interest. outcome: repeated support at the matching closes suggests a possible bullish reversal; confirmation above the pattern is recommended.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Stick Sandwich (3)">
                <line x1="40" y1="30" x2="40" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="35" width="18" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="25" x2="75" y2="80" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="35" width="18" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="30" x2="110" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="35" width="18" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Stick Sandwich (3)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two red candles with matching closing prices sandwiching a green candle in a downtrend.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Support is tested twice at the same price level with an interim bounce showing buying interest.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Repeated support at the matching closes suggests a possible bullish reversal; confirmation above the pattern is recommended.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="homing-pigeon" data-searchable="homing pigeon (2) homing-pigeon bullish reversal 2 bar bars structure: large red candle followed by a smaller red candle whose body is contained completely inside day 1's body. psychology: selling momentum contracts as the second red candle fails to extend lower, reflecting seller hesitation. outcome: selling momentum contracts as the second bearish candle remains inside the first; bullish follow-through is needed to confirm a reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Homing Pigeon (2)">
                <line x1="55" y1="25" x2="55" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="60" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="50" x2="95" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="86" y="55" width="18" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Homing Pigeon (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Large red candle followed by a smaller red candle whose body is contained completely inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling momentum contracts as the second red candle fails to extend lower, reflecting seller hesitation.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Selling momentum contracts as the second bearish candle remains inside the first; bullish follow-through is needed to confirm a reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="ladder-bottom" data-searchable="ladder bottom (5) ladder-bottom bullish reversal 5 bar bars structure: three declining red candles, a fourth candle with an upper shadow showing hesitation, followed by a decisive green candle opening above day 4's body and closing strongly higher. psychology: downtrend momentum slows as buyers attempt an upside move on day 4, followed by strong buying follow-through on day 5. outcome: three declining candles are followed by weakening bearish momentum and then a strong bullish breakout, signaling a potential trend reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Ladder Bottom (5)">
                <line x1="28" y1="20" x2="28" y2="50" stroke="#e74c3c" stroke-width="2"/> <rect x="22" y="25" width="12" height="23" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="50" y1="42" x2="50" y2="68" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="46" width="12" height="19" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="72" y1="60" x2="72" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="63" width="12" height="19" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="94" y1="62" x2="94" y2="98" stroke="#e74c3c" stroke-width="2"/> <rect x="88" y="80" width="12" height="15" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="122" y1="30" x2="122" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="114" y="35" width="16" height="43" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Ladder Bottom (5)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three declining red candles, a fourth candle with an upper shadow showing hesitation, followed by a decisive green candle opening above Day 4&#39;s body and closing strongly higher.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downtrend momentum slows as buyers attempt an upside move on Day 4, followed by strong buying follow-through on Day 5.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Three declining candles are followed by weakening bearish momentum and then a strong bullish breakout, signaling a potential trend reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="matching-low" data-searchable="matching low (2) matching-low bullish reversal 2 bar bars structure: two consecutive red candles in a downtrend sharing approximately the same closing price, typically with little to no lower shadow. psychology: sellers fail to push the close beneath the prior session's level, establishing a potential short-term floor. outcome: repeated support at the same closing price suggests selling pressure is losing strength; bullish confirmation is preferred before treating it as a reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Matching Low (2)">
                <line x1="55" y1="30" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="45" x2="95" y2="80" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="50" width="22" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Matching Low (2)</h3>
                <span class="csp-badge csp-badge-bull">Bullish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two consecutive red candles in a downtrend sharing approximately the same closing price, typically with little to no lower shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers fail to push the close beneath the prior session&#39;s level, establishing a potential short-term floor.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Repeated support at the same closing price suggests selling pressure is losing strength; bullish confirmation is preferred before treating it as a reversal.</span></div>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </section>
    <section id="section-bearish-reversals" class="csp-category-section" data-group="bearish-reversals">
      <div class="csp-category-header">
        <h2>
          <span>Part II: Bearish Reversals</span>
          <span class="csp-badge csp-badge-bear">26 Patterns</span>
        </h2>
        <p class="csp-subtitle">Appears at the peak of an uptrend; signals buyers are exhausted and distribution is underway.</p>
      </div>
      <div class="csp-table-wrapper">
        <table class="csp-pattern-table">
          <thead>
            <tr>
              <th class="csp-col-visual">Visual Pattern</th>
              <th class="csp-col-desc">Pattern Name &amp; Market Dynamics</th>
            </tr>
          </thead>
          <tbody>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="long-black-body" data-searchable="long black body (1) long-black-body bearish reversal 1 bar bars structure: single tall red candle with a large body appearing after an advance. psychology: heavy selling pressure dominates the session from open to close. outcome: strong selling pressure; may signal continuation or, after an advance, a potential bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Long Black Body (1)">
                <line x1="75" y1="20" x2="75" y2="110" stroke="#e74c3c" stroke-width="2"/> <rect x="63" y="35" width="24" height="60" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Long Black Body (1)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Single tall red candle with a large body appearing after an advance.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Heavy selling pressure dominates the session from open to close.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Strong selling pressure; may signal continuation or, after an advance, a potential bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="hanging-man" data-searchable="hanging man (1) hanging-man bearish reversal 1 bar bars structure: small body near the top of an advance with a long lower shadow (&gt;= 2x body) and minimal upper shadow, followed by a red confirmation candle. psychology: intraday sell-off reveals sudden vulnerability; buyers recover the close, but supply is active. outcome: late-session recovery after a sharp sell-off warns of vulnerability; a lower close confirms bearish reversal pressure.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Hanging Man (1)">
                <line x1="75" y1="35" x2="75" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="64" y="38" width="22" height="12" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Hanging Man (1)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body near the top of an advance with a long lower shadow (&gt;= 2x body) and minimal upper shadow, followed by a red confirmation candle.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Intraday sell-off reveals sudden vulnerability; buyers recover the close, but supply is active.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Late-session recovery after a sharp sell-off warns of vulnerability; a lower close confirms bearish reversal pressure.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="shooting-star" data-searchable="shooting star (1) shooting-star bearish reversal 1 bar bars structure: small body near the bottom of the range after an advance, with a long upper shadow (&gt;= 2x body) and minimal lower shadow. psychology: buyers drive price sharply higher but fail to sustain the advance, retreating into the close. outcome: buyers push prices sharply higher but fail to hold the advance; a break below the candle's low strengthens the bearish signal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Shooting Star (1)">
                <line x1="75" y1="25" x2="75" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="64" y="88" width="22" height="12" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Shooting Star (1)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body near the bottom of the range after an advance, with a long upper shadow (&gt;= 2x body) and minimal lower shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buyers drive price sharply higher but fail to sustain the advance, retreating into the close.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Buyers push prices sharply higher but fail to hold the advance; a break below the candle&#39;s low strengthens the bearish signal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-belt-hold" data-searchable="bearish belt hold (1) bearish-belt-hold bearish reversal 1 bar bars structure: tall red candle opening at or near its high after an advance and falling steadily to close near its low with little to no upper shadow. psychology: sellers take control immediately from the open and sustain downward pressure throughout the session. outcome: sellers take control from the open and dominate the session; the pattern warns of a potential bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Belt Hold (1)">
                <line x1="75" y1="25" x2="75" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="63" y="25" width="24" height="75" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Belt Hold (1)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">1 Bar</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Tall red candle opening at or near its high after an advance and falling steadily to close near its low with little to no upper shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers take control immediately from the open and sustain downward pressure throughout the session.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sellers take control from the open and dominate the session; the pattern warns of a potential bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-engulfing" data-searchable="bearish engulfing (2) bearish-engulfing bearish reversal 2 bar bars structure: a small green body engulfed completely by a subsequent taller red body appearing after an advance. psychology: an initial higher open attracts heavy supply, wiping out the prior session's advance. outcome: buyers lose control as sellers overwhelm the prior session's body; a break below the engulfing candle strengthens the reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Engulfing (2)">
                <line x1="55" y1="45" x2="55" y2="90" stroke="#2ecc71" stroke-width="2"/> <rect x="45" y="55" width="20" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="25" x2="95" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="83" y="35" width="24" height="55" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Engulfing (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A small green body engulfed completely by a subsequent taller red body appearing after an advance.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An initial higher open attracts heavy supply, wiping out the prior session&#39;s advance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Buyers lose control as sellers overwhelm the prior session&#39;s body; a break below the engulfing candle strengthens the reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-harami" data-searchable="bearish harami (2) bearish-harami bearish reversal 2 bar bars structure: large green candle followed by a smaller red candle whose body is contained entirely inside day 1's body. psychology: buying momentum stalls as buyers fail to expand the range beyond prior levels. outcome: buying momentum stalls as the smaller candle remains inside the prior body; downside follow-through supports a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Harami (2)">
                <line x1="55" y1="25" x2="55" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="43" y="35" width="24" height="60" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="50" x2="95" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="86" y="55" width="18" height="20" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Harami (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Large green candle followed by a smaller red candle whose body is contained entirely inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buying momentum stalls as buyers fail to expand the range beyond prior levels.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Buying momentum stalls as the smaller candle remains inside the prior body; downside follow-through supports a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-harami-cross" data-searchable="bearish harami cross (2) bearish-harami-cross bearish reversal 2 bar bars structure: long green candle followed by a doji nested completely within day 1's body. psychology: strong buying momentum gives way to hesitation and equilibrium at the highs. outcome: strong buying momentum gives way to indecision; a bearish break after the doji confirms the potential reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Harami Cross (2)">
                <line x1="55" y1="25" x2="55" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="43" y="35" width="24" height="60" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="50" x2="95" y2="80" stroke="#f1c40f" stroke-width="2"/> <line x1="86" y1="65" x2="104" y2="65" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Harami Cross (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a Doji nested completely within Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Strong buying momentum gives way to hesitation and equilibrium at the highs.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Strong buying momentum gives way to indecision; a bearish break after the Doji confirms the potential reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="dark-cloud-cover" data-searchable="dark cloud cover (2) dark-cloud-cover bearish reversal 2 bar bars structure: long green candle followed by a red candle opening above day 1's high and closing below the midpoint of day 1's green body, but above its open. psychology: a gap-up to new highs is rejected as sellers push price below the midpoint of the prior advance. outcome: a gap-up fails as sellers push price below the midpoint of the prior bullish candle, warning of a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Dark Cloud Cover (2)">
                <line x1="55" y1="25" x2="55" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="35" width="22" height="50" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="18" x2="95" y2="80" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="25" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Dark Cloud Cover (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a red candle opening above Day 1&#39;s high and closing below the midpoint of Day 1&#39;s green body, but above its open.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A gap-up to new highs is rejected as sellers push price below the midpoint of the prior advance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A gap-up fails as sellers push price below the midpoint of the prior bullish candle, warning of a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-doji-star" data-searchable="bearish doji star (2) bearish-doji-star bearish reversal 2 bar bars structure: long green candle followed by a doji that gaps above day 1's body. psychology: an opening gap-up stalls as buyers fail to generate further upward progress, resulting in balance. outcome: a gap-up doji shows that buying momentum has stalled; a bearish confirmation candle strengthens the reversal signal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Doji Star (2)">
                <line x1="55" y1="45" x2="55" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="55" width="22" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="42" stroke="#f1c40f" stroke-width="2"/> <line x1="86" y1="28" x2="104" y2="28" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Doji Star (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a Doji that gaps above Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An opening gap-up stalls as buyers fail to generate further upward progress, resulting in balance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A gap-up Doji shows that buying momentum has stalled; a bearish confirmation candle strengthens the reversal signal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-meeting-lines" data-searchable="bearish meeting lines (2) bearish-meeting-lines bearish reversal 2 bar bars structure: long green candle followed by a red candle opening sharply higher and closing at the same price as day 1's close. psychology: an opening surge is met with selling pressure, returning price back to parity with the prior close. outcome: the gap-up advance is rejected and both sessions close near the same level, suggesting a potential bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Meeting Lines (2)">
                <line x1="55" y1="45" x2="55" y2="100" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="50" width="22" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="20" width="22" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Meeting Lines (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a red candle opening sharply higher and closing at the same price as Day 1&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An opening surge is met with selling pressure, returning price back to parity with the prior close.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The gap-up advance is rejected and both sessions close near the same level, suggesting a potential bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-black-crows" data-searchable="three black crows (3) three-black-crows bearish reversal 3 bar bars structure: three consecutive long red candles after an advance, each opening within the prior body and closing near its low. psychology: sellers consistently dominate consecutive sessions, overcoming buying interest without significant pullbacks. outcome: three consecutive strong bearish sessions demonstrate sustained selling pressure and signal a potential trend reversal or acceleration lower.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Black Crows (3)">
                <line x1="40" y1="20" x2="40" y2="65" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="25" width="18" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="45" x2="75" y2="90" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="50" width="18" height="33" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="70" x2="110" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="75" width="18" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Black Crows (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive long red candles after an advance, each opening within the prior body and closing near its low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers consistently dominate consecutive sessions, overcoming buying interest without significant pullbacks.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Three consecutive strong bearish sessions demonstrate sustained selling pressure and signal a potential trend reversal or acceleration lower.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="evening-star" data-searchable="evening star (3) evening-star bearish reversal 3 bar bars structure: long green candle, an upward-gapping small body, and a long red candle closing well into day 1's body (generally below its midpoint). psychology: buying momentum pauses in hesitation before decisive selling takes control. outcome: buying momentum stalls, followed by decisive selling; a strong third candle supports a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Evening Star (3)">
                <line x1="40" y1="45" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="50" width="20" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="42" stroke="#e74c3c" stroke-width="2"/> <rect x="67" y="22" width="16" height="10" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="35" x2="110" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="100" y="45" width="20" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Evening Star (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, an upward-gapping small body, and a long red candle closing well into Day 1&#39;s body (generally below its midpoint).</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buying momentum pauses in hesitation before decisive selling takes control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Buying momentum stalls, followed by decisive selling; a strong third candle supports a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="evening-doji-star" data-searchable="evening doji star (3) evening-doji-star bearish reversal 3 bar bars structure: long green candle, an isolated doji gapping above day 1's body, and a long red candle closing deeply into day 1's body. psychology: buying momentum reaches equilibrium at the top before sellers take control with a sharp decline. outcome: a doji at the top signals pronounced indecision after an advance; a strong bearish third candle confirms the potential reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Evening Doji Star (3)">
                <line x1="40" y1="45" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="50" width="20" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="40" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="28" x2="83" y2="28" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="35" x2="110" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="100" y="45" width="20" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Evening Doji Star (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, an isolated Doji gapping above Day 1&#39;s body, and a long red candle closing deeply into Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buying momentum reaches equilibrium at the top before sellers take control with a sharp decline.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A Doji at the top signals pronounced indecision after an advance; a strong bearish third candle confirms the potential reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-abandoned-baby" data-searchable="bearish abandoned baby (3) bearish-abandoned-baby bearish reversal 3 bar bars structure: long green candle, an isolated doji gapping above both neighboring candles' shadows, and a red candle gapping down. psychology: an island formation develops where buying exhausts on a gap-up, followed by an immediate gap-down. outcome: an isolated doji after a gap-up signals exhaustion; a gap-down bearish candle confirms the potential reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Abandoned Baby (3)">
                <line x1="40" y1="55" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="60" width="20" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="38" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="26" x2="83" y2="26" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="55" x2="110" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="100" y="60" width="20" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Abandoned Baby (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, an isolated Doji gapping above both neighboring candles&#39; shadows, and a red candle gapping down.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An island formation develops where buying exhausts on a gap-up, followed by an immediate gap-down.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">An isolated Doji after a gap-up signals exhaustion; a gap-down bearish candle confirms the potential reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-tri-star" data-searchable="bearish tri-star (3) bearish-tri-star bearish reversal 3 bar bars structure: three consecutive dojis appearing after an advance, with the middle doji gapping above the other two. psychology: buying momentum stalls into extreme indecision across three consecutive sessions. outcome: three dojis indicate extreme indecision near the top; a downside break can signal a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Tri-Star (3)">
                <line x1="40" y1="60" x2="40" y2="90" stroke="#f1c40f" stroke-width="2"/> <line x1="32" y1="75" x2="48" y2="75" stroke="#f1c40f" stroke-width="3"/> <line x1="75" y1="25" x2="75" y2="55" stroke="#f1c40f" stroke-width="2"/> <line x1="67" y1="40" x2="83" y2="40" stroke="#f1c40f" stroke-width="3"/> <line x1="110" y1="60" x2="110" y2="90" stroke="#f1c40f" stroke-width="2"/> <line x1="102" y1="75" x2="118" y2="75" stroke="#f1c40f" stroke-width="3"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Tri-Star (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive Dojis appearing after an advance, with the middle Doji gapping above the other two.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buying momentum stalls into extreme indecision across three consecutive sessions.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Three Dojis indicate extreme indecision near the top; a downside break can signal a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-breakaway" data-searchable="bearish breakaway (5) bearish-breakaway bearish reversal 5 bar bars structure: long green candle, upside gap to a green candle, three smaller advancing bodies, followed by a large red candle closing within the initial gap. psychology: upward momentum gradually decelerates following the initial gap before sellers drive price back into the gap. outcome: the advance loses momentum after the gap-up sequence, and the final bearish candle signals a potential reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Breakaway (5)">
                <line x1="28" y1="70" x2="28" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="21" y="75" width="14" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="50" y1="45" x2="50" y2="65" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="48" width="12" height="12" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="72" y1="32" x2="72" y2="50" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="35" width="12" height="11" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="94" y1="22" x2="94" y2="40" stroke="#2ecc71" stroke-width="2"/> <rect x="88" y="25" width="12" height="11" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="122" y1="25" x2="122" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="114" y="30" width="16" height="50" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Breakaway (5)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, upside gap to a green candle, three smaller advancing bodies, followed by a large red candle closing within the initial gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Upward momentum gradually decelerates following the initial gap before sellers drive price back into the gap.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The advance loses momentum after the gap-up sequence, and the final bearish candle signals a potential reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-inside-down" data-searchable="three inside down (3) three-inside-down bearish reversal 3 bar bars structure: a bearish harami followed by a third red candle closing below day 2's low. psychology: buying stalls inside the prior candle, and follow-through selling confirms sellers are gaining control. outcome: the harami signals weakening buying pressure; the third candle confirms renewed bearish momentum.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Inside Down (3)">
                <line x1="40" y1="25" x2="40" y2="100" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="35" width="20" height="55" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="45" x2="75" y2="80" stroke="#e74c3c" stroke-width="2"/> <rect x="67" y="50" width="16" height="20" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="60" x2="110" y2="110" stroke="#e74c3c" stroke-width="2"/> <rect x="100" y="65" width="20" height="37" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Inside Down (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A Bearish Harami followed by a third red candle closing below Day 2&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buying stalls inside the prior candle, and follow-through selling confirms sellers are gaining control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The Harami signals weakening buying pressure; the third candle confirms renewed bearish momentum.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-outside-down" data-searchable="three outside down (3) three-outside-down bearish reversal 3 bar bars structure: a bearish engulfing pattern followed by a third red candle closing lower than day 2. psychology: sellers take control during the engulfing session, and subsequent selling provides immediate confirmation. outcome: the engulfing candle shifts control toward sellers, while the third candle confirms continuation of the reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Three Outside Down (3)">
                <line x1="40" y1="45" x2="40" y2="80" stroke="#2ecc71" stroke-width="2"/> <rect x="32" y="50" width="16" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="30" x2="75" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="64" y="38" width="22" height="48" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="75" x2="110" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="100" y="80" width="20" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Three Outside Down (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">A Bearish Engulfing pattern followed by a third red candle closing lower than Day 2.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers take control during the engulfing session, and subsequent selling provides immediate confirmation.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The engulfing candle shifts control toward sellers, while the third candle confirms continuation of the reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-kicking" data-searchable="bearish kicking (2) bearish-kicking bearish reversal 2 bar bars structure: green marubozu followed by a red marubozu that gaps down beneath day 1's open. psychology: an immediate downside gap below the prior open reflects an abrupt shift in market balance. outcome: a sharp downside gap between opposing marubozu candles signals an abrupt shift from bullish to bearish control.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Kicking (2)">
                <line x1="55" y1="15" x2="55" y2="65" stroke="#2ecc71" stroke-width="2"/> <rect x="43" y="15" width="24" height="50" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="75" x2="95" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="83" y="75" width="24" height="40" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Kicking (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green Marubozu followed by a red Marubozu that gaps down beneath Day 1&#39;s open.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An immediate downside gap below the prior open reflects an abrupt shift in market balance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A sharp downside gap between opposing Marubozu candles signals an abrupt shift from bullish to bearish control.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="ladder-top" data-searchable="ladder top (5) ladder-top bearish reversal 5 bar bars structure: three advancing green candles, a fourth candle with an upper shadow showing hesitation, followed by a decisive red candle opening lower and closing down. psychology: the advance begins to lose momentum on day 4, followed by a strong bearish move on day 5 that confirms seller control. outcome: the advance begins to lose momentum before a strong bearish fifth candle confirms a potential top.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Ladder Top (5)">
                <line x1="28" y1="80" x2="28" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="22" y="82" width="12" height="23" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="50" y1="62" x2="50" y2="88" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="65" width="12" height="19" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="72" y1="45" x2="72" y2="70" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="48" width="12" height="19" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="94" y1="22" x2="94" y2="58" stroke="#2ecc71" stroke-width="2"/> <rect x="88" y="35" width="12" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="122" y1="45" x2="122" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="114" y="52" width="16" height="43" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Ladder Top (5)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three advancing green candles, a fourth candle with an upper shadow showing hesitation, followed by a decisive red candle opening lower and closing down.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">The advance begins to lose momentum on Day 4, followed by a strong bearish move on Day 5 that confirms seller control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The advance begins to lose momentum before a strong bearish fifth candle confirms a potential top.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="matching-high" data-searchable="matching high (2) matching-high bearish reversal 2 bar bars structure: two consecutive green candles in an uptrend sharing approximately the same closing price, typically opening higher with little to no upper shadow. psychology: buyers fail to push the close above the previous session's close, establishing a resistance level. outcome: repeated failure to close above the same level creates resistance and warns of a potential bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Matching High (2)">
                <line x1="55" y1="35" x2="55" y2="90" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="40" width="22" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="35" x2="95" y2="80" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="40" width="22" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Matching High (2)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two consecutive green candles in an uptrend sharing approximately the same closing price, typically opening higher with little to no upper shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buyers fail to push the close above the previous session&#39;s close, establishing a resistance level.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Repeated failure to close above the same level creates resistance and warns of a potential bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="upside-gap-two-crows" data-searchable="upside gap two crows (3) upside-gap-two-crows bearish reversal 3 bar bars structure: long green candle, an upward-gapping small red body, followed by a red candle opening above day 2's open and closing below day 2's close while remaining above day 1's close. psychology: an upside gap fails to hold momentum; two consecutive down sessions show emerging supply above support. outcome: failure to sustain the gap warns of exhaustion; a subsequent break below the gap supports a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Upside Gap Two Crows (3)">
                <line x1="40" y1="40" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="45" width="20" height="50" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="42" stroke="#e74c3c" stroke-width="2"/> <rect x="67" y="20" width="16" height="20" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="15" x2="110" y2="44" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="18" width="18" height="24" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Upside Gap Two Crows (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, an upward-gapping small red body, followed by a red candle opening above Day 2&#39;s open and closing below Day 2&#39;s close while remaining above Day 1&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An upside gap fails to hold momentum; two consecutive down sessions show emerging supply above support.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Failure to sustain the gap warns of exhaustion; a subsequent break below the gap supports a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="identical-three-crows" data-searchable="identical three crows (3) identical-three-crows bearish reversal 3 bar bars structure: three consecutive red candles where each candle opens at or very close to the preceding candle's close and finishes near its low. psychology: persistent selling with little to no recovery between sessions reflects strong downward pressure. outcome: persistent selling with little recovery between sessions signals strong bearish momentum and possible continuation lower.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Identical Three Crows (3)">
                <line x1="40" y1="20" x2="40" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="25" width="18" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="50" x2="75" y2="90" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="55" width="18" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="80" x2="110" y2="120" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="85" width="18" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Identical Three Crows (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive red candles where each candle opens at or very close to the preceding candle&#39;s close and finishes near its low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Persistent selling with little to no recovery between sessions reflects strong downward pressure.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Persistent selling with little recovery between sessions signals strong bearish momentum and possible continuation lower.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="deliberation" data-searchable="deliberation (3) deliberation bearish reversal 3 bar bars structure: two strong green candles followed by a third small green candle that opens higher, displaying a noticeably smaller body. psychology: after two strong advancing sessions, buyers hesitate and upward progress contracts sharply. outcome: after two strong bullish candles, the smaller third candle shows slowing momentum and warns of a possible stall or reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Deliberation (3)">
                <line x1="40" y1="45" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="50" width="18" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="25" x2="75" y2="75" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="30" width="18" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="15" x2="110" y2="35" stroke="#2ecc71" stroke-width="2"/> <rect x="102" y="18" width="16" height="10" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Deliberation (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two strong green candles followed by a third small green candle that opens higher, displaying a noticeably smaller body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">After two strong advancing sessions, buyers hesitate and upward progress contracts sharply.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">After two strong bullish candles, the smaller third candle shows slowing momentum and warns of a possible stall or reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="advance-block" data-searchable="advance block (3) advance-block bearish reversal 3 bar bars structure: three consecutive green candles making new highs, with progressively smaller bodies and longer upper shadows. psychology: selling pressure intensifies near session highs, repeatedly pushing price off intraday peaks. outcome: repeated rejection at higher prices shows weakening buying momentum and warns of a potential bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Advance Block (3)">
                <line x1="40" y1="55" x2="40" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="60" width="18" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="35" x2="75" y2="90" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="45" width="18" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="18" x2="110" y2="70" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="40" width="18" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Advance Block (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive green candles making new highs, with progressively smaller bodies and longer upper shadows.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling pressure intensifies near session highs, repeatedly pushing price off intraday peaks.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Repeated rejection at higher prices shows weakening buying momentum and warns of a potential bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="two-crows" data-searchable="two crows (3) two-crows bearish reversal 3 bar bars structure: long green candle, an upward-gapping small red candle, followed by a second red candle opening within day 2's body and closing well into day 1's body. psychology: an initial upside gap is rejected, and consecutive down candles show supply overcoming demand. outcome: the gap-up fails to hold and two bearish candles signal weakening demand; downside follow-through supports a bearish reversal.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Two Crows (3)">
                <line x1="40" y1="40" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="30" y="45" width="20" height="50" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="45" stroke="#e74c3c" stroke-width="2"/> <rect x="67" y="20" width="16" height="18" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="25" x2="110" y2="70" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="28" width="18" height="32" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Two Crows (3)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, an upward-gapping small red candle, followed by a second red candle opening within Day 2&#39;s body and closing well into Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">An initial upside gap is rejected, and consecutive down candles show supply overcoming demand.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The gap-up fails to hold and two bearish candles signal weakening demand; downside follow-through supports a bearish reversal.</span></div>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </section>
    <section id="section-bullish-continuations" class="csp-category-section" data-group="bullish-continuations">
      <div class="csp-category-header">
        <h2>
          <span>Part III: Bullish Continuations</span>
          <span class="csp-badge csp-badge-cont-bull">8 Patterns</span>
        </h2>
        <p class="csp-subtitle">Appears during an uptrend; represents consolidation before upward resumption.</p>
      </div>
      <div class="csp-table-wrapper">
        <table class="csp-pattern-table">
          <thead>
            <tr>
              <th class="csp-col-visual">Visual Pattern</th>
              <th class="csp-col-desc">Pattern Name &amp; Market Dynamics</th>
            </tr>
          </thead>
          <tbody>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-separating-lines" data-searchable="bullish separating lines (2) bullish-separating-lines bullish continuation 2 bar bars structure: in an uptrend, a red candle is followed by a green candle that opens at approximately the same opening price and closes higher. psychology: a brief bearish counter-move is immediately repelled at the open as buyers reassert dominance. outcome: a brief bearish counter-move fails as buyers reclaim control; upside continuation is favored.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish Separating Lines (2)">
                <line x1="55" y1="35" x2="55" y2="95" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="45" width="22" height="40" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="20" width="22" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish Separating Lines (2)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In an uptrend, a red candle is followed by a green candle that opens at approximately the same opening price and closes higher.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A brief bearish counter-move is immediately repelled at the open as buyers reassert dominance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A brief bearish counter-move fails as buyers reclaim control; upside continuation is favored.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="rising-three-methods" data-searchable="rising three methods (5) rising-three-methods bullish continuation 5 bar bars structure: long green candle, followed by three small declining red candles contained within the first candle's range, and a final strong green candle closing above day 1's high. psychology: orderly consolidation is absorbed within the initial advance before buyers trigger a decisive breakout. outcome: consolidation within the trend is resolved to the upside; signals potential bullish continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Rising Three Methods (5)">
                <line x1="25" y1="25" x2="25" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="18" y="30" width="14" height="65" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="48" y1="35" x2="48" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="42" y="38" width="12" height="15" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="68" y1="45" x2="68" y2="70" stroke="#e74c3c" stroke-width="2"/> <rect x="62" y="48" width="12" height="15" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="88" y1="55" x2="88" y2="80" stroke="#e74c3c" stroke-width="2"/> <rect x="82" y="58" width="12" height="15" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="115" y1="15" x2="115" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="108" y="20" width="14" height="65" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Rising Three Methods (5)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, followed by three small declining red candles contained within the first candle&#39;s range, and a final strong green candle closing above Day 1&#39;s high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Orderly consolidation is absorbed within the initial advance before buyers trigger a decisive breakout.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Consolidation within the trend is resolved to the upside; signals potential bullish continuation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="upside-tasuki-gap" data-searchable="upside tasuki gap (3) upside-tasuki-gap bullish continuation 3 bar bars structure: green candle, followed by an upward-gapping green candle, and a red candle that closes partially into the gap without filling it completely. psychology: a mild pullback tests the gap zone as support, where buyers step in before the gap is closed. outcome: the pullback tests the gap as support; if the gap remains open and price resumes higher, the uptrend is likely to continue.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Upside Tasuki Gap (3)">
                <line x1="40" y1="55" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="60" width="18" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="18" x2="75" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="22" width="18" height="28" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="28" x2="110" y2="58" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="32" width="18" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Upside Tasuki Gap (3)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle, followed by an upward-gapping green candle, and a red candle that closes partially into the gap without filling it completely.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A mild pullback tests the gap zone as support, where buyers step in before the gap is closed.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The pullback tests the gap as support; if the gap remains open and price resumes higher, the uptrend is likely to continue.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-side-by-side-white-lines" data-searchable="bullish side-by-side white lines (3) bullish-side-by-side-white-lines bullish continuation 3 bar bars structure: green candle followed by an upside gap to two side-by-side green candles with approximately the same opening price and similar body sizes. psychology: price maintains elevated levels following a gap, with buyers defending the higher price plateau across two sessions. outcome: two similar bullish candles hold the higher gap level, suggesting the gap is being accepted and the uptrend may continue.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish Side-by-Side White Lines (3)">
                <line x1="40" y1="55" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="60" width="18" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="20" width="18" height="28" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="15" x2="110" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="20" width="18" height="28" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish Side-by-Side White Lines (3)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle followed by an upside gap to two side-by-side green candles with approximately the same opening price and similar body sizes.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Price maintains elevated levels following a gap, with buyers defending the higher price plateau across two sessions.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Two similar bullish candles hold the higher gap level, suggesting the gap is being accepted and the uptrend may continue.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-three-line-strike" data-searchable="bullish three line strike (4) bullish-three-line-strike bullish continuation 4 bar bars structure: three consecutive green candles with higher closes, followed by a long red candle opening at or above day 3's close and closing at or below day 1's open. psychology: a sharp single-session pullback rapidly unwinds three sessions of gains without establishing a new downtrend. outcome: despite the dramatic single-session drop, classical technical analysis treats this as a temporary resting phase favoring bullish continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish Three Line Strike (4)">
                <line x1="30" y1="65" x2="30" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="23" y="70" width="14" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="55" y1="45" x2="55" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="48" y="50" width="14" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="80" y1="25" x2="80" y2="65" stroke="#2ecc71" stroke-width="2"/> <rect x="73" y="30" width="14" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="115" y1="18" x2="115" y2="110" stroke="#e74c3c" stroke-width="2"/> <rect x="107" y="25" width="16" height="78" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish Three Line Strike (4)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">4 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive green candles with higher closes, followed by a long red candle opening at or above Day 3&#39;s close and closing at or below Day 1&#39;s open.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A sharp single-session pullback rapidly unwinds three sessions of gains without establishing a new downtrend.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Despite the dramatic single-session drop, classical technical analysis treats this as a temporary resting phase favoring bullish continuation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="upside-gap-three-methods" data-searchable="upside gap three methods (3) upside-gap-three-methods bullish continuation 3 bar bars structure: two advancing green candles separated by an upside gap, followed by a red candle that opens within the second body and closes to fill the gap. psychology: a brief corrective pullback fills the recent gap, allowing buyers an opportunity to re-enter at previous price levels. outcome: the gap is filled by a corrective bearish candle, but the prevailing uptrend remains intact; subsequent strength favors continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Upside Gap Three Methods (3)">
                <line x1="40" y1="55" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="60" width="18" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="15" x2="75" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="20" width="18" height="28" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="25" x2="110" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="30" width="18" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Upside Gap Three Methods (3)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two advancing green candles separated by an upside gap, followed by a red candle that opens within the second body and closes to fill the gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A brief corrective pullback fills the recent gap, allowing buyers an opportunity to re-enter at previous price levels.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The gap is filled by a corrective bearish candle, but the prevailing uptrend remains intact; subsequent strength favors continuation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-on-neck-line" data-searchable="bullish on neck line (2) bullish-on-neck-line bullish continuation 2 bar bars structure: in an uptrend, a red candle is followed by a green candle that opens lower and closes precisely at day 1's low, testing support. psychology: a pullback tests prior support without breaking down; buyers absorb the dip and defend the neckline. outcome: modern uptrend continuation variant; upside follow-through above the pattern high confirms trend resumption.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish On Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="85" x2="95" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="85" width="22" height="20" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish On Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In an uptrend, a red candle is followed by a green candle that opens lower and closes precisely at Day 1&#39;s low, testing support.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A pullback tests prior support without breaking down; buyers absorb the dip and defend the neckline.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Modern uptrend continuation variant; upside follow-through above the pattern high confirms trend resumption.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-in-neck-line" data-searchable="bullish in neck line (2) bullish-in-neck-line bullish continuation 2 bar bars structure: in an uptrend, a red candle is followed by a green candle that opens lower and closes slightly inside day 1's body. psychology: a pullback encounters buying interest that recovers slightly into the prior body, reflecting absorption of supply. outcome: modern uptrend continuation variant; confirmation above the pattern high supports bullish resumption.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish In Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="75" x2="95" y2="108" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="78" width="22" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish In Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In an uptrend, a red candle is followed by a green candle that opens lower and closes slightly inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A pullback encounters buying interest that recovers slightly into the prior body, reflecting absorption of supply.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Modern uptrend continuation variant; confirmation above the pattern high supports bullish resumption.</span></div>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </section>
    <section id="section-bearish-continuations" class="csp-category-section" data-group="bearish-continuations">
      <div class="csp-category-header">
        <h2>
          <span>Part IV: Bearish Continuations</span>
          <span class="csp-badge csp-badge-cont-bear">8 Patterns</span>
        </h2>
        <p class="csp-subtitle">Appears during a downtrend; represents temporary pause or pullback before downward resumption.</p>
      </div>
      <div class="csp-table-wrapper">
        <table class="csp-pattern-table">
          <thead>
            <tr>
              <th class="csp-col-visual">Visual Pattern</th>
              <th class="csp-col-desc">Pattern Name &amp; Market Dynamics</th>
            </tr>
          </thead>
          <tbody>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-separating-lines" data-searchable="bearish separating lines (2) bearish-separating-lines bearish continuation 2 bar bars structure: in a downtrend, a green candle is followed by a red candle that opens at approximately the same opening price and closes lower. psychology: a brief counter-trend bounce is immediately repelled at the open as sellers reassert dominance. outcome: a brief bullish counter-move fails as sellers regain control, favoring continuation of the downtrend.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Separating Lines (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="35" width="22" height="40" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="65" x2="95" y2="115" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="75" width="22" height="30" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Separating Lines (2)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In a downtrend, a green candle is followed by a red candle that opens at approximately the same opening price and closes lower.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A brief counter-trend bounce is immediately repelled at the open as sellers reassert dominance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A brief bullish counter-move fails as sellers regain control, favoring continuation of the downtrend.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="falling-three-methods" data-searchable="falling three methods (5) falling-three-methods bearish continuation 5 bar bars structure: long red candle, followed by three small advancing green candles contained within the first candle's range, and a final strong red candle closing below day 1's low. psychology: a minor counter-trend pause is contained entirely within the initial sell-off before sellers resume the decline. outcome: a brief counter-trend rally remains contained within the first candle's range before sellers resume the decline.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Falling Three Methods (5)">
                <line x1="25" y1="15" x2="25" y2="95" stroke="#e74c3c" stroke-width="2"/> <rect x="18" y="20" width="14" height="65" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="48" y1="55" x2="48" y2="80" stroke="#2ecc71" stroke-width="2"/> <rect x="42" y="58" width="12" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="68" y1="45" x2="68" y2="70" stroke="#2ecc71" stroke-width="2"/> <rect x="62" y="48" width="12" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="88" y1="35" x2="88" y2="60" stroke="#2ecc71" stroke-width="2"/> <rect x="82" y="38" width="12" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="115" y1="25" x2="115" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="108" y="30" width="14" height="65" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Falling Three Methods (5)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, followed by three small advancing green candles contained within the first candle&#39;s range, and a final strong red candle closing below Day 1&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A minor counter-trend pause is contained entirely within the initial sell-off before sellers resume the decline.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A brief counter-trend rally remains contained within the first candle&#39;s range before sellers resume the decline.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="downside-tasuki-gap" data-searchable="downside tasuki gap (3) downside-tasuki-gap bearish continuation 3 bar bars structure: red candle, followed by a downward-gapping red candle, and a green candle that closes partially into the gap without filling it completely. psychology: a corrective rebound pauses within the gap zone, where selling interest halts further upside. outcome: the corrective rally stalls within the gap, leaving the gap as resistance and favoring continuation lower.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Downside Tasuki Gap (3)">
                <line x1="40" y1="18" x2="40" y2="65" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="22" width="18" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="65" x2="75" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="70" width="18" height="28" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="60" x2="110" y2="85" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="63" width="18" height="17" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Downside Tasuki Gap (3)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle, followed by a downward-gapping red candle, and a green candle that closes partially into the gap without filling it completely.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A corrective rebound pauses within the gap zone, where selling interest halts further upside.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The corrective rally stalls within the gap, leaving the gap as resistance and favoring continuation lower.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-side-by-side-white-lines" data-searchable="bearish side-by-side white lines (3) bearish-side-by-side-white-lines bearish continuation 3 bar bars structure: red candle followed by a downside gap to two side-by-side green candles with approximately the same opening price and similar body sizes. psychology: two consecutive positive sessions fail to challenge or close the downside gap, showing weak rebound power. outcome: two similar bullish candles fail to reclaim the downside gap, suggesting the downtrend remains intact.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Side-by-Side White Lines (3)">
                <line x1="40" y1="15" x2="40" y2="65" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="20" width="18" height="38" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="65" x2="75" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="72" width="18" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="65" x2="110" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="72" width="18" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Side-by-Side White Lines (3)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle followed by a downside gap to two side-by-side green candles with approximately the same opening price and similar body sizes.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Two consecutive positive sessions fail to challenge or close the downside gap, showing weak rebound power.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Two similar bullish candles fail to reclaim the downside gap, suggesting the downtrend remains intact.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-three-line-strike" data-searchable="bearish three line strike (4) bearish-three-line-strike bearish continuation 4 bar bars structure: three consecutive red candles with lower closes, followed by a long green candle opening at or below day 3's close and closing at or above day 1's open. psychology: a sharp single-session rally temporarily recovers the losses of the prior three sessions without confirming a structural reversal. outcome: a sharp counter-trend rally fails to reverse the broader decline; renewed selling below the pattern supports bearish continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish Three Line Strike (4)">
                <line x1="30" y1="20" x2="30" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="23" y="25" width="14" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="55" y1="40" x2="55" y2="80" stroke="#e74c3c" stroke-width="2"/> <rect x="48" y="45" width="14" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="80" y1="60" x2="80" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="73" y="65" width="14" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="115" y1="15" x2="115" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="107" y="20" width="16" height="78" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish Three Line Strike (4)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">4 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive red candles with lower closes, followed by a long green candle opening at or below Day 3&#39;s close and closing at or above Day 1&#39;s open.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A sharp single-session rally temporarily recovers the losses of the prior three sessions without confirming a structural reversal.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">A sharp counter-trend rally fails to reverse the broader decline; renewed selling below the pattern supports bearish continuation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="downside-gap-three-methods" data-searchable="downside gap three methods (3) downside-gap-three-methods bearish continuation 3 bar bars structure: two falling red candles separated by a downside gap, followed by a green candle that opens within the second body and closes to fill the gap. psychology: a corrective rebound rallies into the recent gap area, testing resistance created by the prior sell-off. outcome: the bullish gap-fill represents a corrective rebound; if sellers regain control afterward, the downtrend resumes.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Downside Gap Three Methods (3)">
                <line x1="40" y1="15" x2="40" y2="65" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="20" width="18" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="65" x2="75" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="70" width="18" height="28" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="35" x2="110" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="40" width="18" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Downside Gap Three Methods (3)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two falling red candles separated by a downside gap, followed by a green candle that opens within the second body and closes to fill the gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A corrective rebound rallies into the recent gap area, testing resistance created by the prior sell-off.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">The bullish gap-fill represents a corrective rebound; if sellers regain control afterward, the downtrend resumes.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-on-neck-line" data-searchable="bearish on neck line (2) bearish-on-neck-line bearish continuation 2 bar bars structure: in a downtrend, a long red candle is followed by a smaller green candle that opens below day 1's low and closes near day 1's low. psychology: a minor rebound after a gap-down fails to make meaningful progress into the prior session's body, stalling at the neckline. outcome: failure of buyers to push price into the previous candle's body indicates persistent weakness, favoring downtrend continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish On Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="85" x2="95" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="85" width="22" height="20" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish On Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In a downtrend, a long red candle is followed by a smaller green candle that opens below Day 1&#39;s low and closes near Day 1&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A minor rebound after a gap-down fails to make meaningful progress into the prior session&#39;s body, stalling at the neckline.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Failure of buyers to push price into the previous candle&#39;s body indicates persistent weakness, favoring downtrend continuation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-in-neck-line" data-searchable="bearish in neck line (2) bearish-in-neck-line bearish continuation 2 bar bars structure: in a downtrend, a long red candle is followed by a smaller green candle that opens below day 1's low and closes slightly inside day 1's body. psychology: buyers attempt a rebound after a gap-down but fail to penetrate significantly into the prior session's range. outcome: weak penetration into the prior candle reflects insufficient demand to reverse the decline, favoring downtrend continuation.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish In Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="75" x2="95" y2="108" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="78" width="22" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish In Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In a downtrend, a long red candle is followed by a smaller green candle that opens below Day 1&#39;s low and closes slightly inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Buyers attempt a rebound after a gap-down but fail to penetrate significantly into the prior session&#39;s range.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Weak penetration into the prior candle reflects insufficient demand to reverse the decline, favoring downtrend continuation.</span></div>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </section>
</div>
