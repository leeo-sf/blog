from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin  # Editor de texto (Quase igual ao word)


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_post', 'autor_post', 'data_post', 'categoria_post', 'publicado_post',)
    list_editable = ('publicado_post',)
    list_display_links = ('id', 'titulo_post',)
    summernote_fields = ('conteudo_post',)


# Sempre adicionar esta linha para poder migrar.
admin.site.register(Post, PostAdmin)


#              TERMINAL
# Primeiro -> python manage.py makemigrations
# Segundo -> python manage.py migrate
