# Swipeleft-ICMC — forkable website with Pages CMS

A clean, static prototype for the Islamic Center of McLean County (Masjid Ibrahim). **This is not yet the organization's production website.**

## What's included
- The original responsive design, site pages, and prayer-time iframe.
- Homepage announcement slideshow, automatic rotation (7 seconds), arrows, reduced-motion support, expiration dates, and publication controls.
- Community announcements, news posts, and event listings on `announcements.html`.
- `.pages.yml` configuring an external, GitHub-authorized visual editor for all three collections.
- Zero-dependency Python static build and GitHub Pages deployment workflow.
- MOHID link supplied for review: `https://us.mohid.co/il/joliet/mi/masjid/online/donation/index/23`. **Verify the payee/recipient with ICMC before promoting it as an official live donation channel** (URL contains a Joliet path).

## Fork and launch (ICMC owner)
1. Fork this repository to ICMC's GitHub account or organization. The organization must own and control its repository.
2. In the fork: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Do not select branch deployment: `.github/workflows/deploy-pages.yml` performs the content build and deployment.
3. Open **https://app.pagescms.org/**, sign in with GitHub, and grant the Pages CMS GitHub App access to the **fork**. Pick that repository and its `main` branch. Admins require GitHub authorization to write to this repository. Do not use a shared administrator password.
4. Open **Announcements / Slides**, **News / Posts**, or **Events**. Create an entry, fill in details, select **Published**. On announcements, also choose **Show in homepage slideshow**. Changes are saved in GitHub; after GitHub Actions deploys, the public pages update.
5. Verify the GitHub Pages URL in the workflow's deployment status. If using `icmclean.org`, coordinate custom-domain DNS and ownership with the organization's domain administrator; do not switch DNS until approved.
6. Test on mobile, add real published content, and remove or edit sample content before the public launch.
7. For public launch, remove `noindex,nofollow` from HTML pages, remove the prototype banner, and replace mirrored `docs/` links and non-sending demo forms as appropriate.

## Everyday editing
- A published announcement appears on the announcements page. Enable `featured` to show it in the rotating homepage slideshow. Set `expires` (YYYY-MM-DD) to remove it automatically from public display after that date.
- A published post appears under **Community news**. A published event appears under **Upcoming events**.
- If `published` is unchecked, the entry stays in GitHub but does not display publicly.
- Upload flyers with the CMS media picker to `media/`. All files remain in the fork. Large files will increase repository size.
- Never commit credentials, private staff details, or personal information to this repository: published JSON feeds are publicly accessible.

## Technical details
- `content/announcements/*.json`, `content/posts/*.json`, and `content/events/*.json` are editable JSON files.
- `python scripts/build_site.py` builds the publishable `_site/` and creates `_site/content/feed.json`. The browser reads this feed via `site.js`; no database, WordPress server, paid hosting, or GitHub API token is used by the public website.
- Run `python scripts/check_static.py` to check original site links, and then `python scripts/build_site.py` locally. To preview, `cd _site && python -m http.server 8000`; open `http://localhost:8000` (don't open HTML directly as a file).
- GitHub Pages workflow deploys on changes to `main`. Pages CMS saves content commits that trigger a rebuild. A custom domain is optional.
- `noindex,nofollow` and a prototype notice are intentionally retained until ICMC authorizes publishing.
- On every fork, GitHub Actions settings and Pages deployment permissions may need to be enabled by its owner. ICMC admins need GitHub access to manage content in Pages CMS.
- GitHub Pages is static: this does **not** provide a local `/admin` login. Staff sign into the external CMS. Existing demo contact forms do not send messages.
- The current slideshow uses summary and links. Uploaded image fields are retained in content, but images are not displayed in the slideshow yet.
- Example posts and announcements are demonstration data, not confirmed event schedules.

## Moving to another host
The build emits a self-contained `_site/` folder. Any static host able to publish this folder can serve the website; Pages CMS continues to edit GitHub files. Deploy `_site/` rather than the repository root, otherwise the CMS feed will not exist. The workflow is specific to GitHub Pages; replace it for a different provider.

## Verification checklist
- [ ] ICMC verifies the MOHID recipient and donation address
- [ ] ICMC authorizes use of this repository and its current design
- [ ] CMS can create/edit an announcement, post, and event in the organization-owned fork
- [ ] GitHub Actions succeeds and the live slideshow/listings change
- [ ] Links, service info, prayer widget, and mobile navigation are tested
- [ ] Organization controls GitHub account, Pages CMS permission, domain, and hosting settings
- [ ] Sample content removed, privacy/security review completed before production

## Existing site limitations
Archived `docs/` content comes from a prior website capture, some links still lead to that archive, and contact forms are demonstration-only. Prayer times rely on an existing third-party embed. Maintain existing source attribution and rights before production.
