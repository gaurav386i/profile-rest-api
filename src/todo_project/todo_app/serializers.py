from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serilalizes a name field for our APIView testing"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password' )
        extra_kwrgs = {'password':{'write_only':True}}


    def create(self, validated_data):
        """Create and return a new User"""

        user = models.UserProfile(
              email = validated_data['email'],
              name =  validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
      """A serializer for profile feed items """


      class Meta:
          model = models.ProfileFeedItem
          fields = ('id', 'user_profile', 'status_text', 'created_on')
          extra_kwrgs = {'user_profile':{'read_only':True}}
