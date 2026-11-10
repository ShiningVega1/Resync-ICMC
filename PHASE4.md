# Phase 4 — ICMC Website Functional Upgrade and Handoff

**Status:** Planned. Check tasks off only after they are developed, verified, and deployed.

## Outcome
Deliver a polished, maintainable site, still compatible with the GitHub Pages + Pages CMS workflow, with dynamic schedules and events where integrations permit. Prepare an ICMC-owned fork for independent operation.

## A. Prayer and MasjiDal integration
- [ ] Confirm the officially supported MasjiDal widget/embed, API, event hooks, or webhooks and their terms.
- [ ] If supported, integrate live salah, iqamah, Jumu'ah and timetable data, with loading and failure states.
- [ ] If not, preserve the existing embed and provide a documented CMS-editable fallback for displayed schedule/link.
- [ ] Identify the authoritative editor and timezone (America/Chicago); test DST and schedule changes.
- [ ] Do not expose credentials or private endpoints in front-end JavaScript.

## B. Calendar and CMS
- [ ] Use existing Pages CMS events as the only event source; do not create a redundant database.
- [ ] Add a responsive month/list calendar with event details and accessible navigation.
- [ ] Handle timezones, multi-day events, cancellations and past/upcoming filtering.
- [ ] Verify published edits appear after build/deployment without code changes.
- [ ] Preserve existing announcement ordering, expiration and CMS publication controls.

## C. Design, navigation and site hygiene
- [ ] Audit for duplicate announcements buttons and overlapping navigation destinations.
- [ ] Refine desktop dropdowns/mobile hamburger, keyboard access, and focus states.
- [ ] Replace browser-tab favicon with approved ICMC logo.
- [ ] Keep the current approved hero emphasis and formal, restrained typography.
- [ ] Remove nonfunctional archived `docs/` links or replace them with intentional placeholders.
- [ ] Verify headings, page layouts, contrast, imagery and accessibility.

## D. Hosting and controlled review
- [ ] Test GitHub Pages deployment from `_site/`.
- [ ] Plan Cloudflare DNS for `icmc.swipeleft.org`; verify custom domain/TLS.
- [ ] For restricted previews, choose real access control. A JS-only password prompt, even one asking for `ICMC_Pass`, is not security and does not restrict GitHub Pages files. Avoid putting sensitive content on public pages.
- [ ] Keep preview `noindex` until an authorized production launch.

## E. Optional knowledge-base chatbot
- [ ] Choose an approved, publicly safe source of FAQs (Google Docs export or CMS content).
- [ ] Prototype free-tier retrieval with citations/links to source answers, without private API keys in browser code.
- [ ] Provide honest “I don't know” behavior and relevant general/imam contact routing.
- [ ] Do not block core site launch on the chatbot.

## F. Fork and operations documentation
- [ ] README covers fork permissions, GitHub Actions, Pages CMS, DNS, domains and deployment.
- [ ] Identify every source-specific link, account, credential placeholder, and image to replace.
- [ ] Write operator instructions for prayer times, announcements, event updates and media.
- [ ] Verify forms can actually send, donation recipient is correct, and policies/permissions are approved.
- [ ] Test fresh fork on an organization-controlled repository and review ownership/backup responsibilities.

## Definition of done
The approved site works on desktop/mobile; prayer times have a supported live source or documented fallback; calendar/events come from one editable data source; CMS changes trigger successful deployment; no misleading placeholder links or duplicate calls to action remain; and ICMC can fork, configure, and administer its site using the README without depending on the original developer.
