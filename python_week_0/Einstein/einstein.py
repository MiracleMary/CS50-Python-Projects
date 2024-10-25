def energy(mass):
    speed_of_light = 300000000
    energy = mass* (speed_of_light  **2)
    return energy


def main():
    mass = int(input("mass in kilogram is: "))
    energy_in_joules = energy(mass)
    print ("Energy in joules:", energy_in_joules)


if __name__=="__main__":
    main()
