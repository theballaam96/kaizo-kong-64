import struct

def float_to_hex(f):
	return hex(struct.unpack("<I", struct.pack("<f",f))[0])

def convert_int_to_arr(input_int,byte_count):
	output_arr = []
	while input_int > 0:
	  byte = input_int % 0x100
	  output_arr.append(byte)
	  input_int //= 0x100
	while len(output_arr) < byte_count:
		output_arr.append(0)
	return reverse(output_arr)

def reverse(lst):
	return [ele for ele in reversed(lst)]

def unsigned_to_signed(val,size):
	if val >= (2 ** ((size * 8) - 1)):
		val = val - (2 ** (size * 8))
	return val

def signed_to_unsigned(val,size):
	if val < 0:
		val = val + (2 ** (size * 8));
	return val

def arrToInt(arr):
	total = 0;
	for x in arr:
		total = (total * 256) + x;
	return total