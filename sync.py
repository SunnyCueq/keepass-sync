#!/usr/bin/env python3
"""
Cross-Platform Wrapper - führt plattformspezifisches Script aus
"""

import os
import sys
import platform
import subprocess

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    system = platform.system()
    
    # Python-Version bevorzugen (Cross-Platform)
    python_script = os.path.join(script_dir, 'python', 'sync_ftp.py')
    if os.path.exists(python_script):
        try:
            subprocess.run([sys.executable, python_script], check=False)
            return
        except Exception as e:
            print(f"Python-Script konnte nicht ausgeführt werden: {e}")
            print("Fallback zu plattformspezifischem Script...")
    
    # Fallback zu plattform-spezifischen Scripts
    if system == 'Windows':
        # Versuche PowerShell zuerst (moderner)
        ps_script = os.path.join(script_dir, 'windows', 'sync_ftp.ps1')
        if os.path.exists(ps_script):
            try:
                subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', ps_script], check=False)
                return
            except:
                pass
        
        # Fallback zu Batch
        bat_script = os.path.join(script_dir, 'windows', 'sync_ftp.bat')
        if os.path.exists(bat_script):
            subprocess.run([bat_script], check=False)
            return
            
    elif system == 'Darwin':  # macOS
        bash_script = os.path.join(script_dir, 'mac', 'sync_ftp.sh')
        if os.path.exists(bash_script):
            subprocess.run(['bash', bash_script], check=False)
            return
            
    elif system == 'Linux':
        bash_script = os.path.join(script_dir, 'linux', 'sync_ftp.sh')
        if os.path.exists(bash_script):
            subprocess.run(['bash', bash_script], check=False)
            return
    
    print("Fehler: Kein passendes Sync-Script gefunden.")
    print(f"System: {system}")
    print(f"Verzeichnis: {script_dir}")
    sys.exit(1)

if __name__ == '__main__':
    main()

