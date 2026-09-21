import glob
from bs4 import BeautifulSoup
import re

def main():
    modified_files = 0
    for filepath in glob.glob('build/**/*.html', recursive=True):
        if "test" in filepath.lower(): continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'lxml')
        changed = False
        
        for a in soup.find_all('a', href=True):
            href = a['href']
            
            # If it's an external link or anchor, skip
            if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#'):
                continue
                
            # Internal link that ends with .html
            if href.endswith('.html'):
                # Handle index.html specifically
                if href == 'index.html' or href == '/index.html':
                    a['href'] = '/'
                    changed = True
                else:
                    # Strip .html
                    a['href'] = href[:-5]
                    changed = True
            elif '.html#' in href:
                # Handle cases like sobre.html#team
                parts = href.split('.html#', 1)
                if parts[0] == 'index' or parts[0] == '/index':
                    a['href'] = '/#' + parts[1]
                else:
                    a['href'] = parts[0] + '#' + parts[1]
                changed = True
                
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            modified_files += 1
            
    print(f"Limpeza de links concluída! {modified_files} arquivos modificados.")

if __name__ == "__main__":
    main()
