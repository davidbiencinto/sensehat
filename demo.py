from sense_hat import SenseHat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

import time
from signal import pause

sense = SenseHat()

print("DEMO LUZ...")

X = [0, 0, 0]  # Red
O = [0, 0, 0]  # White

clear = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

X = [255, 0, 0]  # Red
O = [20, 20, 20]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

X = [255, 0, 0]  # Red
O = [80, 80, 80]  # White

hearth = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(clear)

for x in range(5):
    sense.set_pixels(question_mark)
    time.sleep(0.5)
    sense.set_pixels(hearth)
    time.sleep(0.5)

sense.set_pixels(clear)

print()
print("DEMO SENSORES....")
humidity = sense.get_humidity()
print("Humedad: %s %%rH" % humidity)
# alternatives
print(sense.humidity)

temp = sense.get_temperature()
print("Temperature: %s C" % temp)
# alternatives
print(sense.temp)
print(sense.temperature)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)
# alternatives
print(sense.pressure)

orientation_rad = sense.get_orientation_radians()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))
# alternatives
print(sense.orientation_radians)

orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
# alternatives
print(sense.orientation)

north = sense.get_compass()
print("North: %s" % north)
# alternatives
print(sense.compass)

raw = sense.get_compass_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))
# alternatives
print(sense.compass_raw)

gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
# alternatives
print(sense.gyro)
print(sense.gyroscope)

raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))
# alternatives
print(sense.gyro_raw)
print(sense.gyroscope_raw)

accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
# alternatives
print(sense.accel)
print(sense.accelerometer)

raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))
# alternatives
print(sense.accel_raw)
print(sense.accelerometer_raw)

# event = sense.stick.wait_for_event()
# print("The joystick was {} {}".format(event.action, event.direction))
# time.sleep(0.1)
# event = sense.stick.wait_for_event()
# print("The joystick was {} {}".format(event.action, event.direction))

print()
print("DIRECCIONES")
x = 3
y = 3
sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
refresh()
pause()