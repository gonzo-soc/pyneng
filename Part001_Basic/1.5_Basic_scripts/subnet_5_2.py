#!/usr/bin/env python3.7

subnet = "10.1.0.0/7"
subnet_id = subnet.split("/")[0]
subnet_mask_str = subnet.split("/")[1]
subnet_mask = int(subnet_mask_str)
print("Debug vars: \n")
r_unity = subnet_mask % 8

n_255 = int(subnet_mask / 8)
debug_str = '''
subnet_id {} subnet_mask_str {} subnet_mask {} r_unity {} n_255 {}
'''.format(subnet_id, subnet_mask_str, subnet_mask, r_unity, n_255)

print(debug_str)

unity_mask = n_255 * "11111111 " + r_unity * "1"
r_null = 8 - r_unity
null_count = 32 - subnet_mask - r_null
null_mask = r_null * "0" + int(null_count / 8) * " 00000000"
bin_mask = unity_mask + null_mask
debug_str = "unity_mask {} null_mask {}".format(unity_mask, null_mask)

print(debug_str)

dec_mask = bin_mask.split(" ")
dec_mask[0] = int(dec_mask[0], 2)
dec_mask[1] = int(dec_mask[1], 2)
dec_mask[2] = int(dec_mask[2], 2)
dec_mask[3] = int(dec_mask[3], 2)

print("Digital mask...." + "\n" + "-" * 80 + "\n")
print(subnet + "\n")

print("{:8} {:8} {:8} {:8}\n".format(
    dec_mask[0], dec_mask[1], dec_mask[2], dec_mask[3])
)

print("{:08b} {:08b} {:08b} {:8b}\n".format(
    dec_mask[0], dec_mask[1], dec_mask[2], dec_mask[3])
)
