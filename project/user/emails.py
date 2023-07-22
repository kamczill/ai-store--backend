from django.core.mail import send_mail

def send_password_reset_email(sender, reset_password_token, **kwargs):
    
    message = 'Witaj! Aby zresetować i ustawić nowe hasło, kliknij w link poniżej:\n\n'
    reset_url = f'http://127.0.0.1:3001/password-reset/{reset_password_token.key}'
    message += reset_url

    # response = send_mail(
    #     Source='your@email.com',
    #     Destination={
    #         'ToAddresses': [reset_password_token.user.email]
    #     },
    #     Message={
    #         'Subject': {'Data': 'Password reset'},
    #         'Body': {'Text': {'Data': message}}
    #     }
    # )
    response = send_mail(
                'Resetowanie hasła - AiSzef',
                message,
                'bot.aiswiat@int.pl',
                [reset_password_token.user.email]
            )

    return response