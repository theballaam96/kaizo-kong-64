import subprocess
import os
import shutil
import binascii
import gzip
import sys
from compressFile import compressGZipFile
from n64lib import *

file_dict = {
	"files": [
		{
			"start": 0x113F0,
			"compressed_size": 0xF064C,
			"target_compress_size": 0xB15E0,
			"source_file": "StaticCode.bin",
			"output_file": "StaticCode_Copy.bin.gz",
			"name": "Static ASM Code",
		},
		{
			"start": 0xD36338,
			"compressed_size": 0x8D8,
			"target_compress_size": 0x8D8,
			"source_file": "TrainingGrounds.bin",
			"output_file": "TrainingGrounds_Copy.bin",
			"name": "Training Grounds Setup",
			"table_data": {
				"table_type": "setup",
				"entry_index": 0xB0,
			}
		},
		{
			"start": 0x117CA8C,
			"compressed_size": 0x46,
			"target_compress_size": 0x46,
			"source_file": "TrainingGrounds_Spawners.bin",
			"output_file": "TrainingGrounds_Spawners_Copy.bin",
			"name": "Training Grounds Spawners",
			"table_data": {
				"table_type": "character_spawners",
				"entry_index": 0xB0,
			}
		}
	]
}

new_info_start = [0x2020000]

pointer_tables = {
	"character_spawners": 0x1170D44,
	"loading_zones": 0x1180BF8,
	"setup": 0xD0E86C,
	"cutscenes": 0xCDD29C,
	"walls": 0x43CBEC,
	"floors": 0x63CA6C,
	"geometry": 0x15232C,
}

rewrite_table = {
	"character_spawners": [],
	"loading_zones": [],
	"setup": [],
	"cutscenes": [],
	"walls": [],
	"floors": [],
	"geometry": [],
}

table_size = {
	"character_spawners": 216,
	"loading_zones": 216,
	"setup": 216,
	"cutscenes": 216,
	"walls": 216,
	"floors": 216,
	"geometry": 216,
}

print("DONKEY KONG 64 PRACTICE ROM")
print("ROM and Builder by Ballaam")
print("[0 / 5] - Building ROM")
ROMName = "./../dk64.z64"
with open(ROMName, "r+b") as fh:
	print("[1 / 5] - Unzipping files from ROM")
	for x in file_dict["files"]:
		fh.seek(x["start"])
		byte_read = fh.read(x["compressed_size"])
		binName = x["source_file"]

		if os.path.exists(binName):
		    os.remove(binName)

		with open(binName, "wb") as fg:
			dec = gzip.decompress(byte_read)
			if x["source_file"] == "StaticCode.bin":
				fg.write(dec[:0x149160])
			else:
				fg.write(dec)

import modules
newROMName = "kaizo-kong-64.z64"
if os.path.exists(newROMName):
    os.remove(newROMName)
shutil.copyfile(ROMName, newROMName);

