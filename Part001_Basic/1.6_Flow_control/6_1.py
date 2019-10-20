print("6.1 MAC address conversion\n")
print("-" * 80)

MAC = [
    "EC-B1-D7-72-38-1E",
    "AB:CD:EF:89:10:67",
    "AB:CD:EF:89:10:68",
    "AB:CD:EF:89:10:69"
]

print("Income MAC list:", MAC)

CISCO_MAC = []

for m in MAC:
    if m.find("-"):
        CISCO_MAC.append(m.replace("-", "."))
    elif m.find(":"):
        CISCO_MAC.append(m.replace(":", "."))
    else:
        print("Info: unknown separator:", m)

print("Cisco MAC list:", CISCO_MAC)

print("-" * 80)
print("\nEND")
