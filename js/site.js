(() => {
  document.documentElement.classList.add('js');
  const themeToggle = document.querySelector('.theme-toggle');
  const syncTheme = () => {
    const night = document.documentElement.dataset.theme !== 'day';
    if (themeToggle) {
      themeToggle.textContent = night ? 'Light' : 'Dark';
      themeToggle.setAttribute('aria-label', night ? 'Switch to light theme' : 'Switch to dark theme');
    }
    const themeColor = document.querySelector('meta[name="theme-color"]');
    if (themeColor) themeColor.content = night ? '#101b26' : '#ffffff';
  };
  syncTheme();
  if (themeToggle) themeToggle.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'day' ? 'night' : 'day';
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem('warp-theme', theme); } catch (error) {}
    syncTheme();
  });
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  if (!toggle || !nav) return;
  const close = () => {
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('is-open');
  };
  toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    nav.classList.toggle('is-open', !expanded);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) {
      close();
      toggle.focus();
    }
  });
  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) close();
  });
})();

