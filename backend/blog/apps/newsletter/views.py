import re

from django.http.response import HttpResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SubscribedUser
from .serializers import SubscribedUserSerializer


class Subscribe(CreateAPIView):
    """
    an API View add user to supscribers list
    """

    serializer_class = SubscribedUserSerializer

    def post(self, request, *args, **kwargs):
        """
        add user to subscribers list
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


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
        return HttpResponse("Email confirmed successfully")


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
