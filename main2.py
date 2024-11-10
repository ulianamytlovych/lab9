def create_vegetable_info():

    vegetable_info = []

    while True:
        print("Введіть відомості про овочеву культуру:")

        name = input("Назва культури: ")
        country_of_origin = input("Країна походження насіння: ")
        try:
            yield_per_hectare = float(input("Середня врожайність (ц/Га): "))
        except ValueError:
            print("Невірний формат врожайності. Повторіть введення.")
            continue

        pest_control = input("Необхідність обробки від шкідників (так/ні): ").lower()
        if pest_control not in ['так', 'ні']:
            print("Введіть 'так' або 'ні' для обробки від шкідників.")
            continue

        harvesting_method = input("Метод збирання врожаю: ")

        vegetable = {
            "Назва культури": name,
            "Країна походження насіння": country_of_origin,
            "Середня врожайність (ц/Га)": yield_per_hectare,
            "Необхідність обробки від шкідників": pest_control,
            "Метод збирання врожаю": harvesting_method
        }

        vegetable_info.append(vegetable)

        another = input("Хочете ввести відомості ще про одну культуру? (так/ні): ").lower()
        if another != 'так':
            break

    return vegetable_info


def display_vegetable_info(vegetable_info):
    print("\n Відомості про овочеві культури:")
    for veg in vegetable_info:
        print("\n----------------------------")
        for key, value in veg.items():
            print(f"{key}: {value}")
        print("----------------------------")


vegetable_info = create_vegetable_info()

display_vegetable_info(vegetable_info)
