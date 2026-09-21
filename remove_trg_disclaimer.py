import os

build_dir = "c:/Users/aline/OneDrive/Desktop/Site-terapeuta-valeriagodoy/build"
target_text = "      <span>A TRG é abordagem complementar e não substitui tratamento médico ou psicológico.</span>\n"

count = 0
for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if target_text in content:
                new_content = content.replace(target_text, "")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Removed disclaimer from {path}")
            else:
                # Try without the newline just in case
                target_no_nl = "<span>A TRG é abordagem complementar e não substitui tratamento médico ou psicológico.</span>"
                if target_no_nl in content:
                    new_content = content.replace(target_no_nl, "")
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
                    print(f"Removed disclaimer (inline) from {path}")

print(f"Total updated: {count}")
