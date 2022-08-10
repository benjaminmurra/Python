import csv

# function used to format tables in terminal


def multitab(num):
    return "".join(["\t"]*num)


# create list to store data from csv file
data = []

with open("Car_Sales_Data_Set.csv", newline="",  encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        data.append(row)

# create list to store headers from csv file
headers = []
headers = data[0]
data = data[1:]

# sort data based on country
data = sorted(data, key=lambda sort: (sort[0]))
with open("Car_Sales_Data_Set_First_Sorting.csv", "w", newline="") as csvFile:
    write = csv.writer(csvFile)
    write.writerow(headers)
    write.writerows(data)

# sort based on country and Time_Year
data = sorted(data, key=lambda sort: (sort[0], sort[1]))
with open("Car_Sales_Data_Set_Second_Sorting.csv", "w", newline="") as csvFile:
    write = csv.writer(csvFile)
    write.writerow(headers)
    write.writerows(data)

# sort based on Country, Time_Year and Time_Quarter
data = sorted(data, key=lambda sort: (sort[0], sort[1], sort[2]))
with open("Car_Sales_Data_Set_Third_Sorting.csv", "w", newline="") as csvFile:
    write = csv.writer(csvFile)
    write.writerow(headers)
    write.writerows(data)

# store data values based on headers
dict = {headers[0]: list(set([val[0] for val in data])),
        headers[1]: list(set([val[1] for val in data])),
        headers[2]: list(set([val[2] for val in data])),
        headers[3]: list(set([val[3] for val in data]))}

# print options
print("1.()\n\n2.(Country)\n\n3.(Time_Year)\n\n4.(Time_Quarter-Time_Year)\n\n5.(Car_Manufacturer)\n\n6.(Country, Time_Year)\n\n7.(Country, Time_Quarter-Time_Year)\n")
print("8.(Country, Car_Manufacturer)\n\n9.(Time_Year, Car_Manufacturer)\n\n10.(Time_Quarter-Time_Year, Car_Manufacturer)\n\n11.(Country, Time_Year, Car_Manufacturer)\n\n12.(Country, Time_Quarter-Time_Year, Car_Manufacturer)\n")


# format for option 2, 3
def format1(list1, header):
    for value in list1:
        print(value + multitab(2) + str(sum(list(map(int,
              [(val[4] if val[header] == value else 0) for val in data])))))


# format for option 5
def format1a(list1, header):
    for value in list1:
        print(value + multitab(3) + str(sum(list(map(int,
              [(val[4] if val[header] == value else 0) for val in data])))))


# format for option 4
def format2(list1, list2, column1, column2):
    for value1 in list1:
        for value2 in list2:
            print(value1 + "-" + value2 + multitab(4) + str(sum(list(map(int,
                  [(val[4] if (val[column1] == value1 and val[column2] == value2) else 0) for val in data])))))


# format for option 6, 8, 9
def format3(list1, list2, column1, column2):
    for value1 in list1:
        print("\n" + value1)
        for value2 in list2:
            print(multitab(2) + value2 + multitab(3) + str(sum(list(map(int,
                  [(val[4] if (val[column1] == value1 and val[column2] == value2) else 0) for val in data])))))


# format for option 7
def format4(list1, list2, list3, column1, column2, column3):
    for value1 in list1:
        print("\n" + value1)
        for value2 in list2:
            for value_3 in list3:
                print(multitab(3) + value2 + "-" + value_3 + multitab(3) +
                      str(sum(list(map(int, [(val[4] if (val[column1] == value1 and val[column2] == value2 and val[column3] == value_3) else 0) for val in data])))))

# format for option 10
def format5(list1, list2, list3, column1, column2, column3):
    for value1 in list1:
        for value2 in list2:
            print("\n" + value1 + "-" + value2)
            for value_3 in list3:
                print(multitab(5) + value_3 + multitab(5) +
                      str(sum(list(map(int, [(val[4] if(val[column1] == value1 and val[column2] == value2 and val[column3] == value_3) else 0) for val in data])))))

# format for option 11
def format6(list1, list2, list3, column1, column2, column3):
    for value1 in list1:
        print("\n" + value1)
        for value2 in list2:
            print(multitab(2) + value2)
            for value_3 in list3:
                print(multitab(6) + value_3 + multitab(4) + str(sum(list(map(int, [(val[4] if (
                    val[column1] == value1 and val[column2] == value2 and val[column3] == value_3) else 0) for val in data])))))

# format for option 12
def format7(list1, list2, list3, list4, column1, column2, column3, column4):
    for value1 in list1:
        print(value1)
        for value2 in list2:
            for value_3 in list3:
                print(multitab(3) + value2 + "-" + value_3)
                for value_4 in list4:
                    print(multitab(6) + value_4 + multitab(4) + str(sum(list(map(int, [(val[4] if(val[column1] == value1 and val[column2] == value2 and val[column3] == value_3 and val[column4] == value_4)
                                                                                        else 0) for val in data])))))


# request option and then print tabler based on selected option.
print("Select an option from above and enter a number (1-12): ")
option = int(input())

if (option == 1):
    print("\n" + headers[4])
    print(sum([int(column[4]) for column in data]))

elif (option == 2):
    print("\n" + headers[0] + multitab(2) + headers[4])
    format1(dict[headers[0]], 0)

elif (option == 3):
    print("\n" + headers[1] + multitab(1) + headers[4])
    format1(dict[headers[1]], 1)

elif (option == 4):
    print("\n" + headers[2] + "-" + headers[1] + multitab(2) + headers[4])
    format2(dict[headers[2]], dict[headers[1]], 2, 1)

elif (option == 5):
    print("\n" + headers[3] + multitab(1) + headers[4])
    format1a(dict[headers[3]], 3)

elif (option == 6):
    print("\n" + headers[0] + multitab(2) +
          headers[1] + multitab(2) + headers[4])
    format3(dict[headers[0]], dict[headers[1]], 0, 1)

elif (option == 7):
    print("\n" + headers[0] + multitab(2) + headers[2] +
          "-" + headers[1] + multitab(2) + headers[4])
    format4(dict[headers[0]], dict[headers[2]], dict[headers[1]], 0, 2, 1)

elif (option == 8):
    print("\n" + headers[0] + multitab(2) +
          headers[2] + multitab(2) + headers[4])
    format3(dict[headers[0]], dict[headers[3]], 0, 3)

elif (option == 9):
    print("\n" + headers[1] + multitab(1) +
          headers[3] + multitab(1) + headers[4])
    format3(dict[headers[1]], dict[headers[3]], 1, 3)

elif (option == 10):
    print("\n" + headers[2] + "-" + headers[1] +
          multitab(3) + headers[3] + multitab(3) + headers[4])
    format5(dict[headers[2]], dict[headers[1]], dict[headers[3]], 2, 1, 3)

elif (option == 11):
    print("\n" + headers[0] + multitab(2) + headers[1] +
          multitab(2) + headers[3] + multitab(2) + headers[4])
    format6(dict[headers[0]], dict[headers[1]], dict[headers[3]], 0, 1, 3)

elif (option == 12):
    print("\n" + headers[0] + multitab(2) + headers[2] + "-" +
          headers[1] + multitab(2) + headers[3] + multitab(2) + headers[4])
    format7(dict[headers[0]], dict[headers[2]],
            dict[headers[1]], dict[headers[3]], 0, 2, 1, 3)
