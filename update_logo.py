import os
import shutil
import re

src_img = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\06-imagens\NOVA LOGO.jpeg'
dst_img = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\assets\img\logo-nova.jpeg'

# Copy image
shutil.copyfile(src_img, dst_img)
print(f"Copied image to {dst_img}")

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('/assets/img/logo.png', '/assets/img/logo-nova.jpeg')
            new_content = new_content.replace('/assets/img/logo-rodape.jpeg', '/assets/img/logo-nova.jpeg')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Updated {count} HTML files with the new logo.")
