# Requires cog
# http://nedbatchelder.com/code/cog/

find ./src -name "*.py" -print0 | xargs -0 cog.py -r
