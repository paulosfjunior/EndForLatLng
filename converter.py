import csv
import os.path
import requests

def abrirArquivo(pathArq):
  try:
    linhas = []
    with open(pathArq, 'r', encoding='utf8') as arq:
      temp = csv.reader(arq, delimiter=';')

      for linha in temp:
        linhas.append(linha)

    return linhas
  except Exception as e:
    print(e)
    return False

def converterEndereco(end):
  try:
    endereco = ','.join(end[1:])

    endereco = endereco.replace(' ', '+')
    endereco = endereco.lower()

    return endereco
  except Exception as e:
    print(e)
    return False

def gravarArquivo(dados, latlon, titulo):
  try:
    inserir = dados
    inserir.append('"' + str(latlon['lat']) + '"')
    inserir.append('"' + str(latlon['lng']) + '"')
    inserir.append('"' + str(latlon['lat']) + ', ' + str(latlon['lng']) + '"')
    inserir.append(latlon['status'])

    tipo = 'a+' if os.path.exists('./latlon.csv') else 'w'
    
    with open('./latlon.csv', tipo, encoding='utf8') as arq:
      escrever = csv.writer(arq, delimiter=';', lineterminator='\n')

      if tipo == 'w':
        escrever.writerow(titulo)

      escrever.writerow(inserir)
  except Exception as e:
    print(e)
    return False

def main():
  apiKey = 'minhaapikey'
  
  pathArquivo = './endereco.csv'
  titulo = []

  urlBase = 'https://maps.googleapis.com/maps/api/geocode/json?address=***endereco***&key=***apiKey***'

  enderecos = abrirArquivo(pathArquivo)

  for end in enderecos:
    try:
      if titulo:
        endereco = converterEndereco(end)

        urlReq = urlBase.replace('***endereco***', endereco).replace('***apiKey***', apiKey)

        resp = requests.get(urlReq)
        rJson = resp.json()
        if rJson['results']:
          latlon = rJson['results'][0]['geometry']['location']
          latlon['status'] = 'OK'
        else:
          latlon = {'lat': -500, 'lng': -500}
          latlon['status'] = 'Sem resultado'
          
        gravarArquivo(end, latlon, titulo)
        print('Endereço:', end[0], 'gravado.')
      else:
        titulo = end
        titulo.extend(['latitude', 'longitude', 'coordenada', 'status'])

    except Exception as e:
      print(e)
      print('Não foi possivel gravar o endereço:', end[0], '.')

if __name__ == "__main__":
  main()
