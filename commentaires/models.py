from django.db import models
from articles.models import Article

class Commentaire(models.Model):
    auteur = models.CharField(max_length=200)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.auteur
