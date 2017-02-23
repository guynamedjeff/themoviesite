import urllib, re, logging

# Accepts the name and year of any particular movie.
# Return a YouTube trailer URL to store in the database.
def grab_trailer_url(name, year):
    search_url = "https://www.youtube.com/results?search_query=" + name + " (" + year + ") trailer"
    pattern = r'/watch\?v=[a-zA-Z0-9_\-]+'
    return "https://www.youtube.com" + find_pattern(search_url, pattern)

# Accepts the name and year of any particular movie.
# Return an IMDB poster URL to store in the database.
def grab_poster(name, year):
    search_url = "http://www.imdb.com/find?q=" + name + " (" + year + ")"
    pattern = r'https://images-na.ssl-images-amazon.com/images/M/\w+@*\.'
    return find_pattern(search_url, pattern)

# Returns a string of the code in any given URL.
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return "error"

# Searches for an image pattern on Amazon's picture gallery (page) to locate the poster URL.
# Returns the poster URL for any given page input.
def find_pattern(search_url, pattern):
    attempts = 0
    match = re.search(pattern, get_page(search_url))
    while match == None and attempts < 5:
        logging.error(attempts)
        match = re.search(pattern, get_page(search_url))
        attempts += 1
    return match.group()