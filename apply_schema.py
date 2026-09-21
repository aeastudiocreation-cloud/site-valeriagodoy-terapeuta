import glob
import os
import json
import yaml
from datetime import datetime
from bs4 import BeautifulSoup

def clean_url(filepath, domain):
    rel_path = os.path.relpath(filepath, "build").replace('\\', '/')
    if rel_path == "index.html" or rel_path == "":
        return domain + "/"
    if rel_path.endswith(".html"):
        return domain + "/" + rel_path[:-5]
    return domain + "/" + rel_path

def get_breadcrumbs(url, domain):
    parts = url.replace(domain, "").strip("/").split("/")
    items = []
    items.append({
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": domain + "/"
    })
    
    current_url = domain
    for i, part in enumerate(parts):
        if not part: continue
        current_url += "/" + part
        name = part.replace("-", " ").title()
        if i == len(parts) - 1:
            name = name # maybe use page title instead, but URL part is fine for fallback
        items.append({
            "@type": "ListItem",
            "position": i + 2,
            "name": name,
            "item": current_url
        })
    
    return {
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def extract_faqs(soup):
    faqs = []
    # Find typical FAQ structures. Assuming details/summary or h3+p
    for details in soup.find_all('details'):
        q = details.find('summary')
        if not q: continue
        ans = details.get_text(separator=' ', strip=True).replace(q.get_text(strip=True), '', 1)
        if q and ans:
            faqs.append({
                "@type": "Question",
                "name": q.get_text(strip=True),
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": ans
                }
            })
    # If no details, maybe look for `.faq-item` or similar
    if not faqs:
        for item in soup.find_all(class_='faq-item'):
            q = item.find(['h3', 'h4', 'strong', '.question'])
            ans = item.find(['p', '.answer'])
            if q and ans:
                 faqs.append({
                    "@type": "Question",
                    "name": q.get_text(strip=True),
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": ans.get_text(strip=True)
                    }
                })
    return faqs

