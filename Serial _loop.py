# coding=utf-8
# Author: JQBY
# Date: 2023-03-21
# Description: 串口发送接收数据程序
# Version: 1.0
# Python Version: 3.7.3
# Platform: Windows 10
# Module: pyserial
# Module Version: 3.4
import serial
import time
import binascii
 
serialPort = serial.Serial('COM7', 9600)
  
def myloop():
    while True:
        time.sleep(1)
        while serialPort.inWaiting() > 0:
            n = serialPort.inWaiting()
            data = serialPort.read(n)[0:]
            strData = str(binascii.b2a_hex(data))
            print('serial receive data:' + strData)
            serialPort.write(data)
 
if __name__ == '__main__':
    myloop()
