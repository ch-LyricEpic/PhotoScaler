import os
from natsort import natsorted
current_directory = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(current_directory+'/assets') if os.path.isfile(os.path.join(current_directory+'/assets', f))]
files = natsorted(files)

print('[WORKFLOW 0002] **Creating Images Path**')

with open('data.txt', 'w') as file:
    for filename in files:
        file.write(filename + '\n')
        
print('[WORKFLOW 0002] **Images Path Created.**')
