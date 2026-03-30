# Session Status — March 30, 2026

## Branch Status
- **Branch:** `security/audit-fixes`
- **Remote:** `origin/security/audit-fixes` — up to date
- **Working tree:** clean
- **Upstream issue:** [#271 — Security: World-readable session files, input validation gaps, and information leakage](https://github.com/stickerdaniel/linkedin-mcp-server/issues/271)

## LinkedIn MCP Server
- **Session:** saved at `~/.linkedin-mcp/profile/` (persists across restarts)
- **Authenticated user:** `itayshmool` (https://www.linkedin.com/in/itayshmool/)
- **Server status:** stopped (restart with `uv run -m linkedin_mcp_server`)
- **Browser:** Chromium headless — stopped cleanly

## LinkedIn Profile Audit (Completed)
Pulled full profile via `get_person_profile` with sections: experience, education, interests, honors, languages, contact_info, posts.

### Quick Wins Identified
| # | Fix | Status |
|---|-----|--------|
| 1 | Fix "Computer sicence" typo in Education | Pending (manual) |
| 2 | Add English + Hebrew to Languages | Pending (manual) |
| 3 | End-date QA role, deduplicate VP entries | Pending (manual) |
| 4 | Add modern skills, pin top 3 | Pending (manual) |
| 5 | Add zero2claude.dev link to About section | Pending (manual) |

Note: LinkedIn MCP is read-only. All profile edits must be done manually on linkedin.com.

### Posts Analytics Summary
- Top performer: Course launch post — 19,912 impressions, 234 reactions, 61 comments
- Average engagement rate: ~1.2%
- Key insight: Hebrew-first bilingual posts outperform English-only by ~2x

## Content Strategy (Completed)

### Google Doc
https://docs.google.com/document/d/1es3rq5pEc7y-zgA_-Qy99zj1xiqMw1YycuZK7KPgABQ/edit

### What It Contains
- 3 content pillars (Thought Leadership, zero2claude, Wix Inside)
- Language strategy (Hebrew-first bilingual for Pillars A/B, English for C)
- Post format rules (LinkedIn + Twitter/X)
- 4-week posting schedule (3x/week: Sun, Tue, Thu at 8:30 AM Israel time)
- 12 full post drafts with LinkedIn AND Twitter versions
- Engagement rules
- Metrics tracking targets
- First comment templates with UTM links

### Posting Schedule
| Date | Post | Pillar | Status |
|------|------|--------|--------|
| Thu Mar 27 | "3 Levels of AI Adoption" | A | POSTED (LinkedIn + Twitter) |
| Sun Mar 30 | "Non-Dev Student Story" | B | Ready |
| Tue Apr 1 | "Payments at Scale + Hiring" | C | Ready |
| Thu Apr 3 | "AI-Native Developers" | A | Ready |
| Sun Apr 6 | "Peer Help Feature" | B | Ready |
| Tue Apr 8 | "I Stopped Reviewing PRs" | A | Ready |
| Thu Apr 10 | "Team Spotlight Engineer" | C | Ready (needs engineer name) |
| Sun Apr 13 | "The Genie Shipped 12 Features" | B | Ready (update stats) |
| Tue Apr 15 | "MCP Servers = New APIs" | A | Ready |
| Thu Apr 17 | "2-Month Retrospective" | B | Ready (replace X/Y placeholders) |
| Sun Apr 20 | "14 Years at Wix" | C | Ready |
| Tue Apr 22 | "FAQ Roundup / AMA" | A | Ready |

### Calendar Events
- 12 events created on `itays@wix.com` (primary Wix calendar)
- Each event at 8:30 AM Israel time with full draft, checklist, and hashtags

## Global Config
- LinkedIn username added to `~/.claude/CLAUDE.md` under "User Info"

## To Resume
```bash
# Start LinkedIn MCP server
uv run -m linkedin_mcp_server

# Or with visible browser
uv run -m linkedin_mcp_server --no-headless
```
