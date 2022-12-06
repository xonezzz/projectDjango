from django.core.mail import send_mail


def sent_hello(email):
    send_mail('вас приветствует крутой сайт',
              'привет как дела',
              'maksatovch.1@gmail.com'
              [email]
              )

def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'активация пользователя',
        full_link,
        'maksatovch.1@gmail.com',
        [email]
    )              


def send_confirmation_code(email, code):
    send_mail(
        'восстановление пароля',
        code,
        'maksatovch.1@gmail.com',
        [email]
    )                