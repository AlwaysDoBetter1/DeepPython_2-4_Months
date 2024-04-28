'''
Complete the code below so that the regex variable contains a regular expression that matches the times
of the HH:MM format.

Note 1: Additional validation is required, i.e. the time 54:96 should not match the regex.
'''

import re

regex = r'[01][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]'

# Example
# Input
# So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30
# Output:
# 17:30