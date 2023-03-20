**PROGRAM_6**
	# Program to controlling a light source using web page
	#install the following command in terminal
	#sudo apt-get install python3-flask
	# Create a folder "templates" and write your html pages in this folder.
	

     import RPi.GPIO as GPIO
	import time
	import datetime
	led = 13
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(led, GPIO.OUT,initial=0)
	GPIO.setup(led,GPIO.OUT)
	from flask import Flask, render_template
	app = Flask( name )
	@app.route('/')
	def hello_world():
	    return render_template('web.html')
	@app.route('/redledon')
	def redledon():
	    GPIO.output(13, GPIO.LOW)
	    now  =  datetime.datetime.now()
         timeString  =  now.strftime("%Y-%m-%d  %H:%M")
	   templateData = {
	     'status' : 'ON',
	     'time':  timeString
	     }
	   return  render_template('web.html',  **templateData)
	@app.route('/redledoff') #Route for Turning RedLed Off
	def redledoff():
	    GPIO.output(13, GPIO.HIGH)
	    now  =  datetime.datetime.now()
	    timeString  =  now.strftime("%Y-%m-%d  %H:%M")
	    templateData = {
	      'status' : 'OFF',
	      'time':  timeString
	      }
	    return  render_template('web.html',  **templateData)
 
	if __name__ == "__main__ ":
        app.run(debug = True, port = 4000, host='0.0.0.0')


 
	#templates/web.html
	<html>
	<body>
	<title>Raspberry PI Remote Control</title>
	<h1>Raspberry PI Remote Control</h1>
	<h2>Light Status : {{status}}, Last Modified : {{time}}</h2>
	<form action="http://localhost:4000/redledon">
	   <input type="submit" value="Red LED On">
	</form>
	<form action="http://localhost:4000/redledoff">
	   <input type="submit" value="Red LED Off">
	</form>
	</body>
	</html>
 
