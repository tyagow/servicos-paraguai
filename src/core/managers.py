def path_and_rename_logo(instance, filename):
    return '{}/{}/{}'.format(instance.nome, 'logo', filename)


def path_and_rename_fotos(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'fotos', filename)


def path_and_rename_banner(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'banner', filename)

