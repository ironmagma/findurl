
ipv4num = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" # From http://www.regular-expressions.info/regexbuddy/ipaccurate.html

ipv6num = r"/^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$/" # Courtesy of Stephen Ryan at Dartware <http://forums.dartware.com/viewtopic.php?t=452>

def generateRegex():
    # Join them all into a regex-compatible string

    tlds = getTLDs()
    tldreg = "("+"|".join(tlds)+")"

    

def getTLDs():
    import urllib, itertools

    tlds = iter(urllib.urlopen("http://data.iana.org/TLD/tlds-alpha-by-domain.txt").read().replace('\r\n', '\n').split('\n'))
    
    # Filter out all punycode domains, since that's not supported yet
    tlds = itertools.ifilter(lambda x: x.find('--') == -1, tlds)

    # Kill comments
    tlds = itertools.imap(lambda x: x.split("#", 1)[0], tlds)

    # Kill surrounding whitespace
    tlds = itertools.imap(str.strip, tlds)

    # Kill blank lines
    tlds = itertools.ifilter(lambda x: x != '', tlds)

    return tlds

def getSchemes():
    """Scrape a list of URL schemes from Wikipedia."""

    # Too much work for now, just return a static tuple

    return ('aaa ', 'aaas ', 'acap ', 'cap ', 'cid ', 'crid ', 'data', 'dav', 'dict', 'dns', 'fax', 'file', 'ftp', 'geo', 'go', 'gopher', 'h323', 'http', 'https', 'iax', 'icap', 'im', 'imap', 'info', 'ipp', 'iris', 'iris.beep', 'iris.xpc', 'iris.xpcs', 'iris.lws', 'ldap', 'lsid', 'mailto', 'mid ', 'modem', 'msrp', 'msrps', 'mtqp', 'mupdate', 'news', 'nfs', 'nntp', 'opaquelocktoken', 'pop', 'pres', 'prospero', 'rsync', 'rtsp', 'service', 'shttp', 'sieve', 'sip', 'sips', 'sms', 'snmp', 'soap.beep', 'soap.beeps', 'tag', 'tel ', 'telnet', 'tftp', 'thismessage', 'tip', 'tv', 'urn', 'vemmi', 'wais', 'xmlrpc.beep', 'xmlrpc.beeps', 'xmpp', 'z39.50r', 'z39.50s', 'about', 'adiumxtra', 'aim', 'apt', 'afp', 'aw', 'bitcoin', 'bolo', 'callto ', 'chrome ', 'coap ', 'content ', 'cvs ', 'doi', 'ed2k', 'Facetime', 'feed', 'finger', 'fish', 'git', 'gg', 'gizmoproject', 'gtalk', 'irc', 'ircs', 'irc6', 'itms', 'jar', 'javascript', 'keyparc', 'lastfm', 'ldaps', 'magnet', 'maps', 'mms', 'msnim', 'mumble', 'mvn', 'notes', 'palm', 'paparazzi', 'psyc', 'rmi', 'rtmp', 'secondlife', 'sgn', 'skype ', 'spotify', 'ssh', 'sftp', 'smb', 'soldat', 'steam', 'svn ', 'teamspeak', 'things', 'unreal', 'ut2004', 'ventrilo', 'view-source', 'webcal', 'ws', 'wss', 'wtai', 'wyciwyg', 'xfire', 'xri', 'ymsgr')

    #import urllib, itertools, xml.dom.minidom as xml

    #class FakeOpener(urllib.FancyURLopener):
    #    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17'

    #h = FakeOpener().open("http://en.wikipedia.org/wiki/Special:Export/URI_scheme").read()

    #d = xml.parseString(h).getElementsByTagName("page")[0].getElementsByTagName("revision")[0].getElementsByTagName("text")[0].firstChild.wholeText

    #return d
    
