price = [57.5, 46.51, 97, 456.44, 79.03, 9.99, 15.35, 29.88, 7897.55, 99.99, 199.99]
price_list = []
for el in price:
    rub = int(el)
    k = round((el - rub) * 100)
    price_list.append(f"{rub} руб {k:02d} коп")
    ' ,'.join(price_list)
    print(price_list)