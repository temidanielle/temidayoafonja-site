(function () {
  var v = (location.hash || '#a').slice(1) || 'a';
  document.documentElement.style.setProperty('--img', "url('render-" + v + ".png')");
})();
