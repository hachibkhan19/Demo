from rest_framework import serializers
from .models import InNeed
  
# Create a model serializer 
class InNeedSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = InNeed
        fields = ('url', 'id', 'title', 'description')