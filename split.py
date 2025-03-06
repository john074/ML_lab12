import csv
import random

def read_with_csv(file_name):
    data = []
    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i in reader:
            data.append(i)
    return data


def save_csv(file_name, header, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


def split_train_test(file_name, split_percent):
    data = read_with_csv(file_name)
    header, rows = data[0], data[1:]
    random.shuffle(rows)
    split_idx = int(len(rows) * split_percent)
    train, test = rows[:split_idx], rows[split_idx:]

    save_csv(f'train_{int((round(split_percent, 1)) * 100)}.csv', header, train)
    save_csv(f'test_{int((round(1-split_percent, 1)) * 100)}.csv', header, test)


def split_train_val_test(file_name, test_percent, k):
    data = read_with_csv(file_name)
    header, rows = data[0], data[1:]
    random.shuffle(rows)

    split_idx = int(len(rows) * test_percent)
    test, comp = rows[:split_idx], rows[split_idx:]

    for i in range(k):
        val = comp[int(len(comp)/k*i):int(len(comp)/k*(i+1))]
        train = comp[:int(len(comp)/k*i)] + comp[int(len(comp)/k*(i+1)):]

        save_csv(f'train_split_{i}.csv', header, train)
        save_csv(f'val_split_{i}.csv', header, val)

        # print(f"Валидационный набор k={i+1}")
        # print(header)
        # for j in range(3):
        #     print(val[j])

        print(f"Тестовый набор k={i + 1}")
        print(header)
        for j in range(3):
            if i == 7:
                print(comp[:int(len(comp) / k * i)][j])
            else:
                print(comp[int(len(comp)/k*(i+1)):][j])

    save_csv('test_split.csv', header, test)


split_train_test("output.csv", 0.8)
split_train_test("output.csv", 0.7)
split_train_val_test("output.csv", 0.12, 8)

print("Оригинальный набор:", len(read_with_csv("output.csv")))
print("train_80:", len(read_with_csv("train_80.csv")))
print("test_20:", len(read_with_csv("test_20.csv")))
print("train_70:", len(read_with_csv("train_70.csv")))
print("test_30:", len(read_with_csv("test_30.csv")))
print("test_split:", len(read_with_csv("test_split.csv")))
for i in range(8):
    print(f"train_split_{i}:", len(read_with_csv(f"train_split_{i}.csv")))
    print(f"val_split_{i}:", len(read_with_csv(f"val_split_{i}.csv")))