def main():
    fuel = 0

    with open("puzzle1.txt", "r") as file:
        for index, line in enumerate(file):
            fuel_module = get_fuel_for_module(int(line))
            fuel = fuel + fuel_module

            print("Module {}: {}".format(index, fuel_module))
            print("Fuel: {}".format(fuel))
    
    print("Final fuel: {}".format(fuel))


def get_fuel_for_mass(mass):
    return (mass // 3) - 2


def get_fuel_for_module(mass):
    fuel_total = 0
    fuel_init = get_fuel_for_mass(mass)

    while fuel_init > 0:
        fuel_total = fuel_total + fuel_init
        fuel_init = get_fuel_for_mass(fuel_init)

    return fuel_total


if __name__ == "__main__":
    main() 