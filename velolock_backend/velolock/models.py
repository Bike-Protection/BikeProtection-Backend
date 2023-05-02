from django.db import models
import bluetooth


class Lock(models.Model):
    def open_lock(request):
        addr = '00:00:00:00:00:00'  # Замініть на MAC-адресу вашого Arduino
        port = 1  # Замініть на відповідний порт Bluetooth на вашому Arduino

        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((addr, port))
            sock.send('1')  # Відправити команду відкриття замка
            sock.close()
            return HttpResponse('Lock opened successfully!')
        except:
            return HttpResponse('Failed to open lock!')

    def close_lock(request):
        addr = '00:00:00:00:00:00'  # Замініть на MAC-адресу вашого Arduino
        port = 1  # Замініть на відповідний порт Bluetooth на вашому Arduino

        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((addr, port))
            sock.send('0')  # Відправити команду закриття замка
            sock.close()
            return HttpResponse('Lock closed successfully!')
        except:
            return HttpResponse('Failed to close lock!')
