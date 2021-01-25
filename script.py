import telnetlib, time
#from telnetlib import OSError

HOST = '155.165.240.52'
tel = telnetlib.Telnet(HOST, 23)
#print(tel)
#tel.open(HOST)

tel.write(b'\r') 
tel.write(b'\r')
tel.write(b'\n')
print(tel.read_until(b'>'))

tel.write(b'ar') 
tel.write(b'\r')
tel.write(b'\n')
print(tel.read_until(b'>')) # repeated the same lines since this is the only way 'ar' o/p is seen

while True:

        time.sleep(3)
        
        tel.write(b'aw3=0') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=0') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=5') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=5') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=10') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=10') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=15') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=15') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=20') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=20') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=25') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=25') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=30') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=30') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=25') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=25') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=20') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=20') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=15') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=15') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=10') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=10') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=5') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=5') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        time.sleep(3)

        tel.write(b'aw3=0') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))

        tel.write(b'aw4=0') # set this to the desired attennuator and value 
        tel.write(b'\r')
        tel.write(b'\n')
        print(tel.read_until(b'OK'))



tel.close()



'''

>ar
Attenuator 1 is 95dB
Attenuator 2 is 95dB
Attenuator 3 is 0dB
Attenuator 4 is 0dB
Attenuator 5 is 20dB
Attenuator 6 is 20dB
Attenuator 7 is 95dB
Attenuator 8 is 95dB

'''

'''
"awX=Y" Sets the value of a specific attenuator.
X is channel number on the attenuator (1-8)
Y is the value of attenuation level (0-90db)

'''
