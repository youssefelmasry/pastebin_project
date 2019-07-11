from rest_framework import serializers
from .models import Paste
from django.contrib.auth.models import User
"""
ModelSerializer
display the information that is relevant to model(s)
create, update models

"""

class PasteSerializer(serializers.ModelSerializer):
    # sharedWith = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')

    class Meta:
        model = Paste
        fields = ("__all__")

    def validate(self, data):
        public = data['public']
        private = data['private']
        shared = data['sharedWith']
     
        public_status = (public==True and private==False and shared==[])
        
        private_status = (private==True and public==False and shared==[])
        
        shared_status = (bool(shared)==True and public==False and private==True)

        if public_status or private_status or shared_status:
            return data
        raise serializers.ValidationError("public cannot be selected with private or shared with")

