import os, magic, re, shutil

incoming_dir = './MEDIA_CENTER/_INCOMING_TORRENT_FILES'
tvshows = './MEDIA_CENTER/TV Shows'
movies = './MEDIA_CENTER/FILMY'

from subprocess import call
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

for root, dirs, files in walklevel(incoming_dir, level=0):
    for name in files:
        #print os.path.join(root, name)
        print 'Checking for homeless files...'
        if not os.path.isdir(os.path.join(root, name)[:-4]):
            print 'Found a homeless files...creating folders...'
            os.makedirs(os.path.join(root, name)[:-4])
        try:
            print 'Moving files to new created folders'
            shutil.move(os.path.join(root, name), os.path.join(root, name)[:-4])
        except:
            continue

# Traversing directories. Creates list of names for each root, dirs, files.
for root, dirs, files in walklevel(incoming_dir, level=2):
    for name in dirs:
        # Searching for DIRECTORIES with dirnames containing regex below
        if re.search('^.+[s][0-9]+[e][0-9]+.*', name.lower()) or re.search('.+[s]eason.*', name.lower()):
            print 'Found a TV show directory...'
            # Moving directory to tvhows
            try:
                shutil.move(os.path.join(root, name), tvshows)
                print name, ' moved to TV Shows!'
            except:
                print 'Nothing to move'
    #For files in incoming_dir and subfolders consider "if" statments

    for name in files:
        try:
            ftype = magic.from_file(os.path.join(root, name), mime=True)
        except:
            continue
        if re.search('^.*video.*', ftype) is not None and re.search('^.+[s][0-9]+[e][0-9]+.*', name.lower()):
            print name, ' Found a TV show file...'
            try:
                shutil.move(os.path.join(root, name), tvshows)
                print name, ' ...moved to TV Shows'
            except:
                print 'Nothing to move!'
        elif re.search('^.*video.*', ftype) is not None:
            print name, ' Found a movie file...'
            the_file = os.path.join(root, name)
            the_dir = re.findall('(^[./].+)/', the_file)[0]
            try:
                shutil.move(the_dir, movies)
                print name, ' ...moved to MOVIES folder'
            except:
                print 'Nothing to move!'
        #elif re.search('^.*audio.*', ftype) is not None:
        #    print name, ' Found an audio file'
        #elif re.search('^.*application/pdf.*', ftype) is not None:
        #    print name, ' Found a pdf file'
        #elif re.search('^.*application.*', ftype) is not None:
        #    print name, ' Found an app file'
        else:
            print name, ' Non in searching criteria. Leaving...'
