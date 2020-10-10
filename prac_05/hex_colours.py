CODE_TO_COLOR = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "aquamarine1": "#8b8378", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff"}

color_name = input("Enter color name: ").lower()

while color_name != "":
    if color_name in CODE_TO_COLOR:
        print(color_name, "color code is", CODE_TO_COLOR[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter short state: ").lower()