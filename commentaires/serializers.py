from rest_framework import serializers
from commentaires.models import Commentaire

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'auteur', 'description', 'date_pub', 'article']
