"""A library of regular expression manipulation and generation functions"""

def intoparts(regex, string):
    lastfind = 0

    while True:
        search = r.search(string, lastfind)
        if search is None:
            return

        lastlastfind = lastfind
        lastfind = search.start()

        yield string[lastlastfind:lastfind]
        yield string[lastfind:lastfind+len(search.group(0))]

        lastfind += len(search.group(0))
