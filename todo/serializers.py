from rest_framework import serializers

from .models import ToDo, Tag


class TagsSerializerField(serializers.ListField):
    """
        Custom serializer field to handle tags as a list of strings
    """
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class ToDoSerializer(serializers.ModelSerializer):
    tags = TagsSerializerField(required=True)
    
    class Meta:
        model = ToDo
        fields = ("id", "title", "description", "created_at", "due_date", "status", "tags")

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True}
        }

    def create(self, validated_data):
        """
            check if the tag already exists otherwise create a new one then set these tags to current instance
        """
        tag_names = validated_data.pop("tags", None)
        instance = super().create(validated_data=validated_data)
        if tag_names:
            tags = []
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                tags.append(tag)
            instance.tags.set(tags)
        return instance

    def get_tags(self, instance, validated_data):
        """
            check if the tag already exists otherwise create a new one then update these tags to current instance
        """
        tag_names = validated_data.pop("tags", None)
        instance = super().update(instance, **validated_data)
        if tag_names:
            tags = []
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                tags.append(tag)
            instance.tags.set(tags)
        return instance