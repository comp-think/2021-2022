# 1st Exercise
# ------------

lyrics = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

# (1.a) -------------
def clean_lyrics(txt_lyrics):
    # Split and get a list of words
    lyrics_set = set(txt_lyrics.split(" "))
    # create a set from the list of stopwords (to remove from the lyrics)
    unwanted_set = set(['a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s'])
    # return a new set represented as the difference between <lyrics_set> and the <unwanted_set>
    return lyrics_set.difference(unwanted_set)

# call clean_lyrics()
set_clean_lyrics = clean_lyrics(lyrics)
print(set_clean_lyrics)

# (1.b) -------------
def family_words(s_lyrics):
    # create a set from the list of "family_words"
    s_fam_words = set(["mama", "daddy", "sister", "brother", "boy", "girl"])
    # a new set representing the common words between <s_lyrics> and the <s_fam_words>
    common_set = s_lyrics.intersection(s_fam_words)
    # return the length of the new set, i.e., <common_set>
    return len(common_set)

# call family_words()
len_fam_words = family_words(set_clean_lyrics)
print(len_fam_words)

# (1.c) -------------
def count_words(txt_lyrics):
    result_dict = {}
    lyrics_list = txt_lyrics.split(" ")
    unwanted_list = ['a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s']
    # check each word <w> inside <lyrics_list>
    for w in lyrics_list:
        # check if <w> is not inside the unwanted list (i.e., <unwanted_list>)
        if w not in unwanted_list:
            # if <w> is not part of the dict to return -> initialize the dictionary with (key,value) = (<w>,0)
            if w not in result_dict:
                result_dict[w] = 0
            # increment the number of occurences of <w> by 1
            result_dict[w] += 1
    # return the dictionary of words
    return result_dict

# call count_words()
count_dict = count_words(lyrics)
print(count_dict)

# (1.d) -------------

# a list of songs separated by ";;"
# each song is represented as  "ALBUM_NAME::SONG_NAME"
# e.g., el camino::lonely boy -> ALBUM_NAME = "el camino", SONG_NAME = "lonely boy"
playlist_txt = "el camino::lonely boy ;; el camino::little black submarine ;; el camino::gold on the ceiling ;; turn blue::fever ;; turn blue::gotta get away ;; brothers::howlin for you ;; brothers::tighten up ;; turn blue::it is up to you now"

def build_playlist_dict(a_txt):
    result_dict = {}
    # split and get the list of songs
    songs = a_txt.split(" ;; ")
    # for each <a_song> in <songs>
    for a_song in songs:
        # split the song using "::" as separator
        song_parts = a_song.split("::")
        # the first part (i.e., with index 0) is the name of the album
        album = song_parts[0]
        # the second part (i.e., with index 1) is the name of the song
        song_name = song_parts[1]
        # if <album> is not part of the dict to return -> initialize the dictionary with (key,value) = (<album>,[])
        # the intial value in this case is an empty list
        if album not in result_dict:
            result_dict[album] = []
        # append the new song to the list of its album
        result_dict[album].append(song_name)
    return result_dict

album_dict = build_playlist_dict(playlist_txt)
print(album_dict)
