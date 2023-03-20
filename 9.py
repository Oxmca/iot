**PROGRAM_9**
	#server program to read gas values
	#sudo pip3 install Adafruit_MCP3008


	import socket
	import Adafruit_MCP3008
	import Adafruit_GPIO.SPI as SPI
	import time
	HOST  =  '127.0.0.1'
	PORT = 4000
	SPI_DEVICE = 0
	SPI_PORT = 0
	mcp  =  Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT,  SPI_DEVICE))
	try:
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	        s.bind((HOST,  PORT))
	        s.listen()
	        conn, addr = s.accept()
	        with conn:
	            print('Connected by', addr)
	            while True:
	                value = mcp.read_adc(0)
	                print("Gas Value ", value , "units")
	                if(value >300):
	                    data = "Alert".encode('utf-8')
	                    conn.sendall(data)
	                time.sleep(3)
	except KeyboardInterrupt:
	    s.close()
	    GPIO.cleanup()




	#client program to alert through buzzer.
	import socket
	import RPi.GPIO as GPIO
	import time
	Buzzer = 36
	HOST  =  '127.0.0.1'
	PORT = 4000
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(36, GPIO.OUT)
	GPIO.setwarnings(False)
	try:
	   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	       s.connect((HOST,PORT))
	       while True:
	           data = s.recv(1024).decode('utf-8')
	           print(data)
	           if(str(data) == 'Alert'):
                   print("ALert! Gas Leakage detected")
	             GPIO.output(36, True)
	             time.sleep(3)
	             GPIO.output(36, False)
	             time.sleep(3)
	except KeyboardInterrupt:
	    s.close()
	    GPIO.cleanup()
