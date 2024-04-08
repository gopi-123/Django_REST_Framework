from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #serialize all the fields in Model/Database Item
        fields = '__all__'