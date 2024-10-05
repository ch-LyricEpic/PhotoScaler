import os
from natsort import natsorted
cd = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(cd+'/assets') if os.path.isfile(os.path.join(cd+'/assets', f))]
files = natsorted(files)

print('[WORKFLOW 0002] **Creating Images Path**')

with open('data.txt', 'w') as file:
    for filename in files:
        file.write(filename + '\n')
        
print('[WORKFLOW 0002] **Images Path Created.**')
