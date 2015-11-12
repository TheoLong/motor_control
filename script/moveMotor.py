import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO




def moveLeft(velocity):
	print("move left")
	power=0.0
	power=velocity*4
	power=round(power,0)
	power=int(power)
	#if power > 0, moving forward
	if power>0:
                GPIO.output("P9_11", GPIO.LOW);
                GPIO.output("P9_12", GPIO.HIGH);
                PWM.set_duty_cycle("P9_14",power)
	#if power < 0, move backward
	if power<0:
		power=abs(power)
		GPIO.output("P9_11", GPIO.HIGH);
                GPIO.output("P9_12", GPIO.LOW);
                PWM.set_duty_cycle("P9_14",power)
	#if power = 0, stop
	if power == 0:
		GPIO.output("P9_11", GPIO.LOW);
                GPIO.output("P9_12", GPIO.LOW);
                PWM.set_duty_cycle("P9_14",0)
def moveRight(velocity):
	print("move left")
	rightpwm="p9_16"
	right1="P9_13"
	right2="P9_15"
	power=0.0
	power=velocity*4
	power=round(power,0)
	power=int(power)
	#if power > 0, moving forward
	if power>0:
                GPIO.output("P9_13", GPIO.LOW);
                GPIO.output("P9_15", GPIO.HIGH);
                PWM.set_duty_cycle("p9_16",power)
	#if power < 0, move backward
	if power<0:
		power=abs(power)
		GPIO.output("P9_15", GPIO.HIGH);
                GPIO.output("P9_15", GPIO.LOW);
                PWM.set_duty_cycle("p9_16",power)
	#if power = 0, stop
	if power == 0:
		power=round(power)
		GPIO.output("P9_13", GPIO.LOW);
                GPIO.output("P9_15", GPIO.LOW);
                PWM.set_duty_cycle("p9_16",0)
		

