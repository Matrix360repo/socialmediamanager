"""Matrix 360: portable font path correction for Lakhotia renderer.
Backs up engine.py, updates only the Linux-specific font definitions and validates syntax.
Run from lakhotia_agentic_pilot directory: python fix_lakhotia_fonts.py
"""
from pathlib import Path
import ast
import shutil
import sys

root = Path(__file__).resolve().parent
engine = root / 'engine.py'
if not engine.is_file():
    sys.exit('ERROR: engine.py not found. Place this script alongside app.py and engine.py.')
original = engine.read_text(encoding='utf-8')
old = "FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'\nBOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'"
replacement = '''def _font_path(bold=False):
    """Find an installed font on Windows, Linux or macOS."""
    if os.name == 'nt':
        winfonts = Path(os.environ.get('WINDIR', r'C:\\Windows')) / 'Fonts'
        candidates = ([winfonts / 'arialbd.ttf', winfonts / 'segoeuib.ttf', winfonts / 'calibrib.ttf']
                      if bold else [winfonts / 'arial.ttf', winfonts / 'segoeui.ttf', winfonts / 'calibri.ttf'])
    else:
        candidates = ([Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
                       Path('/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf'),
                       Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf')]
                      if bold else [Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
                                    Path('/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf'),
                                    Path('/System/Library/Fonts/Supplemental/Arial.ttf')])
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError('No supported system font found. Check Windows Fonts installation.')
FONT=_font_path(False)
BOLD=_font_path(True)'''
if '_font_path(bold=False)' in original:
    print('ALREADY PATCHED: portable font selection is present.')
    sys.exit(0)
if original.count(old) != 1:
    sys.exit('ERROR: expected font settings not found exactly once; no files changed. Share the first 20 lines of engine.py.')
updated = original.replace(old, replacement, 1)
ast.parse(updated, filename='engine.py')
backup = root / 'engine_before_font_fix.py'
if backup.exists():
    sys.exit(f'ERROR: backup already exists at {backup.name}. No changes made.')
shutil.copy2(engine, backup)
try:
    engine.write_text(updated, encoding='utf-8')
    ast.parse(engine.read_text(encoding='utf-8'), filename='engine.py')
except Exception:
    shutil.copy2(backup, engine)
    raise
print('SUCCESS: Windows-compatible font paths installed. Backup: engine_before_font_fix.py')
print('NEXT: restart the server and generate a NEW campaign draft.')
