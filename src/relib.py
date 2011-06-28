"""A library of regular expression manipulation and generation functions"""

def intoparts(regex, string):
    lastfind = 0

    while True:
        search = regex.search(string, lastfind)

        lastlastfind = lastfind

        if search is not None:
            lastfind = search.start()
        else:
            lastfind = None

        yield string[lastlastfind:lastfind]

        if search is None:
            return

        yield string[lastfind:lastfind+len(search.group(0))]

        lastfind += len(search.group(0))
