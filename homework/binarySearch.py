def bs(keyword, wordList):
	from bisect import *
	sortedList = wordList.sort()
	indexnum = int(bisect_left(keyword, wordList)) + 1
	return indexnum