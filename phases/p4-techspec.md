# PSI Phase 4: Engineering Spec

**Goal:** Define the complete technical architecture for the approved V1 feature list.
The agent generates this — no interview questions needed unless a critical decision is ambiguous.

**Output file:** `docs/TechDesign-[AppName]-MVP.md`

---

## Research Requirements

Before writing: use real tool calls to research current best practices, actual library docs, and
live pricing pages. Do not rely on prior knowledge for stack recommendations. If you cite a
framework benchmark or pricing number, it must come from a fetched page.

---

## What to Produce

Write `docs/TechDesign-[AppName]-MVP.md` with all of the following sections:

```markdown
# Tech Design: [AppName] MVP
**Version:** 1.0  |  **Updated:** [Date]  |  **Status:** Approved — Phase 4

---

## System Architecture
[Stack overview: frontend, backend, database, hosting, third-party APIs]

For each choice, include:
- What it is
- Why this over alternatives (link to benchmark or doc you actually fetched)
- Any known limitations for this use case

## Non-Functional Requirements

| Requirement | Target | How Verified |
|------------|--------|-------------|
| Page load time | < [X]s on 4G | Lighthouse / WebPageTest |
| API response time | < [X]ms at p95 | Load test |
| Auth security | JWT with [expiry / refresh policy] | Code review |
| Accessibility | WCAG 2.1 AA | axe audit / manual |
| Uptime | [X]% | Uptime monitor |
| Data retention | [X days/years] | DB policy configuration |
| Compliance | [GDPR / HIPAA / N/A] | Checklist |
| Scalability | [X concurrent users without degradation] | Load test |

## Database Schema
```sql
-- Full table definitions for all V1 Must-Have features
-- Include relationships, indexes, and constraints
-- V2 tables are NOT included here
```

## Core API Endpoints

| Method | Path | Description | Auth Required | Request Body | Response |
|--------|------|-------------|--------------|-------------|---------|
| POST | /api/... | ... | Yes / No | { ... } | { ... } |

## Edge Cases & Failure Modes

| Scenario | Likelihood | Technical Behavior | User-Facing Message |
|----------|------------|-------------------|-------------------|
| External API down | Med | [Retry logic / fallback] | [What user sees] |
| DB write fails | Low | [Retry / queue] | [What user sees] |
| Auth token expired | High | [Auto-refresh flow] | [Transparent to user] |
| Empty state | High | [Graceful empty state] | [Empty state copy] |
| Rate limit hit | Med | [Queue or throttle] | [What user sees] |

## Test & Verification Plan

Core acceptance criteria tests (from PRD Given-When-Then):
- [ ] [Feature 1]: Given [state], When [action], Then [outcome] — **PASS / FAIL**
- [ ] [Feature 2]: Given [state], When [action], Then [outcome] — **PASS / FAIL**
- [ ] Core user journey works end-to-end without errors
- [ ] Primary success metric tracking is live and recording

## Tech Stack Setup

**Framework initialization:**
1. Run `npx -y [framework]@latest --help` first to inspect available flags and confirm current CLI interface
2. Then: `npx -y [framework]@latest ./ [verified flags from --help output]`

**Why this framework:** [Rationale — link to benchmark or comparison doc you actually fetched]

**Key dependencies:**
| Package | Version | Purpose | Docs |
|---------|---------|---------|------|
| ... | ... | ... | [fetched link] |

## Deployment Checklist

- [ ] All environment variables configured (see .env.local section below)
- [ ] Database migrations applied and verified
- [ ] Auth flow tested end-to-end (sign up, sign in, sign out, token refresh)
- [ ] Production build verified locally (`npm run build` / equivalent)
- [ ] Hosting provider configured — [Provider] ([fetched pricing link])
- [ ] Domain / DNS configured and propagated
- [ ] Error monitoring configured — [Provider, e.g., Sentry free tier] ([fetched link])
- [ ] Success metric instrumentation live — [Tool, e.g., Posthog] ([fetched link])
- [ ] Core user journey manually tested in production environment
- [ ] **Rollback plan:** [Exactly how to revert if production breaks — specific commands or steps]

## Environment Variables (.env.local)

- [ ] `DATABASE_URL` — [where to get it, link to provider dashboard]
- [ ] `[AUTH_PROVIDER]_SECRET` — [where to get it]
- [ ] `[SERVICE]_API_KEY` — [where to get it]
- [ ] `[SERVICE]_WEBHOOK_SECRET` — [where to get it]

Never commit this file. Add `.env.local` to `.gitignore` before first commit.

## Monthly Cost Estimate (MVP Scale — 0 to 100 users)

| Service | Free Tier Limit | Paid Tier Cost | Source |
|---------|----------------|---------------|--------|
| [Hosting] | [Free tier specs] | $X/mo | [fetched pricing link] |
| [Database] | [Free tier specs] | $X/mo | [fetched pricing link] |
| [Auth] | [Free tier specs] | $X/mo | [fetched pricing link] |
| [Other] | [Free tier specs] | $X/mo | [fetched pricing link] |
| **Total** | — | **$X–$Y/mo** | — |

**At growth scale (1k users):** $X–$Y/mo — [brief explanation of which line items scale]
```

---

## 🛑 Phase 4 Gate

Present `docs/TechDesign-[AppName]-MVP.md` to the user:

> "Engineering Spec is complete. Review it — anything you want to change before we lock in and
> start the build plan?
> Approve and I'll generate the AGENTS.md handoff so you can start coding."

---

## ➡️ After Phase 4 Approval

Read the Phase 5 file and begin immediately:
> `Read: c:\Users\henry\Desktop\Agentic workflows\.agents\skills\vibe-psi\phases\p5-build.md`
