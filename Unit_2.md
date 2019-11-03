
# Unit 2 Reflections

The focus of this unit was the Internet of Things (IoT). Each student in the class was given a kit from SparkFun that contained a 
microbit from the BBC, and electronic components that work with it. We were able to set up circuits and use MicroPython to cause a 
plethora of things to happen such as LEDs to turn on and off, use photoresisters, temperature sensors, the compass and accelerometer 
of the microbit and more. The experiments were fun and interesting. 

The next activity was to develop a project using the microbit. Each person came up with a different project. For my project, I 
purchased a smart robot car from Yahboom that runs off of a microbit. Once the car is assembled, it can do quite a bit when using 
MakeCode, such as obstacle avoidance, tracking, and following, along with lights. It operates via Bluetooth using an iPhone app. 
However, when using Python, Bluetooth does not work. The very minimal Python code was provided by Yahboom. This caused the car to 
move forward indefinitely, full-speed ahead when turned on, and did not allow any control over the car. It also did not work the 
lights or any other features. I used a different microbit’s accelerometer to “steer” the car in combination with the microbit’s 
radio feature. By trial and error (because no documentation was provided) I was able to make the car also steer right, left, backward 
and stop. I am very proud of this accomplishment because it is something I had never tried before, but had always desired to.  I had 
higher hopes to add more features, and did add them to the code, however, because the microbit only have 16kB RAM, I received memory 
errors when adding any additional features. 

Here is a picture of the smart robot car and steering mechanism. I’m choosing to showcase this piece because it represents the 
culmination of my learning in the Unit 2 IoT section. As an additional exercise, I would remove the functionality I put into the 
car (because of lack of memory I would have to remove it), and then see if I could add some of the other, less important features 
such as lights, voice and other things. It is disappointing that not all of these things can be programmed at the same time for this 
little car.

![Yahboom Microbit Robot Car Project](https://github.com/JOYFLOWERS/joyflowers.github.io/blob/master/IMG_4270.jpg)

This is the code that controls the first microbit. This microbit sends messages to the car's microbit to control its direction.

    # Joy Flowers
    # 10/30/19
    import radio
    from microbit import *
    # Starter code for accelerometer came from Steve Brown - BourneToCode.com
    # The radio won't work unless it's switched on.
    radio.on()
    # Event loop.
    # Button A sends a "flash" message.
    # if button_a.is_pressed():
    while True:
        radio.send('flash')  # Start the robot
        sleep(2000)
        x_acc = accelerometer.get_x()
        y_acc = accelerometer.get_y()
        tol = 200
        if x_acc < -1*tol:
            # move left
            left = Image("00900:09000:99999:09000:00900")
            display.show(left)
            radio.send('left')
            sleep(1000)
        elif x_acc > tol:
            # move right
            right = Image("00900:00090:99999:00090:00900")
            display.show(right)
            radio.send('right')
            sleep(1000)
        if y_acc < -1*tol:
            # move forward
            forward = Image("00900:09990:90909:00900:00900")
            display.show(forward)
            radio.send('forward')
            sleep(1000)
        elif y_acc > tol:
            # move backward
            backward = Image("00900:00900:90909:09990:00900")
            display.show(backward)
            radio.send('backward')
            sleep(1000)
            incoming = radio.receive()
            if incoming == 'flash':
                display.show(Image.COW)
        if x_acc >= -1*tol and x_acc <= tol and y_acc >= -1*tol and y_acc <= tol:
            radio.send('stop')
            display.show(Image.HAPPY)
        if button_b.is_pressed():
            radio.send('stop')
            break
            # display.clear()
    radio.off()   

This is the code that was added to the Yahboom Python code in order to made the car move (at a steady speed) backward, left, right, 
forward and to stop.

    def move_car(q12a, q12b, q13a, q13b, q15a, q15b, q14a, q14b):
        pwm.set_pwm(12, q12a, q12b)
        pwm.set_pwm(13, q13a, q13b)
        pwm.set_pwm(15, q15a, q15b)
        pwm.set_pwm(14, q14a, q14b)
    movement = ['forward', 'backward', 'left', 'right', 'stop']
    sleep(5000)
    display.show(Image.HAPPY)
    done = -1
    while done != 0:
        incoming = radio.receive()
        if incoming == 'flash':
            Car_Go = True
            while Car_Go:
                # if button_a.is_pressed(): #from other microbit
                incoming = radio.receive()
                if incoming == movement[0]:
                    move_car(1000, 2000, 0, 0, 1000, 2000, 0, 0)
                elif incoming == movement[1]:
                    move_car(0, 0, 1000, 2000, 0, 0, 1000, 2000)
                elif incoming == movement[2]:
                    move_car(0, 1000, 0, 0, 0, 2000, 0, 0)
                elif incoming == movement[3]:
                    move_car(0, 2000, 0, 0, 0, 1000, 0, 0)
                elif incoming == movement[4]:
                    move_car(0, 0, 0, 0, 0, 0, 0, 0)
                    pwm.set_pwm(3, 0, servo_min)
                    sleep(1000)
                    pwm.set_pwm(3, 0, servo_max)
                    sleep(1000)
                    done = 0
    radio.off()

[Back to About Me README](README.md) 
