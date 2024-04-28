'''
HTML elements are the basis of the HTML language. Each HTML element is identified by a start (opening) and end
(closing) tag. The opening and closing tags contain the name of the element. The opening tag may contain additional
information - attributes and attribute values:

<b>BeeGeek</b>
<a href="https://stepik.org">Stepik</a>
In the example above, the <b> tag does not contain any attributes, and the <a> tag contains an href attribute with the
value https://stepik.org.

Write a program that finds all the attributes of each tag in a fragment of an HTML page.

Input format
The program receives an arbitrary number of lines as input, which form a fragment of an HTML page.

Output format
The program must find all the tags in the entered fragment of the HTML page and display them, indicating the
corresponding attributes for each. Tags, along with all attributes, must be located each on a separate line,
in the following format:

<tag>: <attribute>, <attribute>, ...
Tags, as well as tag attributes, must be arranged in lexicographical order.
'''

import re
import sys

dict={}
for i in sys.stdin:
    for i in re.findall(r'<([^/>][^>]*)>', i):
        param = i.split()
        for j in range(len(param)):
            dict[param[0]] = dict.get(param[0], set()) | set(re.findall(r'(.+)=', param[j]))

for i in sorted(dict):
    print(i, end=": ")
    print(*sorted(dict[i]), sep=", ")

# Example
# Input
# <div id="oldie-warning" class="do-not-print">
#     <p>
#         <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
#         <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
#     </p>
# </div>
# Output:
# a: href
# div: class, id
# em:
# p:
# strong: