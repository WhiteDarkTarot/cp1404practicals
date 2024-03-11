COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

user_input = input("Enter a color name (or blank to stop): ").upper()

if user_input:
    color_code = COLOR_CODES.get(user_input)
    if color_code:
        print(f"The hexadecimal color code for {user_input} is {color_code}.")
    else:
        print("Invalid color name.")
else:
    print("No color name entered.")
