import urllib

def grab_trailer_url(name, year):
    search_url = "https://www.youtube.com/results?search_query=" + name + " " + year + " trailer"
    trailer_url = get_url(get_page(search_url))
    return reformat_url(trailer_url)

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return "error"

def get_url(page):
    start_link = page.find("watch?v=")

    if (start_link == -1):
        return None

    start_quote = page.find('=', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url

def reformat_url(url):
    return "https://www.youtube.com/watch?v=" + url