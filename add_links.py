import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

# File 1: o-que-e-terapia-trg.html
path1 = os.path.join(build_dir, 'blog', 'o-que-e-terapia-trg.html')
with open(path1, 'r', encoding='utf-8') as f:
    content1 = f.read()

# Add link
old_text1 = 'como traumas, fobias, compulsões, depressão e ansiedade.'
new_text1 = 'como <a href="/blog/terapia-trg-para-traumas" style="text-decoration: underline;">traumas</a>, fobias, compulsões, depressão e ansiedade.'
if old_text1 in content1:
    content1 = content1.replace(old_text1, new_text1)
    with open(path1, 'w', encoding='utf-8') as f:
        f.write(content1)
    print('Updated link in o-que-e-terapia-trg.html')

# File 2: terapia-trg-para-ansiedade.html
path2 = os.path.join(build_dir, 'blog', 'terapia-trg-para-ansiedade.html')
with open(path2, 'r', encoding='utf-8') as f:
    content2 = f.read()

# Add link
old_text2 = 'Se você sente que as suas reações diante de medos ou ansiedades'
new_text2 = 'Se você sente que as suas reações diante de <a href="/blog/terapia-trg-para-traumas" style="text-decoration: underline;">medos ou traumas passados</a>'
if old_text2 in content2:
    content2 = content2.replace(old_text2, new_text2)
    with open(path2, 'w', encoding='utf-8') as f:
        f.write(content2)
    print('Updated link in terapia-trg-para-ansiedade.html')
else:
    # Try another generic insertion
    old_text2_alt = 'O cérebro muitas vezes mantém o "sinal de alerta" ligado mesmo quando não há um perigo real e imediato.'
    new_text2_alt = 'O cérebro muitas vezes mantém o "sinal de alerta" ligado mesmo quando não há um perigo real e imediato, funcionando de forma muito parecida com o que vemos na <a href="/blog/terapia-trg-para-traumas" style="text-decoration: underline;">Terapia TRG para traumas</a>.'
    if old_text2_alt in content2:
        content2 = content2.replace(old_text2_alt, new_text2_alt)
        with open(path2, 'w', encoding='utf-8') as f:
            f.write(content2)
        print('Updated link in terapia-trg-para-ansiedade.html (alt)')
