<h1 align="center">Speech To Text - Python</h1>

<p align="center">Project to convert audio files into text with Speech Recognition using python</p>

<hr> 

### :hammer_and_wrench: Technologies & Concepts:

* Python 3.11
* Speech Recognition 3.8.1

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=Python&message=v3.11&color=3572A5&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Settings:

* Launch dockerfile:
```bash
docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb 
```

* Run the following commands:
```bash
python App/src/main.py
```

### :warning: Bugs/Improvements:

##

<div align="center">
	<p>Made with :computer: + :heart: by Leonardo Junio</p>
</div>
