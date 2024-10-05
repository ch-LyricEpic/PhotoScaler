import os

data__path = 'data.txt'
backup_js_path = 'backup.js'
script_js_path = 'script.js'

with open(data__path, 'r', encoding='gbk') as data_file:
    filenames = [line.strip() for line in data_file if line.strip()]

image_files_js = ',\n        '.join([f"'{filename}'" for filename in filenames])

with open(backup_js_path, 'r', encoding='utf-8') as backup_file:
    backup_content = backup_file.read()

script_content = backup_content.replace('const imageFiles = [];', f'const imageFiles = [\n        {image_files_js}\n    ];')

with open(script_js_path, 'w', encoding='utf-8') as output_file:
    output_file.write(script_content)

print('[WORKFLOW 0003] DONE.')
