import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace various encodings of the string
            new_content = content.replace('A&amp;Ä Studio', 'A&amp;A Studio')
            new_content = new_content.replace('A&Ä Studio', 'A&A Studio')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Updated {count} HTML files to fix the A&A Studio name.")
