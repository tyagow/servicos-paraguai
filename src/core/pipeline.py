from src.accounts.models import Profile


def get_avatar(backend, strategy, details, response,
               user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    if url:
        if not user.profile:
            Profile.objects.create(user=user, avatar=url)
        user.profile.avatar = url
        user.save()