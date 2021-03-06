# Everything in this file is generated via cog, using the gen/ files.
# Most of it isn't very readable, and it's mainly here so people can
# just import a module and use some pre-computed things.



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


_cached_regex = None



# From http://www.regular-expressions.info/regexbuddy/ipaccurate.html

ipv4num = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" 


# Courtesy of Stephen Ryan at Dartware <http://forums.dartware.com/viewtopic.php?t=452>
ipv6num = "".join(map(str.strip, r"""(((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:)
            {6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0
            -4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1
            ,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d
            |[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})
            |((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2
            [0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]
            {1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)
            (\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}((
            (:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1
            \d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]
            {1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25
            [0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))
            |:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|
            2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))
            (%.+)?)""".split('\n'))) 

def getStaticRegexString():
    # [[[cog
    #
    # import gen, json, gen
    # cog.outl("return "+json.dumps(gen.genRegexString()))
    #
    # ]]]
    return "(((aaa|aaas|acap|cap|cid|crid|data|dav|dict|dns|fax|file|ftp|geo|go|gopher|h323|http|https|iax|icap|im|imap|info|ipp|iris|iris\\.beep|iris\\.xpc|iris\\.xpcs|iris\\.lws|ldap|lsid|mailto|mid|modem|msrp|msrps|mtqp|mupdate|news|nfs|nntp|opaquelocktoken|pop|pres|prospero|rsync|rtsp|service|shttp|sieve|sip|sips|sms|snmp|soap\\.beep|soap\\.beeps|tag|tel|telnet|tftp|thismessage|tip|tv|urn|vemmi|wais|xmlrpc\\.beep|xmlrpc\\.beeps|xmpp|z39\\.50r|z39\\.50s|about|adiumxtra|aim|apt|afp|aw|bitcoin|bolo|callto|chrome|coap|content|cvs|doi|ed2k|facetime|feed|finger|fish|git|gg|gizmoproject|gtalk|irc|ircs|irc6|itms|jar|javascript|keyparc|lastfm|ldaps|magnet|maps|mms|msnim|mumble|mvn|notes|palm|paparazzi|psyc|rmi|rtmp|secondlife|sgn|skype|spotify|ssh|sftp|smb|soldat|steam|svn|teamspeak|things|unreal|ut2004|ventrilo|view\\-source|webcal|ws|wss|wtai|wyciwyg|xfire|xri|ymsgr)://([a-zA-Z0-9\\-\\.](\\:[a-zA-Z0-9\\-\\.])?@)?([a-zA-Z][a-zA-Z0-9\\-\\.]*\\.)+(AC|AD|AE|AERO|AF|AG|AI|AL|AM|AN|AO|AQ|AR|ARPA|AS|ASIA|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BIZ|BJ|BM|BN|BO|BR|BS|BT|BV|BW|BY|BZ|CA|CAT|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|COM|COOP|CR|CU|CV|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EDU|EE|EG|ER|ES|ET|EU|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GOV|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|INFO|INT|IO|IQ|IR|IS|IT|JE|JM|JO|JOBS|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MG|MH|MIL|MK|ML|MM|MN|MO|MOBI|MP|MQ|MR|MS|MT|MU|MUSEUM|MV|MW|MX|MY|MZ|NA|NAME|NC|NE|NET|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|ORG|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PRO|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|ST|SU|SV|SY|SZ|TC|TD|TEL|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TP|TR|TRAVEL|TT|TV|TW|TZ|UA|UG|UK|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XXX|YE|YT|ZA|ZM|ZW)(?::\\d+)?((/[^\\s]*(#[^\\s]*)?)|((#[^\\s]*)?(?=[^a-zA-Z0-9\\-\\.]))))|(([a-zA-Z0-9\\-\\.](\\:[a-zA-Z0-9\\-\\.])?@)?([a-zA-Z][a-zA-Z0-9\\-\\.]*\\.)+(AC|AD|AE|AERO|AF|AG|AI|AL|AM|AN|AO|AQ|AR|ARPA|AS|ASIA|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BIZ|BJ|BM|BN|BO|BR|BS|BT|BV|BW|BY|BZ|CA|CAT|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|COM|COOP|CR|CU|CV|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EDU|EE|EG|ER|ES|ET|EU|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GOV|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|INFO|INT|IO|IQ|IR|IS|IT|JE|JM|JO|JOBS|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MG|MH|MIL|MK|ML|MM|MN|MO|MOBI|MP|MQ|MR|MS|MT|MU|MUSEUM|MV|MW|MX|MY|MZ|NA|NAME|NC|NE|NET|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|ORG|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PRO|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|ST|SU|SV|SY|SZ|TC|TD|TEL|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TP|TR|TRAVEL|TT|TV|TW|TZ|UA|UG|UK|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|XXX|YE|YT|ZA|ZM|ZW)(?::\\d+)?((/[^\\s]*(#[^\\s]*)?)|((#[^\\s]*)?(?=[^a-zA-Z0-9\\-\\.])))))"
    # [[[end]]]


