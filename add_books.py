import os

html_snippet = """  <section class="wrap bloco" id="livros">
    <div class="trilho"><span>Publicações</span></div>
    <h2>Livros da Valéria Godoy</h2>
    <p class="limite">Conheça as obras publicadas que aprofundam a reflexão sobre o autoconhecimento e o cuidado emocional.</p>
    
    <div class="grade grade--2" style="margin-top: var(--e5); gap: 2rem; align-items: stretch;">
      <div style="background: #fff; padding: 2rem; border-radius: var(--r-md); box-shadow: var(--sombra-1); text-align: center; border: 1px solid rgba(0,0,0,0.05);">
        <div style="height: 300px; background: #f0f4f8; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; overflow: hidden;">
          <span style="color: #666; font-size: 0.9rem; padding: 1rem;">(Espaço para imagem do E-book)</span>
        </div>
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--tinta);">[Nome do E-book]</h3>
        <p style="font-size: 0.95rem; color: var(--cinza); margin-bottom: 1.5rem;">Um material digital focado em ajudar no seu desenvolvimento pessoal.</p>
        <a href="#" class="btn btn--primario" style="width: 100%; justify-content: center;">Saiba mais</a>
      </div>

      <div style="background: #fff; padding: 2rem; border-radius: var(--r-md); box-shadow: var(--sombra-1); text-align: center; border: 1px solid rgba(0,0,0,0.05);">
        <div style="height: 300px; background: #f0f4f8; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; overflow: hidden;">
          <span style="color: #666; font-size: 0.9rem; padding: 1rem;">(Espaço para imagem do Livro Físico)</span>
        </div>
        <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem; color: var(--tinta);">[Nome do Livro]</h3>
        <p style="font-size: 0.95rem; color: var(--cinza); margin-bottom: 1.5rem;">Aprofunde ainda mais seus conhecimentos com a obra física.</p>
        <a href="#" class="btn btn--primario" style="width: 100%; justify-content: center;">Saiba mais</a>
      </div>
    </div>
  </section>

"""

files_to_update = [
    'build/index.html',
    '04-referencia-visual/home.html'
]

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We insert right before `<section class="wrap bloco">\n    <div class="duas-colunas" style="align-items: center;">\n      <div>\n        <div class="trilho"><span>Atendimento</span></div>`
        target_marker = '  <section class="wrap bloco">\n    <div class="duas-colunas" style="align-items: center;">\n      <div>\n        <div class="trilho"><span>Atendimento</span></div>'
        
        if target_marker in content:
            new_content = content.replace(target_marker, html_snippet + target_marker)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath} successfully.")
        else:
            print(f"Target marker not found in {filepath}!")
