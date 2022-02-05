import pyqrcode

def qr_code(s):
    
    d = pyqrcode.create(s)
    d.png('qrcode.png',scale=6)
    print('Code Executed properly')

if __name__ == '__main__':
    qr_code()