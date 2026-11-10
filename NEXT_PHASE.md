# Resync-ICMC — Next Phase Action Plan (Phase 5)

**Status:** Investigation and planning; do not mark integrations completed until verified.  
**Repository rename:** Rename `Swipeleft-ICMC` to `Resync-ICMC` in GitHub repository **Settings → General → Repository name → Rename**. GitHub Pages paths and any external links may need to be reconfigured; audit them after rename. The GitHub connector cannot perform repository renames.

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
- [ ] GitHub owner manually renames `Swipeleft-ICMC` → `Resync-ICMC`.
- [ ] Update repository badges/links, README, workflow paths, `site.js` references, `.pages.yml` settings and any hardcoded `/Swipeleft-ICMC/` base URLs.
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
