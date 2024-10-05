import subprocess
import os
from pyfiglet import Figlet
f = Figlet(font='standard')
print(f.renderText('PhotoScaler'))
print('===================================================')
print('')
print('Welcome to PhotoScaler LAUNCHER.Lets record your photos.')
print('')

current_dir = os.path.dirname(os.path.abspath(__file__))

scripts = ['_conflictHandler.py', '_getData.py', '_jsBackup-autogeneratejs.py']  # 替换为实际的文件名

for script in scripts:
    script_path = os.path.join(current_dir, script)
    
    if os.path.exists(script_path):
        print(f"[WORKFLOW LAUNCHING]")
        try:
            subprocess.run(['python', script_path], check=True)
            print(f"[WORKFLOW DONE]")
        except subprocess.CalledProcessError as e:
            print(f"[WORKFLOW {script} ERROR: {e}]")
    else:
        print(f"[WORKFLOW {script} MISSING!]")

print(input('ALL WORKFLOW READY.Press Enter to quit the program.'))
