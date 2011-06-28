
# Do some crazy path gymnastics in order
# to get everyone (cog, python) okay with
# the fact that other components of 
# findurl are going to be imported from
# this folder.
#
# If you value your sanity, feel free to skip
# this part.

import sys, os
sys.path.append(
    os.path.realpath(
        os.path.join(
            os.path.realpath(
                os.path.dirname(__file__)
            ),
            os.path.pardir
        )
    )
)

#[[[cog
# 
# import sys, os, json
# sys.path.append(
#     os.path.realpath(
#         os.path.join(
#             os.path.realpath(
#                 os.path.dirname(cog.inFile)
#             ),
#             os.path.pardir
#         )
#     )
# )
# 
#
#]]]
#[[[end]]]

# End terrors from the deep


def genRegexString(useStaticTLDTuple = False):
   # Join everything into a regex-compatible string

   if useStaticTLDTuple:
       import static
       tlds = static.getTLDTuple()
   else:
       tlds = genTLDIter()

   tldreg = "("+"|".join(tlds)+")"

   schemes = genSchemes()
   schmreg = "("+"|".join(schemes)+")"


   validbody = r"[a-zA-Z0-9\-\.]"
   invalidbody = "[^"+validbody[1:]

   validstart = r"[a-zA-Z]"
   validmeat = r"[^\s]"
    
   validhash = "(#" + validmeat +"*)?"

   meat = r"(%s(\:%s)?@)?(%s%s*\.)+" % (validbody, validbody, validstart, validbody) +  \
            tldreg + \
                "((/" + validmeat + "*" + validhash + ")|("+validhash+"(?=" +invalidbody+ ")))"

   withoutscheme = "("+meat+")" 

   withscheme = schmreg+r"://"+meat 
   withscheme = "("+withscheme+")"

   return "("+withscheme+"|"+withoutscheme+")"

def genTLDTuple():
   return tuple(genTLDIter())

def genTLDList():
   return list(genTLDIter())

def genTLDIter():
   """Scrape the list of TLDs from IANA"""

   import urllib, itertools
   from re import escape

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


def genSchemes():
    """Scrape a list of URL schemes from Wikipedia."""

    # Too much work for now, just return a static tuple

    schemes=('aaa', 
            'aaas', 
            'acap', 
            'cap', 
            'cid', 
            'crid', 
            'data', 
            'dav', 
            'dict', 
            'dns', 
            'fax', 
            'file', 
            'ftp', 
            'geo', 
            'go', 
            'gopher', 
            'h323', 
            'http', 
            'https', 
            'iax', 
            'icap', 
            'im', 
            'imap', 
            'info', 
            'ipp', 
            'iris', 
            'iris.beep', 
            'iris.xpc', 
            'iris.xpcs', 
            'iris.lws', 
            'ldap', 
            'lsid', 
            'mailto', 
            'mid', 
            'modem', 
            'msrp', 
            'msrps', 
            'mtqp', 
            'mupdate', 
            'news', 
            'nfs', 
            'nntp', 
            'opaquelocktoken', 
            'pop', 
            'pres', 
            'prospero', 
            'rsync', 
            'rtsp', 
            'service', 
            'shttp', 
            'sieve', 
            'sip', 
            'sips', 
            'sms', 
            'snmp', 
            'soap.beep', 
            'soap.beeps', 
            'tag', 
            'tel', 
            'telnet', 
            'tftp', 
            'thismessage', 
            'tip', 
            'tv', 
            'urn', 
            'vemmi', 
            'wais', 
            'xmlrpc.beep', 
            'xmlrpc.beeps', 
            'xmpp', 
            'z39.50r', 
            'z39.50s', 
            'about', 
            'adiumxtra', 
            'aim', 
            'apt', 
            'afp', 
            'aw', 
            'bitcoin', 
            'bolo', 
            'callto', 
            'chrome', 
            'coap', 
            'content', 
            'cvs', 
            'doi', 
            'ed2k', 
            'facetime', 
            'feed', 
            'finger', 
            'fish', 
            'git', 
            'gg', 
            'gizmoproject', 
            'gtalk', 
            'irc', 
            'ircs', 
            'irc6', 
            'itms', 
            'jar', 
            'javascript', 
            'keyparc', 
            'lastfm', 
            'ldaps', 
            'magnet', 
            'maps', 
            'mms', 
            'msnim', 
            'mumble', 
            'mvn', 
            'notes', 
            'palm', 
            'paparazzi', 
            'psyc', 
            'rmi', 
            'rtmp', 
            'secondlife', 
            'sgn', 
            'skype', 
            'spotify', 
            'ssh', 
            'sftp', 
            'smb', 
            'soldat', 
            'steam', 
            'svn', 
            'teamspeak', 
            'things', 
            'unreal', 
            'ut2004', 
            'ventrilo', 
            'view-source', 
            'webcal', 
            'ws', 
            'wss', 
            'wtai', 
            'wyciwyg', 
            'xfire', 
            'xri', 
            'ymsgr')

    from re import escape

    return map(escape, schemes)

    #import urllib, itertools, xml.dom.minidom as xml

    #class FakeOpener(urllib.FancyURLopener):
    #    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17'

    #h = FakeOpener().open("http://en.wikipedia.org/wiki/Special:Export/URI_scheme").read()

    #d = xml.parseString(h).getElementsByTagName("page")[0].getElementsByTagName("revision")[0].getElementsByTagName("text")[0].firstChild.wholeText

    #return d
