import re
with open('data.txt', 'r') as f:
    s  = f.read()

ls = re.split('\n\s*\n', s)

data = """byr
iyr
eyr
hgt
hcl
ecl
pid"""
sdd = set(data.splitlines())
print(sdd)

def f(z):
    return set(re.findall(r'(\w{3})\:', z))

print(sum(sdd.issubset(f(x)) for x in ls))
