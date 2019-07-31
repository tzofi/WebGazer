import sys
import os

for subdir, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if "P_" in subdir and f[-4:] in [".csv", ".txt"]:
	    i = subdir.find("P_")
	    print(subdir + "/" + f)
	    os.system("cp " + subdir + "/" + f + " " + os.getcwd() + "/" + subdir[i:] + "_" + f)
