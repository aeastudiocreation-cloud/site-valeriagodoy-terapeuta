import json

log_file = r'C:\Users\aline\.gemini\antigravity-ide\brain\c3c2de86-120f-435a-87de-ce1ff01f346b\.system_generated\logs\transcript_full.jsonl'
target = 'build/index.html'

found = False
for line in reversed(list(open(log_file, 'r', encoding='utf-8'))):
    try:
        data = json.loads(line)
        if data.get('type') == 'TOOL_RESPONSE' and data.get('source') == 'SYSTEM':
            content = data.get('content', '')
            if 'Showing lines 1 to 418' in content and 'File Path:' in content and 'build/index.html' in content:
                found = True
                print("Found target response!")
                lines = content.split('\n')
                file_lines = []
                started = False
                for l in lines:
                    if l.startswith('1: '): started = True
                    if l.startswith('The above content shows'): break
                    if started:
                        idx = l.find(': ')
                        if idx != -1: file_lines.append(l[idx+2:])
                
                recovered = '\n'.join(file_lines)
                
                old_design = '        <div class="hero__retrato"><img src="/assets/img/valeria-godoy.webp" alt="Consultório Valéria Godoy" style="width:100%; height:100%; object-fit:cover;"></div>\n        <div class="hero__selo">'
                new_design = '      <div style="position: relative; z-index: 1;">\n        <div style="position: absolute; inset: 0; background: var(--ouro-grad); transform: translate(12px, 12px); border-radius: var(--r-lg); z-index: 0; opacity: 0.8; box-shadow: var(--sombra-1);"></div>\n        <div class="hero__retrato" style="position: relative; z-index: 1; border: 6px solid #fff; box-shadow: var(--sombra-2);"><img src="/assets/img/valeria-godoy.webp" alt="Consultório Valéria Godoy" style="width:100%; height:100%; object-fit:cover;"></div>\n      </div>\n      <div class="hero__selo" style="position: relative; z-index: 2;">'
                recovered = recovered.replace(old_design, new_design)
                
                old_bg = '<section class="wrap bloco" style="background: #D2B48C; padding-inline: var(--e4); max-width: 100%; padding-block: var(--e8);">'
                new_bg = '<section class="wrap bloco bloco--escuro" style="background: sienna; padding-inline: var(--e4); max-width: 100%; padding-block: var(--e8);">'
                recovered = recovered.replace(old_bg, new_bg)
                
                recovered = recovered.replace('card--azul-claro', 'card--bege')
                
                with open('build/index.html', 'w', encoding='utf-8') as f: f.write(recovered)
                with open('04-referencia-visual/home.html', 'w', encoding='utf-8') as f: f.write(recovered)
                print('RECOVERED SUCCESSFULLY')
                break
    except Exception as e:
        print("Error parsing line", e)
if not found:
    print("Not found")
