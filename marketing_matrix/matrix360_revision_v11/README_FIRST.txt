Matrix 360 Lakhotia — Creative Revision Workspace v1.1

THIS IS A LOCAL OFFLINE MANUAL-REVISION UPGRADE. IT IS NOT AN AI REVISION AGENT.

INSTALL ON WINDOWS
1. Back up your existing lakhotia_agentic_pilot/data folder (including pilot.sqlite3) separately.
2. Stop Uvicorn with Ctrl+C.
3. Extract this ZIP.
4. Copy install_revision_v11.py and upgrade_files folder into your existing lakhotia_agentic_pilot folder (beside app.py). Do NOT replace app.py or data manually.
5. In Command Prompt from lakhotia_agentic_pilot run: python install_revision_v11.py
6. Restart: python -m uvicorn app:app --reload --host 127.0.0.1 --port 8001
7. Open http://127.0.0.1:8001/revisions/f30b6072-a93f-4f39-a4e9-98b5875d4962/2
   Use another valid draft ID if needed.

WORKFLOW
- Opens existing Option 2, automatically fills headline, subheadline, caption and CTA.
- Previous recorded revision feedback is loaded for convenience.
- Change text fields manually; click Generate new PNG version.
- Each version gets a separate rendered PNG; the original file remains unchanged.
- New revisions require their own approval before ZIP export.
- Review UI links to the revision workspace; duplicate identical consecutive review submissions are suppressed.
- An edited title may not visually affect image templates that place other content differently. Check previews before approving.

LIMITATIONS AND CAUTIONS
- Does not use an OpenAI API key. AI rewriting and AI image editing are NOT included yet.
- Only text content is editable via this form. Layout/photo/logo changes require future renderer capabilities or an authorized editing workflow.
- Local reviewer names are not authenticated; approval is only a prototype test.
- Do NOT publish generated proofs to client channels as-is.
- Existing legacy batch-approval endpoints remain; use version-specific package controls for versioned workflow.
- Duplicate prevention only suppresses identical consecutive decisions, not all historical duplicates.
- No scheduled posting, publishing or ad spending.
- Installer backs up modified app.py/review_addon.py and does not overwrite the existing database or renders.
