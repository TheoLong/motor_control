leftpwm="P9_14"
left1="P9_11"
left2="P9_12"
rightpwm="p9_16"
right1="P9_13"
right2="P9_15"


def moveLeft(power)
	power=0.0
	power=velocity*7.9
	power=round(power,0)
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
	if power == 0
		GPIO.output"(P9_11", GPIO.LOW);
                GPIO.output("P9_12", GPIO.LOW);
                PWM.set_duty_cycle("P9_14",0)
def moveLeft(power)
	power=0.0
	power=velocity*7.9
	power=round(power,0)
	#if power > 0, moving forward
	if power>0:
                GPIO.output(right1, GPIO.LOW);
                GPIO.output(right2, GPIO.HIGH);
                PWM.set_duty_cycle(rightpwm,power)
	#if power < 0, move backward
	if power<0:
		power=abs(power)
		GPIO.output(right1, GPIO.HIGH);
                GPIO.output(right2, GPIO.LOW);
                PWM.set_duty_cycle(rightpwm,power)
	#if power = 0, stop
	if power == 0
		power=round(power)
		GPIO.output(right1, GPIO.LOW);
                GPIO.output(right2, GPIO.LOW);
                PWM.set_duty_cycle(rightpwm,0)
		

