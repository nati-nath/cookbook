# Cookbook

Recipes I like, with the ingredients and the time each one takes. Two jobs: find something to cook
today (filter by time, tag or ingredient), and plan the shop (add recipes, get one merged grocery list).
Built to be added to an iPhone home screen, same as Ritual.

## Adding a recipe

Add an object to `recipes/recipes.json`, then check it parses:

```bash
python3 -m json.tool recipes/recipes.json > /dev/null && echo valid
```

Fields: `id` (permanent, the grocery list on the phone refers to it), `name`, `subtitle`, `tags`,
`image`, `image_alt`, `image_credit` (`text` and `url`), `prep_minutes`, `cook_minutes`, `time_is_estimate`, `source`, `ingredients`, `steps`, `variations`, `note`.

Each ingredient: `name`, `qty` (number or `null`), optional `qty_max` for a range, `unit`, `aisle`,
optional `group` (sub-heading), `note`, `pantry` (goes under "Check you have"), `no_grocery` (never listed, e.g. water).

- The grocery list merges lines with the same `name`. Keep names identical across recipes ("soy sauce", "garlic").
- Teaspoons and tablespoons are added together (3 tsp = 1 tbsp).
- Set `time_is_estimate` to `false` once you have cooked it and timed it; the `~` in the app disappears.
- Set `method_inferred` to `true` if the steps are not from the source; the app flags it.

## Photos

Photos live in `images/`, about 900px on the long side, saved as JPEG so a recipe page loads fast on a phone.
Use your own photo, or one with an open licence (Wikimedia Commons). A CC BY or CC BY-SA photo needs
the `image_credit` line, which the app shows under the picture. Do not add a photo you have no right to publish:
this repo is public.

## Running it locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000. It must be served, not opened as a file.

## Where things are stored

The grocery list and ticked items live on the phone only (`localStorage`), never in the repo.
`sw.js` keeps a copy for offline use, so the list opens in a shop with no signal.
