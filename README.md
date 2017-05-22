# Serviços Paraguai

Sistema de serviços fornecidos no Paraguai

[![Build Status](https://travis-ci.org/tyagow/servicos-paraguai.svg?branch=master)](https://travis-ci.org/tyagow/servicos-paraguai) [![Code Health](https://landscape.io/github/tyagow/servicos-paraguai/master/landscape.svg?style=flat)](https://landscape.io/github/tyagow/servicos-paraguai/master)

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virutalenv com o Python 3.5
3. Ative o Virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Rode as migrations
7. Execute os testes.
8. Rode o servidor

```console
git clone https://github.com/tyagow/servicos-paraguai sparaguaiproject
cd sparaguaiproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
python manage.py runserver
```

## Como criar uma nova feature? 

1) Atualize a branch master antes de criar qualquer branch
2) Crie uma branch com o nome da feature ( novo_banner ), sempre apartir do branch master
3) Modifique os arquivos na branche nova
4) adicione os arquivos alterados ao git ( tente agrupar arquivos e comitalos em pequenos blocos assim fica mais facil de saber o que esta sendo feito) 
5) envie a branch nova para o git
6) volte para a branch master para criar outra feature

```console
git checkout master
git pull origin master
git checkout -b feature_name
git add file
git commit -m "mensagem descrevendo alteracao do(s) arquivo(s)adicionado(s)"
git push origin feature_name
git checkout master
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