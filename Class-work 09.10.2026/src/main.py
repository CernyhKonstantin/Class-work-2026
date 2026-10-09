def show_items(title, items):
    print(f"\n{title}")
    print("-" * len(title))
    if not items:
        print("(empty)")
    else:
        for item in sorted(items, key=str.casefold):
            print(item)


def task1_count_fruit():
    fruits = ("apple", "banana", "orange", "apple", "kiwi", "banana", "apple")
    print(f"Fruit tuple: {fruits}")
    name = input("Enter a fruit name to count: ").strip()
    count = sum(1 for fruit in fruits if fruit.casefold() == name.casefold())
    print(f'"{name}" appears {count} time(s) in the tuple.')


def task2_repeated_fruits():
    fruits = ("apple", "banana", "orange", "apple", "kiwi", "banana", "apple")
    print("Tuple containing repeated fruits:")
    print(fruits)


def task3_replace_car():
    cars = [
        "Lamborghini", "Ferrari", "Bentley", "Rolls-Royce", "Bugatti",
        "Ferrari", "Lamborghini", "Bugatti", "Bentley"
    ]
    print(f"Current car manufacturers: {cars}")
    target = input("Enter the manufacturer to replace: ").strip()
    replacement = input("Enter the replacement word: ").strip()
    if not target or not replacement:
        print("Both the manufacturer and replacement must be non-empty.")
        return
    count = sum(1 for car in cars if car.casefold() == target.casefold())
    cars = [replacement if car.casefold() == target.casefold() else car for car in cars]
    print(f"Replaced {count} exact match(es).")
    print(f"Updated list: {cars}")


def task4_manage_countries():
    countries = {"Germany", "Ukraine", "France", "Italy", "Japan"}
    while True:
        print("\nCountry Set Manager")
        print("1. Show countries")
        print("2. Add a country")
        print("3. Remove a country")
        print("4. Search by entered characters")
        print("5. Check whether a country exists")
        print("0. Return to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_items("Countries", countries)
        elif choice == "2":
            country = input("Country to add: ").strip()
            if country:
                countries.add(country)
                print(f'"{country}" is in the set.')
            else:
                print("Country name cannot be empty.")
        elif choice == "3":
            country = input("Country to remove: ").strip()
            match = next((item for item in countries if item.casefold() == country.casefold()), None)
            if match is None:
                print(f'"{country}" was not found.')
            else:
                countries.remove(match)
                print(f'Removed "{match}".')
        elif choice == "4":
            query = input("Enter characters to search for: ").strip().casefold()
            matches = {country for country in countries if query in country.casefold()}
            show_items("Search results", matches)
        elif choice == "5":
            country = input("Country to check: ").strip()
            found = any(item.casefold() == country.casefold() for item in countries)
            print(f'"{country}" {"is" if found else "is not"} in the set.')
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def read_city_set(prompt):
    text = input(prompt).strip()
    return {city.strip() for city in text.split(",") if city.strip()}


def task5_city_set_operations():
    print("Enter city names separated by commas.")
    first = read_city_set("Cities in the first set: ")
    second = read_city_set("Cities in the second set: ")
    show_items("First set", first)
    show_items("Second set", second)
    show_items("Task 2 - Cities in both sets (intersection)", first & second)
    show_items("Task 3 - Cities only in the first set", first - second)
    show_items("Task 4 - Cities only in the second set", second - first)
    show_items("Task 5 - Unique cities from either set (symmetric difference)", first ^ second)


def task6_manage_capitals():
    capitals = {
        "Germany": "Berlin",
        "Ukraine": "Kyiv",
        "France": "Paris",
        "Italy": "Rome",
        "Japan": "Tokyo",
    }
    while True:
        print("\nCountry-Capital Dictionary")
        print("1. Show all entries")
        print("2. Add a country and capital")
        print("3. Delete a country")
        print("4. Search for a country")
        print("5. Replace a country's capital")
        print("0. Return to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            if not capitals:
                print("(empty)")
            else:
                for country in sorted(capitals, key=str.casefold):
                    print(f"{country} -> {capitals[country]}")
        elif choice == "2":
            country = input("Country name: ").strip()
            capital = input("Capital city: ").strip()
            if not country or not capital:
                print("Both country and capital are required.")
                continue
            existing = next((item for item in capitals if item.casefold() == country.casefold()), None)
            if existing:
                print(f'"{existing}" already exists. Use the replace option to change its capital.')
            else:
                capitals[country] = capital
                print(f"Added: {country} -> {capital}")
        elif choice == "3":
            country = input("Country to delete: ").strip()
            existing = next((item for item in capitals if item.casefold() == country.casefold()), None)
            if existing:
                del capitals[existing]
                print(f'Deleted "{existing}".')
            else:
                print(f'"{country}" was not found.')
        elif choice == "4":
            country = input("Country to search for: ").strip()
            existing = next((item for item in capitals if item.casefold() == country.casefold()), None)
            if existing:
                print(f"{existing} -> {capitals[existing]}")
            else:
                print(f'"{country}" was not found.')
        elif choice == "5":
            country = input("Country whose capital should change: ").strip()
            existing = next((item for item in capitals if item.casefold() == country.casefold()), None)
            if not existing:
                print(f'"{country}" was not found. Add it first.')
                continue
            new_capital = input("New capital city: ").strip()
            if not new_capital:
                print("Capital city cannot be empty.")
                continue
            capitals[existing] = new_capital
            print(f"Updated: {existing} -> {new_capital}")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def main():
    while True:
        print("\n" + "=" * 48)
        print("CLASS-WORK 09.10.2026")
        print("Tuples, Sets, and Dictionaries")
        print("=" * 48)
        print("PART 1")
        print("1. Count a fruit in a tuple")
        print("2. Display a tuple with repeated fruits")
        print("3. Replace a car manufacturer in a list")
        print("\nPART 2")
        print("4. Manage a set of countries")
        print("5. Perform city set operations (Tasks 2-5)")
        print("6. Manage country-capital dictionary")
        print("0. Exit")
        choice = input("Choose a task: ").strip()

        if choice == "1":
            task1_count_fruit()
        elif choice == "2":
            task2_repeated_fruits()
        elif choice == "3":
            task3_replace_car()
        elif choice == "4":
            task4_manage_countries()
        elif choice == "5":
            task5_city_set_operations()
        elif choice == "6":
            task6_manage_capitals()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
