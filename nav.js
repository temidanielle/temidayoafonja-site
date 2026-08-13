/* Accessible mobile navigation.
   Builds a hamburger button and a full-screen overlay menu by cloning the
   existing .nav-links, so the menu markup lives in exactly one place. */
(function () {
  function init() {
    var nav = document.querySelector('nav');
    var links = document.querySelector('.nav-links');
    if (!nav || !links || document.querySelector('.nav-toggle')) return;

    var btn = document.createElement('button');
    btn.className = 'nav-toggle';
    btn.setAttribute('aria-label', 'Open menu');
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', 'mobileMenu');
    btn.innerHTML = '<span></span><span></span><span></span>';
    document.body.appendChild(btn);

    var menu = document.createElement('div');
    menu.className = 'mobile-menu';
    menu.id = 'mobileMenu';
    menu.setAttribute('aria-hidden', 'true');
    var ul = document.createElement('ul');
    ul.innerHTML = links.innerHTML;
    menu.appendChild(ul);
    document.body.appendChild(menu);

    /* Everything the drawer covers while it is open. Marking it inert keeps it
       out of the tab order: without this, tabbing past the last menu item lands
       on links that are completely hidden behind the overlay, which is a WCAG
       2.2 SC 2.4.11 failure as well as plain confusing. The button and the menu
       are appended to <body>, so they are excluded by identity rather than by
       selector. inert is supported in every browser that supports :focus-visible;
       where it is missing the behaviour is simply what it was before. */
    function backdrop() {
      return Array.prototype.filter.call(document.body.children, function (el) {
        return el !== btn && el !== menu;
      });
    }
    function open() {
      menu.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
      btn.setAttribute('aria-label', 'Close menu');
      menu.setAttribute('aria-hidden', 'false');
      document.body.classList.add('menu-open');
      backdrop().forEach(function (el) { el.inert = true; });
    }
    function close() {
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Open menu');
      menu.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('menu-open');
      backdrop().forEach(function (el) { el.inert = false; });
    }
    btn.addEventListener('click', function () {
      menu.classList.contains('open') ? close() : open();
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) { close(); btn.focus(); }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080 && menu.classList.contains('open')) close();
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
