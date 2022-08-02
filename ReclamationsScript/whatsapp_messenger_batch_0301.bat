@echo off
SET logfile="C:\Users\Administrateur\Desktop\Scripts\ReclamationsScript\logs\whatsapp_messenger.log"
"C:\ProgramData\Anaconda3\python.exe" "C:\Users\Administrateur\Desktop\Scripts\ReclamationsScript\Whatsapp_messenger.py" >> %logfile%
quit