// HOME · service worker V10: funciona sin conexión
const CACHE_NAME = 'home-cache-v17-2026-10-26';
const CORE = [
  './',
  './index.html',
  './manifest.json',
  './logo.png',
  './logo_elibi.jpg',
  './iconocalcu.png'
];
// Librerías para hacer PDF: se guardan también para poder usarlas sin internet
const CDN = [
  'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(CORE);
    await Promise.all(CDN.map(u => fetch(u, { mode: 'cors' }).catch(() => fetch(u, { mode: 'no-cors' }))
      .then(r => r && cache.put(u, r)).catch(() => {})));
  })());
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(names => Promise.all(names.map(n => n !== CACHE_NAME ? caches.delete(n) : null)))
      .then(() => self.clients.claim())
  );
});

function withTimeout(promise, ms) {
  return new Promise((resolve, reject) => {
    const t = setTimeout(() => reject(new Error('timeout')), ms);
    promise.then(r => { clearTimeout(t); resolve(r); }, e => { clearTimeout(t); reject(e); });
  });
}

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Librerías externas: primero lo guardado
  if (CDN.includes(req.url)) {
    event.respondWith(caches.match(req.url).then(hit => hit || fetch(req).then(r => {
      const copy = r.clone(); caches.open(CACHE_NAME).then(c => c.put(req.url, copy)); return r;
    })));
    return;
  }
  if (url.origin !== self.location.origin) return;

  // Abrir la app: si hay internet, la versión nueva; si no (o va lenta), la guardada
  if (req.mode === 'navigate') {
    event.respondWith(
      withTimeout(fetch(req), 4000).then(r => {
        if (r && r.ok) { const copy = r.clone(); caches.open(CACHE_NAME).then(c => c.put('./index.html', copy)); }
        return r;
      }).catch(() => caches.match('./index.html').then(hit => hit || caches.match('./')))
    );
    return;
  }

  // Resto de archivos de la app
  event.respondWith(
    withTimeout(fetch(req), 4000).then(r => {
      if (r && r.ok && r.type === 'basic') { const copy = r.clone(); caches.open(CACHE_NAME).then(c => c.put(req, copy)); }
      return r;
    }).catch(() => caches.match(req, { ignoreSearch: true }))
  );
});
