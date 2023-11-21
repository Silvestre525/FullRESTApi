from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        person = super().create(validated_data)
        if password:
            person.set_password(password)  # Hashear la contraseña al crear un usuario
            person.save()
        return person

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        person = super().update(instance, validated_data)
        if password:
            person.set_password(password)  # Hashear la contraseña al actualizar un usuario
            person.save()
        return person
