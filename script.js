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

const detailsPanel = document.getElementById("detailsPanel");
const contactPanel = document.getElementById("contactPanel");

document.getElementById("navDetails").addEventListener("click", () => {
  detailsPanel.classList.toggle("open");
  contactPanel.classList.remove("open");
});

document.getElementById("navContact").addEventListener("click", () => {
  contactPanel.classList.toggle("open");
  detailsPanel.classList.remove("open");
});

document.getElementById("navHome").addEventListener("click", () => {
  detailsPanel.classList.remove("open");
  contactPanel.classList.remove("open");
});

const panels = document.querySelectorAll('.info-panel');
const overlay = document.getElementById('panelOverlay');

// open panel helper
function openPanel(panel) {
  panels.forEach(p => p.classList.remove('open'));
  panel.classList.add('open');
  overlay.classList.add('active');
}

// close all panels
function closePanels() {
  panels.forEach(p => p.classList.remove('open'));
  overlay.classList.remove('active');
}

// close button
document.querySelectorAll('.panel-close').forEach(btn => {
  btn.addEventListener('click', closePanels);
});

// overlay click
overlay.addEventListener('click', closePanels);

// navbar triggers (example)
document.getElementById('navDetails').addEventListener('click', () => {
  openPanel(document.getElementById('detailsPanel'));
});

document.getElementById('navContact').addEventListener('click', () => {
  openPanel(document.getElementById('contactPanel'));
});


