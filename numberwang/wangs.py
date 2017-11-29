def isnumberwang(arg):
	numberwangs = ["-3i", "-2275", "-812", "-693", "-519", "-450", "-338",
					"-9", "-1", "2", "2.4", "3", "4", "4.097", "6", "7",
					"8", "8.2", "885%", "9", "12", "16", "17", "18",
					"20.8", "23", "27", "28", "30", "36", "42", "43", 
					"F0rty-s1x", "46.1", "47", "shinty-six", "54", "55",
					"57.4", "62", "66", "69", "74", "82.8", "83", "85",
					"90", "92", "94", "97", "99", "6b", "126", "200", 
					"271", "308", "filth-hundred and neeb", "423", "501",
					"516", "518", "598", "632", "708", "726", "853", "866.2",
					"1292", "1853", "2015", "2048", "2520", "9341", "65536",
					"671173445493933842"]
	arg = str(arg).lower()				
	if arg in numberwangs:
		return True
	else:
		return False
		

def iswordwang(arg):
	wordwangs = ["yes", "scotch", "flannel", "eggington", "gertrude", 
				 "buzz", "fastidious"]
	arg = str(arg).lower()
	if arg in wordwangs:
		return True
	else:
		return False