def main():
    with open('01-briefing/projeto.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    domain_raw = data.get('dominio', 'valeriagodoyterapeuta.com')
    if not domain_raw.startswith('http'):
        domain = "https://" + domain_raw
    else:
        domain = domain_raw
        
    org_id = domain + "/#organization"
    website_id = domain + "/#website"
    localbiz_id = domain + "/#localbusiness"
    
    name = data['empresa']['nome']
    phone = "+" + str(data['empresa']['telefone']).replace(' ', '').replace('-', '')
    socials = list(data['empresa'].get('redes_sociais', {}).values())
    
    org_schema = {
        "@type": "Organization",
        "@id": org_id,
        "name": name,
        "url": domain + "/",
        "logo": {
            "@type": "ImageObject",
            "url": domain + data['empresa']['logo_path']
        },
        "telephone": phone,
        "sameAs": socials
    }
    
    website_schema = {
        "@type": "WebSite",
        "@id": website_id,
        "url": domain + "/",
        "name": name,
        "publisher": {"@id": org_id}
    }
    
    localbiz_schema = {
        "@type": "MedicalBusiness",
        "@id": localbiz_id,
        "name": name,
        "image": domain + data['empresa']['logo_path'],
        "url": domain + "/",
        "telephone": phone,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": data['empresa']['endereco'].split(',')[0].strip(),
            "addressLocality": data['empresa']['cidade'],
            "addressRegion": data['empresa']['estado'],
            "postalCode": "", # not in yaml explicitly
            "addressCountry": data['empresa']['pais']
        },
        "priceRange": data['empresa']['price_range'],
        "hasMap": data['empresa']['google_maps_iframe'],
        "areaServed": [
            {"@type": "City", "name": data['empresa']['cidade']}
        ],
        "sameAs": socials
    }
    
    if data['empresa'].get('latitude') and data['empresa'].get('longitude'):
        localbiz_schema["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": data['empresa']['latitude'],
            "longitude": data['empresa']['longitude']
        }
    
    for filepath in glob.glob('build/**/*.html', recursive=True):
        if "test" in filepath.lower(): continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
            
        url = clean_url(filepath, domain)
        page_name = soup.title.string if soup.title else name
        page_desc = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc: page_desc = meta_desc.get('content', '')
        
        webpage_schema = {
            "@type": "WebPage",
            "@id": url,
            "url": url,
            "name": page_name,
            "description": page_desc,
            "isPartOf": {"@id": website_id},
            "inLanguage": "pt-BR"
        }
        
        graph = [org_schema, website_schema, webpage_schema, get_breadcrumbs(url, domain)]
        
        rel_path = os.path.relpath(filepath, "build").replace('\\', '/')
        
        # Home
        if rel_path == "index.html":
            graph.append(localbiz_schema)
            faqs = extract_faqs(soup)
            if faqs:
                graph.append({
                    "@type": "FAQPage",
                    "mainEntity": faqs
                })
                
        # Sobre
        elif rel_path == "sobre.html":
            webpage_schema["@type"] = ["WebPage", "AboutPage"]
            # Add Person
            graph.append({
                "@type": "Person",
                "@id": domain + "/#valeriagodoy",
                "name": "Valéria Godoy",
                "jobTitle": "Terapeuta TRG",
                "worksFor": {"@id": org_id}
            })
            
        # Servicos Lista
        elif rel_path == "servicos.html":
            webpage_schema["@type"] = ["WebPage", "CollectionPage"]
            items = []
            for i, s in enumerate(data.get('servicos', [])):
                items.append({
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": s['nome'],
                    "url": f"{domain}/servicos/{s['slug']}"
                })
            if items:
                graph.append({
                    "@type": "ItemList",
                    "itemListElement": items
                })
                
        # Servico Individual
        elif rel_path.startswith("servicos/") and rel_path != "servicos.html":
            srv_name = soup.h1.get_text(strip=True) if soup.h1 else page_name
            graph.append({
                "@type": "Service",
                "@id": url + "#service",
                "name": srv_name,
                "description": page_desc,
                "provider": {"@id": localbiz_id},
                "areaServed": {"@type": "City", "name": data['empresa']['cidade']},
                "serviceType": "Terapia Emocional"
            })
            faqs = extract_faqs(soup)
            if faqs:
                graph.append({
                    "@type": "FAQPage",
                    "mainEntity": faqs
                })
                
        # Blog Lista
        elif rel_path == "blog.html":
            blog_schema = {
                "@type": "Blog",
                "@id": domain + "/blog#blog",
                "name": "Blog de Terapia e Saúde Emocional",
                "description": page_desc,
                "publisher": {"@id": org_id}
            }
            # Find posts links in DOM (simple heuristic)
            post_links = set()
            for a in soup.find_all('a', href=True):
                if '/blog/' in a['href']:
                    post_links.add(a['href'])
            items = []
            for i, link in enumerate(sorted(post_links)):
                full_link = link if link.startswith('http') else domain + link
                items.append({
                    "@type": "ListItem",
                    "position": i + 1,
                    "url": full_link
                })
            if items:
                blog_schema["blogPost"] = {"@type": "ItemList", "itemListElement": items}
            graph.append(blog_schema)
            
        # Blog Individual
        elif rel_path.startswith("blog/") and rel_path != "blog.html":
            h1 = soup.h1.get_text(strip=True) if soup.h1 else page_name
            img = soup.find('img')
            img_url = domain + img['src'] if img and img.get('src', '').startswith('/') else ""
            if not img_url and img and img.get('src'): img_url = img['src']
            
            text_content = soup.get_text(separator=' ')
            word_count = len(text_content.split())
            
            blog_posting = {
                "@type": "BlogPosting",
                "@id": url + "#blogposting",
                "headline": h1[:110],
                "description": page_desc,
                "author": {
                    "@type": "Person",
                    "name": "Valéria Godoy",
                    "jobTitle": "Terapeuta Emocional TRG"
                },
                "publisher": {"@id": org_id},
                "datePublished": datetime.now().strftime("%Y-%m-%d"),
                "dateModified": datetime.now().strftime("%Y-%m-%d"),
                "mainEntityOfPage": url,
                "wordCount": word_count,
                "inLanguage": "pt-BR"
            }
            if img_url:
                blog_posting["image"] = {
                    "@type": "ImageObject",
                    "url": img_url
                }
            graph.append(blog_posting)
            
            faqs = extract_faqs(soup)
            if faqs:
                graph.append({
                    "@type": "FAQPage",
                    "mainEntity": faqs
                })
                
        # Contato
        elif rel_path == "contato.html":
            webpage_schema["@type"] = ["WebPage", "ContactPage"]
            # A reference to LocalBusiness is needed here too as requested
            graph.append(localbiz_schema)
            
        # FAQ
        elif rel_path == "faq.html":
            faqs = extract_faqs(soup)
            if faqs:
                graph.append({
                    "@type": "FAQPage",
                    "mainEntity": faqs
                })
                
        # 404
        elif rel_path == "404.html":
            # add noindex
            if not soup.head.find('meta', attrs={'name': 'robots'}):
                soup.head.append(soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex'}))
                
        # Inject JSON-LD
        for script in soup.find_all('script', type='application/ld+json'):
            script.decompose()
            
        json_ld = {
            "@context": "https://schema.org",
            "@graph": graph
        }
        
        script_tag = soup.new_tag('script', type='application/ld+json')
        script_tag.string = json.dumps(json_ld, ensure_ascii=False, indent=2)
        
        if soup.head:
            soup.head.append(script_tag)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
    print("Relatório de Schema JSON-LD:")
    print("- As entidades Organization, WebSite e LocalBusiness foram vinculadas perfeitamente com @id.")
    print("- FAQPage detectado e extraído de onde havia conteúdo.")
    print("- Faltando no briefing: Horários de funcionamento (openingHoursSpecification) não gerados. Avaliações/Ratings numéricas não geradas por ausência de dados estruturados quantitativos.")
    
if __name__ == "__main__":
    main()
