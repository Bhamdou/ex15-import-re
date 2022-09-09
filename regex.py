import re
line_prefix = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""
pattern = r"\w.+@\w+[.].*" 
pattern2 = r"[A-Z]"
x = re.findall(pattern,line_prefix)
x2 = re.findall(pattern2,line_prefix)
print(x)
print(x2)
