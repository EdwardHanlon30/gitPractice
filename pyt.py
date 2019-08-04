class Calculator():
    __sum = 0
    def __init__(self):
        super()

    def  add(self, value_1 , value_2):
        self.__sum = value_1 + value_2
        return self.__sum

    def subtract(self, value_1, value_2):
        self.__sum = value_1 - value_2
        return self.__sum

    def multiply(self, value_1, value_2):
        self.__sum = value_1 * value_2
        return self.__sum

    def division(self, value_1, value_2):
        self.__sum = value_1  //  value_2
        return self.__sum
    
    def expotent(self, value_1, value_2):
        self.__sum = value_1 ** value_2
        return self.__sum

    def remainder(self, value_1, value_2):
        self.__sum = value_1 % value_2
        return self.__sum

    def displayMenu(self):
        running = True
        while running:
            print("Welcome to the python calculator")
            print("Press 1 for addition")
            print("Press 2 for subtraction")
            print("Press 3 for multiplication")
            print("Press 4 for Division")
            print("Press 5 for Expotents")
            print("Press 6 for Remainders")
            print("Press 7 to Quit the program")
            choice = int(input("Please make your choice now => "))
            if choice == 7:
                running = False
                return
                
            switch = {
                1:self.add,
                2:self.subtract,
                3:self.multiply,
                4:self.division,
                5:self.expotent,
                6:self.remainder
                }
            value_1 = int(input("Please enter the first value => "))
            value_2 = int(input("Please enter the second value => "))
            funk = switch.get(choice)
            sumOfValues = funk(value_1, value_2)
            print(sumOfValues)

def main():
    calc = Calculator()
    calc.displayMenu()

main()
