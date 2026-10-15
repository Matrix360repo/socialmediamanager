# Matrix 360 Agentic Marketing OS — Lakhotia Client 001

## What is actually built
- Local dashboard for Lakhotia with a campaign input form and review queue.
- Versioned seed brand profile with a claim-conflict register.
- Generate three **deterministic sample** copy concepts from any topic. This is deliberately **not** a live LLM integration and does not render branded creative images yet.
- Simple compliance checks, explicit human decision, and approved-draft JSON export.
- SQLite data store and REST API to facilitate future n8n integration.
- Uploaded reference image and three original HTML email templates copied into `assets/`.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --host 127.0.0.1 --port 8001
```
Open http://127.0.0.1:8001 ; API docs at http://127.0.0.1:8001/docs.

## API
- `GET /api/brand` approved/pending client memory
- `GET /api/drafts` review queue
- `POST /api/generate` form: topic, objective, platform
- `GET /api/drafts/{id}` review details
- `POST /api/drafts/{id}/decision` form: action, reviewer
- `GET /api/drafts/{id}/export` approved-only JSON

## Next implementations — required before client release
1. Confirm the 800/1000-bigha conflict and amenity statuses; move confirmed claims into approved registry with source/date/version.
2. Obtain original logo, editable creative templates and artwork masters; do not reconstruct exact brand assets from screenshots.
3. Add authenticated login, database tenant isolation and audit-log of reviewers and revisions. Current reviewer is a self-declared local field only.
4. Replace deterministic concept generator with provider-isolated LLM structured JSON generation; store model IDs, tokens, cost and prompt versions.
5. Add template-based, brand-faithful PNG rendering, creative preview and per-candidate approval.
6. Add n8n workflow: new brief → strategy/copy → compliance → approval request → approved asset library. Keep Meta posting/ad spend behind explicit approval.
7. Add scheduling and channel permissions after an integration security review; no bulk unsolicited outreach.
8. Add tenant/client/agent usage ledger for per-client pricing and marginal-cost analysis.

## Source limitation
The linked Drive folder returned only two image files and one video in its current accessible listing. Other user-shared examples were visible in the conversation, but were not all downloadable as files. The included `reference_image.png` is the single image file mounted in this session, not the entire creative library.

## Licensing and safety
Review each public n8n workflow and license before reuse. Never upload confidential lead databases to unapproved AI services. Preserve human approval for marketing claims, ad spend and publication.
