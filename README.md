<h1 align="center">Speech To Text - Python</h1>

<p align="center">Projeto para converter audios em textos com Speech Recognition (python)</p>

<hr> 

### :hammer_and_wrench: Tecnologias e Conceitos:

* Python 3.11
* Speech Recognition 3.8.1

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=Python&message=v3.11&color=3572A5&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Configurações:

* Verificar se o requirements.txt contem todas as extensões desejadas. Caso precise de algo mais, rodar no docker: pip install SpeechRecognition (depois colocar-la no requirements)
* Executar o dockerfile (docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb)
* Entrar na pasta App
* Rodar o comando: python <_nome_arquivo_>

### :warning: Erros/Aprimoramentos:

* Verificar se não há outras ferramentas mais 'aprimoradas' se comparado a SpeechRecognition
* Aprimorar código/estrutura do projeto
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
