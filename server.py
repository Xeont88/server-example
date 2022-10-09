from socket import *


socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.bind(('', 5400))
socket_object.listen(5)


while True:
    # Ждём запрос на соединение с Клиентом
    connection, address = socket_object.accept()

    # Получаем сообщение, от клиента (кол-во байт)
    message = connection.recv(1024)
    # Расшифровываем сообщение
    str_message = message.decode('utf-8')

    # Получаем ip клиента
    ip_address = address[0]

    # Выводим сообщение от клиента (и его АйПи)
    print('Клиент с ip', ip_address, 'прислал сообщение:', str_message)

    server_answer = 'Я полючиль от тебя ' + str(len(str_message)) + ' бойт.'
    connection.sendall(server_answer.encode('utf-8'))

    # ОБЯЗАТЕЛЬНО закрываем соединение
    connection.close()




    # list_msg = str_message.split(';')
    # print(list_msg)
    #
    # sending_msg = list_msg[1]
    #
    # byte_sending_msg = sending_msg.encode('utf-8')
    #
    # client = socket(AF_INET, SOCK_STREAM)
    #
    # try:
    #     # Подключаемся к серверу
    #     client.connect((list_msg[0], 5402))
    #     # Отправляем сообщение
    #     client.sendall(byte_sending_msg)
    # except:
    #     # Если попытка подключения неудачная - выводим ___
    #     print('Нет соединения')
    # finally:
    #     # В конце попытки обязательно закрываем соединение
    #     client.close()
