# Creator Spark Registry

Micro-CRM for tracking which creators to cheer on. Keeps a lightweight JSON ledger so you never lose track of promising leads from late-night scroll sessions.

## Features
- Append new creators with heat scores, notes, and platform context.
- Fast agenda view that bubbles up who has not been boosted recently.
- Summary stats for a quick pulse (average heat, hottest lead, most stale relationship).
- Plain Python 3.11 script, no third-party dependencies.

## Quick start
```bash
cd projects/nightly/2026-02-13-creator-spark-registry
python3 analyzer.py summary       # Overview snapshot
python3 analyzer.py list --sort staleness --limit 5
python3 analyzer.py agenda --window 7
python3 analyzer.py add @newhandle TikTok "mini vlogs" "Hooks audience on calm B-roll" 0.81
python3 analyzer.py boost @fjordsketch --note "commented + shared reels"
```

### Data format
Creators are stored in `creators.json`. Each record contains:
- `handle` – social handle (prefixed with `@`)
- `platform` – e.g. X, YouTube, TikTok
- `category` – what they publish
- `note` – why they’re interesting / what to do next
- `heat` – float between 0 and 1
- `last_seen`, `last_boosted` – ISO dates (auto-managed by the CLI)

Feel free to edit `creators.json` manually or keep everything inside the CLI.
