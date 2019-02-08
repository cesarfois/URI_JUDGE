import re



for i in s:
    if i in simb:
        a = True
    if re.match("[a-z]", i):
        mi = True
    if re.match("[A-Z]", i):
        ma = True
    if re.match('[0-9]', i):
        n = True