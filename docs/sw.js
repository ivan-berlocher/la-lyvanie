// Service Worker — La Lyvania PWA
const CACHE_NAME = 'lyvania-v1';

// Fichiers essentiels à cacher immédiatement
const CORE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

// Installation : cache les fichiers essentiels
self.addEventListener('install', event => {
  console.log('🦊 Service Worker: Installation...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('🦊 Cache ouvert, ajout des fichiers essentiels');
        return cache.addAll(CORE_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activation : nettoie les anciens caches
self.addEventListener('activate', event => {
  console.log('🦊 Service Worker: Activation...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => {
            console.log('🦊 Suppression ancien cache:', name);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// Stratégie: Network First, fallback to Cache
// (pour toujours avoir le contenu le plus frais)
self.addEventListener('fetch', event => {
  // Ignore les requêtes non-GET
  if (event.request.method !== 'GET') return;
  
  // Ignore les requêtes externes (fonts Google, etc.)
  if (!event.request.url.startsWith(self.location.origin)) {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Clone la réponse pour la mettre en cache
        if (response.ok) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Hors-ligne : cherche dans le cache
        return caches.match(event.request).then(cachedResponse => {
          if (cachedResponse) {
            return cachedResponse;
          }
          // Page hors-ligne de secours pour la navigation
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html');
          }
          return new Response('Contenu non disponible hors-ligne', {
            status: 503,
            statusText: 'Service Unavailable'
          });
        });
      })
  );
});

// Message pour forcer la mise à jour
self.addEventListener('message', event => {
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
  }
});
