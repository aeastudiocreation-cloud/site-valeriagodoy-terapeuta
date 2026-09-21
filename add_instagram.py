import os

instagram_link = '          <li><a href="https://www.instagram.com/valeriagodoyterapeuta/" target="_blank" rel="noopener">Instagram</a></li>'

build_dir = "c:/Users/aline/OneDrive/Desktop/Site-terapeuta-valeriagodoy/build"

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            target = '<li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener">Facebook</a></li>'
            
            if target in content:
                new_content = content.replace(target, target + "\n" + instagram_link)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {path}")
            else:
                print(f"Could not find target in {path}")

print(f"Total updated: {count}")
