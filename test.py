# Importing libraries
import re, os, shutil

#Defining dirs and filters 
incoming_dir = '/mnt/MEDIA_CENTER/testdir'
movies = '/mnt/MEDIA_CENTER/testdir/filmy'
tvshows = '/mnt/MEDIA_CENTER/testdir/seriale'
filters = 'filmy' or name == 'seriale' or name == 'Zdjecia' or name == 'MUSIC'

# Walking thru directories
for root, dirs, files in os.walk(incoming_dir):
    #Listing filenames in the parent dir (incoming_dir) and subfolders
    for name in files:
        #
        #if name.endswith(('.mov', '.MOV', '.avi', '.AVI', '.mpg', '.MPG', '.mkv', '.MKV','.mp4', '.MP4',)) and re.search('^.+S[0-9]+E[0-9]+.*', name):
           # the_sfile = os.path.join(root, name)
        #    try:
        #        shutil.move(name, tvshows)
        #        print name, ' moved to seriale'
        #    except:
        #        print 'Nothing to move'
        
        if name.endswith(('.mov', '.MOV', '.avi', '.AVI', '.mpg', '.MPG', '.mkv', '.MKV','.mp4', '.MP4',)):
            the_file = os.path.join(root, name)
            the_dir = re.findall('(^[./].+)/', the_file)[0]
            if the_dir == os.getcwd(): continue
            try:
                shutil.move(the_dir, movies)
                print the_file, ' moved to filmy'
            except:
                print 'Nothing to move'
     
    for name in dirs:
        if name == filters : continue
        if re.search('^.+S[0-9]+E[0-9]+.*', name) or re.search('^.+Season.*', name):
            try:
                shutil.move(name, tvshows)
                print name, ' moved to TV Shows!'
            except:
                print 'Nothing to move'