import glob

def fix_file(f):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception:
        return
    
    # Add icons
    content = content.replace(
        '<li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener">Facebook</a></li>',
        '<li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg> Facebook</a></li>'
    )
    content = content.replace(
        '<li><a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" rel="noopener">Instagram</a></li>',
        '<li><a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg> Instagram</a></li>'
    )
    
    # Fix CTA text block centering
    if '<div style="text-align: center;">' in content and 'Buscar apoio é uma decisão pessoal' in content:
        old_cta = '''<div style="text-align: center;">
        <h2>Vamos conversar sobre o seu momento emocional?</h2>
        <p>Buscar apoio é uma decisão pessoal. Se você deseja conhecer a Terapia TRG, entender como funciona o atendimento ou tirar dúvidas sobre as sessões, Valéria Godoy está disponível para conversar com você.</p>
        <p style="font-size:var(--t-sm);color:rgba(255,255,255,0.9);margin-top:var(--e3)">Entre em contato para consultar horários, condições de atendimento e os próximos passos.</p>
      </div>'''
        new_cta = '''<div style="text-align: center; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
        <h2>Vamos conversar sobre o seu momento emocional?</h2>
        <p style="max-width: 650px;">Buscar apoio é uma decisão pessoal. Se você deseja conhecer a Terapia TRG, entender como funciona o atendimento ou tirar dúvidas sobre as sessões, Valéria Godoy está disponível para conversar com você.</p>
        <p style="font-size:var(--t-sm);color:rgba(255,255,255,0.9);margin-top:var(--e3);max-width: 650px;">Entre em contato para consultar horários, condições de atendimento e os próximos passos.</p>
      </div>'''
        content = content.replace(old_cta, new_cta)
    
    try:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception:
        pass

for f in glob.glob('build/**/*.html', recursive=True):
    fix_file(f)
fix_file('04-referencia-visual/home.html')
print('Done!')
