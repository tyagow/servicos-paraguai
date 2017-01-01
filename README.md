# Serviços Paraguai

Sistema de serviços fornecidos no Paraguai

[![Build Status](https://travis-ci.org/tyagow/servicos-paraguai.svg?branch=master)](https://travis-ci.org/tyagow/servicos-paraguai) [![Code Health](https://landscape.io/github/tyagow/servicos-paraguai/master/landscape.svg?style=flat)](https://landscape.io/github/tyagow/servicos-paraguai/master)

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Roda o collectstatic para configurar arquivos staticos
7. Execute os testes.

```console
git clone https://github.com/tyagow/servicos-paraguai sparaguaiproject
cd sparaguaiproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py collectstatic
python manage.py test
python manage.py runserver
```

## Como fazer deploy ?

1. Adicionar git remote apontando para o servidor com dokku instalado (Necessario ter ssh-key adicionado no dokku para autentificacao)
2. Fazer o comando collectstatic localmente caso tenha alterado algum static file
3. Enviar projeto com git push 
4. Caso precise rodar migrações conecte via ssh ao servidor e rode o comando via dokku-cli

```console
git remote add dokku dokku@<server-ip>:<dokku-app-name>
(linux) DEBUG=False python manage.py collectstatic
git push dokku master
(servidor)dokku run <dokku-app-name> python manage.py migrate
```

**NOTES**

**static e media** files são salvos **localmente** com **DEBUG=True** e salvos no **AmazonAWS S3** com **DEBUG=False**