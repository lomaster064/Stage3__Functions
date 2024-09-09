def check_email(email):
    pos_dog = email.find('@')

    variants = ('.com', '.ru', '.net')
    # Простой аналог будет email[len(email)-4:] - для .com/.net and email[len(email)-3:] - для .ru
    # Но метод компактней
    if email.endswith(variants) and pos_dog != -1 and pos_dog > 0 and (pos_dog < len(email) - 4):
        return True
    else:
        return False

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if sender == recipient:
        print('Нельзя отправить письмо самому себе')
        return False

    if check_email(sender) and check_email(recipient):
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            return True
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            return True
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return False

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')