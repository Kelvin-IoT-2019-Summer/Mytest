# author  Kelvin
# date    07-10-2019
# email   ffotturish@gmail.com

def Rocket_lander():
    P = 100  # Position
    V = 0  # Velocity
    F = 100  # Fuel
    G = -10  # Gravity
    A = 0  # Acceleration

    while P > 0:
        if F <= 0:
            while True:
                if P <= 0:
                    break
                F = 0
                print "P: %2d V:%2d F:%2d" % (P, V, F)
                print "No fuel -- rocket is in free-fall!"
                t = 0
                A = G + t
                P = P + V + (A * 0.5)
                V += A
            break
        print "P: %2d V:%2d F:%2d" % (P, V, F)
        t = int(input("Set thrusters(0-20): "))
        if t > F:
            print "Out of fuel! Thrusters at %d" % F
            A = G + F
            F = 0
            P = P + V + (A * 0.5)
            V += A
            continue
        if t < 0:
            print "No thrusters(0)!"
            t = 0
        elif t > 20:
            print "Thrusters at max(20)!"
            t = 20
        F -= t
        A = G + t
        P = P + V + (A*0.5)
        V += A

    P = 0
    print "P: %2d V:%2d F:%2d" % (P, V, F)
    if V > -3:
        print "Landing successful!"
    else:
        print "Rocket crashed! Velocity was %d m/s" % V

Rocket_lander()
