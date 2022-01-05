#!/usr/bin/env python3


#import libraries
import shutil
import os
    
def main():

    #This will allow the user to run the program from any location on the system, and our script still
    #always start at /home/student/mycode/
    os.chdir('/home/student/mycode/')
    
    #Calling shutil.move(source, destination) will move the file or folder at the path source to the path 
    #destination and will return a string of the absolute path of the new location. If destination points to    #a folder, the source file gets moved into destination and keeps its current filename.
    shutil.move('raynor.obj', 'ceph_storage/')
    
    #Prompt the user for a new name for the kerrigan.obj file.
    xname = input('What is the new name for kerrigan.obj? ')
    
    #Rename the current kerrigan.obj file.
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

