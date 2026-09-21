import sys

files = [
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build\index.html',
    r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\04-referencia-visual\home.html'
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Section 4 (Benefícios e diferenciais)
    s4_start = content.find('<section class="wrap bloco">\n    <div class="trilho"><span>Benefícios e diferenciais</span></div>')
    if s4_start == -1:
        print("S4 not found in " + path)
        continue
    s4_end = content.find('  </section>', s4_start) + len('  </section>')

    # Find Section 5 (Quem somos)
    s5_start = content.find('<section class="wrap bloco bloco--escuro" style="background: sienna;', s4_end)
    if s5_start == -1:
        print("S5 not found in " + path)
        continue
    s5_end = content.find('  </section>', s5_start) + len('  </section>')

    # Extract sections
    s4_content = content[s4_start:s4_end]
    s5_content = content[s5_start:s5_end]

    # Reconstruct
    before = content[:s4_start]
    # between is whatever whitespace exists between s4 and s5
    between = content[s4_end:s5_start]
    after = content[s5_end:]

    # Since S5 is originally after S4, when we swap, S5 comes first, then between, then S4.
    new_content = before + s5_content + between + s4_content + after

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Swapped successfully")
