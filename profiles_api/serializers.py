from rest_framework import serializers
from .models import UserProfile, Lift

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    lifts = serializers.HyperlinkedRelatedField(many=True, view_name='lift-detail', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['url', 'id', 'name', 'email', 'lifts']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class LiftSerializer(serializers.HyperlinkedModelSerializer):
    user_profile = serializers.ReadOnlyField(source='user_profile.username')

    class Meta:
        model = Lift
        fields = ['url', 'user_profile', 'id', 'exercise', 'sets', 'reps', 'weight', 'date']
        extra_kwargs = {'user_profile': {'read_only':True}}