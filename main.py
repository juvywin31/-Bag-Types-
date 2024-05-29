from abc import ABC, abstractmethod  # Import the Abstract Base Class and abstractmethod to create abstract classes and methods

# Define an abstract class Bag to enforce a common interface
class Bag(ABC):  # Abstract base class for different types of bags
    @abstractmethod
    def display_info(self):  # Abstract method to display information about the bag
        pass  # No implementation in the base class, as it is meant to be overridden by subclasses

# Define the Handbag class inheriting from Bag
class Handbag(Bag):  # Subclass of Bag, representing a handbag
    def __init__(self, brand, material, color, size):  # Constructor to initialize a handbag
        # Encapsulated attributes to restrict direct access
        self.__brand = brand
        self.__material = material
        self.__color = color
        self.__size = size

    def get_brand(self):  # Getter method to access the brand attribute
        return self.__brand

    def set_brand(self, brand):  # Setter method to change the brand attribute
        self.__brand = brand

    def display_info(self):  # Implementation of the abstract method from Bag class
        return f"A {self.__color} {self.__size}-sized {self.__material} handbag by {self.__brand}"  # Return a formatted string describing the handbag

# Define a derived class ToteBag inheriting from Bag
class ToteBag(Bag):  # Subclass of Bag, representing a tote bag
    # Constructor with additional attribute for strap length
    def __init__(self, brand, material, color, size, strap_length):
        # Encapsulated attributes
        self.__brand = brand
        self.__material = material
        self.__color = color
        self.__size = size
        self.__strap_length = strap_length

    def display_info(self):  # Implementation of the abstract method from Bag class
        return f"A {self.__color} {self.__size}-sized {self.__material} tote bag by {self.__brand} with strap length {self.__strap_length} inches"

# Create instances of Handbag and ToteBag
handbag1 = Handbag("Louis Vuitton", "leather", "black", "medium")
handbag2 = Handbag("Gucci", "suede", "brown", "small")
totebag1 = ToteBag("Prada", "canvas", "blue", "large", 24)
totebag2 = ToteBag("Michael Kors", "nylon", "red", "extra large", 28)

# Display information about each bag
print(handbag1.display_info())
print("------------------------------------------------------")
print(handbag2.display_info())
print("------------------------------------------------------")
print(totebag1.display_info())
print("------------------------------------------------------")
print(totebag2.display_info())
