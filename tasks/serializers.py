from rest_framework import serializers
from tasks.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
        )


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Task
        fields = (
            "user",
            "title",
            "is_complete",
            "created_at",
            "completed_at",
        )


class TaskDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Task
        fields = (
            "user",
            "title",
            "description",
            "is_complete",
            "created_at",
            "completed_at",
        )
