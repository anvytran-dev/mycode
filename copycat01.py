#!/usr/bin/env python3

# import libraries to complete the tasks
import shutil
import os

def main():

    #this script allows our program to always start at /homr/student/mycode/ --allowing the program to run
    #from any location on the system
    os.chdir("/home/student/mycode/")

    #this script copies the file at the path source to the folder at the path destination
    #shutil.copy(source, destintation) -- both arguments are strings
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #this script copies an entire folder and every folder and file contained in it to the folder at the path    # destination
    #shutil.copytree(source, destination) --both arguments are strings
    shutil.copytree("5g_research/", "5g_research_backup/")

main()

