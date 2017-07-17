from django.conf import settings
from sparkpost import SparkPost
from sparkpost.exceptions import SparkPostAPIException


def get_sparkpost_template_list():
    sp = SparkPost(settings.SPARKPOST_API_KEY)
    return sp.templates.list()


def get_sparkpost_recipients_list():
    sp = SparkPost(settings.SPARKPOST_API_KEY)
    return sp.recipient_lists.list()


def enviar_sparkpost(newsletter):
    """
    Envia um requisicao para o sparkpost enviar um template de email para um lista de emails de usuarios.
    Recebe um EnvioNewsletter e seta ele para enviado.
    Deve-se verificar antes de chamar esta funcao se o EnvioNewsletter.enviado ja foi enviado e ter certeza,
    que deseja este comportamento de reenviar.
    """
    try:
        sp = SparkPost(settings.SPARKPOST_API_KEY)
        response = sp.transmissions.send(
            recipient_list=newsletter.recipients,
            template=newsletter.template,
            track_opens=True,
            track_clicks=True,
        )
        newsletter.enviado = True
        newsletter.response = response
        newsletter.save()
        print (str(newsletter) + ' - enviado.')
    except SparkPostAPIException as err:
        print(err.status)
        print(err.response.json())
        print(err.errors)
        response = err.errors

    return response

