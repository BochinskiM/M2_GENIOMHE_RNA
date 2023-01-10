import re
import argparse
import pandas as pd
from math import sqrt, floor, ceil



parser = argparse.ArgumentParser()
parser.add_argument("-f", type = str, required = True, help = "Choose an RNA in pdb file format")

args = parser.parse_args()
file = args.f



def Calcul_Score(file):
	energie = 0
	graphe = pd.read_csv("frequency.csv")

	with open(file, "r") as ARN:		#Open the RNA file
		for line in ARN:
			if re.search('^ATOM', line) and line[18] == " " and line[12:16] == " C3'":		#Select only the necessary lines
				line_test = line
				indice = int(line_test[22:26])

				with open(file, "r") as ARN_calc:
					for line_calc in ARN_calc:			#Select only the necessary lines for computing the distance
						if re.search('^ATOM', line_calc) and line_calc[18] == " " and line_calc[12:16] == " C3'" and int(line_calc[22:26]) >= (indice+4):

							dist = sqrt((float(line_calc[30:38])-float(line_test[30:38]))**2+(float(line_calc[38:46])-float(line_test[38:46]))**2+(float(line_calc[46:54])-float(line_test[46:54]))**2)

							if dist < 20:		#If distance < 20 we keep it
								if ((line_calc[19] == "C" or line_calc[19] == "G" or line_calc[19] == "U") and line_test[19] == "A") or ((line_calc[19] == "G" or line_calc[19] == "U") and line_test[19] == "C") or (line_calc[19] == "U" and line_test[19] == "G"):
									paire = line_test[19] + line_calc[19]

								else:
									paire = line_calc[19] + line_test[19]

								#Computing the energy of every pair selected and adding them to the total
								x1 = floor(dist)
								y1 = float(graphe.get(f"{paire}")[floor(dist)])
								y2 = float(graphe.get(f"{paire}")[ceil(dist)])
								energie += y1 + ((dist - x1) * (y2 - y1))

	print(f"Free energy of {file} =",energie)



if __name__ == "__main__":
	Calcul_Score(file)
