from sys import argv

script, namelist = argv
# namelist = "**ali#thomas#ghadi#akmar#smith#barija**"
indicator = namelist.startswith("**") and namelist.endswith("**")
names = namelist.replace("##", "#").strip("**")
hashmarknum = namelist.count("#") + 1
namenum = len(names.split("#"))
print(names, hashmarknum, namenum, namelist.count("#"), names.split("#"))
if hashmarknum == namenum and indicator:
	print("Valid string")
else:
	print("Not a valid string")