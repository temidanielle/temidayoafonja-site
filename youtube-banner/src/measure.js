document.fonts.ready.then(function () {
  var t = document.getElementById('t'), s = document.getElementById('s');
  var stage = document.querySelector('.stage');
  var sr = stage.getBoundingClientRect();
  var box = [t, s].map(function (el) { return el.getBoundingClientRect(); });
  var left = Math.min.apply(null, box.map(function (b) { return b.left; }));
  var right = Math.max.apply(null, box.map(function (b) { return b.right; }));
  var top = Math.min.apply(null, box.map(function (b) { return b.top; }));
  var bot = Math.max.apply(null, box.map(function (b) { return b.bottom; }));
  document.getElementById('m').textContent =
    'MEASURE title=' + Math.round(box[0].width) +
    ' support=' + Math.round(box[1].width) +
    ' contentW=' + Math.round(right - left) +
    ' contentH=' + Math.round(bot - top) +
    ' leftGap=' + Math.round(left - sr.left) +
    ' rightGap=' + Math.round(sr.right - right) +
    ' topGap=' + Math.round(top - sr.top);
});
