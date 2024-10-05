import os
import re
print ('[WORKFLOW 0001] **Handling Images ID Conflict.**')
cd = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(cd, 'assets')
pattern = re.compile(r'(\d+)-(.*)\.(\w+)$')
files = os.listdir(folder_path)
file_info = []
unlabeled_files = []

for file_name in files:
    match = pattern.match(file_name)
    if match:
        file_id = int(match.group(1)) 
        description = match.group(2)   
        file_format = match.group(3)   
        file_info.append((file_id, description, file_format, file_name))
    else:
        if (file_name == 'assetsDescription') == 0:
            unlabeled_files.append(file_name)
        
file_info.sort(key=lambda x: x[0])

for i in range(len(file_info)):
    new_id = i + 1
    file_info[i] = (new_id, file_info[i][1], file_info[i][2], file_info[i][3])

next_id = len(file_info) + 1

for file_name in unlabeled_files:
    name, file_format = os.path.splitext(file_name)
    file_format = file_format[1:]
    file_info.append((next_id, name, file_format, file_name))
    next_id += 1

for file_id, description, file_format, old_name in file_info:
    new_name = f"{file_id}-{description}.{file_format}"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"[WORKFLOW 0001] Renamed: {old_name} -> {new_name}")

print("[WORKFLOW 0001] **ID Conflict Handled.**")
