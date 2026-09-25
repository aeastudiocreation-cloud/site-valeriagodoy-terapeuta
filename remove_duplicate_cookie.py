import os
import re

build_dir = r'c:\Users\aline\OneDrive\Desktop\Site-terapeuta-valeriagodoy\build'

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use regex to remove everything from <style>\r?\n#cookie-consent-banner to the LAST </script>
            new_content = re.sub(r'<style>\r?\n#cookie-consent-banner.*?</script>', '', content, flags=re.DOTALL)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Removed duplicate cookie banner from {count} HTML files.")
