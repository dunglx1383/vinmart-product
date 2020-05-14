set root=C:\ProgramData\Anaconda3
set local=%CD%
call %root%\Scripts\activate.bat %root%

call %root%\python.exe "%local%\src\main.py"
pause