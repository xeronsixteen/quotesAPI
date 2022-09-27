from rest_framework import serializers
from webapp.models import Quote


class QuoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
        read_only_fields = ['author', 'rating', 'created_at', 'email']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
        read_only_fields = ['rating', 'status', 'created_at']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Quote.objects.create(**validated_data)