with open(newROMName, "r+b") as fh:
	print("[2 / 7] - Checking for increased entropy in pointer table files")
	for x in file_dict["files"]:
		temp_keys = x.keys()
		if "table_data" in temp_keys:
			binName = x["output_file"]
			with open(binName, "rb") as fg:
				byte_read = fg.read()
				compress = gzip.compress(byte_read, compresslevel=9)
				if len(compress) > x["target_compress_size"]:
					rewrite_table[x["table_data"]["table_type"]].append(x["table_data"]["entry_index"]);
					#print("Rewriting the " + x["table_data"]["table_type"] + " type is required")
	table_keys = rewrite_table.keys()
	for x in table_keys:
		if len(rewrite_table[x]) > 0:
			ptr_table = pointer_tables[x]
			for y in range(table_size[x]):
				ptr_table_entry_location = ptr_table + (y * 4)
				if not y in rewrite_table[x]:
					fh.seek(ptr_table_entry_location)
					old_rom_location = 0x101C50 + arrToInt(list(fh.read(4)))
					next_entry = ptr_table_entry_location + 4
					fh.seek(next_entry)
					old_rom_next_location = 0x101C50 + arrToInt(list(fh.read(4)))
					size = old_rom_next_location - old_rom_location
					#
					fh.seek(old_rom_location)
					compressed_bytes = fh.read(size)
					# compression_pending = True
					# try:
					# 	fh.seek(old_rom_location)
					# 	compressed_bytes = fh.read(size - 1)
					# 	decompressed = gzip.decompress(compressed_bytes)
					# 	compression_pending = False
					# except:
					# 	a = 1
					# if compression_pending:
					# 	try:
					# 		fh.seek(old_rom_location)
					# 		compressed_bytes = fh.read(size)
					# 		decompressed = gzip.decompress(compressed_bytes)
					# 	except:
					# 		print("orl: " + hex(old_rom_location))
					# 		print("s: " + hex(size))
					# 		print("ERROR")
					#

					new_ptr = new_info_start[0] - 0x101C50
					if y != 0:
						fh.seek(ptr_table_entry_location)
						fh.write(bytearray(convert_int_to_arr(new_ptr,4)))
					fh.seek(new_info_start[0])
					#compressed_bytes = gzip.compress(decompressed, compresslevel=9)
					fh.write(compressed_bytes)
					#print(hex(new_info_start[0]))
					new_info_start[0] = new_info_start[0] + len(compressed_bytes)
					if y == table_size[x] - 1:
						fh.seek(ptr_table_entry_location + 4)
						fh.write(bytearray(convert_int_to_arr(new_info_start[0] - 0x101C50,4)))
				else:
					fh.seek(ptr_table_entry_location)
					new_ptr = new_info_start[0] - 0x101C50
					fh.write(bytearray(convert_int_to_arr(new_ptr,4)))
					fh.seek(new_info_start[0])
					for z in file_dict["files"]:
						temp_keys = z.keys()
						written_data = False;
						if "table_data" in temp_keys:
							if z["table_data"]["table_type"] == x:
								if z["table_data"]["entry_index"] == y:
									if not written_data:
										with open(z["output_file"], "rb") as fg:
											byte_read = fg.read()
											compress = gzip.compress(byte_read, compresslevel=9)
											fh.write(compress)
											#print(hex(new_info_start[0]))
											new_info_start[0] = new_info_start[0] + len(compress)
											written_data = True;
											if y == table_size[x] - 1:
												fh.seek(ptr_table_entry_location + 4)
												fh.write(bytearray(convert_int_to_arr(new_info_start[0] - 0x101C50,4)))
with open(newROMName, "r+b") as fh:
	print("[2 / 5] - Writing modified compressed files to ROM")
	for x in file_dict["files"]:
		binName = x["output_file"]
		if os.path.exists(binName):
			with open(binName, "rb") as fg:
				byte_read = fg.read()
				if x["source_file"] != "StaticCode.bin":
					compress = gzip.compress(byte_read, compresslevel=9)
				else:
					compress = byte_read
				temp_keys = x.keys()
				if len(compress) <= x["target_compress_size"]:
					if "table_data" in temp_keys:
						if len(rewrite_table[x["table_data"]["table_type"]]) == 0:
							fh.seek(x["start"])
							fh.write(compress)
					else:
						fh.seek(x["start"])
						fh.write(compress)
				else:
					if "table_data" in temp_keys:
						if len(rewrite_table[x["table_data"]["table_type"]]) == 0:
							print("Cannot write " + x["output_file"] + " to ROM. Compression size (" + str(len(compress)) + ") too big (" + str(x["target_compress_size"]) + ")")
		else:
			print(x["output_file"] + " does not exist")

# for x in file_dict["files"]:
# 	if os.path.exists(x["output_file"]):
# 		os.remove(x["output_file"])
# 	if os.path.exists(x["source_file"]):
# 		os.remove(x["source_file"])
# 	if os.path.exists("StaticCode_Copy.bin"):
# 		os.remove("StaticCode_Copy.bin")

print("[3 / 5] - Loading ASM: This may take some time")
import asmloader
print("[4 / 5] - ASM Written")

# crc patch
with open(newROMName, "r+b") as fh:
    fh.seek(0x3154)
    fh.write(bytearray([0, 0, 0, 0]))
crcresult = subprocess.check_output(["n64crc", newROMName])
print("[5 / 5] - CRC Updated")
print("Your ROM is now built")
exit()