from collections import OrderedDict
favorite_sprache = OrderedDict()
favorite_sprache['jen'] = 'python'
favorite_sprache['sarah'] = 'c++'
favorite_sprache['edward'] = 'ruby'
favorite_sprache['phil'] = 'python'
for name, sprache in favorite_sprache.items():
    print(f"{name.title()}'s favorite language is {sprache.title()}.")
