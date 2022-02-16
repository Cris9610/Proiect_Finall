from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import os

def email():
    subject = 'Subiectul mailului'
    message = 'Primul mail trimis din aplicatia django. Felicitari Cris!'
    email_from = 'from@mysite.com'
    recipient_list = ['croli_sto@yahoo.com']
    send_mail(subject, message, email_from, recipient_list)

def send_register_mail(user):
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email':user.email,
    }

    template = get_template('users/emails/register.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Contul a fost creat cu succes!',
        body=content,
        to=[user.email],
    )
    mail.content_subtype = 'html'
    mail.attach_file(os.path.join(settings.MEDIA_ROOT, 'images/image.jpg'))
    mail.send()