def getStaticTLDs():
   """Return a pre-generated list of TLDs"""

   import gen

   # [[[cog
   #
   # import gen
   # 
   # tlds = "(\n   " + ",\n   ".join(map(json.dumps, (x for x in gen.genTLDIter()))) + "\n)"
   #
   # cog.outl("return " + tlds)
   # 
   # ]]]
   return (
      "AC",
      "AD",
      "AE",
      "AERO",
      "AF",
      "AG",
      "AI",
      "AL",
      "AM",
      "AN",
      "AO",
      "AQ",
      "AR",
      "ARPA",
      "AS",
      "ASIA",
      "AT",
      "AU",
      "AW",
      "AX",
      "AZ",
      "BA",
      "BB",
      "BD",
      "BE",
      "BF",
      "BG",
      "BH",
      "BI",
      "BIZ",
      "BJ",
      "BM",
      "BN",
      "BO",
      "BR",
      "BS",
      "BT",
      "BV",
      "BW",
      "BY",
      "BZ",
      "CA",
      "CAT",
      "CC",
      "CD",
      "CF",
      "CG",
      "CH",
      "CI",
      "CK",
      "CL",
      "CM",
      "CN",
      "CO",
      "COM",
      "COOP",
      "CR",
      "CU",
      "CV",
      "CX",
      "CY",
      "CZ",
      "DE",
      "DJ",
      "DK",
      "DM",
      "DO",
      "DZ",
      "EC",
      "EDU",
      "EE",
      "EG",
      "ER",
      "ES",
      "ET",
      "EU",
      "FI",
      "FJ",
      "FK",
      "FM",
      "FO",
      "FR",
      "GA",
      "GB",
      "GD",
      "GE",
      "GF",
      "GG",
      "GH",
      "GI",
      "GL",
      "GM",
      "GN",
      "GOV",
      "GP",
      "GQ",
      "GR",
      "GS",
      "GT",
      "GU",
      "GW",
      "GY",
      "HK",
      "HM",
      "HN",
      "HR",
      "HT",
      "HU",
      "ID",
      "IE",
      "IL",
      "IM",
      "IN",
      "INFO",
      "INT",
      "IO",
      "IQ",
      "IR",
      "IS",
      "IT",
      "JE",
      "JM",
      "JO",
      "JOBS",
      "JP",
      "KE",
      "KG",
      "KH",
      "KI",
      "KM",
      "KN",
      "KP",
      "KR",
      "KW",
      "KY",
      "KZ",
      "LA",
      "LB",
      "LC",
      "LI",
      "LK",
      "LR",
      "LS",
      "LT",
      "LU",
      "LV",
      "LY",
      "MA",
      "MC",
      "MD",
      "ME",
      "MG",
      "MH",
      "MIL",
      "MK",
      "ML",
      "MM",
      "MN",
      "MO",
      "MOBI",
      "MP",
      "MQ",
      "MR",
      "MS",
      "MT",
      "MU",
      "MUSEUM",
      "MV",
      "MW",
      "MX",
      "MY",
      "MZ",
      "NA",
      "NAME",
      "NC",
      "NE",
      "NET",
      "NF",
      "NG",
      "NI",
      "NL",
      "NO",
      "NP",
      "NR",
      "NU",
      "NZ",
      "OM",
      "ORG",
      "PA",
      "PE",
      "PF",
      "PG",
      "PH",
      "PK",
      "PL",
      "PM",
      "PN",
      "PR",
      "PRO",
      "PS",
      "PT",
      "PW",
      "PY",
      "QA",
      "RE",
      "RO",
      "RS",
      "RU",
      "RW",
      "SA",
      "SB",
      "SC",
      "SD",
      "SE",
      "SG",
      "SH",
      "SI",
      "SJ",
      "SK",
      "SL",
      "SM",
      "SN",
      "SO",
      "SR",
      "ST",
      "SU",
      "SV",
      "SY",
      "SZ",
      "TC",
      "TD",
      "TEL",
      "TF",
      "TG",
      "TH",
      "TJ",
      "TK",
      "TL",
      "TM",
      "TN",
      "TO",
      "TP",
      "TR",
      "TRAVEL",
      "TT",
      "TV",
      "TW",
      "TZ",
      "UA",
      "UG",
      "UK",
      "US",
      "UY",
      "UZ",
      "VA",
      "VC",
      "VE",
      "VG",
      "VI",
      "VN",
      "VU",
      "WF",
      "WS",
      "XXX",
      "YE",
      "YT",
      "ZA",
      "ZM",
      "ZW"
   )
   #[[[end]]]
