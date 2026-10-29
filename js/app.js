/**
 * WAHH Security Academy - Main Application Logic
 * Implements Curriculum Navigation, Interactive Quizzes, Security Labs,
 * Global Search, Notes Persistence, and Exam Certification.
 */

(function () {
  'use strict';

  // State Management
  const state = {
    currentModuleId: 'intro',
    activeTab: 'notes',
    categoryFilter: 'all',
    completed: JSON.parse(localStorage.getItem('wahh_completed') || '[]'),
    bookmarks: JSON.parse(localStorage.getItem('wahh_bookmarks') || '[]'),
    quizResults: JSON.parse(localStorage.getItem('wahh_quiz_results') || '{}'),
    notes: JSON.parse(localStorage.getItem('wahh_notes') || '{}'),
    theme: localStorage.getItem('wahh_theme') || 'cyan',
    examState: null
  };

  // Safe Lucide icon initializer
  function refreshIcons() {
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  // Markdown-to-HTML Light Parser
  function renderMarkdown(md) {
    if (!md) return '';
    let html = md.trim();

    // Tables
    html = html.replace(/\n\|(.+)\|\n\|[-:| ]+\|\n((?:\|.*\|\n?)*)/g, function (match, header, rows) {
      const ths = header.split('|').filter(c => c.trim()).map(c => `<th>${c.trim()}</th>`).join('');
      const trs = rows.trim().split('\n').map(row => {
        const tds = row.split('|').filter(c => c.trim()).map(c => `<td>${c.trim()}</td>`).join('');
        return `<tr>${tds}</tr>`;
      }).join('');
      return `<div style="overflow-x:auto;"><table><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table></div>`;
    });

    // Code blocks with copy button
    html = html.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, function (match, lang, code) {
      const cleanCode = code.trim();
      const escapedCode = cleanCode
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
      return `<pre><button class="copy-code-btn" onclick="copySnippet(this)">Copy</button><code class="language-${lang}">${escapedCode}</code></pre>`;
    });

    // Blockquotes
    html = html.replace(/^>\s*(.+)$/gm, '<blockquote>$1</blockquote>');

    // Headers
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

    // Bold & Italics
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

    // Inline Code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Unordered Lists
    html = html.replace(/^\* (.*$)/gim, '<li>$1</li>');
    html = html.replace(/((?:<li>.*<\/li>\s*)+)/g, '<ul>$1</ul>');

    // Paragraphs
    const lines = html.split('\n\n');
    html = lines.map(block => {
      block = block.trim();
      if (!block) return '';
      if (block.startsWith('<h') || block.startsWith('<pre') || block.startsWith('<ul') ||
          block.startsWith('<div') || block.startsWith('<table') || block.startsWith('<blockquote')) {
        return block;
      }
      return `<p>${block.replace(/\n/g, '<br>')}</p>`;
    }).join('\n');

    return html;
  }

  // Copy code utility exposed to window
  window.copySnippet = function (btn) {
    const pre = btn.closest('pre');
    const code = pre.querySelector('code');
    if (code) {
      navigator.clipboard.writeText(code.innerText).then(() => {
        const orig = btn.innerText;
        btn.innerText = 'Copied!';
        btn.style.background = 'var(--accent)';
        btn.style.color = '#000';
        setTimeout(() => {
          btn.innerText = orig;
          btn.style.background = '';
          btn.style.color = '';
        }, 1800);
      });
    }
  };

  // Get current module object
  function getCurrentModule() {
    return (window.WAHH_CURRICULUM || []).find(m => m.id === state.currentModuleId) || window.WAHH_CURRICULUM[0];
  }

  // Save state to localStorage
  function saveState() {
    localStorage.setItem('wahh_completed', JSON.stringify(state.completed));
    localStorage.setItem('wahh_bookmarks', JSON.stringify(state.bookmarks));
    localStorage.setItem('wahh_quiz_results', JSON.stringify(state.quizResults));
    localStorage.setItem('wahh_notes', JSON.stringify(state.notes));
    localStorage.setItem('wahh_theme', state.theme);
    updateProgressStats();
  }

  // Update header progress pill & statistics
  function updateProgressStats() {
    const modules = window.WAHH_CURRICULUM || [];
    const total = modules.length;
    const completedCount = state.completed.length;
    const pct = total > 0 ? Math.round((completedCount / total) * 100) : 0;

    const fillEl = document.getElementById('headerProgressFill');
    const textEl = document.getElementById('headerProgressText');
    const statComp = document.getElementById('statCompleted');
    const statQuiz = document.getElementById('statQuizzes');

    if (fillEl) fillEl.style.width = `${pct}%`;
    if (textEl) textEl.textContent = `${pct}%`;
    if (statComp) statComp.textContent = `${completedCount}/${total}`;

    // Passed quizzes count
    let passedCount = 0;
    Object.values(state.quizResults).forEach(res => {
      if (res && res.passed) passedCount++;
    });
    if (statQuiz) statQuiz.textContent = `${passedCount}/${total}`;
  }

  // Render Sidebar Modules List
  function renderSidebar() {
    const container = document.getElementById('modulesNavList');
    if (!container) return;

    const modules = window.WAHH_CURRICULUM || [];
    const filter = state.categoryFilter;

    const filtered = modules.filter(m => {
      if (filter === 'all') return true;
      return m.category === filter;
    });

    container.innerHTML = filtered.map(m => {
      const isActive = m.id === state.currentModuleId;
      const isCompleted = state.completed.includes(m.id);
      const isBookmarked = state.bookmarks.includes(m.id);
      const quizRes = state.quizResults[m.id];
      const hasScore = quizRes && typeof quizRes.score === 'number';

      const numDisplay = m.number === 0 ? 'Intro' : (m.number === 22 ? 'Index' : `Ch ${m.number}`);

      return `
        <div class="module-nav-item ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}" data-id="${m.id}">
          <div class="nav-item-left">
            <span class="module-num">${numDisplay}</span>
            <div class="module-title-wrap">
              <strong>${m.title.replace(/^Chapter \d+:\s*/, '')}</strong>
              <span>${m.category} • ${m.readingTime}</span>
            </div>
          </div>
          <div class="nav-item-badges">
            ${isBookmarked ? '<span title="Bookmarked" style="color:var(--accent-warning);font-size:0.75rem;">★</span>' : ''}
            ${hasScore ? `<span class="quiz-score-badge" title="Quiz score">${quizRes.score}/${quizRes.total}</span>` : ''}
            <span class="check-indicator" title="Completed">✓</span>
          </div>
        </div>
      `;
    }).join('');

    // Attach click events
    container.querySelectorAll('.module-nav-item').forEach(item => {
      item.addEventListener('click', () => {
        const id = item.getAttribute('data-id');
        navigateToModule(id);
      });
    });
  }

  // Navigate to a specific module
  function navigateToModule(id) {
    state.currentModuleId = id;
    renderSidebar();
    renderCurrentModule();
    saveState();

    // Close mobile drawer if open
    const sidebar = document.getElementById('appSidebar');
    if (sidebar) sidebar.classList.remove('open');
  }

  // Render Current Module (Banner, Notes, Quiz, Notes Tab)
  function renderCurrentModule() {
    const mod = getCurrentModule();
    if (!mod) return;

    // Banner
    const bannerCategory = document.getElementById('bannerCategory');
    const bannerReadTime = document.getElementById('bannerReadTime');
    const bannerTitle = document.getElementById('bannerTitle');
    const bannerSubtitle = document.getElementById('bannerSubtitle');
    const bannerOverview = document.getElementById('bannerOverview');
    const markCompleteBtn = document.getElementById('markCompleteBtn');
    const markCompleteText = document.getElementById('markCompleteBtnText');
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    const bookmarkBtnText = document.getElementById('bookmarkBtnText');

    if (bannerCategory) bannerCategory.textContent = mod.category;
    if (bannerReadTime) bannerReadTime.textContent = `⏱️ ${mod.readingTime} read`;
    if (bannerTitle) bannerTitle.textContent = mod.title;
    if (bannerSubtitle) bannerSubtitle.textContent = mod.subtitle;
    if (bannerOverview) bannerOverview.textContent = mod.overview;

    // Completion button state
    const isCompleted = state.completed.includes(mod.id);
    if (markCompleteBtn) {
      if (isCompleted) {
        markCompleteBtn.style.background = 'var(--bg-card)';
        markCompleteBtn.style.color = 'var(--accent)';
        markCompleteBtn.style.borderColor = 'var(--accent)';
        markCompleteText.textContent = 'Completed ✓';
      } else {
        markCompleteBtn.style.background = 'var(--accent)';
        markCompleteBtn.style.color = '#000';
        markCompleteBtn.style.borderColor = 'var(--accent)';
        markCompleteText.textContent = 'Mark Complete';
      }
    }

    // Bookmark button state
    const isBookmarked = state.bookmarks.includes(mod.id);
    if (bookmarkBtn) {
      if (isBookmarked) {
        bookmarkBtn.style.borderColor = 'var(--accent-warning)';
        bookmarkBtn.style.color = 'var(--accent-warning)';
        bookmarkBtnText.textContent = 'Bookmarked ★';
      } else {
        bookmarkBtn.style.borderColor = 'var(--border-subtle)';
        bookmarkBtn.style.color = 'var(--text-main)';
        bookmarkBtnText.textContent = 'Bookmark';
      }
    }

    // Render Tab 1: Study Notes
    renderStudyNotes(mod);

    // Render Tab 2: Quizzes
    renderQuiz(mod);

    // Render Tab 4: User Chapter Notes
    const notesArea = document.getElementById('userChapterNotes');
    if (notesArea) {
      notesArea.value = state.notes[mod.id] || '';
    }

    // Quiz Tab Badge Count
    const quizCountEl = document.getElementById('quizTabCount');
    if (quizCountEl) {
      quizCountEl.textContent = (mod.quiz || []).length;
    }

    refreshIcons();
  }

  // Render Notes Tab with Complete Topic & Subtopic Explorer
  function renderStudyNotes(mod) {
    const container = document.getElementById('notesContainer');
    if (!container) return;

    if (!mod.sections || mod.sections.length === 0) {
      container.innerHTML = `<div style="padding: 2rem; color: var(--text-dim);">No study notes available for this section.</div>`;
      return;
    }

    // Build Syllabus Explorer Header
    const topics = mod.topics || [];
    const totalSubtopics = topics.reduce((acc, t) => acc + (t.subtopics ? t.subtopics.length : 0), 0);

    let explorerHtml = `
      <div class="syllabus-explorer-card">
        <div class="syllabus-explorer-header">
          <div>
            <h3><i data-lucide="list-tree" style="width: 18px; color: var(--accent);"></i> Chapter Syllabus & Subtopic Roadmap</h3>
            <p>100% Comprehensive Coverage • <strong>${topics.length}</strong> Topics • <strong>${totalSubtopics}</strong> Subtopics from the Official Handbook</p>
          </div>
          <span class="coverage-badge">Full Syllabus Included</span>
        </div>
        <div class="syllabus-topics-grid">
          ${topics.map((top, tIdx) => `
            <div class="syllabus-topic-block">
              <h5>${tIdx + 1}. ${top.title}</h5>
              <div class="subtopics-pill-wrap">
                ${(top.subtopics || []).map(sub => `
                  <a href="#sub-${encodeURIComponent(sub.replace(/\\s+/g, '-').toLowerCase())}" class="subtopic-chip">
                    • ${sub}
                  </a>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    const sectionsHtml = mod.sections.map((sec, idx) => {
      let parsedContent = renderMarkdown(sec.content);

      // Add anchor IDs for each subtopic inside the content so chips scroll smoothly
      (sec.subtopics || []).forEach(sub => {
        const anchorId = `sub-${encodeURIComponent(sub.replace(/\\s+/g, '-').toLowerCase())}`;
        const targetHeader = `<h3>${sub}</h3>`;
        const replacementHeader = `<h3 id="${anchorId}" class="subtopic-target-header"><span class="subtopic-prefix-tag">SUBTOPIC</span> ${sub}</h3>`;
        parsedContent = parsedContent.replace(targetHeader, replacementHeader);
      });

      const takeaways = (sec.keyTakeaways || []).map(t => `<li>${t}</li>`).join('');

      return `
        <article class="section-block" id="${sec.id}">
          <h2>${idx + 1}. ${sec.title}</h2>
          <div class="section-subtopics-bar">
            <span>Covered Subtopics:</span>
            ${(sec.subtopics || []).map(s => `<span class="sec-sub-tag">${s}</span>`).join('')}
          </div>
          <div class="section-body">
            ${parsedContent}
          </div>
          ${takeaways ? `
            <div class="takeaways-box">
              <h4><i data-lucide="check-circle" style="width:16px;"></i> Key Takeaways & Defense Rules</h4>
              <ul>${takeaways}</ul>
            </div>
          ` : ''}
        </article>
      `;
    }).join('');

    container.innerHTML = explorerHtml + sectionsHtml;
  }

  // Render Quiz Tab
  function renderQuiz(mod) {
    const container = document.getElementById('quizCardsList');
    const chapterTitleEl = document.getElementById('quizChapterTitle');
    if (!container) return;

    if (chapterTitleEl) {
      chapterTitleEl.textContent = `${mod.title} - Assessment Quiz`;
    }

    const quizzes = mod.quiz || [];
    if (quizzes.length === 0) {
      container.innerHTML = `<div style="padding: 2rem; color: var(--text-dim);">No quiz available for this module.</div>`;
      return;
    }

    const saved = state.quizResults[mod.id] || { answers: {} };

    container.innerHTML = quizzes.map((q, qIndex) => {
      const chosenIdx = saved.answers ? saved.answers[q.id] : undefined;
      const isAnswered = typeof chosenIdx === 'number';

      return `
        <div class="quiz-card" data-qid="${q.id}" data-correct="${q.correctIndex}">
          <div class="quiz-card-header">
            <span class="q-number">QUESTION ${qIndex + 1} OF ${quizzes.length}</span>
            <span class="q-diff">${q.difficulty || 'Intermediate'}</span>
          </div>
          <div class="q-question-text">${q.question}</div>
          <div class="q-options-list">
            ${q.options.map((opt, optIndex) => {
              let optClass = '';
              if (isAnswered) {
                if (optIndex === q.correctIndex) {
                  optClass = 'correct';
                } else if (optIndex === chosenIdx) {
                  optClass = 'incorrect';
                }
              }
              const letters = ['A', 'B', 'C', 'D'];
              return `
                <div class="q-option ${optClass}" data-opt="${optIndex}">
                  <span class="option-marker">${letters[optIndex]}</span>
                  <span>${opt}</span>
                </div>
              `;
            }).join('')}
          </div>
          <div class="quiz-explanation-box ${isAnswered ? 'visible' : ''}">
            <h5>Explanation</h5>
            <p>${q.explanation}</p>
          </div>
        </div>
      `;
    }).join('');

    // Attach option click handlers
    container.querySelectorAll('.quiz-card').forEach(card => {
      const qid = card.getAttribute('data-qid');
      const correctIdx = parseInt(card.getAttribute('data-correct'), 10);
      const explanationBox = card.querySelector('.quiz-explanation-box');

      card.querySelectorAll('.q-option').forEach(optEl => {
        optEl.addEventListener('click', () => {
          const selectedIdx = parseInt(optEl.getAttribute('data-opt'), 10);

          // Update result in state
          if (!state.quizResults[mod.id]) {
            state.quizResults[mod.id] = { answers: {}, score: 0, total: quizzes.length, passed: false };
          }
          state.quizResults[mod.id].answers[qid] = selectedIdx;

          // Recompute overall chapter quiz score
          let score = 0;
          quizzes.forEach(item => {
            if (state.quizResults[mod.id].answers[item.id] === item.correctIndex) {
              score++;
            }
          });
          state.quizResults[mod.id].score = score;
          state.quizResults[mod.id].total = quizzes.length;
          state.quizResults[mod.id].passed = (score / quizzes.length) >= 0.65;

          // Update UI styles
          card.querySelectorAll('.q-option').forEach((el, idx) => {
            el.classList.remove('selected', 'correct', 'incorrect');
            if (idx === correctIdx) {
              el.classList.add('correct');
            } else if (idx === selectedIdx) {
              el.classList.add('incorrect');
            }
          });

          if (explanationBox) {
            explanationBox.classList.add('visible');
          }

          saveState();
          renderSidebar();
        });
      });
    });
  }

  // Setup Security Playground Labs
  function setupPlaygroundLabs() {
    // Lab 1: SQL Injection
    const sqliInput = document.getElementById('sqliInput');
    const sqliScenario = document.getElementById('sqliScenarioSelect');
    const sqliOutput = document.getElementById('sqliOutputQuery');
    const sqliPill = document.getElementById('sqliStatusPill');
    const sqliFeedback = document.getElementById('sqliResultFeedback');

    function updateSqli() {
      if (!sqliInput || !sqliOutput) return;
      const val = sqliInput.value;
      const scenario = sqliScenario.value;

      if (scenario === 'login') {
        const query = `SELECT * FROM users WHERE username = '${val}' AND password = 'secretPassword123';`;
        sqliOutput.textContent = query;

        if (val.includes("'") && (val.toLowerCase().includes('or') || val.includes('--') || val.includes('#'))) {
          sqliPill.className = 'lab-status-pill pill-danger';
          sqliPill.textContent = 'CRITICAL: SQL Logic Altered';
          sqliFeedback.innerHTML = `⚠️ <strong>Vulnerability Exploded!</strong> The quotes or comments bypassed password verification. Query conditions evaluate to true, logging in as administrative user!`;
        } else {
          sqliPill.className = 'lab-status-pill pill-success';
          sqliPill.textContent = 'Normal Literal Evaluation';
          sqliFeedback.textContent = `Input is evaluated safely inside string literal. No auth bypass detected.`;
        }
      } else {
        const query = `SELECT title, description FROM products WHERE id = '${val}';`;
        sqliOutput.textContent = query;

        if (val.toLowerCase().includes('union') && val.toLowerCase().includes('select')) {
          sqliPill.className = 'lab-status-pill pill-danger';
          sqliPill.textContent = 'CRITICAL: UNION Injection Active';
          sqliFeedback.innerHTML = `⚠️ <strong>Data Exfiltration!</strong> UNION query appended. Data from injected tables (e.g. users, credentials) will be included in the product response.`;
        } else {
          sqliPill.className = 'lab-status-pill pill-success';
          sqliPill.textContent = 'Normal Single Query';
          sqliFeedback.textContent = `Standard product lookup without UNION branching.`;
        }
      }
    }

    if (sqliInput) sqliInput.addEventListener('input', updateSqli);
    if (sqliScenario) sqliScenario.addEventListener('change', updateSqli);
    updateSqli();

    // Lab 2: XSS Reflector
    const xssInput = document.getElementById('xssInput');
    const xssMode = document.getElementById('xssModeSelect');
    const xssHtml = document.getElementById('xssRenderedHtml');
    const xssExec = document.getElementById('xssExecutionResult');
    const xssPill = document.getElementById('xssStatusPill');

    function updateXss() {
      if (!xssInput || !xssHtml) return;
      const raw = xssInput.value;
      const mode = xssMode.value;

      let rendered = raw;
      if (mode === 'naive') {
        // Naive single strip of <script>
        rendered = raw.replace(/<script>/gi, '').replace(/<\/script>/gi, '');
      } else if (mode === 'secure') {
        // Full HTML entity encoding
        rendered = raw
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&#39;');
      }

      xssHtml.textContent = rendered;

      // Check if dangerous HTML would trigger script execution
      const isDangerous = (mode !== 'secure') && (
        /<script[\s>]/i.test(rendered) ||
        /onerror\s*=/i.test(rendered) ||
        /onload\s*=/i.test(rendered) ||
        /javascript:/i.test(rendered)
      );

      if (isDangerous) {
        xssPill.className = 'lab-status-pill pill-danger';
        xssPill.textContent = 'XSS Payload Executable';
        xssExec.style.color = '#ef4444';
        xssExec.innerHTML = `💥 <strong>Malicious Script Fires!</strong> Client browser executes arbitrary JavaScript in the victim's session context!`;
      } else if (mode === 'secure') {
        xssPill.className = 'lab-status-pill pill-success';
        xssPill.textContent = 'Securely Sanitized / Encoded';
        xssExec.style.color = '#10b981';
        xssExec.textContent = `🛡️ Characters are rendered safely as inert text. No DOM script execution possible.`;
      } else {
        xssPill.className = 'lab-status-pill pill-success';
        xssPill.textContent = 'Benign Output';
        xssExec.style.color = '#94a3b8';
        xssExec.textContent = `No active script tags or dangerous event triggers detected in current input.`;
      }
    }

    if (xssInput) xssInput.addEventListener('input', updateXss);
    if (xssMode) xssMode.addEventListener('change', updateXss);
    updateXss();

    // Lab 3: Path Traversal
    const pathInput = document.getElementById('pathInput');
    const pathResolved = document.getElementById('pathResolved');
    const pathCanonical = document.getElementById('pathCanonical');
    const pathPill = document.getElementById('pathStatusPill');
    const pathResult = document.getElementById('pathResultText');

    function updatePath() {
      if (!pathInput || !pathResolved) return;
      const raw = pathInput.value;
      const basePath = '/var/www/html/uploads/';
      const rawCombined = basePath + raw;

      // Simulate path normalization
      const parts = rawCombined.split('/');
      const stack = [];
      for (const p of parts) {
        if (!p || p === '.') continue;
        if (p === '..') {
          if (stack.length > 0) stack.pop();
        } else {
          stack.push(p);
        }
      }
      const canonical = '/' + stack.join('/');

      pathResolved.textContent = rawCombined;
      pathCanonical.textContent = canonical;

      if (!canonical.startsWith('/var/www/html/uploads')) {
        pathPill.className = 'lab-status-pill pill-danger';
        pathPill.textContent = 'Directory Traversal Detected!';
        pathResult.style.color = '#ef4444';
        pathResult.innerHTML = `🚨 <strong>Root Directory Escaped!</strong> Path points outside intended upload directory to: <code>${canonical}</code>. System files are exposed!`;
      } else {
        pathPill.className = 'lab-status-pill pill-success';
        pathPill.textContent = 'Contained Inside Sandboxed Directory';
        pathResult.style.color = '#10b981';
        pathResult.textContent = `File safely confined to /var/www/html/uploads/.`;
      }
    }

    if (pathInput) pathInput.addEventListener('input', updatePath);
    updatePath();
  }

  // Setup Global Search Modal
  function setupSearch() {
    const modal = document.getElementById('searchModal');
    const triggerBtn = document.getElementById('searchTriggerBtn');
    const closeBtn = document.getElementById('closeSearchBtn');
    const input = document.getElementById('searchInput');
    const resultsContainer = document.getElementById('searchResults');

    function openSearch() {
      if (!modal) return;
      modal.classList.add('open');
      if (input) {
        input.value = '';
        input.focus();
      }
      performSearch('');
    }

    function closeSearch() {
      if (modal) modal.classList.remove('open');
    }

    if (triggerBtn) triggerBtn.addEventListener('click', openSearch);
    if (closeBtn) closeBtn.addEventListener('click', closeSearch);

    // Close on overlay click
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeSearch();
      });
    }

    // Keyboard shortcut (Ctrl+K or /)
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openSearch();
      } else if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSearch();
      } else if (e.key === 'Escape') {
        closeSearch();
        const backupModal = document.getElementById('backupModal');
        if (backupModal) backupModal.classList.remove('open');
      }
    });

    function performSearch(query) {
      const q = query.trim().toLowerCase();
      if (!resultsContainer) return;

      if (q.length < 2) {
        resultsContainer.innerHTML = `
          <div style="padding: 2rem; text-align: center; color: var(--text-dim);">
            Type at least 2 characters to search across all 21 chapters, code blocks, and quiz questions.
          </div>
        `;
        return;
      }

      const modules = window.WAHH_CURRICULUM || [];
      const hits = [];

      modules.forEach(m => {
        // Check title, subtitle, overview
        if (m.title.toLowerCase().includes(q) || m.subtitle.toLowerCase().includes(q) || m.overview.toLowerCase().includes(q)) {
          hits.push({
            moduleId: m.id,
            title: m.title,
            snippet: m.subtitle,
            type: 'Chapter'
          });
        }

        // Check topics and subtopics explicitly
        (m.topics || []).forEach(top => {
          if (top.title.toLowerCase().includes(q)) {
            hits.push({
              moduleId: m.id,
              title: `${m.title} » Topic: ${top.title}`,
              snippet: `Topic covering: ${(top.subtopics || []).slice(0, 3).join(', ')}...`,
              type: 'Topic'
            });
          }
          (top.subtopics || []).forEach(sub => {
            if (sub.toLowerCase().includes(q)) {
              hits.push({
                moduleId: m.id,
                title: `${m.title} » Subtopic: ${sub}`,
                snippet: `Syllabus subtopic in ${top.title}`,
                type: 'Subtopic'
              });
            }
          });
        });

        // Check sections
        (m.sections || []).forEach(sec => {
          if (sec.title.toLowerCase().includes(q) || sec.content.toLowerCase().includes(q)) {
            // Extract snippet
            const idx = sec.content.toLowerCase().indexOf(q);
            const start = Math.max(0, idx - 40);
            const end = Math.min(sec.content.length, idx + 80);
            const snippet = '...' + sec.content.substring(start, end).replace(/\n/g, ' ') + '...';
            hits.push({
              moduleId: m.id,
              title: `${m.title} » ${sec.title}`,
              snippet: snippet,
              type: 'Section'
            });
          }
        });

        // Check quizzes
        (m.quiz || []).forEach(quiz => {
          if (quiz.question.toLowerCase().includes(q) || quiz.explanation.toLowerCase().includes(q)) {
            hits.push({
              moduleId: m.id,
              title: `${m.title} » Quiz Question`,
              snippet: quiz.question,
              type: 'Quiz'
            });
          }
        });
      });

      if (hits.length === 0) {
        resultsContainer.innerHTML = `
          <div style="padding: 2rem; text-align: center; color: var(--text-dim);">
            No matching results found for "${query}".
          </div>
        `;
        return;
      }

      resultsContainer.innerHTML = hits.slice(0, 15).map(hit => `
        <div class="search-result-item" data-id="${hit.moduleId}">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.2rem;">
            <h5>${hit.title}</h5>
            <span style="font-size: 0.7rem; color: var(--accent); border: 1px solid var(--accent); padding: 0.1rem 0.4rem; border-radius: 4px;">${hit.type}</span>
          </div>
          <p>${hit.snippet}</p>
        </div>
      `).join('');

      resultsContainer.querySelectorAll('.search-result-item').forEach(item => {
        item.addEventListener('click', () => {
          const modId = item.getAttribute('data-id');
          closeSearch();
          navigateToModule(modId);
        });
      });
    }

    if (input) {
      input.addEventListener('input', () => {
        performSearch(input.value);
      });
    }
  }

  // Grand Certification Exam Implementation
  function setupGrandExam() {
    const startView = document.getElementById('examStartView');
    const activeView = document.getElementById('examActiveView');
    const resultView = document.getElementById('examResultView');
    const startBtn = document.getElementById('startExamBtn');
    const submitBtn = document.getElementById('submitExamBtn');
    const retakeBtn = document.getElementById('retakeExamBtn');
    const questionsContainer = document.getElementById('examQuestionsList');
    const progressLabel = document.getElementById('examProgressLabel');

    if (!startBtn) return;

    startBtn.addEventListener('click', () => {
      // Gather all quizzes from all modules
      const allQuizzes = [];
      (window.WAHH_CURRICULUM || []).forEach(m => {
        (m.quiz || []).forEach(q => {
          allQuizzes.push({ ...q, chapter: m.title });
        });
      });

      // Shuffle and pick 25 questions
      const shuffled = [...allQuizzes].sort(() => 0.5 - Math.random());
      const selected = shuffled.slice(0, 25);

      state.examState = {
        questions: selected,
        answers: {},
        startTime: Date.now()
      };

      startView.style.display = 'none';
      resultView.style.display = 'none';
      activeView.style.display = 'block';

      renderExamQuestions();
    });

    function renderExamQuestions() {
      if (!state.examState || !questionsContainer) return;
      const qs = state.examState.questions;

      questionsContainer.innerHTML = qs.map((q, idx) => {
        const selected = state.examState.answers[idx];
        const letters = ['A', 'B', 'C', 'D'];
        return `
          <div class="quiz-card" data-eidx="${idx}">
            <div class="quiz-card-header">
              <span class="q-number">QUESTION ${idx + 1} OF ${qs.length}</span>
              <span class="q-diff">${q.chapter}</span>
            </div>
            <div class="q-question-text">${q.question}</div>
            <div class="q-options-list">
              ${q.options.map((opt, oIdx) => `
                <div class="q-option ${selected === oIdx ? 'selected' : ''}" data-oidx="${oIdx}">
                  <span class="option-marker">${letters[oIdx]}</span>
                  <span>${opt}</span>
                </div>
              `).join('')}
            </div>
          </div>
        `;
      }).join('');

      questionsContainer.querySelectorAll('.quiz-card').forEach(card => {
        const eidx = parseInt(card.getAttribute('data-eidx'), 10);
        card.querySelectorAll('.q-option').forEach(opt => {
          opt.addEventListener('click', () => {
            const oidx = parseInt(opt.getAttribute('data-oidx'), 10);
            state.examState.answers[eidx] = oidx;

            card.querySelectorAll('.q-option').forEach((el, idx) => {
              if (idx === oidx) el.classList.add('selected');
              else el.classList.remove('selected');
            });

            // Update answered progress
            const answeredCount = Object.keys(state.examState.answers).length;
            if (progressLabel) {
              progressLabel.textContent = `Answered ${answeredCount} of ${qs.length} questions`;
            }
          });
        });
      });
    }

    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        if (!state.examState) return;
        const qs = state.examState.questions;
        let correctCount = 0;

        qs.forEach((q, idx) => {
          if (state.examState.answers[idx] === q.correctIndex) {
            correctCount++;
          }
        });

        const total = qs.length;
        const pct = Math.round((correctCount / total) * 100);
        const passed = pct >= 80;

        activeView.style.display = 'none';
        resultView.style.display = 'block';

        const scoreDisplay = document.getElementById('examScoreDisplay');
        const resTitle = document.getElementById('examResultTitle');
        const resSub = document.getElementById('examResultSubtitle');

        if (scoreDisplay) {
          scoreDisplay.textContent = `${pct}%`;
          scoreDisplay.style.color = passed ? 'var(--accent)' : 'var(--accent-danger)';
        }

        if (resTitle) {
          resTitle.textContent = passed ? '🎉 Congratulations! You Passed!' : 'Mastery Exam Failed';
        }

        if (resSub) {
          resSub.innerHTML = passed
            ? `Outstanding achievement! You scored <strong>${correctCount}/${total}</strong>. You have demonstrated rigorous mastery across the 21 chapters of The Web Application Hacker's Handbook.`
            : `You scored <strong>${correctCount}/${total}</strong>. The passing threshold is 80% (20/25). Review your study notes and retake the exam.`;
        }
      });
    }

    if (retakeBtn) {
      retakeBtn.addEventListener('click', () => {
        resultView.style.display = 'none';
        startView.style.display = 'block';
      });
    }
  }

  // Setup Backup & Restore Modal
  function setupBackupModal() {
    const modal = document.getElementById('backupModal');
    const triggerBtn = document.getElementById('backupDataBtn');
    const closeBtn = document.getElementById('closeBackupModalBtn');
    const exportBtn = document.getElementById('exportDataBtn');
    const importInput = document.getElementById('importFileInput');
    const resetAllBtn = document.getElementById('resetAllProgressBtn');

    if (triggerBtn) {
      triggerBtn.addEventListener('click', () => {
        if (modal) modal.classList.add('open');
      });
    }

    if (closeBtn && modal) {
      closeBtn.addEventListener('click', () => {
        modal.classList.remove('open');
      });
    }

    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        const payload = {
          completed: state.completed,
          bookmarks: state.bookmarks,
          quizResults: state.quizResults,
          notes: state.notes,
          exportedAt: new Date().toISOString()
        };
        const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `wahh_study_progress_${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
      });
    }

    if (importInput) {
      importInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (evt) => {
          try {
            const data = JSON.parse(evt.target.result);
            if (data.completed) state.completed = data.completed;
            if (data.bookmarks) state.bookmarks = data.bookmarks;
            if (data.quizResults) state.quizResults = data.quizResults;
            if (data.notes) state.notes = data.notes;
            saveState();
            renderSidebar();
            renderCurrentModule();
            alert('Study progress successfully restored!');
            if (modal) modal.classList.remove('open');
          } catch (err) {
            alert('Invalid progress JSON file.');
          }
        };
        reader.readAsText(file);
      });
    }

    if (resetAllBtn) {
      resetAllBtn.addEventListener('click', () => {
        if (confirm('Are you sure you want to reset all completed chapters, quiz scores, and study notes? This cannot be undone.')) {
          state.completed = [];
          state.bookmarks = [];
          state.quizResults = {};
          state.notes = {};
          saveState();
          renderSidebar();
          renderCurrentModule();
          if (modal) modal.classList.remove('open');
        }
      });
    }
  }

  // Setup Theme Switcher
  function updateThemeDots() {
    document.querySelectorAll('.theme-dot').forEach(dot => {
      if (dot.getAttribute('data-set-theme') === state.theme) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function setupTheme() {
    document.body.setAttribute('data-theme', state.theme);
    updateThemeDots();

    document.querySelectorAll('.theme-dot').forEach(dot => {
      dot.addEventListener('click', () => {
        const t = dot.getAttribute('data-set-theme');
        state.theme = t;
        document.body.setAttribute('data-theme', t);
        updateThemeDots();
        saveState();
      });
    });
  }

  // Setup Tab Bar Navigation
  function setupTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        state.activeTab = targetTab;

        tabButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        tabPanes.forEach(pane => {
          if (pane.id === `pane-${targetTab}`) {
            pane.classList.add('active');
          } else {
            pane.classList.remove('active');
          }
        });

        refreshIcons();
      });
    });
  }

  // Setup User Action Buttons (Mark Complete, Bookmark, Reset Quiz, Notes Save)
  function setupActions() {
    // Mobile Drawer Toggle
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('appSidebar');
    if (menuToggle && sidebar) {
      menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
      });
    }

    // Logo click goes to Intro
    const logoHome = document.getElementById('logoHomeBtn');
    if (logoHome) {
      logoHome.addEventListener('click', () => {
        navigateToModule('intro');
      });
    }

    // Category Filter Pills
    const filterContainer = document.getElementById('categoryFilters');
    if (filterContainer) {
      filterContainer.querySelectorAll('.filter-pill').forEach(pill => {
        pill.addEventListener('click', () => {
          filterContainer.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          state.categoryFilter = pill.getAttribute('data-category');
          renderSidebar();
        });
      });
    }

    // Mark Complete Button
    const markCompleteBtn = document.getElementById('markCompleteBtn');
    if (markCompleteBtn) {
      markCompleteBtn.addEventListener('click', () => {
        const modId = state.currentModuleId;
        const idx = state.completed.indexOf(modId);
        if (idx === -1) {
          state.completed.push(modId);
        } else {
          state.completed.splice(idx, 1);
        }
        saveState();
        renderSidebar();
        renderCurrentModule();
      });
    }

    // Bookmark Button
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    if (bookmarkBtn) {
      bookmarkBtn.addEventListener('click', () => {
        const modId = state.currentModuleId;
        const idx = state.bookmarks.indexOf(modId);
        if (idx === -1) {
          state.bookmarks.push(modId);
        } else {
          state.bookmarks.splice(idx, 1);
        }
        saveState();
        renderSidebar();
        renderCurrentModule();
      });
    }

    // Reset Quiz Button
    const resetQuizBtn = document.getElementById('resetQuizBtn');
    if (resetQuizBtn) {
      resetQuizBtn.addEventListener('click', () => {
        const modId = state.currentModuleId;
        if (state.quizResults[modId]) {
          delete state.quizResults[modId];
          saveState();
          renderSidebar();
          renderCurrentModule();
        }
      });
    }

    // Save Notes Button
    const saveNotesBtn = document.getElementById('saveNotesBtn');
    const clearNotesBtn = document.getElementById('clearNotesBtn');
    const notesArea = document.getElementById('userChapterNotes');

    if (saveNotesBtn && notesArea) {
      saveNotesBtn.addEventListener('click', () => {
        state.notes[state.currentModuleId] = notesArea.value;
        saveState();
        const orig = saveNotesBtn.innerText;
        saveNotesBtn.innerText = 'Saved ✓';
        setTimeout(() => { saveNotesBtn.innerText = orig; }, 1500);
      });
    }

    if (clearNotesBtn && notesArea) {
      clearNotesBtn.addEventListener('click', () => {
        if (confirm('Clear notes for this chapter?')) {
          notesArea.value = '';
          delete state.notes[state.currentModuleId];
          saveState();
        }
      });
    }

    // Auto-save notes on input
    if (notesArea) {
      notesArea.addEventListener('input', () => {
        state.notes[state.currentModuleId] = notesArea.value;
        localStorage.setItem('wahh_notes', JSON.stringify(state.notes));
      });
    }
  }

  // Keyboard navigation (J / K for next / prev module)
  function setupKeyboardNav() {
    window.addEventListener('keydown', (e) => {
      if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA') return;

      const modules = window.WAHH_CURRICULUM || [];
      const currIdx = modules.findIndex(m => m.id === state.currentModuleId);

      if (e.key === 'j' || e.key === 'n') { // Next module
        if (currIdx < modules.length - 1) {
          navigateToModule(modules[currIdx + 1].id);
        }
      } else if (e.key === 'k' || e.key === 'p') { // Previous module
        if (currIdx > 0) {
          navigateToModule(modules[currIdx - 1].id);
        }
      } else if (e.key === 'm') { // Toggle complete
        const markCompleteBtn = document.getElementById('markCompleteBtn');
        if (markCompleteBtn) markCompleteBtn.click();
      }
    });
  }

  // App Initialization
  function init() {
    setupTheme();
    setupTabs();
    setupActions();
    setupPlaygroundLabs();
    setupSearch();
    setupGrandExam();
    setupBackupModal();
    setupKeyboardNav();

    renderSidebar();
    renderCurrentModule();
    updateProgressStats();
    refreshIcons();
  }

  // Run on DOM load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
