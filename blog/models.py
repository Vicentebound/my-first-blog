from django.db import models
from django.utils import timezone
"""
class Post(models.Model): - esta linha define o nosso modelo (é um objeto).
class é uma palavra-chave especial que indica que estamos definindo um objeto.
Post é o nome do nosso modelo, podemos lhe dar um nome diferente (mas é preciso evitar os espaços em branco e caracteres especiais). Sempre comece um nome de classe com uma letra maiúscula.
models.Model significa que o Post é um modelo de Django, então o Django sabe ele que deve ser salvo no banco de dados.
"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title