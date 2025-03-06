import csv

def read_with_csv(file_name):
    data = []
    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i in reader:
            data.append(i)
    return data


def save_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def extend_data(data):
    data[0].append("Rent per Sq M")
    data[0].append("Avg Rent in Locality")

    # Словарь для хранения общей суммы аренды и количества объявлений в районе
    locality_rent = {}

    # Собираем данные о средней цене аренды в каждом районе
    for row in data[1:]:
        rent = int(row[2])
        locality = row[7]

        if locality not in locality_rent:
            locality_rent[locality] = [0, 0]

        locality_rent[locality][0] += rent
        locality_rent[locality][1] += 1

    # Заполняем колонки данными на основе собранной информации
    for row in data[1:]:
        rent = int(row[2])
        size = int(row[3])
        locality = row[7]

        rent_per_sqft = rent / size
        avg_rent = locality_rent[locality][0] / locality_rent[locality][1]

        for j in [round(rent_per_sqft, 2), round(avg_rent, 2)]:
            row.append(j)

    return data


save_csv("output.csv", extend_data(read_with_csv("input.csv")))
for i in read_with_csv("output.csv"):
     print(i[:11])
