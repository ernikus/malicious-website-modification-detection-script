def file_localisation():
    import sys

    # path = repr(sys.argv[0])
    
    path = str(sys.argv[0])
    npath = path.rsplit("/",1)[0] + "/"
    
    return(npath)

    

from os import *
import os
    
#get dirs
def get_dirs(path):
    # dir_entries = scandir("/home/ernest/Documents/MegaSync/Project Python/")
    dir_entries = scandir(path)
    
    # we need to probably change that :/
    max_time = 0
    max_dir = "test"
    
    for entry in dir_entries:
        if entry.is_dir():
            info = entry.stat()
            time = os.path.getctime(entry)
            
            # print(entry.name, "\t", time)
            
            if time > max_time:
                # print("Changed from: ", max_dir, " to: ", entry.name)
                # print("Time before: ", max_time, " , after: ", time)
                
                max_time = time
                max_dir = entry.name
                       
    return(max_dir)
                
            
path = ""
    
path = file_localisation()
print("Path: ", path)

dir = get_dirs(path)
print("Dir: ", dir)

dir_path = path + dir + "/"

print("Dir Path: ", dir_path)