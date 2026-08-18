(function () {
  var parts = (location.hash || '#a').slice(1).split(',');
  var v = parts[0] || 'a';
  document.documentElement.style.setProperty('--img', "url('render-" + v + ".png')");
  if (parts.indexOf('dark') !== -1) document.body.classList.add('dark');
})();
