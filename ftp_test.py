import ftplib
import os
import zipfile
import shutil
host = '95.165.155.163'
port = 21
ftp = ftplib.FTP()#(host, port)
ftp.connect(host, port)
print(ftp.getwelcome())
#ftp.login("Fill","Vlad040202")

try:
    print('Logging in...')
    ftp.login("Fill","Vlad040202")
except:
    print("failed to login")
    
    
    
    
remotefile = 'FTP_YSK.zip'
download = 'FTP_YSK'

with open(download, 'wb') as file:
    ftp.retrbinary('RETR %s' % remotefile, file.write)
directory = ftp.nlst()

print(directory)

shutil.rmtree('/home/pi/Documents/done_zip')

with zipfile.ZipFile('FTP_YSK', 'r') as zip_ref:
    zip_ref.extractall('/home/pi/Documents/done_zip')

list_dir = os.listdir('/home/pi/Documents/done_zip')
with open(r"/home/pi/Documents/list_of_music.txt", "w") as file:
    for line in list_dir:
        file.write(line + '\n')
