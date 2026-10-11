// Network first, cache as fallback: updates show up straight away online, and the grocery list still opens in a shop with no signal.
const CACHE = "cookbook-v4";
const FILES = ["./", "index.html", "recipes/recipes.json", "manifest.webmanifest", "icon-180.png"];
self.addEventListener("install", (e) => e.waitUntil(caches.open(CACHE).then((c) => c.addAll(FILES))));
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(fetch(e.request).then((res) => {
    const copy = res.clone();
    caches.open(CACHE).then((c) => c.put(e.request, copy));
    return res;
  }).catch(() => caches.match(e.request)));
});
