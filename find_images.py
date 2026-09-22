import glob, re
html_files = glob.glob('build/**/*.html', recursive=True)
images = set()
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        for match in re.findall(r'<img[^>]+src="([^"]+)"', content):
            images.add(match)
        for match in re.findall(r'background(?:-image)?:\s*url\([\'"]?([^\'")]+)[\'"]?\)', content):
            images.add(match)

for img in sorted(images):
    print(img)
