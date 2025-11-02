#!/usr/bin/env python3
"""
Cross-Platform Installer Wrapper
Ruft python/installer.py auf
"""

import os
import sys
import subprocess

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    installer_path = os.path.join(script_dir, 'python', 'installer.py')
    
    if os.path.exists(installer_path):
        try:
            subprocess.run([sys.executable, installer_path], check=False)
        except Exception as e:
            print(f"Fehler beim Ausführen des Installers: {e}")
            sys.exit(1)
    else:
        print("Fehler: Installer nicht gefunden!")
        print(f"Pfad: {installer_path}")
        sys.exit(1)

if __name__ == '__main__':
    main()

