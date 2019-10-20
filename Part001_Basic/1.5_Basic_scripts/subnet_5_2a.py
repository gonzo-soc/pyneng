#!/usr/bin/env python3.7

# host_addr = "10.16.0.3/7"
host_addr = "172.16.100.3/30"
# host_addr = "10.16.0.3/16"

node_id = host_addr.split("/")[0]
subnet_mask_str = host_addr.split("/")[1]
subnet_mask = int(subnet_mask_str)

# print("Debug vars: \n")
r_unity = subnet_mask % 8

n_255 = int(subnet_mask / 8)
debug_str = '''
subnet_mask {} r_unity {} n_255 {}
'''.format(subnet_mask, r_unity, n_255)

# print(debug_str)
r_null = (8 - r_unity) % 8
null_count = 32 - subnet_mask - r_null

unity_mask = int(n_255 > 0) * "11111111" + (n_255 - 1) * ".11111111"
point_cond = "." * int((4 - n_255) * n_255 * r_unity > 0)
unity_null_mask = r_unity * "1" + r_null * "0"
null_mask = int(null_count / 8) * ".00000000"
bin_mask = unity_mask + point_cond + unity_null_mask + null_mask
# print(bin_mask)

dec_mask = bin_mask.split(".")
dec_mask[0] = int(dec_mask[0], 2)
dec_mask[1] = int(dec_mask[1], 2)
dec_mask[2] = int(dec_mask[2], 2)
dec_mask[3] = int(dec_mask[3], 2)

print("Subnet mask...." + "\n" + "-" * 80 + "\n")
print("Host address: " + host_addr + "\n")

print("{:8} {:8} {:8} {:8}\n".format(
    dec_mask[0], dec_mask[1], dec_mask[2], dec_mask[3])
)

print("{:08b} {:08b} {:08b} {:08b}\n".format(
    dec_mask[0], dec_mask[1], dec_mask[2], dec_mask[3])
)

bin_node_id = []
node_id_arr = node_id.split(".")
bin_node_id.append('{:08b}'.format(int(node_id_arr[0])))
bin_node_id.append('{:08b}'.format(int(node_id_arr[1])))
bin_node_id.append('{:08b}'.format(int(node_id_arr[2])))
bin_node_id.append('{:08b}'.format(int(node_id_arr[3])))

is_interest_oct = int(r_unity > 0)
# print(str(n_255) + "/" + str(is_interest_oct) + "/" + str(r_null))
# print(bin_node_id[3][0:8])
bin_node_id[
    n_255 - 1 + is_interest_oct
] = bin_node_id[n_255 - 1 + is_interest_oct][0:(8 - r_null)] + "0" * r_null

# print(bin_node_id[0:(n_255 + is_interest_oct)])

bin_subnet = ".".join(
    bin_node_id[0:(n_255 + is_interest_oct)]
) + (4 - (n_255 + is_interest_oct)) * ("." + ("0" * 8))

print("Subnetwork...." + "\n" + "-" * 80 + "\n")

print("Binary view\n")
bin_subnet_arr = bin_subnet.split(".")
print("{:8} {:8} {:8} {:8}\n".format(
    bin_subnet_arr[0], bin_subnet_arr[1],
    bin_subnet_arr[2], bin_subnet_arr[3]
))

print("Decimal view\n")
bin_subnet_arr = bin_subnet.split(".")
print("{:8} {:8} {:8} {:8}\n".format(
    int(bin_subnet_arr[0], 2), int(bin_subnet_arr[1], 2),
    int(bin_subnet_arr[2], 2), int(bin_subnet_arr[3], 2)
))
