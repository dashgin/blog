from django.utils.functional import empty
from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from .models import SubscribedUser
from ..utils.confirmation_link_generator import generate_confirmation_link

class SubscribedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedUser
        fields = ("email",)

    def create(self, validated_data):
        email = validated_data["email"]
        if SubscribedUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        else:
            user = SubscribedUser.objects.create(**validated_data)
            conf_btn = f"<a href={generate_confirmation_link(user)} style='backgorund:#000, padding:5px'>confirm</a>"
            send_mail(
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[user.email],
                subject="Newsletter Confirmation",
                html_message=f"Thank you for signing up for my email newsletter! Please complete the process by clicking {conf_btn} to confirm your registration.if you did\'nt enter your email don\'t mention this email",  # noqa
                message=''
            )
            return user
