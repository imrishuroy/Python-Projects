# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100.0)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

