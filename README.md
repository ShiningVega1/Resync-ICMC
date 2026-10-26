# Swipeleft-ICMC

Static redesign prototype for the Islamic Center of McLean County (Masjid Ibrahim), intended for review before any live domain cutover.

## Repository structure
- Root HTML pages (`index.html`, `about.html`, `education.html`, etc.) are the redesigned prototype.
- `site.css` and `site.js` provide shared layout, navigation, and lightweight form-validation behavior.
- `docs/` contains captured public source content and assets referenced by some service links.
- `scripts/mirror.py` and `scripts/normalize.py` are maintenance scripts for refreshing mirrored source content.

## Deployment

### GitHub Pages
1. In repository settings, enable **Pages**.
2. Set source to **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**.
4. Keep `.nojekyll` in place so files with underscore-prefixed paths remain accessible.

### Cloudflare Pages
This repository includes `wrangler.toml` with:
- `pages_build_output_dir = "."`

Use these settings in Cloudflare Pages:
- Framework preset: **None**
- Build command: *(leave empty)*
- Build output directory: `.` (repository root)

## Mirror workflow safety
- `.github/workflows/mirror.yml` and `.github/workflows/normalize.yml` are now **manual-only** (`workflow_dispatch`).
- They upload artifacts for review instead of auto-committing to the repository.
- This prevents automated mirror refreshes from overwriting redesign work on active branches.

## Maintenance notes
- Keep all prototype forms non-sending; do not route submissions to live institutional inboxes from this sandbox.
- Preserve verified contact/donation/program information from `https://icmclean.org/`; do not publish unverified claims.
- Do not modify the separate `ShiningVega1/swipeleft` repository from this project.
