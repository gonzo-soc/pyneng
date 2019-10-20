
print("\nFor for arrays")
print("-" * 80 + "\n")

words = ["worried", "fall", "lie", "dress", "revenue"]
u_words = []

for w in words:
    u_words.append(w.upper())

print(u_words)

print("\nDictionary")
print("-" * 80 + "\n")

dict = {
  "IGP": "EIGRP",
  "network_001": "10.10.0.7/30",
  "network_002": "192.168.0.0/24"
}

for k in dict:
  print(k)

print("Keys and values in dictionaries")
print("-" * 80)
for k, v in dict.items():
  print (k + "=>" + v)

print("\nIf and for")
print("-" * 80 + "\n")

access_template = ['switchport mode access',
                  'switchport access vlan',
                  'spanning-tree portfast',
                  'spanning-tree bpduguard enable']

fast_int = {'access': { '0/12':10,
                        '0/14':11,
                        '0/16':17,
                        '0/17':150}}

for fint, vlan in fast_int['access'].items():
  print('interface Fa{}'.format(fint))
  for l in access_template:
    if l.endswith('access vlan'):
      print('{} {}'.format(l, vlan))
    else:
      print('{}'.format(l))
  print ("\n")

print("\nWhile")
print("-" * 80 + "\n")

username = input("Enter username: ")
pwd = input("Enter password: ")

isValid = False

while not isValid: 
  if (len(pwd) < 8):
    print("Password length [ " + str(len(pwd)) + " ] < 8")
    pwd = input("Enter correct password: ")
  elif username in pwd:
    print("Password [ " + pwd + " ] contains username [ " + username + " ]")
    pwd = input("Enter correct password: ")
  else:
    print("Password [ " + pwd + " ] is fine")
    isValid = True

print("\ntry/except")
print("-" * 80 + "\n")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
finally:
    print("Sweep trash")
  