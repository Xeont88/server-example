from socket import *
from threading import Thread
from time import sleep


server_address = ('192.168.134.16', 5400)

ip_names_dictionary = {'Den4ik':'192.168.134.55',
                       'Matvey4ik':'192.168.134.54',
                       'Dian4ik':'192.168.134.180',
                       'Bogdan':'192.168.134.237',
                       'Ya':'192.168.134.16'}


def work_in():
    '''
    Функция для приема сообщений от сервера
    '''
    # lock_server_addr = ('192.168.134.16', 5402)
    lock_server_addr = ('localhost', 5402)
    lock_server = socket(AF_INET, SOCK_STREAM)
    lock_server.bind(lock_server_addr)
    lock_server.listen(5)

    while True:
        # Ожидаем сообщения от общего сервера
        connection, address = lock_server.accept()
        byte_msg = connection.recv(1024)
        str_msg = byte_msg.decode('utf-8')
        connection.close()

        print(str_msg)
        sleep(0.001)



# Создаем отдельный поток
tr_in = Thread(target=work_in)
tr_in.daemon = True
tr_in.start()


# всегда
while True:

    # Ожидаем сообщения от пользователя
    client_name = input('Введите имя получателя: ')
    msg = input('Ваше сообщение: ')

    # Получаем ip получателя
    client_ip = ip_names_dictionary[client_name]

    # кодируем сообщение для передачи
    byte_msg = client_ip.encode('utf-8') + b';' + msg.encode('utf-8')

    # Создаем объект соединения (клиент)
    client = socket(AF_INET, SOCK_STREAM)

    # пробуем ...
    try:
        # ... подключиться к серверу
        client.connect(server_address)
        # и отправить соощение
        client.sendall(byte_msg)
    # если не получилось
    except:
        # Выводим сообщение ___
        print('нет соединения')
    # В любом случае - закрываем соединение
    finally:
        client.close()

