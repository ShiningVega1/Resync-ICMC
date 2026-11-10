# Resync-ICMC — Next Phase Action Plan (Phase 5)

**Status:** Investigation and planning; do not mark integrations completed until verified.  
**Repository rename:** Completed on GitHub; verified as `ShiningVega1/Resync-ICMC`. GitHub Pages deployment and external links still require validation.

## Objective
Turn the mostly static ICMC prototype into a dependable, editable site with authoritative prayer times, a CMS-backed event calendar, and clean organization-owned fork documentation. Avoid redundant data sources, fragile scraping, or unverified integrations.

## Track 1 — MasjiDal investigative practices (highest priority)
1. **Evidence inventory:** Review official [widget guidance](https://help.masjidal.com/knowledge-base/widget/), [prayer-times API reference](https://help.masjidal.com/knowledge-base/prayer-times-api/) and [integration overview](https://mymasjidal.com/pages/integration). Record the date, capabilities, restrictions, and source of each finding.
2. **Account ownership:** Determine whether ICMC already controls its MasjiDal masjid listing, Masjid ID, and Web Integration settings; request an authorized administrator to confirm. Do not collect or disclose keys.
3. **Widget prototype:** In a dedicated branch, embed an official daily/iqamah widget and dynamic monthly timetable with the correct ICMC Masjid ID. Assess sizing, mobile layout, accessibility, Jumu'ah formatting, timezone and visual consistency.
4. **API feasibility:** Determine whether customized timetable/calendar presentation warrants API use. The documented server endpoint is `GET https://api.masjidal.com/timings?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`. It requires an `msj_sk_` server key in an `x-api-key` header and API version `Accept: application/vnd.masjidal.com.v1+json`. **Never place server keys in client JS, HTML, or repository files.** GitHub Actions secrets plus a scheduled data-build could be evaluated, but assess freshness, failed builds, and provider terms before deciding.
5. **Frontend keys:** Verify whether the newer official website widget flow uses domain-restricted `msj_pk_` frontend keys and whether the exact ICMC deployment host must be allowlisted. Keep frontend/server key handling distinct.
6. **Hooks/webhooks:** Ask MasjiDal support whether schedule-change webhooks, callbacks, push notifications, or other supported hooks exist. Do not claim they exist unless officially confirmed. If unavailable, prefer widget auto-refresh or a documented scheduled refresh strategy.
7. **Behavioral tests:** Compare prayer and iqamah values against MasjiDal's own public display on normal days, schedule-change dates, month transitions, and America/Chicago DST transitions. Verify no misleading stale data appears during outages. Preserve a clearly labeled monthly PDF fallback where appropriate.
8. **Decision record:** Document widget-first vs API-driven options, cost, security, refresh latency, accessibility, administrator burden, and recommended approach; obtain ICMC sign-off before production integration.

### Sources and initial evidence
- Official widget documentation: https://help.masjidal.com/knowledge-base/widget/
- Official server-side prayer-times API documentation: https://help.masjidal.com/knowledge-base/prayer-times-api/
- Official widget overview: https://mymasjidal.com/pages/integration/
- Confirmed from documentation: daily and monthly widget options, server-side timings API.
- **Not yet confirmed:** webhook/change-event support, account-specific features, exact ICMC credentials/ID, and API response schema in the organization's account.

## Track 2 — Dynamic community events
- [ ] Reuse the existing Pages CMS events collection as the **single** authoritative calendar data source.
- [ ] Implement accessible monthly and list views generated from published events, with links and event details.
- [ ] Ensure time zone, cancelled events, date ranges, upcoming/past behavior and empty/error states work.
- [ ] Confirm editing through Pages CMS updates the public site after GitHub Actions deployment.
- [ ] Do not confuse the MasjiDal *monthly prayer timetable* with the website *community events calendar*; they are separate views with different data owners.

## Track 3 — Design and content cleanup
- [ ] Consolidate redundant calls to action, dead archive links and placeholder pages.
- [ ] Validate dropdown/mobile navigation, keyboard access, heading hierarchy, performance, responsive images and favicon.
- [ ] Keep the masjid photo central and the styling formal and restrained.
- [ ] Confirm contact forms are functional before describing them as submission channels.

## Track 4 — Rename, hosting and independent ICMC fork
- [x] GitHub owner renamed `Swipeleft-ICMC` → `Resync-ICMC`; repository identity verified.
- [x] Update README and phase documentation for the new repository name; checked current deployment workflow, `site.js`, and `.pages.yml` (no hardcoded old repository name found in those files).
- [ ] Audit remaining archive/media/static files and any external links for hardcoded `/Swipeleft-ICMC/` paths.
- [ ] In GitHub Pages, verify the deployment for `https://shiningvega1.github.io/Resync-ICMC/` only **after** the rename and rebuild; do not assume the URL works automatically.
- [ ] Do not reintroduce the canceled `swipeleft.org` domain.
- [ ] Document how ICMC forks to its own account, enables Pages and Actions, approves Pages CMS, configures the MasjiDal account/widget, verifies the official donation recipient, connects its own domain if authorized, and replaces demonstration forms/content.
- [ ] Use proper access-controlled hosting for any restricted preview; a client-side password is not secure.
- [ ] Perform a clean-room fork/redeployment test with an ICMC-owned repository before handoff.

## Track 5 — Optional chatbot
- [ ] Evaluate an approved publicly shareable FAQ source and a free-tier or static retrieval approach.
- [ ] Provide source citations and fallback contact routing; don't disclose private docs or credentials.
- [ ] Treat this as optional so it does not delay prayer-time or calendar improvements.

## Milestones / acceptance
**M1:** MasjiDal investigation and integration decision documented; required ICMC approvals identified.  
**M2:** Official widget or tested API pipeline reliably displays authoritative daily/iqamah/monthly timing data.  
**M3:** Calendar edits in Pages CMS appear in one responsive event-calendar experience.  
**M4:** Name, routes, deployment and documentation reflect `Resync-ICMC`; mobile, links, accessibility and forms tested.  
**M5:** ICMC can fork and reproduce the deployment using documented instructions, without the original author's domain or credentials.

All items remain proposals until implemented and tested.

## MasjiDal investigation update — 2026-11-09

### Confirmed integration modules
The current official widget editor at https://help.masjidal.com/knowledge-base/widget/ documents:
- **Prayer-times widget**: Grid, Table, Table 2, Ribbon, Compact, and Minimal Bar layouts; header options and Hijri date behavior.
- **Announcements widget**: Stacked, Compact, and Ribbon layouts.
- Both use a single page-level script `https://widgets.masjidal.com/timetable/v0/widget.js` and separate `<masjidal-widget>` instances with `widget-id`, `type`, and a **domain-allowlisted public frontend key** (`msj_pk_`). Obtain exact snippets from the authorized MasjiDal portal; don't commit credentials.
- Legacy widget resources at https://mymasjidal.com/pages/integration and historical widget help advertise dynamic monthly prayer timetables. Determine whether the newer editor has the same monthly option, or whether a separate legacy embed is necessary.
- The server API at https://help.masjidal.com/knowledge-base/prayer-times-api/ uses `msj_sk_` and a date-scoped timings endpoint; server-side only. Official docs recommend caching and avoiding repeated requests for identical dates.
- MasjiDal's ecosystem includes Athan+ and Al-Iqamah signage, and Google Calendar event links. Those are **not automatically website embed modules**.

### Recommended proof of concept
1. Authorized ICMC MasjiDal admin verifies the listing, opens **Integrations → Widgets**, previews all six prayer layout options, and publishes one. Do not share frontend or server keys in chat.
2. In a temporary development branch, insert the widget loader once and the portal-provided prayer widget snippet. Register the actual GitHub Pages hostname as an allowed frontend-key domain.
3. Compare Grid, Table, Compact, and Minimal Bar for homepage and Prayer & Worship pages; test desktop/mobile, prayer start vs iqamah, Jumu'ah, loading, errors and display updates.
4. Separately test the **monthly timetable** link/embed. Preserve the existing official PDF as a fallback until it works reliably.
5. Keep **Pages CMS announcements** authoritative for the website unless ICMC explicitly adopts MasjiDal for announcements; avoid duplicate entry and conflicting schedules.
6. Document webhook/JS event hook availability as **unknown** pending confirmation from MasjiDal support (`masjidsupport@masjidal.com`). Don't promise event callbacks without an official contract.
7. If the widget cannot meet design/accessibility requirements, request API access via an authorized ICMC admin and compare server-side scheduled JSON generation in GitHub Actions against the native embed. Never expose `msj_sk_` to browser code.

### Decision criteria
Accuracy against the existing MasjiDal schedule, usability/accessibility, refresh behavior, domain authorization, free vs Professional features, failure-mode messaging, and ease of operation by ICMC after a fork.
