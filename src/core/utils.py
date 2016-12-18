import unicodedata


def path_and_rename_logo(instance, filename):
    return '{}/{}/{}'.format(instance.nome, 'logo', filename)


def path_and_rename_fotos(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'fotos', filename)


def path_and_rename_banner(instance, filename):
    return '{}/{}/{}'.format(instance.estabelecimento.nome, 'banner', filename)


def path_and_rename_categoria(instance, filename):
    ext = filename.split('.')[-1]
    fname = strip_accents(instance.nome)
    return '{}/{}_{}.{}'.format('categorias', fname, 'icon', ext)


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')