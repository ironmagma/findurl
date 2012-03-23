import re

protocol = r"""
        (
            http|
            https
        )
        :/{0,2} # maybe a :, :/, or ://
"""

sl_domain_name = r"""
    (
        [\w\d]+ # second level domain names cannot begin with a dash
        [-\w\d]*
        (
            \.
            [\w\d]
            [-\w\d]*
        )*
    )
"""

domain_shebang = r"""
    (
        ( # username(:password?)? block
            [\w\d_]+ # Username
            (
                :
                ([\w\d_]+)? # Password
            )?
            @
        )?
        """ + sl_domain_name + r"""
    )
"""

tld = r"""
    (
        \.
        (
            com|
            org|
            net
        )
    )
"""

c = re.compile(r"""
    (?<!q) # not an alphanumeric character behind us
    (
        ( # we have a protocol
         """ + protocol + r"""
         """ + domain_shebang + r"""
        ) |
        ( # no protocol
         """ + domain_shebang + r"""
         """ + tld + r"""
        )
    )
    (?!\w) # not an alphanumeric character in front of us
""", flags= re.VERBOSE | re.IGNORECASE)

for x in c.finditer("well ironmagma:@google.com there"):
    print x.group()
