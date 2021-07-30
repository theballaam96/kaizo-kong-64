extract = {
	"unknown_array": [],
	"character_spawners": []
}

from n64lib import *

def unpackCharacterSpawners(data):
	read_header = 0;
	if not data:
		unknown_array_count = 0;
	else:
		unknown_array_count = arrToInt(list(data[read_header:read_header + 2]))
		read_header += 2
	unk_arr_iterator = 0;
	if unknown_array_count > 0:
		while unk_arr_iterator < unknown_array_count:
			start_read_header = read_header
			ivar13 = 0;
			if not data:
				ivar11 = 0
			else:
				ivar11 = arrToInt(list(data[read_header:read_header + 2]))
				read_header += 2
			if ivar11 > 0:
				read_header = read_header + (6 * ivar11)
			ivar13 = 0;
			if not data:
				ivar11 = 0
			else:
				ivar11 = arrToInt(list(data[read_header:read_header + 2]))
				read_header += 2
			if ivar11 > 0:
				read_header = read_header + (10 * ivar11)
			if data:
				read_header += 4
			unknown_data = {
				"stream": list(data[start_read_header:read_header])
			}
			extract["unknown_array"].append(unknown_data)
			unk_arr_iterator += 1
	unk_arr_iterator = 0;
	if not data:
		spawn_count = 0;
	else:
		spawn_count = arrToInt(list(data[read_header:read_header + 2]))
		read_header += 2
	if spawn_count > 0:
		while unk_arr_iterator < spawn_count:
			#print(hex(read_header))
			start_read_header = read_header
			ivar14 = 0
			puvar7 = read_header + 0x16;
			val_enemy = arrToInt(list(data[read_header:read_header+1]))
			val_yrot = arrToInt(list(data[read_header+2:read_header+4]))
			val_xpos = unsigned_to_signed(arrToInt(list(data[read_header + 4:read_header + 6])),2)
			val_ypos = unsigned_to_signed(arrToInt(list(data[read_header + 6:read_header + 8])),2)
			val_zpos = unsigned_to_signed(arrToInt(list(data[read_header + 8:read_header + 10])),2)
			val_csmodel = arrToInt(list(data[read_header + 0xA:read_header + 0xB]))
			val_maxidle = arrToInt(list(data[read_header + 0xC:read_header + 0xD]))
			val_maxaggro = arrToInt(list(data[read_header + 0xD:read_header + 0xE]))
			val_scale = arrToInt(list(data[read_header + 0xF:read_header + 0x10]))
			val_aggro = arrToInt(list(data[read_header + 0x10:read_header + 0x11]))
			val_extracount = arrToInt(list(data[read_header + 0x11:read_header + 0x12]))
			val_initspawnstate = arrToInt(list(data[read_header + 0x12:read_header + 0x13]))
			val_spawntrigger = arrToInt(list(data[read_header + 0x13:read_header + 0x14]))
			val_initrespawntimer = arrToInt(list(data[read_header + 0x14:read_header + 0x16]))
			if arrToInt(list(data[read_header + 0x11: read_header + 0x12])) != 0:
				puvar7 = puvar7 + (2 * arrToInt(list(data[read_header + 0x11: read_header + 0x12])))
			unk_arr_iterator += 1
			read_header = puvar7
			spawner_data = {
				"stream": list(data[start_read_header:read_header]),
				"vanilla_index": unk_arr_iterator,
				"enemy_val": val_enemy,
				"y_rot": val_yrot,
				"x": val_xpos,
				"y": val_ypos,
				"z": val_zpos,
				"csmodel": val_csmodel,
				"max_idle_speed": val_maxidle,
				"max_aggro_sped": val_maxaggro,
				"scale": val_scale,
				"aggro": val_aggro,
				"initial_spawn_state": val_initspawnstate,
				"extra_count": val_extracount,
				"spawn_trigger": val_spawntrigger,
				"initial_respawn_timer": val_initrespawntimer,
			}
			extract["character_spawners"].append(spawner_data)
			#print(hex(read_header))
	return extract

# with open("./../../dk64.z64","rb") as fh:
# 	fh.seek(0x1171D24)
# 	zip_bytes = fh.read(0x112)
# 	# fh.seek(0x11714AC)
# 	# zip_bytes = fh.read(0x57)
# 	unzip_bytes = gzip.decompress(zip_bytes)
# 	#print(unzip_bytes)
# 	unpackCharacterSpawners(unzip_bytes)