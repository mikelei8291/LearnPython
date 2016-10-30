def strV(namelist):
	import re
	# namelist = "**ali#thomas#ghadi#akmar#smith#barija**"
	indicator = namelist.startswith("**") and namelist.endswith("**")
	hashmarknum = len(re.findall("#", namelist)) + 1
	namenum = len(re.findall(r"\b[\w]", namelist))
	if hashmarknum - namenum == 0 and indicator:
		return("Valid string")
	else:
		return("Not a valid string")