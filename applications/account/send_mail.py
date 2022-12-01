from django.core.mail import send_mail


def sent_hello(email):
    send_mail('вас приветствует крутой сайт',
              'привет как дела',
              'maksatovch.1@gmail.com'
              [email]
              )