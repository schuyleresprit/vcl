const DATA = url(timeline.json)

if(document.getElementById('pubdate')) {
  let timeline = new Timeline('timeline', DATA, {
    mobileBreakpoint: 500
  });
  timeline.init();
}
