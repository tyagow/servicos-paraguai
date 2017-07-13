from pagedown.widgets import PagedownWidget
from django import forms


from src.posts.models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(label='Titulo')
    content = forms.CharField(label='Conteudo', widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(label='Publicar em', widget=forms.SelectDateWidget)
    image = forms.ImageField(label='Capa do post')
    # type = forms.IntegerField(label='Categoria')

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            'type',
            "image",
            "draft",
            "publish",
        ]