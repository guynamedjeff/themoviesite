import urllib, re

def grab_trailer_url(name, year):
    search_url = "https://www.youtube.com/results?search_query=" + name + " " + year + " trailer"
    trailer_code = get_url_code(get_page(search_url), "watch?v=", "=", "\"")
    return make_trailer_url(trailer_code)

def grab_poster(name, year):
    search_url = "http://www.imdb.com/find?q=" + name + " " + year
    title_code = get_url_code(get_page(search_url), "/title/", "/", "\"")
    imdb_url = make_title_url(title_code)
    poster_code = get_url_code(get_page(imdb_url), "mediaviewer/", "/", "\"")
    mediaviewer_url = create_mediaviewer_url(shorten_title_code(title_code), poster_code)
    return find_poster_pattern(get_page(mediaviewer_url))

def find_poster_pattern(page):
    match = re.search(r'https://images-na.ssl-images-amazon.com/images/M/\w+@', page)
    return match.group()


def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return "error"

def get_url_code(page, pattern, start, end):

    start_link = page.find(pattern)

    if (start_link == -1):
        return None

    start_id = page.find(start, start_link)
    end_id = page.find(end, start_id + 1)

    if pattern == "amazon.com/images":
        return page[start_id + 1:end_id]

    if pattern == "/title/":
        return page[start_id + 7:end_id]

    if pattern == "watch?v=" or pattern == "mediaviewer/":
        return page[start_id + 1:end_id]


# Returns final movie trailer URL
def make_trailer_url(url):
    return "https://www.youtube.com/watch?v=" + url

# Returns IMDB title code from unique title URL.
def shorten_title_code(title_code):
    slash_index = title_code.find('/')
    short_title_code = title_code[0:slash_index]
    return short_title_code

# Returns and IMDB URL for a specific title.
def make_title_url(url):
    return "http://www.imdb.com/title/" + url

# Opens a title's IMDB photo gallery on the poster.
def create_mediaviewer_url(title_code, poster_code):
    return "http://www.imdb.com/title/" + title_code + "/mediaviewer/" + poster_code