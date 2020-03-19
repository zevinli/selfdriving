backMotorInput1 = 7
backMotorInput2 = 11

frontMotorInput1 = 13
frontMotorInput2 = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(backMotorInput1,GPIO.OUT)
GPIO.setup(backMotorInput2,GPIO.OUT)
GPIO.setup(frontMotorInput1,GPIO.OUT)
GPIO.setup(frontMotorInput2,GPIO.OUT)

GPIO.output(backMotorInput1,GPIO.HIGH)
GPIO.output(backMotorInput2,GPIO.LOW)
GPIO.output(frontMotorInput1,GPIO.HIGH)
GPIO.output(frontMotorInput2,GPIO.LOW)
time.sleep(2)

GPIO.output(backMotorInput1,GPIO.LOW)
GPIO.output(backMotorInput2,GPIO.HIGH)
GPIO.output(frontMotorInput1,GPIO.LOW)
GPIO.output(frontMotorInput2,GPIO.HIGH)
time.sleep(2)

GPIO.cleanup()