# Importing libraries
import re, os, shutil

#Defining dirs and filters : needs to be personalized!
incoming_dir = '/mnt/MEDIA_CENTER/testdir'
movies = '/mnt/MEDIA_CENTER/testdir/FILMY'
tvshows = '/mnt/MEDIA_CENTER/testdir/TV Shows'
filters = 'FILMY' or name == 'TV Shows' or name == 'Zdjecia' or name == 'MUSIC' or name == 'Home_Videos' or name == 'TEMP' or name == 'testdir'
filter_for_dir = '^/mnt/MEDIA_CENTER.+Zdjecia|/mnt/MEDIA_CENTER.+TEMP.*|/mnt/MEDIA_CENTER.+MUSIC.*|/mnt/MEDIA_CENTER.+Home_Videos.*|/mnt/MEDIA_CENTER.+TEMP.*|/mnt/MEDIA_CENTER.+TV Shows.*'

# Defining function that works as os.walk, but pass it a level parameter that indicates how deep the recursion will go. 
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# Traversing directories. Creates list of names for each root, dirs, files.  
for root, dirs, files in walklevel(incoming_dir, level=3):
    #For files in incoming_dir and subfolders consider "if" statments
    for name in files:
        the_file = os.path.join(root, name)
        if re.search(filter_for_dir, the_file) is not None: continue
        elif name.endswith(('.mov', '.MOV', '.avi', '.AVI', '.mpg', '.MPG', '.mkv', '.MKV','.mp4', '.MP4')) and re.search('^.+S[0-9]+E[0-9]+.*', name):
            try:
                shutil.move(name, tvshows)
                print name, ' moved to seriale'
            except:
                print 'Nothing to move 111'
        elif name.endswith(('.mov', '.MOV', '.avi', '.AVI', '.mpg', '.MPG', '.mkv', '.MKV','.mp4', '.MP4')):
            the_file = os.path.join(root, name)
            the_dir = re.findall('(^[./].+)/', the_file)[0]
            #print os.getcwd()
            if the_dir == os.getcwd(): continue
            try:
                shutil.move(the_dir, movies)
                print the_file, ' moved to filmy 888'
            except:
                print 'Nothing to move 222'
    #For dirs in incoming_dir and subfolders consider "if" statments
    for name in dirs:
        if name == filters : continue
        if re.search('^.+S[0-9]+E[0-9]+.*', name) or re.search('^.+Season.*', name):
            try:
                shutil.move(name, tvshows)
                print name, ' moved to TV Shows!'
            except:
                print 'Nothing to move 333'
#Moving movies files from incoming_dir to movies
files_in_root = os.listdir(incoming_dir)
for name in files_in_root:
    if name.endswith(('.mov', '.MOV', '.avi', '.AVI', '.mpg', '.MPG', '.mkv', '.MKV','.mp4', '.MP4')):
        try:
            shutil.move(name, movies)
            print name, ' moved to filmy 444'
        except:
            print 'Nothing to move 444'