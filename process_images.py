import os
from PIL import Image, ImageOps

source_dir = '06-imagens'
dest_dir = 'build/assets/img'

mappings = [
    # (Source filename, Destination filename, Max Width, Max Height, Crop)
    ('quem-somos.jpg', 'hero.webp', 900, 1200, True),
    ('WhatsApp Image 2026-09-11 at 14.35.47.jpeg', 'valeria-godoy.webp', 900, 1200, True),
    ('WhatsApp Image 2026-09-11 at 14.50.26.jpeg', 'valeria-godoy-small.webp', 400, 400, True),
    ('ansiedade.jpg', 'blog-1.webp', 1200, 800, True),
    ('homem na cortina.jpg', 'blog-2.webp', 1200, 800, True),
    ('logo valeria.jpeg', 'logo-valeria.webp', 1600, 1093, False), # Keeping it as logo
    ('logo valeria.jpeg', 'favicon.png', 512, 512, True) # Also making a favicon from it
]

for src_name, dest_name, w, h, crop in mappings:
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if not os.path.exists(src_path):
        print(f"Skipping {src_name}, not found.")
        continue
        
    try:
        with Image.open(src_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize
            if crop:
                img = ImageOps.fit(img, (w, h), Image.Resampling.LANCZOS)
            else:
                img.thumbnail((w, h), Image.Resampling.LANCZOS)
                
            # Save
            if dest_name.endswith('.webp'):
                img.save(dest_path, 'WEBP', quality=85)
            elif dest_name.endswith('.png'):
                img.save(dest_path, 'PNG')
            else:
                img.save(dest_path, 'JPEG', quality=85)
                
            print(f"Processed {src_name} -> {dest_name}")
    except Exception as e:
        print(f"Error processing {src_name}: {e}")
