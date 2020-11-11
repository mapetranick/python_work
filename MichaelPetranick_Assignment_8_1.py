class Vehicle: #CLASS VEHICLE

    def __init__(self, make, model, color, fuelType, options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getFuelType(self):
        return self.fuelType

    def getOptions(self):
        return self.options

class Car(Vehicle):
    def __init__(self, make, model, color, engineSize, numDoors, fuelType, options):
        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors
    
    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

class Truck(Vehicle):
    def __init__(self, make, model, color, fuelType, cabStyle, bedLength, options):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle(self):
        return self.cabStyle

    def getBedLength(self):
        return self.bedLength

c = Car("Ford", "Mustang", "Black", "V6", "2-door", "Unleaded", ['Bluetooth', 'cruise control'])

t = Truck("Ford", "F-150", "Blue", "Regular", "Extended", "Diesel", ['Bluetooth', 'Stereo'])

VirtualGarage = []
VirtualGarage.append(c)
VirtualGarage.append(t)
i=1
while i == 1:
    print('-----MENU-----')
    print("1. Add Car\n2. Add Truck\n3. Exit\n4. Show virtual garage")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        make = input("Make: ")
        model = input("Model: ")
        color = input("Color: ")
        engineSize = input("Engine size: ")
        numDoors = input("2-Door or 4-Door: ")
        fuelType = input("Fuel Type: ")
        options = input("Enter options: ")

        c1 = Car(make, model, color, engineSize, numDoors, fuelType, [options])
        VirtualGarage.append(c1)
    
    elif choice == 2:
        make = input("Make: ")
        model = input("Model: ")
        color = input("Color: ")
        cabStyle = input("Cab Style (Regular or Extended): ")
        bedLength = input("Bed Length (Regular or Extended): ")
        fuelType = input("Fuel Type: ")
        options = input("Enter options: ")
      
        t1 = Truck(make, model, color, cabStyle, bedLength, fuelType, [options])
        VirtualGarage.append(t1)
      
    elif choice == 3:
        i=0

    elif choice == 4:
        print("-----Your Garage-----")
        for c in VirtualGarage:
            print(c.getMake(), c.getModel(), c.getColor(), c.getEngineSize(), c.getNumDoors() + "-door", c.getFuelType(), c.getOptions())
        
        for t in VirtualGarage:
            print(t.getMake(), t.getModel(), t.getColor(), t.getCabStyle(), t.getBedLength(), t.getFuelType(), t.getOptions())