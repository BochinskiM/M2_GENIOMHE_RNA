import re
from os import listdir
from math import sqrt, log



def Calcul_Distance():
	compteur_tot = 0		#The counting of the pairsare made by using dictionaries
	AA, AC, AG, AU, CC, CG, CU, GG, GU, UU, tot = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
	liste_paire = {"AA":AA, "AC":AC, "AG":AG, "AU":AU, "CC":CC, "CG":CG, "CU":CU, "GG":GG, "GU":GU, "UU":UU}

	for paire in liste_paire:		#Initializing all counts as 0
		for i in range(0,21):
			liste_paire[paire][i] = 0
			tot[i] = 0

	for file in listdir("PDB_Files/"):
		liste_chaine = []
		chaine = "First"
		with open(f'PDB_Files/{file}','r') as fichier_test:
			for line_test in fichier_test:
				if re.search('^ATOM',line_test) and line_test[12:16] == " C3'" and line_test[18] == " ":		#Select only the lines used for computing
					
					if chaine != line_test[21]:		#This list prevent the same chain to be compute several times if it has more than one copy
						liste_chaine.append(chaine)
						chaine = line_test[21]

					if chaine not in liste_chaine:
						indice = int(line_test[22:26])
						with open(f'PDB_Files/{file}','r') as fichier_calcul:
							for line_calc in fichier_calcul:						#Select only the lines used for computing
								if re.search('^ATOM',line_calc) and line_calc[18] == " " and line_calc[12:16] == " C3'" and int(line_calc[22:26]) >= (indice+4):
									dist = sqrt((float(line_calc[30:38])-float(line_test[30:38]))**2+(float(line_calc[38:46])-float(line_test[38:46]))**2+(float(line_calc[46:54])-float(line_test[46:54]))**2)
									
									if dist < 21:		#Select only the distancies lower than 21 Angstrom
										compteur_tot += 1
										tot[int(dist)] += 1

										#Adding 1 to the count of the pair in the right distance
										if ((line_calc[19] == "C" or line_calc[19] == "G" or line_calc[19] == "U") and line_test[19] == "A") or ((line_calc[19] == "G" or line_calc[19] == "U") and line_test[19] == "C") or (line_calc[19] == "U" and line_test[19] == "G"):
											add_dico = f"{line_test[19]}{line_calc[19]}[int(dist)] += 1"
											exec(add_dico)

										else:
											add_dico = f"{line_calc[19]}{line_test[19]}[int(dist)] +=1"
											exec(add_dico)

		print(f"Counting of {file} completed")
    

    #Observed frequency

	for paire in liste_paire.keys():
		nb_paire = 0
		for element in liste_paire[paire].keys():
			nb_paire += liste_paire[paire][element]
		for element in liste_paire[paire].keys():
			liste_paire[paire][element] = liste_paire[paire][element] / nb_paire


	#Reference frequency

	for intervalle in tot:
		tot[intervalle] = tot[intervalle] / compteur_tot


	#Energy score for each distance of each pair

	for paire in liste_paire.keys():
		for element in liste_paire[paire].keys():
			if liste_paire[paire][element] != 0:
				liste_paire[paire][element] = -log(liste_paire[paire][element] / tot[element])
			else:
				liste_paire[paire][element] = 10

	Creation_fichier(liste_paire)


#Creating the frequency.csv file including every counts

def Creation_fichier(liste):
	with open(f'frequency.csv','w') as filout:
		filout.write("Distance,AA,AC,AG,AU,CC,CG,CU,GG,GU,UU\n")
		for i in range(0,21):
			filout.write(f"{i+1},")
			for paire in liste.keys():
				if paire != "UU":
					filout.write(f"{liste[paire][i]},")
				else:
					filout.write(f"{liste[paire][i]}\n")
	print("Counting of all files completed")



if __name__ == "__main__":
    Calcul_Distance()
