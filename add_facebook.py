import os

footer_add = """      <div>
        <h4>Redes Sociais</h4>
        <ul class="footer__lista">
          <li><a href="https://www.facebook.com/valeriagodoy.terapeuta" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>"""

build_dir = "c:/Users/aline/OneDrive/Desktop/Site-terapeuta-valeriagodoy/build"

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find a consistent anchor point to inject the new column
            target = "        </ul>\n      </div>\n\n      </div>"
            
            if target in content:
                new_content = content.replace(target, "        </ul>\n      </div>\n\n" + footer_add + "\n\n      </div>")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {path}")
            else:
                print(f"Could not find target in {path}")

print(f"Total updated: {count}")
