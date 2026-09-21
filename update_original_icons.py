import glob
import re

facebook_old_svg = r'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"[^>]*><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>'
facebook_new_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="12" fill="#1877F2"/><path d="M15.36 12l.66-4.29h-4.09V4.93c0-1.18.57-2.32 2.42-2.32h1.87V-.25A22.8 22.8 0 0 0 13 0c-3.27 0-5.41 1.98-5.41 5.56v2.15H4v4.29h3.59v10.4c1.32.21 2.67.21 4 0V12h3.77z" fill="white"/></svg>'

instagram_old_svg = r'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"[^>]*><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'
instagram_new_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="2" width="20" height="20" rx="5" fill="url(#ig-grad)"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" stroke="white" stroke-width="2" fill="none"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke="white" stroke-width="2"/><defs><linearGradient id="ig-grad" x1="2" y1="22" x2="22" y2="2" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f09433"/><stop offset="0.3" stop-color="#e6683c"/><stop offset="0.6" stop-color="#dc2743"/><stop offset="0.8" stop-color="#cc2366"/><stop offset="1" stop-color="#bc1888"/></linearGradient></defs></svg>'

def fix_file(f):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception:
        return
        
    # Replace Facebook SVG
    content = re.sub(facebook_old_svg, facebook_new_svg, content)
    # Remove text color from Facebook link
    content = content.replace('color: #1877F2;', '')
    
    # Replace Instagram SVG
    content = re.sub(instagram_old_svg, instagram_new_svg, content)
    # Remove text color from Instagram link
    content = content.replace('color: #E1306C;', '')
    
    try:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception:
        pass

for f in glob.glob('build/**/*.html', recursive=True):
    fix_file(f)
fix_file('04-referencia-visual/home.html')
print('Done!')
