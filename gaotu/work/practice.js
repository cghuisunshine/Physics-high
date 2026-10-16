(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const $$ = selector => [...document.querySelectorAll(selector)];
  const data = JSON.parse($('#studyPageStructure').textContent);
  const lessonTitles = JSON.parse($('#lessonTranslations').textContent);
  const answers = $$('.answer');
  const sections = $$('.section');
  const cards = $$('.question');
  const languageKey = 'physics-language-v1';
  const ui = {
    zh: {
      title: '力与运动 · 高中物理练习与分步解析', brand: '物理练习室',
      navigation: '学习目录 / CONTENTS', sidebar: '章节导航',
      topbar: '高中物理 / 力与运动', showAll: '展开全部答案', hideAll: '收起全部答案',
      print: '打印 / PDF', printAnswers: '打印含答案',
      eyebrow: '高途高中物理 · 第 7—11 讲', heading: '把每一步，想明白。',
      description: '从常见力到牛顿第二定律，整理原题与配图。点击每题下方的 Show answer，查看受力分析、分步推导与易错提醒。',
      stats: ['个专题', '道练习', '份分步解析'],
      placeholder: '搜索题目或知识点，如：弹簧、摩擦、加速度', searchLabel: '搜索题目或知识点',
      count: n => `${n} 道题目`, found: n => `找到 ${n} 道题`,
      lesson: n => `第 ${n} 讲 · 5 道练习`, exerciseCount: '5 道练习',
      exercise: n => `练习 ${String(n).padStart(2, '0')}`, page: n => `原 PDF 第 ${n} 页`,
      options: '选项', diagram: '原题配图', show: 'Show answer', showHint: '查看分步解析',
      hide: 'Hide answer', hideHint: '收起解析', result: '参考答案', steps: '一步一步推导',
      trap: '易错提醒', copyTitle: '双击复制公式', copied: '公式已复制', copyFallback: '请选中公式并复制',
      progress: n => `已查看 ${n} / 25 道解析`, progressLabel: '已查看解析进度',
      studyHint: '先独立作答，再展开解析。\n公式框支持双击复制。\n单文件 · 无需联网',
      empty: '没有找到匹配的题目，试试其他关键词。',
      footer: [
        '资料来源：本目录中的高途高中物理第 7—11 讲学生版 PDF。原题配图已嵌入，题目中的公式与数值已按页面图像核对。',
        '参考答案与解析为重新推导，非原资料附带的官方答案。选择题可能有多个正确选项；存在条件歧义的题目已在解析中说明。'
      ],
      menu: '打开语言与目录菜单', language: '语言 / Language',
      browse: '浏览章节目录', showSidebar: '显示章节目录', hideSidebar: '隐藏章节目录'
    },
    en: {
      title: 'Forces and Motion · Physics Practice and Worked Solutions', brand: 'Physics Workbook',
      navigation: 'LESSON CONTENTS', sidebar: 'Lesson navigation',
      topbar: 'High school physics / Forces and motion', showAll: 'Show all', hideAll: 'Hide all',
      print: 'Print / PDF', printAnswers: 'Include answers',
      eyebrow: 'GAOTU HIGH SCHOOL PHYSICS · LESSONS 7–11', heading: 'Understand every step.',
      description: 'Explore forces and Newton’s laws through the original exercises and diagrams. Choose Show answer for force analysis, step-by-step solutions, and common mistakes.',
      stats: ['topics', 'exercises', 'solutions'],
      placeholder: 'Search topics: springs, friction, acceleration…', searchLabel: 'Search exercises or topics',
      count: n => `${n} exercises`, found: n => `${n} found`,
      lesson: n => `Lesson ${n} · 5 exercises`, exerciseCount: '5 exercises',
      exercise: n => `Exercise ${String(n).padStart(2, '0')}`, page: n => `Original PDF · p. ${n}`,
      options: 'Answer choices', diagram: 'Original diagram', show: 'Show answer', showHint: 'Step-by-step solution',
      hide: 'Hide answer', hideHint: 'Close solution', result: 'ANSWER', steps: 'Step by step',
      trap: 'COMMON MISTAKE', copyTitle: 'Double-click to copy the formula', copied: 'Formula copied', copyFallback: 'Select the formula and copy it',
      progress: n => `${n} / 25 solutions viewed`, progressLabel: 'Solutions viewed',
      studyHint: 'Try each exercise before opening its solution.\nDouble-click a formula to copy it.\nOne file · Works offline',
      empty: 'No matching exercises. Try another keyword.',
      footer: [
        'Source: the Gaotu high school physics student PDFs for Lessons 7–11 in this folder. Original diagrams are embedded; numerical values and formulas were checked against the source pages. English captions explain the original diagram labels.',
        'The worked solutions were derived for this workbook and are not official source answer keys. Multiple-choice questions may have more than one correct answer. Any ambiguity in a question’s conditions is explained in its solution.'
      ],
      menu: 'Open language and navigation menu', language: 'Language / 语言',
      browse: 'Browse lessons', showSidebar: 'Show lesson list', hideSidebar: 'Hide lesson list'
    }
  };
  let language = 'zh';
  try { if (localStorage.getItem(languageKey) === 'en') language = 'en'; } catch (_) {}
  let viewed = new Set();
  try {
    const saved = JSON.parse(localStorage.getItem('physics-viewed-v1') || '[]');
    if (Array.isArray(saved)) viewed = new Set(saved);
  } catch (_) {}
  const validIds = new Set(cards.map(card => card.id));
  viewed = new Set([...viewed].filter(id => validIds.has(id)));
  let printState = null;

  // Keep the existing lesson sidebar and expose language choices from the hamburger.
  const menuButton = $('#toggleSidebar');
  const menuPanel = document.createElement('section');
  menuPanel.id = 'menuPanel';
  menuPanel.className = 'menu-panel';
  menuPanel.hidden = true;
  menuPanel.innerHTML = '<h2 id="languageHeading"></h2><div class="language-options" role="group" aria-labelledby="languageHeading"><button type="button" data-language="zh" lang="zh-CN">中文</button><button type="button" data-language="en" lang="en">English</button></div><button type="button" id="browseLessons" class="browse-lessons"></button>';
  $('.topbar').append(menuPanel);
  menuButton.setAttribute('aria-controls', 'menuPanel');
  menuButton.setAttribute('aria-expanded', 'false');

  function mobile() { return matchMedia('(max-width:800px)').matches; }
  function menu(open, returnFocus = false) {
    menuPanel.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
    if (open) menuPanel.querySelector(`[data-language="${language}"]`).focus();
    else if (returnFocus) menuButton.focus();
  }
  function sidebarControl() {
    $('#browseLessons').textContent = mobile() ? ui[language].browse :
      ui[language][document.body.classList.contains('sidebar-hidden') ? 'showSidebar' : 'hideSidebar'];
  }
  function progress() {
    $('#progressText').textContent = ui[language].progress(viewed.size);
    $('#progressBar').style.width = `${viewed.size / 25 * 100}%`;
    $('[role="progressbar"]').setAttribute('aria-valuenow', viewed.size);
    try { localStorage.setItem('physics-viewed-v1', JSON.stringify([...viewed])); } catch (_) {}
  }
  function lines(element, text, tag) {
    element.replaceChildren(...text.split('\n').map(line => {
      const node = document.createElement(tag);
      node.textContent = line;
      return node;
    }));
  }
  function answerLabel(element, label, hint) {
    const small = document.createElement('span');
    small.textContent = hint;
    element.replaceChildren(document.createTextNode(label), small);
  }
  function filterQuestions() {
    const term = $('#search').value.trim().toLocaleLowerCase();
    let count = 0;
    cards.forEach(card => {
      const hit = card.dataset.search.toLocaleLowerCase().includes(term);
      card.hidden = !hit;
      card.classList.toggle('hl', Boolean(term) && hit);
      if (hit) count++;
    });
    sections.forEach(section => {
      section.hidden = ![...section.querySelectorAll('.question')].some(card => !card.hidden);
      if (term && !section.hidden) section.open = true;
    });
    $('#searchCount').textContent = ui[language][term ? 'found' : 'count'](count);
    $('#empty').hidden = count > 0;
    $$('.toc a').forEach(link => { link.hidden = $('#lesson-' + link.dataset.lesson).hidden; });
  }

  data.forEach(item => {
    const card = document.getElementById(item.id);
    card.dataset.search = [item.title, item.text, ...item.options, lessonTitles.zh[item.lesson],
      item.en.title, item.en.text, ...item.en.options, lessonTitles.en[item.lesson]].join(' ').toLocaleLowerCase();
  });

  function setLanguage(next, remember = true) {
    if (!ui[next]) return;
    const anchor = window.scrollY > 200 ? cards.find(card => !card.hidden && card.getBoundingClientRect().bottom > 100) : null;
    const anchorTop = anchor?.getBoundingClientRect().top;
    language = next;
    const t = ui[language];
    document.documentElement.lang = language === 'en' ? 'en' : 'zh-CN';
    document.title = t.title;
    $('meta[name="description"]').content = t.description;
    const brandSubtitle = document.createElement('small');
    brandSubtitle.textContent = 'PHYSICS WORKBOOK';
    $('.brand > span:last-child').replaceChildren(document.createTextNode(t.brand), brandSubtitle);
    $('.nav-label').textContent = t.navigation;
    $('#sidebar').setAttribute('aria-label', t.sidebar);
    $('.topbar-title').textContent = t.topbar;
    $('#showAll').textContent = t.showAll;
    $('#hideAll').textContent = t.hideAll;
    $('#print').textContent = t.print;
    $('#printLabel').textContent = t.printAnswers;
    $('.eyebrow').textContent = t.eyebrow;
    $('#pageTitle').textContent = t.heading;
    $('.hero-description').textContent = t.description;
    $$('.stats span').forEach((span, i) => { span.textContent = t.stats[i]; });
    $('#search').placeholder = t.placeholder;
    $('#search').setAttribute('aria-label', t.searchLabel);
    $('[role="progressbar"]').setAttribute('aria-label', t.progressLabel);
    $('.side-bottom p').textContent = t.studyHint;
    $('#empty').textContent = t.empty;
    $$('footer p').forEach((p, i) => { p.textContent = t.footer[i]; });
    menuButton.setAttribute('aria-label', t.menu);
    menuPanel.setAttribute('aria-labelledby', 'languageHeading');
    $('#languageHeading').textContent = t.language;
    $$('[data-language]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.language === language));
    });
    sections.forEach(section => {
      const n = section.id.replace('lesson-', '');
      section.querySelector('.lesson-heading h2').textContent = lessonTitles[language][n];
      section.querySelector('.lesson-heading small').textContent = t.lesson(n);
      const linkLabel = $(`.toc a[data-lesson="${n}"] > span:last-child`);
      const count = document.createElement('small');
      count.textContent = t.exerciseCount;
      linkLabel.replaceChildren(document.createTextNode(lessonTitles[language][n]), count);
    });
    data.forEach(item => {
      const text = language === 'en' ? item.en : item;
      const card = document.getElementById(item.id);
      card.querySelector('.question-index').textContent = t.exercise(item.number);
      card.querySelector('.question-meta > span:last-child').textContent = t.page(item.page);
      card.querySelector('h3').textContent = text.title;
      lines(card.querySelector('.question-text'), text.text, 'p');
      const options = card.querySelector('.options');
      options.setAttribute('aria-label', t.options);
      [...options.querySelectorAll('li > span:last-child')].forEach((span, i) => { span.textContent = text.options[i]; });
      const image = card.querySelector('figure img');
      if (image) {
        image.alt = text.alt;
        card.querySelector('figcaption').textContent = language === 'en' ? `${t.diagram} · ${text.alt}` : t.diagram;
      }
      answerLabel(card.querySelector('.show-label'), t.show, t.showHint);
      answerLabel(card.querySelector('.hide-label'), t.hide, t.hideHint);
      card.querySelector('.result > span').textContent = t.result;
      card.querySelector('.result strong').textContent = text.answer;
      card.querySelector('.answer-body h4').textContent = t.steps;
      card.querySelector('.steps').replaceChildren(...text.steps.map(step => {
        const li = document.createElement('li');
        li.textContent = step;
        return li;
      }));
      card.querySelector('.equation').textContent = text.formula;
      card.querySelector('.equation').title = t.copyTitle;
      card.querySelector('.trap strong').textContent = t.trap;
      card.querySelector('.trap p').textContent = text.trap;
    });
    sidebarControl();
    progress();
    filterQuestions();
    if (remember) {
      try { localStorage.setItem(languageKey, language); } catch (_) {}
    }
    if (anchor && !anchor.hidden) {
      window.scrollBy({ top: anchor.getBoundingClientRect().top - anchorTop, behavior: 'instant' });
    }
  }

  menuButton.addEventListener('click', () => menu(menuPanel.hidden));
  $$('[data-language]').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language)));
  $('#browseLessons').addEventListener('click', () => {
    if (mobile()) {
      document.body.classList.add('sidebar-visible');
      $('.toc a:not([hidden])')?.focus();
    } else document.body.classList.toggle('sidebar-hidden');
    sidebarControl();
    menu(false);
  });
  document.addEventListener('click', event => {
    if (!menuPanel.hidden && !menuPanel.contains(event.target) && !menuButton.contains(event.target)) menu(false);
  });
  $('#overlay').addEventListener('click', () => document.body.classList.remove('sidebar-visible'));
  window.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (!menuPanel.hidden) menu(false, true);
      if (document.body.classList.contains('sidebar-visible')) {
        document.body.classList.remove('sidebar-visible');
        menuButton.focus();
      }
    }
  });
  window.addEventListener('resize', sidebarControl);
  $$('.toc a').forEach(link => link.addEventListener('click', () => {
    $('#lesson-' + link.dataset.lesson).open = true;
    document.body.classList.remove('sidebar-visible');
  }));
  answers.forEach(answer => answer.addEventListener('toggle', () => {
    if (answer.open && !printState) {
      viewed.add(answer.closest('.question').id);
      progress();
    }
  }));
  $('#showAll').addEventListener('click', () => {
    sections.filter(section => !section.hidden).forEach(section => { section.open = true; });
    answers.filter(answer => !answer.closest('.question').hidden).forEach(answer => { answer.open = true; });
  });
  $('#hideAll').addEventListener('click', () => answers.forEach(answer => { answer.open = false; }));
  $('#search').addEventListener('input', filterQuestions);
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) $$('.toc a').forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === '#' + entry.target.id);
        });
      }
    }, { rootMargin: '-90px 0px -70% 0px' });
    sections.forEach(section => observer.observe(section));
  }
  let toastTimer;
  function toast(text) {
    $('#toast').textContent = text;
    $('#toast').hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { $('#toast').hidden = true; }, 2000);
  }
  $$('[data-copy]').forEach(element => element.addEventListener('dblclick', async () => {
    const text = element.innerText.trim();
    try {
      if (navigator.clipboard) await navigator.clipboard.writeText(text);
      else {
        const area = document.createElement('textarea');
        area.value = text;
        area.style.position = 'fixed';
        area.style.opacity = '0';
        document.body.append(area);
        area.select();
        const copied = document.execCommand('copy');
        area.remove();
        if (!copied) throw new Error('Copy failed');
      }
      toast(ui[language].copied);
    } catch (_) { toast(ui[language].copyFallback); }
  }));
  window.addEventListener('beforeprint', () => {
    if (printState) return;
    printState = { sections: sections.map(section => section.open), answers: answers.map(answer => answer.open) };
    sections.forEach(section => { section.open = true; });
    const include = $('#printAnswers').checked;
    document.body.classList.toggle('no-print-answers', !include);
    answers.forEach(answer => { answer.open = include; });
  });
  window.addEventListener('afterprint', () => {
    if (!printState) return;
    sections.forEach((section, i) => { section.open = printState.sections[i]; });
    answers.forEach((answer, i) => { answer.open = printState.answers[i]; });
    printState = null;
    document.body.classList.remove('no-print-answers');
  });
  $('#print').addEventListener('click', () => window.print());
  setLanguage(language, false);
})();
