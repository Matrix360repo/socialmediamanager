"""Install v1.2 additive visual direction selector, preserving all stored data."""
from pathlib import Path
import shutil,datetime,ast
base=Path(__file__).resolve().parent
upgrade=base/'upgrade_files'
files=('revision_agent.py','visual_layouts_v12.py')
if not (base/'app.py').is_file() or not (base/'review_addon.py').is_file() or not (base/'creative_renderer_v07.py').is_file():
    raise SystemExit('ERROR: Install alongside existing app.py, review_addon.py and creative_renderer_v07.py')
for name in files:
    src=upgrade/name
    if not src.is_file():raise SystemExit(f'Missing upgrade_files/{name}')
    ast.parse(src.read_text(encoding='utf8'))
for name in files:
    dest=base/name
    if dest.exists():
        suffix=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        shutil.copy2(dest,base/f'{dest.stem}_before_v12_{suffix}.py')
    shutil.copy2(upgrade/name,dest)
print('SUCCESS: Visual revision v1.2 installed; existing drafts and PNGs preserved.')
print('Restart server. Open /revisions/<draft-id>/2 and select Visual design direction.')
