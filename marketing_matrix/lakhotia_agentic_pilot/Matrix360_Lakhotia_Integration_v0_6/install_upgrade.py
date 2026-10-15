"""Matrix 360 v0.6 installation: preserves existing data/pilot.sqlite3."""
from pathlib import Path
import shutil, py_compile, json, sys
base=Path(__file__).resolve().parent
payload=base/'upgrade_files'
target=base
if not (target/'app.py').exists() or not (target/'data'/'brand_profile.json').exists():
    print('ERROR: Place this installer and upgrade_files folder inside your EXISTING lakhotia_agentic_pilot folder.'); input('Press Enter...'); sys.exit(1)
if not (payload/'app.py').exists():
    print('ERROR: upgrade_files folder is missing.'); input('Press Enter...'); sys.exit(1)
profile=json.loads((payload/'brand_profile.json').read_text(encoding='utf8'))
assert profile['approved_facts']['current_development_bighas']==1000
py_compile.compile(str(payload/'app.py'),doraise=True)
py_compile.compile(str(payload/'engine.py'),doraise=True)
for name in ('app.py','engine.py','requirements.txt'):
    dest=target/name
    if dest.exists(): shutil.copy2(dest,target/(name+'.backup_before_v06'))
    shutil.copy2(payload/name,dest)
(target/'assets').mkdir(exist_ok=True)
shutil.copy2(payload/'lakhotia_group_logo_official.png',target/'assets'/'lakhotia_group_logo_official.png')
shutil.copy2(target/'data'/'brand_profile.json',target/'data'/'brand_profile_backup_before_v06.json')
shutil.copy2(payload/'brand_profile.json',target/'data'/'brand_profile.json')
print('SUCCESS: v0.6 installed. Existing drafts database preserved. Restart server and visit /health and dashboard.')
print('Run: python -m pip install -r requirements.txt')
print('Run: python -m uvicorn app:app --reload --host 127.0.0.1 --port 8001')
input('Press Enter to close...')
