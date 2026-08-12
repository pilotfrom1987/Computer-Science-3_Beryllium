def calculate_space_weight(earth_weight, destination):
    earth_weight = float(earth_weight)
    if destination == "mars":
        return earth_weight * 0.36
    elif destination == "jupiter":
        return earth_weight * 2.34
    elif destination == "the moon" or destination == "moon":
        return earth_weight * 0.16
    else:
        print("Invalid destination")
        return 0
    
earth_weight = input("Enter your weight on Earth (in kilograms): ")
destination = input("Enter your destination (mars, jupiter, the moon): ")
print("your weight on " + destination + " is " + str(calculate_space_weight(earth_weight, destination)) + " kilograms")