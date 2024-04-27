'''
You have access to a named User tuple, which contains data about the user of a certain resource.
The first element of the named tuple is the user's name, the second is the last name, the third is
the email address, and the fourth is the subscription status. A list of users containing these tuples is also available.

Display data about each user from this list, having previously sorted them by subscription status from expensive
to cheap, and if the statuses match, in the lexicographical order of email addresses. Data about each user
must be specified in the following format:

<name> <last name>
   Email: <email address>
   Plan: <subscription status>
'''

from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

s = ["Gold", "Silver", "Bronze", "Basic"]
for i in sorted(users, key=lambda x: (s.index(x[-1]), x[-2])):
    row = i._asdict()
    print(f"{row['name']} {row['surname']}", f"  Email: {row['email']}", f"  Plan: {row['plan']}", "", sep="\n")

