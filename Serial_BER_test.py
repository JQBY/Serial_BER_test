# Author: JQBY
# Date: 2023-03-21
# Description: 串口误码率测试程序
# Version: 1.0
# Python Version: 3.7.3
# Platform: Windows 10
# Module: pyserial
# Module Version: 3.4

# 处理误码率
def caculate_scale():
    send = str_send.split(' ')
    recv = str_recv.split(' ')
    send_len = len(send)
    recv_len = len(recv)
    if send_len != recv_len:
        print('数据丢失：%s个字节,请人工处理误码率。' % (send_len - recv_len) + '\r\n')
    else:
        err_cnt: int = 0
        for index in range(send_len):
            if send[index] != recv[index]:
                err_cnt += 1
                print('误码：%s  %s' % (send[index], recv[index]) + '\r\n')
                print('err_cnt', err_cnt)
                print('send_len', send_len)
        print('误码：%s个字节,误码率%f' % (send_len - recv_len, err_cnt / send_len) + '\r\n')    
# send_len、err_cnt 都是按字节算的，所以误码率也是按字节算的
with open('rec.TXT', encoding='utf-8') as file_send:
     str_send=file_send.read()
     print(str_send.rstrip())     ##rstrip()删除字符串末尾的空行

with open('send.TXT', encoding='utf-8') as file_recv:
     str_recv=file_recv.read()
     print(str_recv.rstrip())     ##rstrip()删除字符串末尾的空行

# 调用 caculate_scale 方法
if __name__ == "__main__":
    caculate_scale()