
class SalaryTooLowException(Exception):
    def __init__(self, message="Salary is less than ₹1,00,000. Access Denied!"):
        super().__init__(message)



class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__fuel_type = fuel_type
        self.__transmission = transmission
        self.__color = color

    def get_details(self):
        return {
            "Brand": self.__brand,
            "Model": self.__model,
            "Price": self.__price,
            "Fuel Type": self.__fuel_type,
            "Transmission": self.__transmission,
            "Color": self.__color
        }

    def get_model(self):
        return self.__model

class Showroom:
    def __init__(self):
        self.inventory = []

    
    def view_cars(self):
        if not self.inventory:
            print("No cars available in the showroom.")
        else:
            print("\nAvailable Cars:")
            for i, car in enumerate(self.inventory, 1):
                print(f"{i}. {car.get_model()}")

    def display_car_details(self, model, salary):
        try:
            if salary < 100000:
                raise SalaryTooLowException()
            for car in self.inventory:
                if car.get_model().lower() == model.lower():
                    print("\nCar Details:")
                    for key, value in car.get_details().items():
                        print(f"{key}: {value}")
                    return
            print("Car not found in inventory.")
        except SalaryTooLowException as e:
            print(e)

    
    def sell_car(self, model):
        for car in self.inventory:
            if car.get_model().lower() == model.lower():
                self.inventory.remove(car)
                print(f"{model} has been sold and removed from inventory.")
                return
        print("Car not found in inventory.")

    def buy_car(self, car):
        self.inventory.append(car)
        print(f"{car.get_model()} has been added to the inventory.")


def main():
    showroom = Showroom()

    
    showroom.buy_car(Car("Toyota", "Fortuner", 3500000, "Diesel", "Automatic", "White"))
    showroom.buy_car(Car("Honda", "Civic", 1800000, "Petrol", "Manual", "Black"))
    showroom.buy_car(Car("Maruti", "Swift", 800000, "Petrol", "Automatic", "Red"))

    while True:
        print("\n--- Car Showroom Management System ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            showroom.view_cars()

        elif choice == "2":
            model = input("Enter car model to view details: ")
            salary = int(input("Enter your salary: "))
            showroom.display_car_details(model, salary)

        elif choice == "3":
            model = input("Enter car model to sell: ")
            showroom.sell_car(model)

        elif choice == "4":
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = int(input("Enter price: "))
            fuel = input("Enter fuel type: ")
            transmission = input("Enter transmission: ")
            color = input("Enter color: ")
            new_car = Car(brand, model, price, fuel, transmission, color)
            showroom.buy_car(new_car)

        elif choice == "5":
            print("Exiting... Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
