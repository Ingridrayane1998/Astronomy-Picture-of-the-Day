import requests


url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
headers = {
    "Authorization": "bearer UGGf9NrEevdggm84RUVQHJSK0uGfpeEwyn438fAT",
}
resposta = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida (Status 200)
if resposta.status_code == 200:
    # Salva o conteúdo binário da imagem no computador
    with open("imagem_baixada.jpg", "wb") as arquivo:
        arquivo.write(resposta.content)
    print("Imagem salva com sucesso!")
else:
    print(f"Erro ao buscar imagem. Status: {resposta.status_code}")