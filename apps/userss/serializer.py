from rest_framework import serializers
from django.contrib.auth import get_user_model

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True}} #para que al crear u usuario no nos muestre la contraseña 


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
    


    
