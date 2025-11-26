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

// List of tours with button IDs, URLs, and labels
const tours = [
  { id: 'tourA-btn', url: 'https://agentmrc.github.io/virtual-tour-project/tourA/', label: 'Tour A' },
  { id: 'tourB-btn', url: 'https://agentmrc.github.io/virtual-tour-project/tourB/', label: 'Tour B' },
  { id: 'tourC-btn', url: 'https://agentmrc.github.io/virtual-tour-project/tourC/', label: 'Tour C' },
  { id: 'tourD-btn', url: 'https://agentmrc.github.io/virtual-tour-project/tourD/', label: 'Tour D' },
  { id: 'tourE-btn', url: 'https://agentmrc.github.io/virtual-tour-project/tourE/', label: 'Tour E' },
];

tours.forEach(tour => {
  const button = document.getElementById(tour.id);
  if(button) {
    button.addEventListener('click', () => {
      // GA4 event
      gtag('event', 'click_tour', {
        'event_category': 'virtual_tour',
        'event_label': tour.label
      });
      // Redirect to virtual tour
      window.location.href = tour.url;
    });
  }
});

