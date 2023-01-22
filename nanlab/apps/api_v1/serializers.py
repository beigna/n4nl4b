from rest_framework import serializers


class IssueSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()


class BugSerializer(serializers.Serializer):
    description = serializers.CharField()


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    category = serializers.CharField()

    def validate_category(self, value):
        if value not in ['Maintenance', 'Research', 'Test']:
            raise serializers.ValidationError()

        return value
