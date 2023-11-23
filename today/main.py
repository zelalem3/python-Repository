import pandas

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# sum = 0
# len = len(temp_list)
# print(data["temp"].mean())
#
# max = data[(data.temp.max() == data.temp)]
# print(max.condtion)
# monday = data[data.day == "Monday"]
# print(monday.condition)
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
# result = [int(num) for num in file_1_data if num in  file_2_data]
# print(result)

# names = ['alez', 'beth', 'caroline', 'dave', 'zelalem', 'freddie']
# student_score = {
#
# }
weather_C = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 22,
    "sunday": 24,
}
# (temp_C*9/5) + 32 = temp_f
weather_f = {day:value*9/5+32 for (day,value) in weather_C.items()}
print(weather_f)
