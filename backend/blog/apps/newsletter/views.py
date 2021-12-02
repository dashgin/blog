import re

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SubscribedUser


class Subscribe(APIView):
    """
    an API View for send email verification to add user to supscribers list
    """

    def post(self, request, email):
        """
        post method for sending email verification to add user to subscribers list
        """
        if not email:
            return Response({"message": "email is required"}, status=400)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({"message": "email is invalid"}, status=400)
        if SubscribedUser.objects.filter(email=email).exists():
            return Response({"message": "email already exists"}, status=400)
        subscriber = SubscribedUser.objects.create(email=email)

        send_mail(
            from_email=settings.ADMIN_EMAIL,
            recipient_list=[subscriber.email],
            subject="Newsletter Confirmation",
            message=f'Thank you for signing up for my email newsletter! \
                        Please complete the process by \
                        <a href="{reverse("api:newsletter:confirm")}?email={subscriber.email}&conf_num={subscriber.conf_num}"> clicking here to  confirm your registration</a>. if you did\'nt enter your email don\'t mention this email',  # noqa
        )
        return Response(
            {"message": "email sent successfully, please confirm"}, status=200
        )


class Confirm(APIView):
    """
    an API View for confirm email verification
    """

    def get(self, request):
        """
        get method for confirm email verification
        """
        email = request.GET.get("email")
        conf_num = request.GET.get("conf_num")
        if not email:
            return Response({"message": "email is required"}, status=400)
        if not conf_num:
            return Response({"message": "confirmation number is required"}, status=400)
        if not SubscribedUser.objects.filter(email=email, conf_num=conf_num).exists():
            return Response(
                {"message": "email or confirmation number is invalid"}, status=400
            )
        subscriber = SubscribedUser.objects.get(email=email, conf_num=conf_num)
        subscriber.is_active = True
        subscriber.save()
        return Response({"message": "email confirmed successfully"}, status=200)


class Unsubscribe(APIView):
    """
    an API View for unsubscribe user from newsletter
    """

    def get(self, request, email):
        """
        get method for unsubscribe user from newsletter
        """
        conf_num = request.GET.get("conf_num")
        if not email or not conf_num:
            return Response({"message": "email and conf_num are required"}, status=400)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({"message": "email is invalid"}, status=400)
        if (
            not SubscribedUser.objects.filter(email=email)
            .filter(conf_num=conf_num)
            .filter(is_active=True)
            .exists()
        ):
            return Response({"message": "email not in subscriber list"}, status=400)
        subscriber = SubscribedUser.objects.get(email=email)
        subscriber.delete()
        return Response({"message": "email unsubscribed successfully"}, status=200)
