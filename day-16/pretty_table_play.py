from prettytable import PrettyTable, TableStyle

table = PrettyTable(["Name", "Age","Cat Name"], align="l")
table.set_style(style=TableStyle.MARKDOWN)

table.add_row(["John", 30, "Whiskers"])
table.add_row(["Jane", 25, "Fluffy"])
table.add_row(["Bob", 35, "Mittens"])

table.add_column("City", ["New York", "Los Angeles", "Chicago"])
table.add_column("Cat Colour", ["Orange", "Black", "Tortoise"])
table.add_column("Cat Personality", ["Playful", "Shy", "Friendly"])

print(table)

