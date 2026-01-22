from rest_framework import serializers
from bson.objectid import ObjectId
from .models import User, Team, Activity, Workout, Leaderboard

class ObjectIdField(serializers.Field):
    """Custom field to convert ObjectId to string"""
    def to_representation(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
    
    def to_internal_value(self, data):
        try:
            return ObjectId(data)
        except:
            raise serializers.ValidationError("Invalid ObjectId")

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True, source='_id')
    
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True, source='_id')
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True, source='_id')
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True, source='_id')
    suggested_for = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True, source='_id')
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = '__all__'
