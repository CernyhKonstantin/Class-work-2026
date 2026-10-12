class Person:
    def __init__(
        self,
        full_name="Unknown",
        age=0,
        date_of_birth="Unknown",
        contact_phone="Unknown",
        city="Unknown",
        country="Unknown",
        home_address="Unknown",
    ):
        self.full_name = full_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.contact_phone = contact_phone
        self.city = city
        self.country = country
        self.home_address = home_address


    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, new_name):
        if not new_name or not new_name.strip():
            raise ValueError("Full name cannot be empty")
        self.__full_name = new_name.strip()


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age >= 120:
            raise ValueError(f"Invalid Age {new_age}")
        self.__age = new_age


    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, new_dob):
        self.__date_of_birth = new_dob.strip() if new_dob else "Unknown"


    @property
    def contact_phone(self):
        return self.__contact_phone

    @contact_phone.setter
    def contact_phone(self, new_phone):
        self.__contact_phone = new_phone.strip() if new_phone else "Unknown"


    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city.strip() if new_city else "Unknown"


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        self.__country = new_country.strip() if new_country else "Unknown"


    @property
    def home_address(self):
        return self.__home_address

    @home_address.setter
    def home_address(self, new_address):
        self.__home_address = new_address.strip() if new_address else "Unknown"

    def input_data(self):
        """Read all person details from the keyboard."""
        print("\nEnter person details. Press Enter to keep current values.")

        name_input = input("Full name: ").strip()
        if name_input:
            try:
                self.full_name = name_input
            except ValueError as e:
                print(f"Error: {e}. Name was not updated.")

        age_input = input("Age: ").strip()
        if age_input:
            try:
                self.age = int(age_input)
            except ValueError as e:
                print(f"Error: {e}. Age was not updated.")

        dob_input = input("Date of birth (DD.MM.YYYY): ").strip()
        if dob_input:
            self.date_of_birth = dob_input

        phone_input = input("Contact phone: ").strip()
        if phone_input:
            self.contact_phone = phone_input

        city_input = input("City: ").strip()
        if city_input:
            self.city = city_input

        country_input = input("Country: ").strip()
        if country_input:
            self.country = country_input

        address_input = input("Home address: ").strip()
        if address_input:
            self.home_address = address_input

    def show_data(self):
        """Display all person details."""
        print("\nPerson Details")
        print("--------------")
        print(f"Full name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Date of birth: {self.date_of_birth}")
        print(f"Contact phone: {self.contact_phone}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Home address: {self.home_address}")

    def __str__(self):
        return (
            f"Person: {self.full_name}, "
            f"Age: {self.age}, "
            f"Date of birth: {self.date_of_birth}, "
            f"Phone: {self.contact_phone}, "
            f"City: {self.city}, "
            f"Country: {self.country}, "
            f"Home address: {self.home_address}"
        )


def main():
    person1 = Person()

    while True:
        print("\nPERSON MANAGEMENT")
        print("1. Enter person data")
        print("2. Display person data")
        print("3. Display object using __str__")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            person1.input_data()
        elif choice == "2":
            person1.show_data()
        elif choice == "3":
            print(person1)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
