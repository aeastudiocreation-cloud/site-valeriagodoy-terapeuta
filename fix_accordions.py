import os
import glob
import re

def fix_accordions(directory):
    for filepath in glob.glob(directory + '/*.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find alpine accordions
        pattern = r'<div x-data="\{ open: false \}"[^>]*>\s*<button[^>]*><span>(.*?)</span>.*?</button>\s*<div[^>]*>(.*?)</div>\s*</div>'
        
        def replacer(match):
            question = match.group(1)
            answer = match.group(2)
            return f'''<details class="faq">
          <summary>{question}</summary>
          <div>
            <p>{answer}</p>
          </div>
        </details>'''
        
        new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed accordions in {filepath}")

fix_accordions('build/servicos')
fix_accordions('build/blog')
