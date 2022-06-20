
colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#000FF"
}

colors["blue"] = colors["blue"].strip("#")

print(colors)               # {'red': '#FF0000', 'green': '#00FF00', 'blue': '000FF'}