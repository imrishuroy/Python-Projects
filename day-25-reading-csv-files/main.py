import pandas

data = pandas.read_csv("squirrel_data.csv")
color = (data["Primary Fur Color"])
colors_list = color.to_list()

gray_colors = []
cinnamon_colors = []
black_colors = []

# grey_squirrel_count = len(data[data["Primary Fur Color"]] == "Gray")
# print(grey_squirrel_count)

for color in colors_list:
    if color == "Gray":
        gray_colors.append(color)
    if color == "Black":
        black_colors.append(color)
    if color == "Cinnamon":
        cinnamon_colors.append(color)

black = len(black_colors)
gray = len(gray_colors)
cinnamon = len(cinnamon_colors)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")



# print(colors_list)

#
#
# gray_color = []
# for color in colors_list:
#     if color == "Gray":
#         gray_color.append(color)
#
# cinnamon_color = []
# for color in colors_list:
#     if color == "Cinnamon":
#         cinnamon_color.append(color)
#
# black_color = []
# for color in colors_list:
#     if color == "Black":
#         black_color.append(color)
#
#
# print(gray_color)
# print(cinnamon_color)
# print(black_color)
#
# gray = len(gray_color)
# black = len(black_color)
# cinnamon = len(cinnamon_color)
#
# data_dict = {
#     "Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray, black, cinnamon]
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("squirrel_count.csv")
#


# gray_color = []
# if data["grey_color = data.Primary Fur Color"] == "Gray" == "Gray":
#     gray_color.append(data["grey_color = data.Primary Fur Color"] == "Gray")
#
















#
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# temp = data["temp"]
# print(temp)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_sum = 0
#
# for temp in temp_list:
#     temp_sum += temp
#
# average = temp_sum / len(temp_list)
# print(f"Average Temperature is {average}")
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# monday_temp = monday.temp + 237
# print(monday_temp)
#
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(new_data)

 # with csv library
# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
# print(weather_data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
