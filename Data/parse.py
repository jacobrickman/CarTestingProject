import pandas as pd 
import numpy as np


def main():
	P_File = open('data_P.txt', 'r')
	DFrame = pd.DataFrame()
	i = 1

	for line in P_File:
		list_P = line.strip('\n\r').split(',')

		list_Floats = [float(i) for i in list_P]

		data_P = pd.Series(list_Floats)

		DFrame[i] = data_P
		
		i += 1


	print(DFrame)

if __name__ == '__main__':
	main()