import qrcode
import os

qr_list = ['www.naver.com','www.google.com','www.daum.net','www.moe.go.kr','www.sen.go.kr']
desktop_path =  os.path.expanduser('~') + r'/Desktop/qr_code'
try:
    os.makedirs(desktop_path)
except:
    pass

for url in qr_list:
    qr_img = qrcode.make(url)

    file_name = url.split('.')[1]
    save_path = f'{desktop_path}//{file_name}.png'
    qr_img.save(save_path)
