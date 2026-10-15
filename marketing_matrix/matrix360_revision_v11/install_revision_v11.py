"""Install additive v1.1 revision workspace alongside review-v2."""
from pathlib import Path
import shutil,ast,datetime
base=Path(__file__).resolve().parent
app=base/'app.py';src=base/'upgrade_files'/'revision_agent.py';dest=base/'revision_agent.py'
if not (app.is_file() and src.is_file() and (base/'review_addon.py').is_file()):
    raise SystemExit('ERROR: Put installer and upgrade_files alongside app.py; install review v1.0 first.')
marker='from revision_agent import router as revision_router\napp.include_router(revision_router)'
code=app.read_text(encoding='utf-8')
new=code if marker in code else code.rstrip()+'\n\n# Matrix360 local creative revision versioning v1.1\n'+marker+'\n'
ast.parse(new)
if dest.exists():
    shutil.copy2(dest,base/('revision_agent_backup_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'.py'))
if new!=code:
    shutil.copy2(app,base/('app_before_revision_v11_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'.py'))
shutil.copy2(src,dest)
if new!=code:app.write_text(new,encoding='utf-8')
# Add a discovery link on the existing review screen without modifying existing approvals.
review=base/'review_addon.py'
old=review.read_text(encoding='utf-8')
needle="dl=f'<a href="
if 'Open revision workspace' not in old and needle in old:
    old=old.replace("parts.append(f'''<article>","dl+=f' · <a href=\"/revisions/{escape(draft_id)}/{opt}\">Open revision workspace</a>'\n        parts.append(f'''<article>")
    ast.parse(old)
    shutil.copy2(review,base/('review_addon_before_revision_v11_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'.py'))
    review.write_text(old,encoding='utf-8')
# Prevent accidental consecutive duplicate reviews on the same option.
if 'Duplicate review request ignored' not in old:
    needle="        count=db.execute('SELECT COALESCE(MAX(version),0) FROM creative_events"
    if needle in old:
        inject="""        prior=db.execute('SELECT action, reviewer, feedback FROM creative_events WHERE draft_id=? AND option_no=? ORDER BY event_id DESC LIMIT 1',(draft_id,option)).fetchone()
        if prior and prior['action']==action and prior['reviewer']==reviewer.strip() and prior['feedback']==feedback.strip():
            db.commit()
            return {'draft_id':draft_id,'option':option,'status':action,'deduplicated':True,'message':'Duplicate review request ignored'}
"""
        old=old.replace(needle,inject+needle)
    if old!=review.read_text(encoding='utf-8'):
        ast.parse(old)
        review.write_text(old,encoding='utf-8')
print('SUCCESS: Revision workspace v1.1 installed. Database and original renders preserved.')
print('Restart uvicorn, then open /revisions/<draft-id>/2')
