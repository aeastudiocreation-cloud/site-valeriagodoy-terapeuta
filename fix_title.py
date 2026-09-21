from bs4 import BeautifulSoup

filepath = 'build/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    
correct_title = "Valéria Godoy | Terapeuta TRG em Santa Bárbara d'Oeste"
if soup.title:
    soup.title.string = correct_title
    
for og in soup.head.find_all('meta', property='og:title'):
    og['content'] = correct_title
for tw in soup.head.find_all('meta', attrs={'name': 'twitter:title'}):
    tw['content'] = correct_title
    
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print('Fixed index.html title')
