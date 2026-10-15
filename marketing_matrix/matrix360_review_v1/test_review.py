import os, tempfile, shutil, sys
from pathlib import Path
from fastapi.testclient import TestClient
from importlib import import_module
root=Path('/mnt/data/lakhotia_v08_build/test_install')
with tempfile.TemporaryDirectory() as temp:
    d=Path(temp)
    shutil.copy2(root/'app.py',d/'app.py')
    shutil.copy2(root/'engine.py',d/'engine.py')
    shutil.copy2(Path('/mnt/data/lakhotia_v08_build/test_install/creative_renderer_v07.py'),d/'creative_renderer_v07.py')
    shutil.copytree(root/'data',d/'data')
    shutil.copytree(root/'assets',d/'assets')
    shutil.copy2(Path(__file__).parent/'install_review_v1.py',d/'install_review_v1.py')
    shutil.copytree(Path(__file__).parent/'upgrade_files',d/'upgrade_files')
    import subprocess
    x=subprocess.run([sys.executable,str(d/'install_review_v1.py')],capture_output=True,text=True,check=True)
    print(x.stdout.strip())
    sys.path.insert(0,str(d))
    a=import_module('app')
    # Keep tests deterministic, do not invoke generator or network
    from uuid import uuid4
    did=str(uuid4())
    with a.conn() as db:
        payload=[{'option':i,'headline':f'Test {i}','caption':'+91 74500 08999 www.lakhotiaindustrialcomplex.com'} for i in (1,2,3)]
        checks=[{'option':i,'passed':True,'issues':[]} for i in (1,2,3)]
        db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?,?)',(did,'now','Test topic','Awareness','Instagram','review',__import__('json').dumps(payload),__import__('json').dumps(checks)))
    from PIL import Image
    for i in (1,2,3):Image.new('RGB',(1080,1350)).save(d/'data'/'renders'/f'{did}_{i}.png')
    c=TestClient(a.app)
    assert c.get('/api/review-v2/'+did).status_code==200
    assert c.get('/api/review-v2/'+did+'/1/download').status_code==403
    r=c.post('/api/review-v2/'+did+'/1/decision',data={'action':'revision_requested','reviewer':'Tanmayi','feedback':'Increase image prominence'})
    assert r.status_code==200, r.text
    assert 'revision_requested' in r.text
    state=c.get('/api/review-v2/'+did).json();assert len(state['events'])==1
    assert c.get('/api/review-v2/'+did+'/1/download').status_code==403
    r=c.post('/api/review-v2/'+did+'/2/decision',data={'action':'approved','reviewer':'Tanmayi'})
    assert r.status_code==200,r.text
    assert c.get('/api/review-v2/'+did+'/2/download').status_code==200
    assert c.get('/api/review-v2/'+did+'/2/package').status_code==200
    assert c.get('/api/review-v2/'+did+'/1/package').status_code==403
    assert c.get('/review-v2/'+did).status_code==200
    assert c.post('/api/review-v2/'+did+'/3/decision',data={'action':'revision_requested','reviewer':'Tanmayi','feedback':''}).status_code==422
    assert c.post('/api/review-v2/'+did+'/2/decision',data={'action':'rejected','reviewer':'Tanmayi'}).status_code==409
    print('PASS: individual approvals, feedback, immutable events, gated downloads, UI, ZIP export')
