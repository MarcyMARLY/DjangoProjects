from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    person_name = serializers.CharField(max_length = 200)
    person_phone = serializers.CharField(max_length = 200)
    person_photo = serializers.CharField(max_length = 200)


    def create(self, validated_data):
        return Person.objects.create(**validated_data)
    def update(self, instance, validated_data ):
        instance.person_name = validated_data.get('person_name', instance.person_name)
        instance.person_phone = validated_data.get('person_phone', instance.person_phone)
        instance.person_photo = validated_data.get('person_photo', instance.person_photo)
        instance.save()
        return instance
class PersonSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"
