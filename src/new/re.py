import re

c = re.compile(r"""
    (?<!q) # not an alphanumeric character behind us
    (
    (
        (
            http|
            https
        )
        :/{0,2} # maybe a :, :/, or ://
    )?
    hello
    )
    (?!\w) # not an alphanumeric character in front of us
""", flags= re.VERBOSE | re.IGNORECASE)

for x in c.finditer("well http:/hello there"):
    print x.group()
