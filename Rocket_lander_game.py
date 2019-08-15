# Kelvin
# 2019/07/15
# QI IoT 2019 Summer
# Moon Lander Game
# LanderLander

GRAVITY = -10

position = 100
velocity = 0
acceleration = 0
fuel = 100
thrust = 0

# print initial conditions
print "P: %3d V: %3d F: %3d" % (position, velocity, fuel)

while position > 0:
    # get user input for thrusters
    if fuel > 0:
        thrust = int(raw_input("Set thrusters(0-20): "))
        if thrust >= 20:
            thrust = 20
            print "Thrusters at max(20)!"
        if thrust < 0:
            thrust = 0
            print "No thrusters(0)!"
        if thrust > fuel:
            thrust = fuel
            print "Out of fuel! Thrusters at {0}".format(thrust)
    else:
        print("No fuel -- rocket is in free-fall!")
        thrust = 0

    # calculate new state variables
    fuel = fuel - thrust
    acceleration = GRAVITY + thrust
    position = position + velocity + 0.5*acceleration
    if position < 0:
        position = 0
    velocity = velocity + acceleration

    # print status
    print "P: %3d V: %3d F: %3d" % (position, velocity, fuel)

# print final result
if velocity < -3:
    print "Rocket crashed! Velocity was {0} m/s".format(velocity)
else:
    print "Landing successful!"
