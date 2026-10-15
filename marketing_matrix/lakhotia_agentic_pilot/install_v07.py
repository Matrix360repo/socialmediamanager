from pathlib import Path
import shutil,py_compile,sys
base=Path(__file__).resolve().parent
original=base/'engine.py'
add=base/'upgrade_files'/'engine_v07.py'
asset=base/'upgrade_files'/'consultation_reference.png'
if not original.exists() or not add.exists() or not asset.exists():
    print('ERROR: Keep install_v07.py and upgrade_files alongside your existing engine.py');sys.exit(1)
code=original.read_text(encoding='utf8')
if 'def render_card_v07' in code:
    print('Already upgraded; no changes made.');sys.exit(0)
if 'def render_card(' not in code:
    print('ERROR: Existing engine.py lacks expected render_card function; no changes made.');sys.exit(1)
# Retain content_create and verify; route render_card to new module.
patch='\n\nfrom creative_renderer_v07 import render_card_v07\nrender_card = render_card_v07\n'
shutil.copy2(original,base/'engine_backup_before_v07.py')
shutil.copy2(add,base/'creative_renderer_v07.py')
(base/'assets').mkdir(exist_ok=True)
shutil.copy2(asset,base/'assets'/'consultation_reference.png')
original.write_text(code+patch,encoding='utf8')
try:
    py_compile.compile(str(original),doraise=True)
    py_compile.compile(str(base/'creative_renderer_v07.py'),doraise=True)
except Exception:
    shutil.copy2(base/'engine_backup_before_v07.py',original)
    raise
print('SUCCESS: v0.7 visual renderer installed. Existing app.py and data/pilot.sqlite3 untouched.')
print('Restart: python -m uvicorn app:app --reload --host 127.0.0.1 --port 8001')
