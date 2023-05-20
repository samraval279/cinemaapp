from rest_framework import serializers
from movie.models import *

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id','name', 'protagonists', 'poster', 'start_date', 'status', 'ranking']
        