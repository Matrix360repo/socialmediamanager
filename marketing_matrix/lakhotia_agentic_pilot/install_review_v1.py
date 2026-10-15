"""Install additive creative review module without changing drafts database."""
from pathlib import Path
import shutil, datetime, ast
base=Path(__file__).resolve().parent
app=base/'app.py'
source=base/'upgrade_files'/'review_addon.py'
if not app.is_file() or not source.is_file():
    raise SystemExit('ERROR: Put install_review_v1.py and upgrade_files next to app.py.')
code=app.read_text(encoding='utf-8')
marker='from review_addon import router as review_router\napp.include_router(review_router)\n'
if marker not in code:
    updated=code.rstrip()+'\n\n# Matrix360 additive per-creative review module\n'+marker
    ast.parse(updated)
    backup=base/('app_before_review_v1_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'.py')
    shutil.copy2(app,backup)
    app.write_text(updated,encoding='utf-8')
else: print('Review router already linked; app.py unchanged.')
shutil.copy2(source,base/'review_addon.py')
print('SUCCESS: Review v1 installed. Drafts database and rendering files preserved.')
print('Restart server. Open /review-v2/<your-draft-id> to approve individual creatives.')
