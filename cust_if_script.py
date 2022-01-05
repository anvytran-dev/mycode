#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

# collect the user's age
month  = int(input("What month (in number) were you born in?"))
intro = "Your birthstone is: "
if month == 1:
    message = intro + "Garnet"
elif month == 2:
    message = intro + "Amethyst"
elif month == 3:
    message = intro + "Aquamarine"
elif month == 4:
    message = intro + "Diamond"
elif month == 5:
    message = intro + "Emerald"
elif month == 6:
    message = intro + "Pearl"
elif month == 7:
    message = intro + "Ruby"
elif month == 8:
    message = intro + "Peridot"
elif month == 9:
    message = intro + "Sapphire"
elif month == 10:
    message = intro + "Opal"
elif month == 11:
    message = intro + "Topaz"
elif month == 12:
    message = intro + "Tanzanite"
else:
    message = "Please enter a valid input. Valid Input: 1-12"
print(message)

