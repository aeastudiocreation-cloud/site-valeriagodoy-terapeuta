import os
import glob

def fix_files(directory, placeholder):
    for filepath in glob.glob(directory + '/*.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if placeholder in content:
            continue
            
        content = content.replace('<main id="conteudo">\n\n</main>', f'<main id="conteudo">\n{placeholder}\n</main>')
        content = content.replace('<main id="conteudo"></main>', f'<main id="conteudo">\n{placeholder}\n</main>')
        content = content.replace('<main id="conteudo">\n</main>', f'<main id="conteudo">\n{placeholder}\n</main>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

fix_files('build/servicos', '<!-- SERVICO CONTENT HERE -->')
fix_files('build/blog', '<!-- BLOG POST CONTENT HERE -->')
