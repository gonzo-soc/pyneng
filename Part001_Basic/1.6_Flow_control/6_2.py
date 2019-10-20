print("6.2a-b IP address type\n")
print("-" * 80)

isValid = False

while not isValid:
    ip_addr = input("Enter ip address (xxx.xxx.xxx.xxx/xx) : ")

    node_id = ip_addr.split("/")[0].split(".")
    isValid = True
    errMsg = ""
    if (len(node_id) != 4):
        isValid = False
    errMsg = "wrong length of the ip address"

    for o in node_id:
        if int(o) < 0 or int(o) > 255:
            isValid = False
            errMsg = "one of the octets is out of range, must be (0.. 255)"
            if (not isValid):
                print('''
                    Error: ip address you entered is corrupted: {},
                    error msg: {}
                    '''.format(ip_addr, errMsg))

isUnicast = (int(node_id[0]) >= 1 and int(node_id[0]) <= 223)
isMulticast = (int(node_id[0]) >= 224 and int(node_id[0]) < 239)
isBroadCast = True
isUnsigned = True

for o in node_id:
    if o != "255":
        isBroadCast = False

for o in node_id:
    if o != "0":
        isUnsigned = False

if isUnicast:
    print("Info: UNICAST")
elif isMulticast:
    print("Info: MULTICAST")
elif isBroadCast:
    print("Info: Broadcast")
elif isUnsigned:
    print("Info: Unsigned")
else:
    print("Info: Unused")
