import os
import pandas as pd
import matplotlib.pyplot as plt



def Make_Plot():
	if not os.path.isdir("Graph"):		#Creating the Graph folder if it doesn't exist
		os.mkdir("Graph")

	liste_paire = ["AA","AC","AG","AU","CC","CG","CU","GG","GU","UU"]
	graphe = pd.read_csv("frequency.csv")

	for paire in liste_paire:
		new_graphe = f"plt.plot(graphe.Distance,graphe.{paire})"
		exec(new_graphe)

		plt.title(f"{paire} pair")
		plt.xlabel("Distance in Å")
		plt.ylabel("Pseudo-energy score")
		plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
		plt.yticks([-4,-2,0,2,4,6,8,10])
		plt.axhline(0,color='black')
		
		plt.savefig(f"Graph/{paire}.png")
		plt.clf()
		print(f"Plotting of the {paire} pair completed")



if __name__ == "__main__":
    Make_Plot()
