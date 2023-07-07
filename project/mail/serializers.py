from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class MailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    text = serializers.CharField()
    # html_ = serializers.CharField()
    recipient_list = serializers.CharField()
    