from data import purchases


# Функция рассчёта и вывода общей выручки
def total_revenue(purchases: list) -> str:
    total = 0
    for p in purchases:
        total += p['price'] * p['quantity']

    print(f'Общая выручка: {total}')


# total_revenue(purchases)

#-----------------------------------------

# Фунцкия вывода словаря с уникальными покупками по категории
def items_by_category(purchases: list) -> dict:

    result_dict = {}
    for p in purchases:
        cat = p['category']
        item = p['item']
        result_dict[cat] = result_dict.get(cat, [])
        if item not in result_dict[cat]:
            result_dict[cat].append(item)

    print(f'Товары по категориям: {result_dict}')


# items_by_category(purchases)

#-----------------------------------------

# Функция вывода всех покупок, большей или равной некой min_price
def expensive_purchases(purchases: list, min_price: float = 1.0) -> list:
    result_list = [p for p in purchases if p['price'] >= min_price]

    print(f'Покупки дороже {min_price}: {result_list}')

# expensive_purchases(purchases, 1.0)

#-----------------------------------------

# Функция рассчёта и вывода средней цены товаров по каждой категории
def average_price_by_category(purchases: list) -> dict:
    result_dict = {}
    items_set = set()

    for p in purchases:
        cat = p['category']
        item = p['item']
        price = p['price']
        if item not in items_set:
            result_dict[cat] = result_dict.get(cat, []) + [price]
            items_set.add(item)

    result_dict = {k: (sum(v)/len(v)) for k, v in result_dict.items()}
    print(f'Средняя цена по категориям: {result_dict}')

# average_price_by_category(purchases)

#-----------------------------------------

# Функция вывода категории с наибольшим количеством купленного товара в штуках
def most_frequent_category(purchases: list) ->str:
    result_dict = {}

    for p in purchases:
        cat = p['category']
        price = p['price']
        quantity = p['quantity']
        result_dict[cat] = result_dict.get(cat, 0) + price * quantity

    print(f'Категория с наибольшим количеством проданных товаров: {max(result_dict, key=result_dict.get)}')

# most_frequent_category(purchases)

# Конечный вывод:
def main():
    total_revenue(purchases)
    items_by_category(purchases)
    expensive_purchases(purchases)
    average_price_by_category(purchases)
    most_frequent_category(purchases)


if __name__ == '__main__':
    main()

















