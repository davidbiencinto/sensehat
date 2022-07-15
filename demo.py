from sense_hat import SenseHat
import time


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

X = [255, 0, 255]  # Red
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
    time.sleep(1.1)
    sense.set_pixels(hearth)
    time.sleep(1.1)

sense.set_pixels(clear)


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

event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
time.sleep(0.1)
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))