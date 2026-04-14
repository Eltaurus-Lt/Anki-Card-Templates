@echo off

:: upd epoch
python -c "import time,json,re; f=open('manifest.json','r+'); text=f.read(); man=json.loads(text); man['mod']=int(time.time()); f.seek(0); ind=re.search(r'\n(\s+)\"',text); json.dump(man,f,indent=len(ind.group(1)) if ind else None,ensure_ascii=False); f.truncate(); f.close()"

set zipped="temp.zip"
set "script_name=%~nx0"
set "script_path=%~dp0"

:: remove garbage files
for /d /r %%i in (__pycache__) do (
    if exist "%%i" rd /s /q "%%i"
)
REM if exist "meta.json" del /f /q "meta.json"
if exist "%zipped%" del /f /q "%zipped%"
if exist "%~dp0*.ankiaddon" del "%~dp0*.ankiaddon" /q

:: zip
python -c "import os, zipfile; excl={'meta.json','%script_name%', '%zipped%'}; z=zipfile.ZipFile('%zipped%','w',zipfile.ZIP_DEFLATED); [z.write(p,os.path.relpath(p,'.')) for r,_,fs in os.walk('.') for f in fs if f not in excl for p in [os.path.join(r,f)]]; z.close()"
REM dir /b "%script_path%" | findstr /v /i "%script_name% __pycache__ meta.json %zipped%"' | tar -caf %zipped% --files-from -

:: proper add-on name
python -c "import os, json; os.rename('%zipped%', json.load(open('manifest.json',encoding='utf-8'))['name']+'.ankiaddon')"