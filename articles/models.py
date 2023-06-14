from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
