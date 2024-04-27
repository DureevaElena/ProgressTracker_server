from rest_framework import serializers
from rest_framework import serializers
from .models import Plans

# class PlansModel:
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content


class PlansSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Plans
#        fields = ("title", "content", "cat")
        fields = ("__all__")