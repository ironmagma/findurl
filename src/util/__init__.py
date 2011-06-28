
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

def findURLsInText(text, useStatic = True):
    import re
    import relib

    if useStatic:
        import static
        r = static.getStaticRegexString()
    else:
        import gen
        r = gen.genRegexString()

    m = re.compile(r, flags=re.IGNORECASE)

    # FIXME escape quotation marks in \1

    return relib.intoparts(m, text)


# import gen
# import re
# 
# r = gen.genRegexString()
# print r
# m = re.compile(r, flags=re.IGNORECASE)
# 
# print m.search("hi http://google.com/hello/ there").groups()
