# returns the path where the file is located
def PathFinder():
    import sys
    
    path = str(sys.argv[0])
    npath = path.rsplit("/",1)[0] + "/";
    #zmień na / dla linux

    return(npath)

    
# ~ don't know how to put these in the get_dir() function :// ~
from os import *
import os

# need the path where are the directories
# returns name of the last modified directories
def get_dir(path):

    dir_entries = scandir(path)
    
    # ~ we need to probably change that :/ ~
    # theoretically the last modify dir
    max_time = 0
    max_dir = "test"
    
    # check for every dir in the folder
    for entry in dir_entries:
        if entry.is_dir():
            # folder with (unexpected) changes in files -> starts with '!' 
            if not entry.name.startswith( '!' ):
                
                # get stats and creation time of dir
                info = entry.stat()
                time = os.path.getctime(entry)
                
#                print(entry.name, "\t", time)
                
                # if dir is newer ...
                if time > max_time:
#                    print("Changed from: ", max_dir, " to: ", entry.name)
#                    print("Time before: ", max_time, " , after: ", time)
                    
                    # ... save that
                    max_time = time
                    max_dir = entry.name
                       
    return(max_dir)
                
def directory():
    path = PathFinder() + "logs"
    #print("\n")
    dire = get_dir(path)
    #print("Dir: ", dir)
    #print("\n")
    dir_path = path + dire + "/" #zmien na / dla linux
    return(dir_path)
#    print("Dir Path: ", dir_path)


# path = ""

#powinien zwracać aktualną ścieżke gdzie jest odpalony program bez jego nazwy
#path = PathFinder()
#print("Path: ", path)
#path += "logs"
#print("Path: ", path)

#print("\n")
#zwraca najnowszy folder w danej lokacji
#dir = get_dir(path)
#print("Dir: ", dir)

#print("\n")
#dir_path = path + dir + "\\"

#print("Dir Path: ", dir_path)
