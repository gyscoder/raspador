import requests
from bs4 import BeautifulSoup

user_input = input(str("por favor entre com a URL do site: "))
url = requests.get(user_input)

soup = BeautifulSoup(url.content, 'html5lib')

searchw = soup.find(class_='card-body card-padding card-body-di text-center') # filtra os dados dentro do html parser
resulta = searchw.find_all('p')

feio = soup.find(class_='pagination')
feio.decompose()

print("pagina solicitada tem: ")
for paginas in resulta:
	karai = paginas.string
	print(str(karai).replace('None',' '))

pagina = input("qual pagina quer pesquisar?: ")
print("pesquisando...")

url2 = requests.get(user_input+pagina)
soup = BeautifulSoup(url2.content, 'html5lib')
searcha = soup.find(class_='card-body card-padding') # filtra os dados dentro do html parser
result = searcha.find_all('a')

for kaka in result:
	links = kaka.get('href')
	krl = kaka.string
	print(f'{krl} : {links}\n')
