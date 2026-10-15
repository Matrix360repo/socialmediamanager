# Matrix 360 Lakhotia — Review & Revision v1.0 (local MVP)

This additive upgrade retains the existing generation/preview routes and untouched `data/pilot.sqlite3` draft rows. It creates separate `creative_reviews` and `creative_events` tables inside the same SQLite database when first used.

## Install (Windows)
1. Stop uvicorn (`Ctrl+C`). Back up the entire `data` folder separately.
2. Place `install_review_v1.py` and `upgrade_files/` alongside your existing `app.py`.
3. Run `python install_review_v1.py`.
4. Restart with `python -m uvicorn app:app --reload --host 127.0.0.1 --port 8001`.
5. Open `http://127.0.0.1:8001/review-v2/<draft-id>` using a recent draft ID.
6. Choose a decision on a single option. For revision requests, enter feedback. For approval, download the ZIP containing its PNG, caption and metadata.

## Boundaries and safety
- Revision requests are **recorded**, not executed by an AI agent. They do not create new candidate artwork automatically.
- `event_version` indicates decision-log sequence, **not a new image revision**.
- Approval uses a self-declared reviewer name. This is **not suitable for public deployment** or actual client authorization.
- The previous `/api/drafts/{id}/decision` batch approval remains for backward compatibility. Use the **new per-option export** route for selective approval; do not use the old batch export path as a client authorization control.
- No social publishing, ad spend or outbound messaging occurs.
- Avoid putting confidential client data into test briefs.
