MATRIX360 LAKHOTIA VISUAL RENDERER v0.7
=====================================
Development proof package — no publishing, no advertising, no claim of client approval.

HOW TO INSTALL
1. Stop local Python server with Ctrl+C.
2. Copy install_v07.py and upgrade_files/ to the same folder as your existing app.py and engine.py.
3. Run: python install_v07.py
4. Start: python -m uvicorn app:app --reload --host 127.0.0.1 --port 8001
5. Generate a NEW draft and open review page.

WHAT CHANGES
- A photo-led opportunity card, 3-stage decision card, and consultation-led card
- Approved logo is read from assets/lakhotia_group_logo_official.png
- Original consultation reference is included and used as illustrative visual
- Creates three PNG files at 1080x1350
- Existing database and app.py are preserved
- Backup of engine.py created: engine_backup_before_v07.py

LIMITATIONS
- The only available creative photograph is from supplied Lakhotia consultation artwork. It is a reference crop, not a verified project photograph.
- Offline generation still uses deterministic text until AI credentials are configured.
- No n8n Cloud execution, automatic posting, or account authentication is set up by this visual patch.
- Designs are proofs, not ready for publication; check text contrast and all factual claims.
