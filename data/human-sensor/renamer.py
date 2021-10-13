import os
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("./") if isfile(join("./", f))]

# remove and rename 
for file in files:
    if "_Study" in file:
        splitted_str = file.split("_Study")
        print(splitted_str)
        new_filename = "p"+str(splitted_str.split("_")[1]).split(".")[0]+"_" + splitted_str[1][0];
        file_extension_split = splitted_str[1].split(".")
        new_filename += "."+file_extension_split[1]
        os.rename("./"+file, "./"+new_filename)
    