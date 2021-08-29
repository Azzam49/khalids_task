from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from task.app.serializers import PostUserSerializer
from task.app.common.common import JsonUtils

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from task.settings import APP_URL, EMAIL_FROM

# testing endpoint
def index(request):
    html = "Success"
    return HttpResponse(html)


@api_view(["POST"],)
def create_user(request):
    try:
        if request.data:
            serializer = PostUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return JsonResponse(JsonUtils.json_object("user", 1, serializer.validated_data))
            else:
                return JsonResponse(JsonUtils.json_object("user", 1, {}, serializer.errors))
        else:
            return JsonResponse({'Bad Request': "Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST)
    except ConnectionError:
        return JsonResponse({'Connection Error': 'Server facing some issues please try again...'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.commercial_registration_num,
        'email': reset_password_token.user.email,
        'reset_password_key': reset_password_token.key,
        'reset_password_link': APP_URL + "resetpassword?t="
    }

    # render email text
    email_html_message = render_to_string('email.html', context)
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        EMAIL_FROM,
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()