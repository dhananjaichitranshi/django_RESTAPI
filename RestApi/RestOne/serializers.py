from rest_framework import serializers
from RestOne.models import ModelEmail

class EmailCommonSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelEmail
        fields = "__all__"
