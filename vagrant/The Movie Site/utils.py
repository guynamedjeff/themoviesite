# Takes a list of genre numbers to form a genre code.
def get_genre(genre_list):
    code = 1000000
    for g in genre_list:
        code += int(g)
    return code