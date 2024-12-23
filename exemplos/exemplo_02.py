# Importa a biblioteca requests para fazer chamadas HTTP
import requests
# Define a URL da API que retorna comentários
url = "https://jsonplaceholder.typicode.com/comments"
#Define parâmetros da requisição - filtra comentários do usuário 1
params = {'userId': 1}
# Faz uma requisição GET para a URL com os parâmetros especificados
response = requests.get(url, params=params)
# Converte a resposta JSON para um objeto Python
comentarios = response.json()
# Imprime o número total de comentários retornados
print(f"Total de comentários: {len(comentarios)}")
# Imprime o código de status HTTP e a razão da resposta
print(f"Código de status: {response.status_code} - {response.reason}")
