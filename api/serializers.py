"""doc"""
from rest_framework import serializers, validators # pylint: disable=E0401

from api.models import ApiUser, Hotel, Room, Booking # pylint: disable=E0401


class UserSerializer(serializers.Serializer):
    """doc"""
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)

    def update(self, instance, validated_data):
        """doc"""
        if email := validated_data.get('email'):
            instance.email = email
            instance.save(update_fields=['email'])

        if password := validated_data.get('password'):
            instance.set_password(password)
            instance.save(update_fields=['password'])
        return instance

    def create(self, validated_data):
        """doc"""
        user = ApiUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])
        return user


class HotelSerializer(serializers.ModelSerializer): # pylint: disable=R0903
    """doc"""
    class Meta:# pylint: disable=R0903
        """doc"""
        model = Hotel
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class RoomSerializer(serializers.ModelSerializer):# pylint: disable=R0903
    """doc"""
    class Meta:# pylint: disable=R0903
        """doc"""
        model = Room
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class BookingSerializer(serializers.ModelSerializer):# pylint: disable=R0903
    """doc"""
    class Meta:# pylint: disable=R0903
        """doc"""
        model = Booking
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
