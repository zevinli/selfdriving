import RPi.GPIO as GPIO
import time
backMotorInput1 = 7
backMotorInput2 = 11

frontMotorInput1 = 13
frontMotorInput2 = 15

backMotorEn = 12
frontMotorEn = 16

speed = 66
backMotorPwm = GPIO.PWM(backMotorEn,100)
backMotorPwm.start(0)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(backMotorInput1,GPIO.OUT)
GPIO.setup(backMotorInput2,GPIO.OUT)
GPIO.setup(frontMotorInput1,GPIO.OUT)
GPIO.setup(frontMotorInput2,GPIO.OUT)

def carMoveForward():
	GPIO.output(backMotorInput1,GPIO.LOW)
	GPIO.output(backMotorInput2,GPIO.HIGH)
	backMotorPwm.ChangeDutyCycle(speed)
	
def carMoveBackward():
	GPIO.output(backMotorInput1,GPIO.HIGH)
	PIO.output(backMotorInput2,GPIO.LOW)
	
    
def carTurnLeft():
	GPIO.output(frontMotorEn,GPIO.HIGH)
	GPIO.output(frontMotorInput1,GPIO.HIGH)
	GPIO.output(frontMotorInput2,GPIO.LOW)
	
def carTurnRight():
	GPIO.output(frontMotorEn,GPIO.HIGH)
	GPIO.output(frontMotorInput1,GPIO.LOW)
	GPIO.output(frontMotorInput2,GPIO.HIGH)
	
def carTurnStraight():
	GPIO.output(frontMotorEn,GPIO.LOW)
	
def carStop():
	GPIO.output(backMotorInput1,GPIO.LOW)
	GPIO.output(backMotorInput2,GPIO.LOW)	
	     
def cleanGPIO():
	GPIO.cleanup()
	backMotorPwm.stop()

	
if  __name__ == '__main__':
	#carTurnStraight()
	#backMotorPwm = GPIO.PWM(backMotorEn,100)
	carMoveForward()
	time.sleep(2)
	carMoveBackward()
	time.sleep(2)
	cleanGPIO()