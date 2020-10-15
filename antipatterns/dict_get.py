jack = {
    'name': 'Jack',
    'car': 'BMW'
}

car_anti = jack['car']  # антипаттерн: у jack'а может и не быть 'car'

# лучше так, если 'car' нет, вернёт 'нет машины'
car = jack.get('car', 'нет машины')

print(car)
