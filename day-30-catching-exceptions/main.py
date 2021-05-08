# try:
#     file = open("my-file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("my-file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     contents = file.read()
#     print(contents)
# finally:
#     # file.close()
#     # print("File closed")
#     raise TypeError("This is my generated error")


# Generating our own error
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))

if height > 3:
    raise TypeError("Human height can't be grater than 3")

bmi = weight / height ** 2
print(f"Your BMI is {bmi}")
