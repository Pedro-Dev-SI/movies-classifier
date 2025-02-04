import requests
from bs4 import BeautifulSoup
import json

def collect_data():
    # URL da página de filmes do IMDb (Top 250)
    url = "https://www.imdb.com/chart/top"
    
    # Definindo o cabeçalho User-Agent para simular um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # Fazendo a requisição HTTP com o cabeçalho definido
    response = requests.get(url, headers=headers)
        
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = []

        # Encontrar o <script> que contém os dados em JSON
        script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
        if script_tag:
            json_data = json.loads(script_tag.string)
            
            # Acessando os filmes dentro do JSON
            chart_titles = json_data['props']['pageProps']['pageData']['chartTitles']['edges']
            for item in chart_titles:
                movie_data = item['node']
                                
                # Pegando o título
                movie_title = movie_data['originalTitleText']['text']
                
                # Pegando a descrição (classificação etária, duração, etc.)
                certificate = movie_data['certificate']
                classification = certificate.get('rating', 'N/A') if certificate else 'N/A'
                plot = movie_data['plot']['plotText']['plainText']
                                
                # Armazenando as informações
                movies.append(
                    {
                        'title': movie_title,
                        'plot': plot,
                        'classification': classification
                    }
                )
        
        return movies
    else:
        print(f"Falha ao acessar a página. Status code: {response.status_code}")
        return []

if __name__ == '__main__':
    movie_data = collect_data()
     # Salvando os dados em um arquivo JSON na pasta local
    with open("movie_data.json", "w", encoding="utf-8") as file:
        json.dump(movie_data, file, ensure_ascii=False, indent=4)
    # for movie in movie_data:
    #     print(f"Title: {movie['title']}, Plot: {movie['plot']}, Classification: {movie['classification']}")
