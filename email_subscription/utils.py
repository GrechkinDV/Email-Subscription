from django.core.mail import send_mail


def send_subscription_success(email):
    """
    A util to notify users about successfull subscription
    """

    send_mail(
        'Test Subscription',
        'You\'ve subscribed successfully.',
        'dmitrygrechkin04@gmail.com',
        [email],
        fail_silently=True,
    )
