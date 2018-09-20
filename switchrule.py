def getRowMap():
	return {} # if your db row "encrypt" means "method", write {"encrypt": "method"}

def getKeys(key_list):
	return key_list
	#return key_list + ['plan'] # append the column name 'plan'

def isTurnOn(row):
	return True
	#return row['plan'] == 'B' # then judge here

