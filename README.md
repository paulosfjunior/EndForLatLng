# **Converter Endereço em Latitude Longitude**

Script em PYTHON para converter endereços em latitude e longitude utilizando "googleapis".

> ***É necessário ter o Python 3 instalado na máquina***

***

## **Passo a passo**

Abra o terminal e clone o projeto  

> `git clone git@gitlab.com:paulosfjunior/EndForLatLng.git`

Navegue para pasta do projeto

> `cd EndForLatLng`

Instale as dependências

> `pip install -r requirements.txt`

Realize as seguintes modificações no nos arquivos

> [**converter.py**](https://gitlab.com/paulosfjunior/EndForLatLng/-/blob/master/converter.py)  
> Substitua o valor da variável **"apiKey"** que está dentro da função **"main"** pela ***api key*** que a google gerou para você.

> [**endereco.csv**](https://gitlab.com/paulosfjunior/EndForLatLng/-/blob/master/endereco.csv)  
> Insira as informações dos endereços conforme modelo *(não apague a linha de titulo)*. Salve o arquivo com o padrão de **`encoding='utf8'`** e **`delimiter=';'`**.

Execute o script e aguarde ler todos os endereços do arquivo "endereco.csv"
> `python converter.py`

***

## **Considerações**

Quando finalizar de executar o script os dados gerados estarão no arquivo **"latlon.csv"** na pasta do projeto.  
Além dos dados de endereço serão adicionadas quatro novas colunas *`['latitude', 'longitude', 'coordenada', 'status']`*. A coluna **"status"** indica se a pesquisa do endereço foi bem sucedida, caso o endereço não seja encontrado as novas colunas receberam os seguintes valores: *`["-500", "-500", "-500, -500", "Sem resultado"]`*
