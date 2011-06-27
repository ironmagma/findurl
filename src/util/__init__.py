
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

def linkifyURLs(text, useStatic = False):
    import re

    if useStatic:
        import static
        r = static.getStaticRegexString()
    else:
        import gen
        r = gen.genRegexString()

    r = r"(?<=\b)" + r + r"(?=\b)" # Add some lookahead/lookbehind

    m = re.compile(r, flags=re.IGNORECASE)

    return re.sub(m, r'<a href="\1">\1</a>', text) # FIXME escape quotation marks in \1

