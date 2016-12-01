# Serviços Paraguai

Sistema de serviços fornecidos no Paraguai

[![Build Status](https://travis-ci.org/tyagow/servicos-paraguai.svg?branch=master)](https://travis-ci.org/tyagow/servicos-paraguai) [![Code Health](https://landscape.io/github/tyagow/servicos-paraguai/master/landscape.svg?style=flat)](https://landscape.io/github/tyagow/servicos-paraguai/master)

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os testes.

```console
git clone https://github.com/tyagow/servicos-paraguai sparaguaiproject
cd sparaguaiproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

### Como fazer deploy ?

1. Adicionar git remote apontando para o servidor com dokku instalado

1.1. git remote add dokku dokku@<server-ip>:<dokku-app-name>


