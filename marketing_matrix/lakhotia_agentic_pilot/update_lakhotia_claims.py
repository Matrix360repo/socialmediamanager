from pathlib import Path
import shutil, sys
folder=Path(__file__).resolve().parent
app=folder/'app.py'
if not app.exists():
    print('ERROR: app.py not found in this folder. Put this script next to app.py.');input('Press Enter to close...');sys.exit(1)
s=app.read_text(encoding='utf-8')
old="if re.search(r'\\b(?:800|1,?000)\\s*bighas\\b',txt,re.I): issues.append('Area figure requires approval')"
new="if re.search(r'\\b800\\s*bighas\\b',txt,re.I): issues.append('Outdated claim: 800 bighas is prohibited; approved current development is 1,000 bighas')"
if old not in s:
    if new in s:
        print('Already updated; no changes needed.');input('Press Enter to close...');sys.exit(0)
    print('STOP: expected code line not found. No changes made. Share this message for review.');input('Press Enter to close...');sys.exit(2)
backup=folder/'app_before_claims_update.py'
if backup.exists():
    print('STOP: backup file already exists. No changes made to prevent overwriting it.');input('Press Enter to close...');sys.exit(3)
shutil.copy2(app,backup)
s=s.replace(old,new,1)
s=s.replace('Area claim conflict: 800 vs 1,000 bighas requires owner confirmation. Logo and artwork master assets required for production-quality rendering.','Approved current development: 1,000 bighas. Planned amenities require verification before operational claims. Logo and artwork master assets required for production-quality rendering.')
app.write_text(s,encoding='utf-8')
print('SUCCESS: app.py updated. Backup: app_before_claims_update.py')
print('NOTICE: This updates brand claims only. The API is NOT ready for public deployment; authentication is still required.')
input('Press Enter to close...')
