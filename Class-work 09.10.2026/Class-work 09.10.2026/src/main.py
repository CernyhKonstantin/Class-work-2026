
def print_items(title, items):
    print(f"\n{title}")
    print("-" * len(title))

    if not items:
        print("(empty)")
    else:
        for item in sorted(items, key=str.casefold):
            print(item)


# ============================================================
# PART 1 - TASK 1
# Count a fruit in a tuple
# ============================================================

def count_fruit():
    fruits = (
        "apple",
        "banana",
        "orange",
        "apple",
        "kiwi",
        "banana",
        "apple"
    )

    print_items("Available fruits", fruits)

    fruit_name = input("Enter a fruit name to count: ").strip()

    count = sum(
        1 for fruit in fruits
        if fruit.casefold() == fruit_name.casefold()
    )

    print(f'"{fruit_name}" appears {count} time(s) in the tuple.')


# ============================================================
# PART 1 - TASK 2
# Create a tuple with repeated fruits
# ============================================================

def show_fruit_tuple():
    fruits = (
        "apple",
        "banana",
        "orange",
        "apple",
        "kiwi",
        "banana",
        "apple"
    )

    print("Fruit tuple, including repeated fruits:")
    print(fruits)


# ============================================================
# PART 1 - TASK 3
# Replace all exact car manufacturer matches
# ============================================================

def replace_car_manufacturer():
    cars = [
        "Lamborghini",
        "Ferrari",
        "Bentley",
        "Rolls-Royce",
        "Bugatti",
        "Ferrari",
        "Lamborghini",
        "Bugatti",
        "Bentley"
    ]

    print(f"Current car manufacturers: {cars}")

    manufacturer = input(
        "Enter the manufacturer to replace: "
    ).strip()

    replacement = input(
        "Enter the replacement word: "
    ).strip()

    if not manufacturer:
        print("The manufacturer name cannot be empty.")
        return

    if not replacement:
        print("The replacement word cannot be empty.")
        return

    matches = sum(
        1 for car in cars
        if car.casefold() == manufacturer.casefold()
    )

    cars = [
        replacement if car.casefold() == manufacturer.casefold()
        else car
        for car in cars
    ]

    print(f"Replaced {matches} exact match(es).")
    print(f"Updated list: {cars}")


# ============================================================
# PART 2 - TASK 1
# Country set management
# ============================================================

