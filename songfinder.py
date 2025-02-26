import time


# -- Find songs by title
#    Use a regular "for" loop to find and return a list of
#    songs with the given title.
def search_by_title_slow(title, all_songs):
    print("Problem 1(a) not implemented")
    return []


# -- Find songs by lyrics
#    Use "for" loops to search through all the lyrics in all
#    the songs. Return a list of songs whose lyrics contain
#    the given word
def search_lyrics_slow(word, all_songs):
    print("Problem 2(a) not implemented")
    return []


# -- Build an index of songs by title
#    Make and return a dictionary that maps a song title (the key)
#    to the corresponding song tuple (the value)
def build_title_index(all_songs):
    print("Problem 3 not implemented")
    return {}

# -- Lookup a song in the title index
#    Given a song title and a dictionary mapping song titles to songs
#    lookup and return the corresponding song, or return None
#    NOTE: this code should not fail if there is not song with that title.
def lookup_title_index(title, song_index):
    print("Problem 3 not implemented")
    return None

# -- Build an index of songs by lyrics
#    Make and return a dictionary that maps a word (the key) to
#    the list of songs whose lyrics contain that word.
def build_word_index(all_songs):
    print("Problem 4 not implemented")
    return {}

# -- Lookup songs with lyrics using index
#    Given a word and a dictionary mapping words to lists of songs
#    with those words, use the index to return that list of songs.
#    Return empty list if there are none.
def lookup_word_index(word, word_index):
    print("Problem 4 not implemented")
    return []

# -- Lookup songs with two words in their lyrics
#    Given two word and a dictionary mapping words to lists of songs
#    return a list of songs that contain both words.
#    Return empty list if there are none.
def lookup_2word_index(word1, word2, word_index):
    print("Problem 5 not implemented")
    return []

# -- Print song info
#    Print out the artist, title, and lyrics
def print_song(song):
    print("Problem 1(b) not implemented")

# -- Print song with context
#    Print out the artist and title, and just the lines
#    of lyrics that have the given word
def print_song_context(word, song):
    print("Problem 2(b) not implemented")



# -- Read the song file and return a list of songs. Each song
#    is a tuple of the form (artist, title, lyrics) where
#    lyrics is a list of lines. Each line is a string.
def read_song_file(songfile):
    songlist = []
    with open(songfile) as f:
        done = False
        while not done:
            artist = f.readline().rstrip()
            if artist:
                title = f.readline().rstrip()
                lyrics = []
                donesong = False
                while not donesong:
                    line = f.readline().rstrip()
                    if line == '<BREAK>':
                        donesong = True
                    else:
                        lyrics.append(line)
                song = (artist, title, lyrics)
                songlist.append(song)
            else:
                done = True
    return songlist


# -- Here's where the program actually starts running...
filename = input('Enter song file name: ')
print("Read file...")
t1 = time.time()
allsongs = read_song_file((filename))
t2 = time.time()
print("..done in " + str(t2-t1) + " seconds")
print("Found " + str(len(allsongs)) + " songs")

# -- Build the indexes here
print("Build indexes...")
t1 = time.time()

title_index = build_title_index(allsongs)
word_index = build_word_index(allsongs)

t2 = time.time()
print("..done in " + str(t2-t1) + " seconds")

done = False
while not done:
    print('Choose a query...')
    print('1: Find songs by title (SLOW)')
    print('2: Find songs with a word in lyrics (VERY SLOW)')
    print('3: Find songs by title (FAST)')
    print('4: Find songs with a word in lyrics (FAST)')
    print('5: Find songs with two words')
    s = input('Enter 1-5 (any other number to quit): ')

    choice = int(s)
    if choice == 1:
        t = input('Enter a title: ')
        t1 = time.time()
        results = search_by_title_slow(t, allsongs)
        t2 = time.time()
        print("Done in " + str(t2 - t1) + " seconds")
        for s in results:
            print_song(s)
    elif choice == 2:
        w = input('Enter a word: ')
        t1 = time.time()
        results = search_lyrics_slow(w, allsongs)
        t2 = time.time()
        print("Done in " + str(t2 - t1) + " seconds")
        for s in results:
            print_song_context(w, s)
    elif choice == 3:
        t = input('Enter a title: ')
        t1 = time.time()
        song = lookup_title_index(t, title_index)
        t2 = time.time()
        if song != None:
            print_song(song)
        else:
            print('Not found')
        print("Done in " + str(t2 - t1) + " seconds")
    elif choice == 4:
        w = input('Enter a word: ')
        t1 = time.time()
        results = lookup_word_index(w, word_index)
        t2 = time.time()
        for s in results:
            print_song_context(w, s)
        print("Done in " + str(t2 - t1) + " seconds")
    elif choice == 5:
        w1 = input('Enter first word: ')
        w2 = input('Enter second word: ')
        t1 = time.time()
        results = lookup_2word_index(w1, w2, word_index)
        t2 = time.time()
        for s in results:
            print_song_context(w, s)
        print("Done in " + str(t2 - t1) + " seconds")
    else:
        done = True
