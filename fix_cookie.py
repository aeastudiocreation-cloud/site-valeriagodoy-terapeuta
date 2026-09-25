import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # The JS has: banner.innerHTML = '... <button id="btn-reject-cookies">Recusar</button><button id="btn-accept-cookies">Aceitar</button></div>';
            content = content.replace(
                '<button id="btn-reject-cookies">Recusar</button><button id="btn-accept-cookies">Aceitar</button>',
                '<button id="btn-reject-cookies-novo">Recusar</button><button id="btn-accept-cookies-novo">Aceitar</button>'
            )
            
            content = content.replace("getElementById('btn-accept-cookies')", "getElementById('btn-accept-cookies-novo')")
            content = content.replace("getElementById('btn-reject-cookies')", "getElementById('btn-reject-cookies-novo')")
            content = content.replace("#btn-accept-cookies {", "#btn-accept-cookies-novo {")
            content = content.replace("#btn-reject-cookies {", "#btn-reject-cookies-novo {")
            
            # Break cache again
            content = re.sub(r'style-v2\.css\?v=\d+', 'style-v2.css?v=21', content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print('Done replacing.')