def manage_countries():
    countries = {
        "Germany",
        "Ukraine",
        "France",
        "Italy",
        "Japan"
    }

    while True:
        print("\nCountry Set Manager")
        print("1. Show countries")
        print("2. Add a country")
        print("3. Remove a country")
        print("4. Search countries by characters")
        print("5. Check whether a country exists")
        print("0. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print_items("Countries", countries)

        elif choice == "2":
            country = input("Country to add: ").strip()

            if not country:
                print("Country name cannot be empty.")
            elif any(
                item.casefold() == country.casefold()
                for item in countries
            ):
                print(f'"{country}" already exists.')
            else:
                countries.add(country)
                print(f'Added "{country}".')

        elif choice == "3":
            country = input("Country to remove: ").strip()

            existing = next(
                (
                    item for item in countries
                    if item.casefold() == country.casefold()
                ),
                None
            )

            if existing is None:
                print(f'"{country}" was not found.')
            else:
                countries.remove(existing)
                print(f'Removed "{existing}".')

        elif choice == "4":
            query = input(
                "Enter characters to search for: "
            ).strip()

            matches = {
                country for country in countries
                if query.casefold() in country.casefold()
            }

            print_items("Search results", matches)

        elif choice == "5":
            country = input("Country to check: ").strip()

            found = any(
                item.casefold() == country.casefold()
                for item in countries
            )

            if found:
                print(f'"{country}" is in the set.')
            else:
                print(f'"{country}" is not in the set.')

        elif choice == "0":
            break

        else:
            print("Invalid option. Please choose again.")


# ============================================================
# PART 2 - TASKS 2, 3, 4, 5
# City set operations
# ============================================================

def read_city_set(prompt):
    raw = input(prompt).strip()

    if not raw:
        return set()

    return {
        city.strip()
        for city in raw.split(",")
        if city.strip()
    }


def city_set_operations():
    print("Enter city names separated by commas.")

    first = read_city_set("Cities in the first set: ")
    second = read_city_set("Cities in the second set: ")

    print_items("First city set", first)
    print_items("Second city set", second)

    # Task 2: Cities present in both sets.
    common_cities = first & second
    print_items(
        "Task 2 - Cities in both sets",
        common_cities
    )

    # Task 3: Cities only in the first set.
    first_only = first - second
    print_items(
        "Task 3 - Cities only in the first set",
        first_only
    )

    # Task 4: Cities only in the second set.
    second_only = second - first
    print_items(
        "Task 4 - Cities only in the second set",
        second_only
    )

    # Task 5: Cities that are in exactly one set.
    unique_cities = first ^ second
    print_items(
        "Task 5 - Unique cities in either set",
        unique_cities
    )


# ============================================================
# PART 2 - TASK 6
# Country and capital dictionary management
# ============================================================

def manage_capitals():
    capitals = {
        "Germany": "Berlin",
        "Ukraine": "Kyiv",
        "France": "Paris",
        "Italy": "Rome",
        "Japan": "Tokyo"
    }

    while True:
        print("\nCountry and Capital Dictionary")
        print("1. Show all countries and capitals")
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
                for country in sorted(
                    capitals,
                    key=str.casefold
                ):
                    print(f"{country} -> {capitals[country]}")

        elif choice == "2":
            country = input("Country name: ").strip()
            capital = input("Capital city: ").strip()

            if not country or not capital:
                print("Both country and capital are required.")
                continue

            existing = next(
                (
                    item for item in capitals
                    if item.casefold() == country.casefold()
                ),
                None
            )

            if existing:
                print(
                    f'"{existing}" already exists. '
                    "Use the replace option to change its capital."
                )
            else:
                capitals[country] = capital
                print(f"Added: {country} -> {capital}")

        elif choice == "3":
            country = input("Country to delete: ").strip()

            existing = next(
                (
                    item for item in capitals
                    if item.casefold() == country.casefold()
                ),
                None
            )

            if existing:
                del capitals[existing]
                print(f'Deleted "{existing}".')
            else:
                print(f'"{country}" was not found.')

        elif choice == "4":
            country = input("Country to search for: ").strip()

            existing = next(
                (
                    item for item in capitals
                    if item.casefold() == country.casefold()
                ),
                None
            )

            if existing:
                print(f"{existing} -> {capitals[existing]}")
            else:
                print(f'"{country}" was not found.')

        elif choice == "5":
            country = input(
                "Country whose capital should change: "
            ).strip()

            existing = next(
                (
                    item for item in capitals
                    if item.casefold() == country.casefold()
                ),
                None
            )

            if not existing:
                print(
                    f'"{country}" was not found. '
                    "Add the country first."
                )
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
            print("Invalid option. Please choose again.")


# ============================================================
# PART 3 - HIGHER-ORDER FUNCTIONS
# Draw a horizontal or vertical line
# ============================================================

def show_horizontal_line(symbol):
    print(symbol * 20)


def show_vertical_line(symbol):
    for _ in range(10):
        print(symbol)


def show_line(symbol, function_to_call):
    """
    Higher-order function:
    receives another function as an argument and calls it.
    """
    function_to_call(symbol)


def line_menu():
    print("\nLine Drawing")
    print("1. Draw a horizontal line")
    print("2. Draw a vertical line")

    symbol_input = input("Enter a symbol: ")

    if not symbol_input:
        print("Please enter a symbol.")
        return

    symbol = symbol_input[0]

    choice = input("Choose a line type (1 or 2): ").strip()

    if choice == "1":
        show_line(symbol, show_horizontal_line)

    elif choice == "2":
        show_line(symbol, show_vertical_line)

    else:
        print("Invalid choice.")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        print("\n" + "=" * 48)
        print("CLASS-WORK 09.10.2026")
        print("Python: Tuples, Sets, Dictionaries, Functions")
        print("=" * 48)

        print("\nPART 1 - TUPLES AND LISTS")
        print("1. Count a fruit in a tuple")
        print("2. Display a tuple with repeated fruits")
        print("3. Replace a car manufacturer")

        print("\nPART 2 - SETS AND DICTIONARIES")
        print("4. Manage a set of countries")
        print("5. Perform city set operations")
        print("6. Manage country-capital dictionary")

        print("\nPART 3 - HIGHER-ORDER FUNCTIONS")
        print("7. Draw a horizontal or vertical line")

        print("\n0. Exit")

        choice = input("\nChoose a task: ").strip()

        if choice == "1":
            count_fruit()

        elif choice == "2":
            show_fruit_tuple()

        elif choice == "3":
            replace_car_manufacturer()

        elif choice == "4":
            manage_countries()

        elif choice == "5":
            city_set_operations()

        elif choice == "6":
            manage_capitals()

        elif choice == "7":
            line_menu()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()