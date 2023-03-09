from webbrowser import open
from urllib import request

url = input('Digite a URL: ')
try:
    print(f'Acessando o site {url}')
    site = request.urlopen(f'{url}')
except:
    print('URL incorreto ou fora do ar')
else:
    print('Site em operação')
    while True:
        site = input(f'Deseja acessar {url}? (s/n): ').strip().lower()[0]
        if site == 's':
            open(url)
            break
        elif site == 'n': break
        print('Comando inválido...')
