from rest_framework import serializers

from .models import TodoModel

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model=TodoModel
        fields='__all__'


        