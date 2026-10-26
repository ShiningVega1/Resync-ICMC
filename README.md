# Swipeleft-ICMC

Static redesign prototype for the Islamic Center of McLean County (Masjid Ibrahim), intended for review before any live domain cutover.

## What is implemented now
- Root pages (`index.html`, `about.html`, `education.html`, `services.html`, `imam.html`, `announcements.html`, `contact.html`, `donate.html`, `maktab.html`, `weekend-school.html`) provide the redesigned static experience.
- `site.css` and `site.js` provide shared layout, responsive navigation, and prototype-only form validation behavior.
- Prayer times use ICMC’s existing embedded provider (no hardcoded prayer schedule).
- Verified contact and donation links are preserved from ICMC’s published information.
- Mirror/normalization workflows are manual-only and publish artifacts instead of committing directly.

## Prototype limitations (still intentional)
- No WordPress backend is included.
- Contact forms are non-sending and do not store submissions.
- Some linked service and announcement content still points to mirrored `docs/` capture pages.
- External services (maps, donation portals, prayer widget) remain external dependencies.

## Static integrity checks
Run locally:

```bash
python scripts/check_static.py
```

This validates:
- Internal link and asset resolution across root HTML pages
- Presence of essential assets (logo, stylesheet, script, key service pages)
- Basic page integrity (`<nav>` and `<footer>` presence)

GitHub Actions workflow: `.github/workflows/static-integrity.yml`

## Deployment

### GitHub Pages
1. In repository settings, enable **Pages**.
2. Source: **Deploy from a branch**.
3. Branch: **main**, folder: **/(root)**.
4. Keep `.nojekyll` committed.

### Cloudflare Pages
`wrangler.toml` is configured for static root output:

```toml
name = "swipeleft-icmc"
compatibility_date = "2026-10-26"
pages_build_output_dir = "."
```

Recommended Pages settings:
- Framework preset: **None**
- Build command: *(empty)*
- Build output directory: `.`

To reduce accidental exposure of development-only paths, `_redirects` blocks direct access to `.github`, `scripts`, and mirror metadata files.

## Maintenance guardrails
- Preserve verified program/contact/donation information from `https://icmclean.org/`.
- Do not wire prototype forms to live submission endpoints from this repository.
- Do not modify the separate `ShiningVega1/swipeleft` repository from this project.
