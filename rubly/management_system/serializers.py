from rest_framework import serializers
from .models import Goods_received

class GoodsReceivedSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='Project_Type.client.name', read_only=True)
    project_name = serializers.CharField(source='Project_Type.name', read_only=True)
    description = serializers.CharField(source='description.Description', read_only=True)
    stock_type = serializers.CharField(source='description.Type', read_only=True)
    packaging = serializers.CharField(source='description.Packaging', read_only=True)
    # Purchase_Order = serializers.CharField(source='Purchase_Order.purchase_ID', read_only=True)
    
    class Meta:
        model = Goods_received
        fields = ['stock_type', 'price', 'Quantity', 'description', 'packaging', 'remaining', 'client_name', 'project_name']