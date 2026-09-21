import sys

files = [
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\index.html',
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\04-referencia-visual\home.html'
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Section 3 (Serviços)
    s3_start = content.find('<div class="trilho"><span>Serviços</span></div>')
    if s3_start == -1:
        print("S3 not found in " + path)
        continue
    
    # We want to replace inside section 3, so until the next section
    s3_end = content.find('<section', s3_start)
    if s3_end == -1:
        s3_end = len(content)

    s3_content = content[s3_start:s3_end]
    new_s3_content = s3_content.replace('card--bege', 'card--azul-claro')

    new_content = content[:s3_start] + new_s3_content + content[s3_end:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated section 3 successfully")
