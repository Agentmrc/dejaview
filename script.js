const iframe = document.getElementById('mpIframe');

// Fullscreen button
document.getElementById('openFullscreen').addEventListener('click', () => {
  if (iframe.requestFullscreen) {
    iframe.requestFullscreen();
  } else if (iframe.webkitRequestFullscreen) {
    iframe.webkitRequestFullscreen();
  } else {
    alert('Your browser does not support fullscreen via this method.');
  }
});

// Reset view (reload iframe)
document.getElementById('resetView').addEventListener('click', () => {
  const src = iframe.src;
  iframe.src = '';   // force reload
  setTimeout(() => iframe.src = src, 50);
});
