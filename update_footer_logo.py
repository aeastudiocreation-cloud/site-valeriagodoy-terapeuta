import glob
import re

def fix_file(f):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception:
        return
    
    # 1. Colorize the social media icons
    # Facebook
    content = content.replace(
        '<li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"',
        '<li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem; color: #1877F2; text-decoration: none; font-weight: 500;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"'
    )
    # Instagram
    content = content.replace(
        '<li><a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"',
        '<li><a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem; color: #E1306C; text-decoration: none; font-weight: 500;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"'
    )
    
    # 2. Change the footer logo
    # The footer logo is inside `<footer class="footer">` which has `<div class="footer__grade">`
    # Let's just use regex to replace logo-valeria.webp with logo.png ONLY in the footer.
    
    # Find the footer section
    if '<footer' in content:
        parts = content.split('<footer', 1)
        footer_html = '<footer' + parts[1]
        footer_html = footer_html.replace('logo-valeria.webp', 'logo.png')
        content = parts[0] + footer_html
    
    try:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception:
        pass

for f in glob.glob('build/**/*.html', recursive=True):
    fix_file(f)
fix_file('04-referencia-visual/home.html')
print('Done!')
