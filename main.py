catalog = [
    {('mersedes', 's'): {
        'price': 2000,
        'двигатель': 3,
        'привод': 'задний',
        'разгон до 100': 6.2,
        'выпуск': 2018,
        'страна': 'Германия'
        }
    },
    {('bmw', 'm5'): {
        'price': 2500,
        'двигатель': 4.4,
        'привод': 'полный',
        'разгон до 100': 3.4,
        'выпуск': 2020,
        'страна': 'Германия'
        }
    },
    {('audi', 'a8'): {
        'price': 2300,
        'двигатель': 3.0,
        'привод': 'полный',
        'разгон до 100': 5.6,
        'выпуск': 2019,
        'страна': 'Германия'
        }
    },
    {('toyota', 'camry'): {
        'price': 1200,
        'двигатель': 2.5,
        'привод': 'передний',
        'разгон до 100': 8.3,
        'выпуск': 2021,
        'страна': 'Япония'
        }
    },
    {('honda', 'accord'): {
        'price': 1300,
        'двигатель': 2.0,
        'привод': 'передний',
        'разгон до 100': 7.6,
        'выпуск': 2020,
        'страна': 'Япония'
        }
    },
    {('ford', 'mustang'): {
        'price': 2800,
        'двигатель': 5.0,
        'привод': 'задний',
        'разгон до 100': 4.2,
        'выпуск': 2017,
        'страна': 'США'
        }
    },
    {('chevrolet', 'camaro'): {
        'price': 2600,
        'двигатель': 6.2,
        'привод': 'задний',
        'разгон до 100': 4.0,
        'выпуск': 2018,
        'страна': 'США'
        }
    },
    {('kia', 'stinger'): {
        'price': 2000,
        'двигатель': 3.3,
        'привод': 'полный',
        'разгон до 100': 4.9,
        'выпуск': 2021,
        'страна': 'Южная Корея'
        }
    },
    {('volvo', 's90'): {
        'price': 2200,
        'двигатель': 2.0,
        'привод': 'полный',
        'разгон до 100': 6.1,
        'выпуск': 2020,
        'страна': 'Швеция'
        }
    },
    {('porsche', '911'): {
        'price': 5000,
        'двигатель': 3.8,
        'привод': 'задний',
        'разгон до 100': 3.2,
        'выпуск': 2022,
        'страна': 'Германия'
        }
    }
]

index = 0
while index < len(catalog):
    installment = list(catalog[index].values())[0]
    if installment['price'] > 3000:
        installment.update({'рассрочка': False})
    else:
        installment.update({'рассрочка': True})
    index += 1


def find_cars(catalog, param, kriteriy):
    result = []
    for car in catalog:
        car_name, car_info = list(car.items())[0]
        if car_info.get(param) == kriteriy:
            result.append(car_name)
    return result

param = input("Введите параметр для поиска: ").strip()
value = input("Введите значение для параметра: ").strip()

if value.isdigit():
    value = int(value)
elif value.lower() == 'true':
    value = True
elif value.lower() == 'false':
    value = False

selected_cars = find_cars(catalog, param, value)
if selected_cars:
    print("Подходящие машины:", selected_cars)
else:
    print("Машин, подходящих под эти критерии, не найдено.")