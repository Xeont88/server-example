from socket import *


# server_address = ('localhost', 5400)
server_address = ('192.168.76.16', 5400)

while True:
    # Ждем сообщения от пользователя
    msg = input('>> ')

    # Шифруем это сообщение для передачи
    bin_msg = msg.encode('utf-8')

    # Создаем объект соединения (клиент)
    client = socket(AF_INET, SOCK_STREAM)

    try:
        # Подключаемся к серверу
        client.connect(server_address)
        # Отправляем сообщение
        client.sendall(bin_msg)
    except:
        # Если попытка подключения неудачная - выводим ___
        print('Нет соединения')
    finally:
        # В конце попытки обязательно закрываем соединение
        client.close()
