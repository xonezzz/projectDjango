from rest_framework import serializers

from applications.product.views import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        product = Product.objects.create(owner=user, **validated_data)
        return product  