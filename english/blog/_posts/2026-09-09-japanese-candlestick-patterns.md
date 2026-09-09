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
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="long-white-body" data-searchable="long white body (1) long-white-body bullish reversal 1 bar bars structure: single tall green candle with a large body appearing after a decline. psychology: relentless buying pressure dominates from opening to close. outcome: bullish breakout toward overhead resistance.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Relentless buying pressure dominates from opening to close.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bullish breakout toward overhead resistance.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="hammer" data-searchable="hammer (1) hammer bullish reversal 1 bar bars structure: small body at the top of the range with a long lower shadow (&gt;= 2x body) and minimal upper shadow. psychology: severe intraday sell-off rejected violently by buyers. outcome: bullish reversal upon a higher close next session.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body at the top of the range with a long lower shadow (&gt;= 2x body) and minimal upper shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Severe intraday sell-off rejected violently by buyers.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bullish reversal upon a higher close next session.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="inverted-hammer" data-searchable="inverted hammer (1) inverted-hammer bullish reversal 1 bar bars structure: small body at the bottom of the range with a long upper shadow (&gt;= 2x body) and minimal lower shadow. psychology: bulls stage an intraday counter-attack, showing emerging demand. outcome: requires bullish confirmation candle next session.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body at the bottom of the range with a long upper shadow (&gt;= 2x body) and minimal lower shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bulls stage an intraday counter-attack, showing emerging demand.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Requires bullish confirmation candle next session.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-belt-hold" data-searchable="belt hold (1) bullish-belt-hold bullish reversal 1 bar bars structure: opens on the absolute low of the day (shaved bottom) and rallies steadily to close near the high. psychology: bulls seize control instantly at the open without conceding ground. outcome: immediate floor established; upside continuation expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Opens on the absolute low of the day (shaved bottom) and rallies steadily to close near the high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bulls seize control instantly at the open without conceding ground.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Immediate floor established; upside continuation expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-engulfing" data-searchable="engulfing pattern (2) bullish-engulfing bullish reversal 2 bar bars structure: small red body engulfed completely by a tall green real body. psychology: a lower open attracts massive demand, overwhelming supply. outcome: high reliability upward reversal; stop placed below day 2 low.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small red body engulfed completely by a tall green real body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">A lower open attracts massive demand, overwhelming supply.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">High reliability upward reversal; stop placed below Day 2 low.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-harami" data-searchable="harami (2) bullish-harami bullish reversal 2 bar bars structure: large red candle followed by a smaller green candle contained entirely inside day 1's body. psychology: downward momentum hits a sudden stop; sellers fail to expand range. outcome: trend deceleration; break above day 1 midpoint confirms reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Large red candle followed by a smaller green candle contained entirely inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downward momentum hits a sudden stop; sellers fail to expand range.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Trend deceleration; break above Day 1 midpoint confirms reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-harami-cross" data-searchable="harami cross (2) bullish-harami-cross bullish reversal 2 bar bars structure: long red candle followed by a doji inside the boundaries of day 1's body. psychology: market reaches total equilibrium and indecision following intense selling. outcome: potent turning point; upside expansion expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a Doji inside the boundaries of Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Market reaches total equilibrium and indecision following intense selling.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Potent turning point; upside expansion expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="piercing-line" data-searchable="piercing line (2) piercing-line bullish reversal 2 bar bars structure: long red candle followed by a green candle that opens below day 1 low and closes above the 50% midpoint of day 1. psychology: heavy gap-down rejected; buyers recover over half of day 1 losses. outcome: institutional accumulation; upward test of resistance.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a green candle that opens below Day 1 low and closes above the 50% midpoint of Day 1.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Heavy gap-down rejected; buyers recover over half of Day 1 losses.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Institutional accumulation; upward test of resistance.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-doji-star" data-searchable="doji star (2) bullish-doji-star bullish reversal 2 bar bars structure: long red body followed by a doji that gaps down beneath day 1's body. psychology: sellers force a lower opening but are completely unable to follow through. outcome: early alert of trend exhaustion; look for a strong green candle to confirm.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red body followed by a Doji that gaps down beneath Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers force a lower opening but are completely unable to follow through.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Early alert of trend exhaustion; look for a strong green candle to confirm.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-meeting-lines" data-searchable="meeting lines (2) bullish-meeting-lines bullish reversal 2 bar bars structure: long red candle followed by a green candle opening sharply lower but closing at the exact same price as day 1's close. psychology: bulls counter-attack the gap-down with equal force to close level with day 1. outcome: downward trend halted cold; upward reversal anticipated.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a green candle opening sharply lower but closing at the exact same price as Day 1&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bulls counter-attack the gap-down with equal force to close level with Day 1.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Downward trend halted cold; upward reversal anticipated.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-white-soldiers" data-searchable="three white soldiers (3) three-white-soldiers bullish reversal 3 bar bars structure: three consecutive long green candles, each opening within the prior body and closing higher near highs. psychology: steady, overpowering institutional buying demolishing resistance. outcome: sustained bull run initiation.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive long green candles, each opening within the prior body and closing higher near highs.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Steady, overpowering institutional buying demolishing resistance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sustained bull run initiation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="morning-star" data-searchable="morning star (3) morning-star bullish reversal 3 bar bars structure: long red candle, downward gapping small body, and a long green candle closing deeply into day 1. psychology: panic capitulation shifts into indecision, then aggressive buyer dominance. outcome: major cyclical bottom; high-probability upward trend.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, downward gapping small body, and a long green candle closing deeply into Day 1.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Panic capitulation shifts into indecision, then aggressive buyer dominance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Major cyclical bottom; high-probability upward trend.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="morning-doji-star" data-searchable="morning doji star (3) morning-doji-star bullish reversal 3 bar bars structure: identical to morning star, but the middle candle is an isolated doji. psychology: perfect supply-demand equilibrium at the bottom before bulls launch a rally. outcome: extremely potent trend reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Identical to Morning Star, but the middle candle is an isolated Doji.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Perfect supply-demand equilibrium at the bottom before bulls launch a rally.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Extremely potent trend reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-abandoned-baby" data-searchable="abandoned baby (3) bullish-abandoned-baby bullish reversal 3 bar bars structure: long red candle, an isolated doji gapping below both neighboring candles' shadows, and a green candle gapping up. psychology: true island reversal; sellers trapped completely at the extreme low. outcome: rapid upward repricing via aggressive short covering.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">True island reversal; sellers trapped completely at the extreme low.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Rapid upward repricing via aggressive short covering.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-tri-star" data-searchable="tri-star (3) bullish-tri-star bullish reversal 3 bar bars structure: three consecutive dojis with the middle doji gapping below the other two. psychology: rare sequence marking absolute exhaustion of selling drive. outcome: macro bottom signal; price pivots upward.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive Dojis with the middle Doji gapping below the other two.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Rare sequence marking absolute exhaustion of selling drive.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Macro bottom signal; price pivots upward.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-breakaway" data-searchable="breakaway (5) bullish-breakaway bullish reversal 5 bar bars structure: long red candle, gap-down red, 3 smaller declining bodies, followed by a large green candle closing within the original gap. psychology: downward momentum fizzles out; big green candle traps late shorts. outcome: bullish reversal into overhead resistance.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, gap-down red, 3 smaller declining bodies, followed by a large green candle closing within the original gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downward momentum fizzles out; big green candle traps late shorts.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bullish reversal into overhead resistance.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-inside-up" data-searchable="three inside up (3) three-inside-up bullish reversal 3 bar bars structure: bullish harami followed by a third green candle closing above day 2's high. psychology: follow-through confirmation validates that buyers have seized command. outcome: high-probability long trigger targeting recent swing highs.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Bullish Harami followed by a third green candle closing above Day 2&#39;s high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Follow-through confirmation validates that buyers have seized command.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">High-probability long trigger targeting recent swing highs.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-outside-up" data-searchable="three outside up (3) three-outside-up bullish reversal 3 bar bars structure: bullish engulfing pattern followed by a third candle closing higher. psychology: rapid confirmation attracts momentum buyers and triggers short stops. outcome: sustained trend reversal with upward acceleration.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Bullish Engulfing pattern followed by a third candle closing higher.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Rapid confirmation attracts momentum buyers and triggers short stops.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sustained trend reversal with upward acceleration.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-kicking" data-searchable="kicking (2) bullish-kicking bullish reversal 2 bar bars structure: red marubozu followed by a green marubozu that gaps up above day 1's open. psychology: sudden catalyst flips market sentiment 180 degrees overnight. outcome: powerful runaway bullish momentum; shallow pullbacks.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sudden catalyst flips market sentiment 180 degrees overnight.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Powerful runaway bullish momentum; shallow pullbacks.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="unique-three-rivers-bottom" data-searchable="unique three rivers bottom (3) unique-three-rivers-bottom bullish reversal 3 bar bars structure: long red candle; red body with long lower shadow making a new low; small green body trading above the extreme low. psychology: final desperate sell push rejected; selling pressure dissipates. outcome: basing structure leads into an upward reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle; red body with long lower shadow making a new low; small green body trading above the extreme low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Final desperate sell push rejected; selling pressure dissipates.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Basing structure leads into an upward reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="three-stars-in-the-south" data-searchable="three stars in the south (3) three-stars-in-the-south bullish reversal 3 bar bars structure: three declining red candles with progressively smaller bodies and higher lows; day 1 has a long lower wick. psychology: bears make decreasing downward progress each session. outcome: seller burnout; upward bounce expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three declining red candles with progressively smaller bodies and higher lows; Day 1 has a long lower wick.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bears make decreasing downward progress each session.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Seller burnout; upward bounce expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="concealing-swallow" data-searchable="concealing swallow (4) concealing-swallow bullish reversal 4 bar bars structure: four red candles: two falling marubozus, an inverted-hammer-like red candle gapping down, engulfed by a fourth red engulfing candle. psychology: climax selling frenzy completely exhausts all remaining supply. outcome: violent short-squeeze snapback rally.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Climax selling frenzy completely exhausts all remaining supply.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Violent short-squeeze snapback rally.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="bullish-stick-sandwich" data-searchable="stick sandwich (3) bullish-stick-sandwich bullish reversal 3 bar bars structure: two red candles with identical closing prices sandwiching a green candle. psychology: support level tested twice at the exact same tick and holds. outcome: micro double bottom; strong bounce expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two red candles with identical closing prices sandwiching a green candle.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Support level tested twice at the exact same tick and holds.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Micro double bottom; strong bounce expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="homing-pigeon" data-searchable="homing pigeon (2) homing-pigeon bullish reversal 2 bar bars structure: long red candle followed by a smaller red candle contained entirely inside day 1. psychology: sellers are unable to push beyond the prior body; selling momentum dries up. outcome: upward breakout above day 1 high triggers reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle followed by a smaller red candle contained entirely inside Day 1.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sellers are unable to push beyond the prior body; selling momentum dries up.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Upward breakout above Day 1 high triggers reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="ladder-bottom" data-searchable="ladder bottom (5) ladder-bottom bullish reversal 5 bar bars structure: three declining red bodies, a fourth body with a tall upper wick, followed by a strong green candle gapping up. psychology: downtrend decelerates; day 4 tests the upside and day 5 confirms bulls took over. outcome: structural reversal into sustained upward trend.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three declining red bodies, a fourth body with a tall upper wick, followed by a strong green candle gapping up.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Downtrend decelerates; Day 4 tests the upside and Day 5 confirms bulls took over.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Structural reversal into sustained upward trend.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-reversals" data-id="matching-low" data-searchable="matching low (2) matching-low bullish reversal 2 bar bars structure: two consecutive red candles sharing the exact same closing price. psychology: bears fail to close even one tick lower, signaling a solid floor. outcome: support confirmed; expect an immediate relief rally.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two consecutive red candles sharing the exact same closing price.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bears fail to close even one tick lower, signaling a solid floor.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Support confirmed; expect an immediate relief rally.</span></div>
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
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="long-black-body" data-searchable="long black body (1) long-black-body bearish reversal 1 bar bars structure: single tall red candle with a large body appearing after an advance. psychology: heavy selling pressure dominates the session from open to close. outcome: bearish breakdown toward lower support.">
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
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bearish breakdown toward lower support.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="hanging-man" data-searchable="hanging man (1) hanging-man bearish reversal 1 bar bars structure: small body at the top of an uptrend with a long lower shadow (&gt;= 2x body) and minimal upper shadow. psychology: intraday sell-off reveals emerging supply despite late-session recovery. outcome: bearish reversal confirmed upon a lower close next session.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small body at the top of an uptrend with a long lower shadow (&gt;= 2x body) and minimal upper shadow.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Intraday sell-off reveals emerging supply despite late-session recovery.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bearish reversal confirmed upon a lower close next session.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="shooting-star" data-searchable="shooting star (1) shooting-star bearish reversal 1 bar bars structure: small real body at the bottom of the range with a long upper shadow (&gt;= 2x body) following an uptrend. psychology: strong morning buying totally rejected by aggressive afternoon distribution. outcome: bearish reversal; short entries triggered beneath the star's low.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small real body at the bottom of the range with a long upper shadow (&gt;= 2x body) following an uptrend.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Strong morning buying totally rejected by aggressive afternoon distribution.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bearish reversal; short entries triggered beneath the star&#39;s low.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-belt-hold" data-searchable="bearish belt hold (1) bearish-belt-hold bearish reversal 1 bar bars structure: opens on the absolute high of the day (shaved head) and falls steadily to close near the low. psychology: bears seize control immediately at the open with zero upside conceded. outcome: immediate resistance ceiling established; downward continuation expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Opens on the absolute high of the day (shaved head) and falls steadily to close near the low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bears seize control immediately at the open with zero upside conceded.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Immediate resistance ceiling established; downward continuation expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-engulfing" data-searchable="bearish engulfing (2) bearish-engulfing bearish reversal 2 bar bars structure: small green body engulfed completely by a tall red real body. psychology: higher open attracts an overwhelming flood of supply, trapping breakout buyers. outcome: high reliability downward reversal; stop placed above day 2 high.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Small green body engulfed completely by a tall red real body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Higher open attracts an overwhelming flood of supply, trapping breakout buyers.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">High reliability downward reversal; stop placed above Day 2 high.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-harami" data-searchable="bearish harami (2) bearish-harami bearish reversal 2 bar bars structure: large green candle followed by a smaller red candle contained entirely inside day 1's body. psychology: uptrend hits a wall; buyers fail to expand range beyond prior levels. outcome: trend deceleration; break below day 1 midpoint confirms reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Large green candle followed by a smaller red candle contained entirely inside Day 1&#39;s body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Uptrend hits a wall; buyers fail to expand range beyond prior levels.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Trend deceleration; break below Day 1 midpoint confirms reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-harami-cross" data-searchable="bearish harami cross (2) bearish-harami-cross bearish reversal 2 bar bars structure: long green candle followed by a doji nested completely within day 1's body. psychology: complete standstill at peak prices; buyers and sellers lock in indecision. outcome: potent top turning point; downside break accelerates liquidation.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Complete standstill at peak prices; buyers and sellers lock in indecision.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Potent top turning point; downside break accelerates liquidation.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="dark-cloud-cover" data-searchable="dark cloud cover (2) dark-cloud-cover bearish reversal 2 bar bars structure: long green candle followed by a red candle opening above day 1 high and closing below day 1's midpoint. psychology: gap-up to new highs fails; sellers erase more than 50% of prior gains. outcome: high-probability bearish reversal; institutional distribution confirmed.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a red candle opening above Day 1 high and closing below Day 1&#39;s midpoint.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Gap-up to new highs fails; sellers erase more than 50% of prior gains.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">High-probability bearish reversal; institutional distribution confirmed.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-doji-star" data-searchable="bearish doji star (2) bearish-doji-star bearish reversal 2 bar bars structure: long green candle followed by a doji that gaps above day 1's body. psychology: bullish gap-up stalls completely; buyers fail to achieve any forward progress. outcome: early alert of top exhaustion; confirmation candle triggers short positions.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bullish gap-up stalls completely; buyers fail to achieve any forward progress.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Early alert of top exhaustion; confirmation candle triggers short positions.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-meeting-lines" data-searchable="bearish meeting lines (2) bearish-meeting-lines bearish reversal 2 bar bars structure: long green candle followed by a red candle opening sharply higher but closing at the exact same price as day 1's close. psychology: bullish opening surge is met with ferocious counter-selling returning price to parity. outcome: advance stopped cold; downward reversal expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by a red candle opening sharply higher but closing at the exact same price as Day 1&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bullish opening surge is met with ferocious counter-selling returning price to parity.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Advance stopped cold; downward reversal expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-black-crows" data-searchable="three black crows (3) three-black-crows bearish reversal 3 bar bars structure: three consecutive long red candles, each opening within the prior body and closing lower near lows. psychology: sustained institutional liquidation overwhelms all remaining buyers. outcome: powerful top reversal initiating an extended downward trend.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive long red candles, each opening within the prior body and closing lower near lows.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sustained institutional liquidation overwhelms all remaining buyers.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Powerful top reversal initiating an extended downward trend.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="evening-star" data-searchable="evening star (3) evening-star bearish reversal 3 bar bars structure: long green candle, upward gapping small body, and a long red candle closing deeply into day 1. psychology: bullish euphoria pauses in hesitation before sellers take firm control. outcome: major cyclical top reversal; high-probability short opportunity.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, upward gapping small body, and a long red candle closing deeply into Day 1.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bullish euphoria pauses in hesitation before sellers take firm control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Major cyclical top reversal; high-probability short opportunity.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="evening-doji-star" data-searchable="evening doji star (3) evening-doji-star bearish reversal 3 bar bars structure: identical to evening star, but the apex candle is an isolated doji. psychology: peak supply-demand equilibrium followed by swift long liquidation. outcome: very potent top reversal pattern; downward momentum expands rapidly.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Identical to Evening Star, but the apex candle is an isolated Doji.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Peak supply-demand equilibrium followed by swift long liquidation.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Very potent top reversal pattern; downward momentum expands rapidly.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-abandoned-baby" data-searchable="bearish abandoned baby (3) bearish-abandoned-baby bearish reversal 3 bar bars structure: long green candle, isolated doji gapping above both neighbors' shadows, and a red candle gapping down. psychology: island reversal; buyers trapped on an island at the extreme high. outcome: panic selling and rapid downside cascade.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, isolated Doji gapping above both neighbors&#39; shadows, and a red candle gapping down.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Island reversal; buyers trapped on an island at the extreme high.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Panic selling and rapid downside cascade.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-tri-star" data-searchable="bearish tri-star (3) bearish-tri-star bearish reversal 3 bar bars structure: three consecutive dojis with the middle doji gapping above the outer two. psychology: extreme exhaustion of buying power at resistance. outcome: macro top signal; price rotates downward.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive Dojis with the middle Doji gapping above the outer two.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Extreme exhaustion of buying power at resistance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Macro top signal; price rotates downward.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-breakaway" data-searchable="bearish breakaway (5) bearish-breakaway bearish reversal 5 bar bars structure: long green candle, gap-up green, 3 smaller advancing bodies, followed by a large red candle closing within the original gap. psychology: upward momentum decelerates until a large red candle traps late buyers. outcome: bearish reversal breaking into underlying support.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, gap-up green, 3 smaller advancing bodies, followed by a large red candle closing within the original gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Upward momentum decelerates until a large red candle traps late buyers.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bearish reversal breaking into underlying support.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-inside-down" data-searchable="three inside down (3) three-inside-down bearish reversal 3 bar bars structure: bearish harami followed by a third red candle closing below day 2's low. psychology: follow-through confirmation validates that sellers hold full market control. outcome: high-probability short entry targeting recent swing support.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Bearish Harami followed by a third red candle closing below Day 2&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Follow-through confirmation validates that sellers hold full market control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">High-probability short entry targeting recent swing support.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="three-outside-down" data-searchable="three outside down (3) three-outside-down bearish reversal 3 bar bars structure: bearish engulfing pattern followed by a third candle closing lower. psychology: immediate continuation prompts cascading stop-loss selling. outcome: sustained downward trend with acceleration.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Bearish Engulfing pattern followed by a third candle closing lower.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Immediate continuation prompts cascading stop-loss selling.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Sustained downward trend with acceleration.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="bearish-kicking" data-searchable="bearish kicking (2) bearish-kicking bearish reversal 2 bar bars structure: green marubozu followed by a red marubozu that gaps down beneath day 1's open. psychology: severe overnight catalyst flips market sentiment completely downward. outcome: violent runaway bearish trend; any bounce is short-lived.">
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
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Severe overnight catalyst flips market sentiment completely downward.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Violent runaway bearish trend; any bounce is short-lived.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="latter-top" data-searchable="latter top (5) latter-top bearish reversal 5 bar bars structure: three advancing green bodies, a fourth body with a tall upper wick, followed by a red candle opening lower. psychology: uptrend exhausts on day 4; day 5 confirms rejection of higher prices. outcome: structural top; bearish trend reversal initiated.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Latter Top (5)">
                <line x1="28" y1="80" x2="28" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="22" y="82" width="12" height="23" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="50" y1="62" x2="50" y2="88" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="65" width="12" height="19" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="72" y1="45" x2="72" y2="70" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="48" width="12" height="19" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="94" y1="22" x2="94" y2="58" stroke="#2ecc71" stroke-width="2"/> <rect x="88" y="35" width="12" height="15" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="122" y1="45" x2="122" y2="100" stroke="#e74c3c" stroke-width="2"/> <rect x="114" y="52" width="16" height="43" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Latter Top (5)</h3>
                <span class="csp-badge csp-badge-bear">Bearish Reversal</span>
                <span class="csp-badge csp-badge-bars">5 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three advancing green bodies, a fourth body with a tall upper wick, followed by a red candle opening lower.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Uptrend exhausts on Day 4; Day 5 confirms rejection of higher prices.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Structural top; bearish trend reversal initiated.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="matching-high" data-searchable="matching high (2) matching-high bearish reversal 2 bar bars structure: two consecutive green candles sharing the exact same closing price. psychology: resistance proves impenetrable; buyers fail to close even one tick higher. outcome: double-top ceiling confirmed; downward correction expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two consecutive green candles sharing the exact same closing price.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Resistance proves impenetrable; buyers fail to close even one tick higher.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Double-top ceiling confirmed; downward correction expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="upside-gap-two-crows" data-searchable="upside gap two crows (3) upside-gap-two-crows bearish reversal 3 bar bars structure: long green candle, upward-gapping small red body, and a second red body engulfing day 2 while remaining above day 1 close. psychology: gap-up fails to hold; two consecutive down sessions reveal latent distribution. outcome: bearish reversal breaking into the gap zone.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, upward-gapping small red body, and a second red body engulfing Day 2 while remaining above Day 1 close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Gap-up fails to hold; two consecutive down sessions reveal latent distribution.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bearish reversal breaking into the gap zone.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="identical-three-crows" data-searchable="identical three crows (3) identical-three-crows bearish reversal 3 bar bars structure: three consecutive red candles where each candle opens at or very near the preceding candle's close. psychology: relentless cascade of selling pressure with zero intraday rebounds. outcome: severe bearish momentum; ongoing trend down.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive red candles where each candle opens at or very near the preceding candle&#39;s close.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Relentless cascade of selling pressure with zero intraday rebounds.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Severe bearish momentum; ongoing trend down.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="deliberation" data-searchable="deliberation (3) deliberation bearish reversal 3 bar bars structure: two long green candles followed by a third small green body (or star) opening higher. psychology: rapid advance suddenly slows as buyers deliberate on valuation. outcome: trend exhaustion warning; imminent stall or sharp pullback.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two long green candles followed by a third small green body (or star) opening higher.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Rapid advance suddenly slows as buyers deliberate on valuation.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Trend exhaustion warning; imminent stall or sharp pullback.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="advance-block" data-searchable="advance block (3) advance-block bearish reversal 3 bar bars structure: three consecutive green candles making new highs, with diminishing real bodies and expanding upper shadows. psychology: stiffening overhead supply repeatedly pushes buyers off the session highs. outcome: rally stalls; high probability of trend reversal.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three consecutive green candles making new highs, with diminishing real bodies and expanding upper shadows.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Stiffening overhead supply repeatedly pushes buyers off the session highs.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Rally stalls; high probability of trend reversal.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-reversals" data-id="two-crows" data-searchable="two crows (3) two-crows bearish reversal 3 bar bars structure: long green candle followed by an upward-gapping small red candle, and a second red candle that opens in day 2 and closes inside day 1. psychology: gap-up fails to hold; bears penetrate deeply into day 1 gains. outcome: trend reversal confirmed; sell-off toward baseline support.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle followed by an upward-gapping small red candle, and a second red candle that opens in Day 2 and closes inside Day 1.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Gap-up fails to hold; bears penetrate deeply into Day 1 gains.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Trend reversal confirmed; sell-off toward baseline support.</span></div>
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
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-separating-lines" data-searchable="bullish separating lines (2) bullish-separating-lines bullish continuation 2 bar bars structure: red candle in an uptrend followed by a green candle that opens at the exact same price as day 1's open and rallies. psychology: bears mount a counter-attack, but bulls instantly reclaim the open and surge higher. outcome: powerful bullish continuation; uptrend resumes with conviction.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle in an uptrend followed by a green candle that opens at the exact same price as Day 1&#39;s open and rallies.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Bears mount a counter-attack, but bulls instantly reclaim the open and surge higher.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Powerful bullish continuation; uptrend resumes with conviction.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="rising-three-methods" data-searchable="rising three methods (5) rising-three-methods bullish continuation 5 bar bars structure: long green candle, 3 small declining red candles held within day 1's high-low range, followed by a strong green breakout candle. psychology: routine profit-taking is cleanly absorbed; buyers trigger the next expansion leg. outcome: classic continuation pattern; upward trend resumes immediately.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long green candle, 3 small declining red candles held within Day 1&#39;s high-low range, followed by a strong green breakout candle.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Routine profit-taking is cleanly absorbed; buyers trigger the next expansion leg.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Classic continuation pattern; upward trend resumes immediately.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="upside-tasuki-gap" data-searchable="upside tasuki gap (3) upside-tasuki-gap bullish continuation 3 bar bars structure: green candle, upward-gapping green candle, followed by a red candle closing into the gap without completely filling it. psychology: mild pullback tests the gap support where aggressive buyers step in. outcome: unfilled gap validates strong upward momentum; buy on gap retest.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Upside Tasuki Gap (3)">
                <line x1="40" y1="55" x2="40" y2="105" stroke="#2ecc71" stroke-width="2"/> <rect x="31" y="60" width="18" height="35" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="75" y1="18" x2="75" y2="55" stroke="#2ecc71" stroke-width="2"/> <rect x="66" y="22" width="18" height="28" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="110" y1="28" x2="110" y2="70" stroke="#e74c3c" stroke-width="2"/> <rect x="101" y="32" width="18" height="25" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Upside Tasuki Gap (3)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle, upward-gapping green candle, followed by a red candle closing into the gap without completely filling it.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Mild pullback tests the gap support where aggressive buyers step in.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Unfilled gap validates strong upward momentum; buy on gap retest.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-side-by-side-white-lines" data-searchable="bullish side-by-side white lines (3) bullish-side-by-side-white-lines bullish continuation 3 bar bars structure: green candle followed by two side-by-side green candles that gap up and share similar opens and body heights. psychology: demand remains robust at higher prices; sellers are completely absent. outcome: strong bullish continuation with upward targets.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle followed by two side-by-side green candles that gap up and share similar opens and body heights.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Demand remains robust at higher prices; sellers are completely absent.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Strong bullish continuation with upward targets.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-three-line-strike" data-searchable="bullish three line strike (4) bullish-three-line-strike bullish continuation 4 bar bars structure: three advancing green candles followed by a massive red candle that engulfs all three prior bodies. psychology: sudden liquidity flush shakes out leveraged longs right before institutional continuation. outcome: counter-intuitive continuation pattern; uptrend typically restarts rapidly.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three advancing green candles followed by a massive red candle that engulfs all three prior bodies.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Sudden liquidity flush shakes out leveraged longs right before institutional continuation.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Counter-intuitive continuation pattern; uptrend typically restarts rapidly.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="upside-gap-three-methods" data-searchable="upside gap three methods (3) upside-gap-three-methods bullish continuation 3 bar bars structure: two rising green candles with an upside gap, followed by a red candle that completely fills the gap. psychology: healthy gap-filling pullback clears order book before the next rally leg. outcome: gap filled; strong upward resumption from newly tested support.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two rising green candles with an upside gap, followed by a red candle that completely fills the gap.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Healthy gap-filling pullback clears order book before the next rally leg.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Gap filled; strong upward resumption from newly tested support.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-on-neck-line" data-searchable="bullish on neck line (2) bullish-on-neck-line bullish continuation 2 bar bars structure: red candle in an uptrend followed by a green candle opening lower and closing precisely at day 1's low. psychology: minor dip stabilizes cleanly at prior support; sellers fail to press lower. outcome: moderate bullish continuation once price crosses above day 1 high.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish On Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="75" x2="95" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="80" width="22" height="22" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish On Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle in an uptrend followed by a green candle opening lower and closing precisely at Day 1&#39;s low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Minor dip stabilizes cleanly at prior support; sellers fail to press lower.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Moderate bullish continuation once price crosses above Day 1 high.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bullish-continuations" data-id="bullish-in-neck-line" data-searchable="bullish in neck line (2) bullish-in-neck-line bullish continuation 2 bar bars structure: red candle followed by a green candle opening lower and closing slightly inside day 1's real body. psychology: selling pressure falters quickly; buyers absorb shallow pullback. outcome: bullish continuation confirmed when price clears the day 1 high.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bullish In Neck Line (2)">
                <line x1="55" y1="25" x2="55" y2="85" stroke="#e74c3c" stroke-width="2"/> <rect x="44" y="35" width="22" height="45" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="95" y1="65" x2="95" y2="110" stroke="#2ecc71" stroke-width="2"/> <rect x="84" y="70" width="22" height="30" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bullish In Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bull">Bullish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle followed by a green candle opening lower and closing slightly inside Day 1&#39;s real body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Selling pressure falters quickly; buyers absorb shallow pullback.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Bullish continuation confirmed when price clears the Day 1 high.</span></div>
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
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-separating-lines" data-searchable="bearish separating lines (2) bearish-separating-lines bearish continuation 2 bar bars structure: green candle in a downtrend followed by a red candle that opens at the exact same price as day 1's open and falls. psychology: short-lived bounce is instantly crushed; sellers assert undisputed authority. outcome: reliable bearish continuation; downtrend accelerates into new lows.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle in a downtrend followed by a red candle that opens at the exact same price as Day 1&#39;s open and falls.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Short-lived bounce is instantly crushed; sellers assert undisputed authority.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Reliable bearish continuation; downtrend accelerates into new lows.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="falling-three-methods" data-searchable="falling three methods (5) falling-three-methods bearish continuation 5 bar bars structure: long red candle, 3 small green candles held entirely within day 1's range, followed by a long red candle closing to a new low. psychology: feeble counter-trend rally runs out of steam; bears resume intense selling. outcome: textbook bearish continuation; breakdown below swing lows.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Long red candle, 3 small green candles held entirely within Day 1&#39;s range, followed by a long red candle closing to a new low.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Feeble counter-trend rally runs out of steam; bears resume intense selling.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Textbook bearish continuation; breakdown below swing lows.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="downside-tasuki-gap" data-searchable="downside tasuki gap (3) downside-tasuki-gap bearish continuation 3 bar bars structure: red candle, downward-gapping red candle, followed by a green candle closing into the gap without completely filling it. psychology: weak short-covering bounce stalls directly at gap resistance where fresh sellers reload. outcome: unfilled gap acts as rigid resistance; downward trend continues.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Downside Tasuki Gap (3)">
                <line x1="40" y1="18" x2="40" y2="65" stroke="#e74c3c" stroke-width="2"/> <rect x="31" y="22" width="18" height="35" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="75" y1="65" x2="75" y2="105" stroke="#e74c3c" stroke-width="2"/> <rect x="66" y="70" width="18" height="28" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/> <line x1="110" y1="50" x2="110" y2="90" stroke="#2ecc71" stroke-width="2"/> <rect x="101" y="55" width="18" height="25" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Downside Tasuki Gap (3)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">3 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle, downward-gapping red candle, followed by a green candle closing into the gap without completely filling it.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Weak short-covering bounce stalls directly at gap resistance where fresh sellers reload.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Unfilled gap acts as rigid resistance; downward trend continues.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-side-by-side-white-lines" data-searchable="bearish side-by-side white lines (3) bearish-side-by-side-white-lines bearish continuation 3 bar bars structure: red candle followed by two side-by-side green candles that gap down below day 1's low and share matching levels. psychology: two consecutive green days cannot penetrate above the gap; bears retain total dominance. outcome: highly reliable bearish continuation; downward resumption expected.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Red candle followed by two side-by-side green candles that gap down below Day 1&#39;s low and share matching levels.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Two consecutive green days cannot penetrate above the gap; bears retain total dominance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Highly reliable bearish continuation; downward resumption expected.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-three-line-strike" data-searchable="bearish three line strike (4) bearish-three-line-strike bearish continuation 4 bar bars structure: three declining red candles followed by a massive green candle that opens lower and engulfs all three prior bodies. psychology: violently squeezes short positions before the prevailing downward trend resumes. outcome: counter-intuitive continuation pattern; downtrend restarts quickly.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Three declining red candles followed by a massive green candle that opens lower and engulfs all three prior bodies.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Violently squeezes short positions before the prevailing downward trend resumes.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Counter-intuitive continuation pattern; downtrend restarts quickly.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="downside-gap-three-methods" data-searchable="downside gap three methods (3) downside-gap-three-methods bearish continuation 3 bar bars structure: two falling red candles separated by a downward gap, followed by a green candle that rallies to close the gap completely. psychology: gap fill creates optimal shorting liquidity at resistance for institutional bears. outcome: gap resistance rejected; steep downtrend resumes.">
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
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Two falling red candles separated by a downward gap, followed by a green candle that rallies to close the gap completely.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Gap fill creates optimal shorting liquidity at resistance for institutional bears.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Gap resistance rejected; steep downtrend resumes.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-on-neck-line" data-searchable="bearish on neck line (2) bearish-on-neck-line bearish continuation 2 bar bars structure: in a downtrend, a green candle is met by a red candle opening higher and closing precisely at day 1's high. psychology: intraday rally gets completely repulsed right at the neckline resistance. outcome: downward continuation; failure to break through resistance resumes sell-off.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish On Neck Line (2)">
                <line x1="55" y1="35" x2="55" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="40" width="22" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="55" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="20" width="22" height="20" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish On Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">In a downtrend, a green candle is met by a red candle opening higher and closing precisely at Day 1&#39;s high.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Intraday rally gets completely repulsed right at the neckline resistance.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Downward continuation; failure to break through resistance resumes sell-off.</span></div>
              </div>
            </td>
          </tr>
          <tr class="csp-pattern-row" data-group="bearish-continuations" data-id="bearish-in-neck-line" data-searchable="bearish in neck line (2) bearish-in-neck-line bearish continuation 2 bar bars structure: green candle followed by a red candle opening higher and penetrating barely into day 1's real body. psychology: weak penetration fails to spark any buying conviction; bears maintain control. outcome: downtrend continuation; break below day 1 low initiates next leg lower.">
            <td class="csp-cell-visual">
              <svg class="csp-pattern-svg" width="150" height="130" viewBox="0 0 150 130" aria-label="Bearish In Neck Line (2)">
                <line x1="55" y1="35" x2="55" y2="95" stroke="#2ecc71" stroke-width="2"/> <rect x="44" y="40" width="22" height="45" fill="#2ecc71" rx="1" stroke="#1b7a43" stroke-width="1"/> <line x1="95" y1="15" x2="95" y2="60" stroke="#e74c3c" stroke-width="2"/> <rect x="84" y="22" width="22" height="22" fill="#e74c3c" rx="1" stroke="#b30000" stroke-width="1"/>
              </svg>
            </td>
            <td class="csp-cell-desc">
              <div class="csp-pattern-header-row">
                <h3 class="csp-pattern-title">Bearish In Neck Line (2)</h3>
                <span class="csp-badge csp-badge-cont-bear">Bearish Continuation</span>
                <span class="csp-badge csp-badge-bars">2 Bars</span>
              </div>
              <div class="csp-pattern-body">
                <div><span class="csp-label">Structure:</span> <span class="csp-desc-text">Green candle followed by a red candle opening higher and penetrating barely into Day 1&#39;s real body.</span></div>
                <div><span class="csp-label">Psychology:</span> <span class="csp-desc-text">Weak penetration fails to spark any buying conviction; bears maintain control.</span></div>
                <div><span class="csp-label">Outcome:</span> <span class="csp-desc-text">Downtrend continuation; break below Day 1 low initiates next leg lower.</span></div>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </section>
</div>
