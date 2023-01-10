The objective of these 3 scripts is to count the frequencies of nucleotides pairs in a set of RNAs by distance, and then to compute the Free-energy of one based on these frequencies.


First, create a folder named "PDB_Files" and put all the RNAs that you want to use as training in it, all in pdb format.

Second launch the train.py scipt that will use the files in "PDB_Files" and count the frequencies of all pairs according to their distance. it will create a frequency.csv file.

The plot.py is optionnal, it takes the csv file and use it to plot the frequency of each pair by distance in the Graph folder.

Finally, the score.py script takes a single RNA file (also in pdb format) and use the frequency.csv to compute its Free-energy with the "-f" agrument.