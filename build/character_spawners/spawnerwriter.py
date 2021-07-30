from n64lib import *

def writeSpawners(vanilla_spawners,edits,output_file):
	edit_keys = edits.keys()
	if "spawners" in edit_keys:
		for x in edits["spawners"]:
			spawner_keys = x.keys()
			if x["action"] == "add":
				write_stream = [];
				for y in range(0x16):
					write_stream.append(0)
				new_type = 0;
				if "type" in spawner_keys:
					new_type = x["type"] % 256
					write_stream[0] = new_type
				if "y_rot" in spawner_keys:
					new_ry = convert_int_to_arr(x["y_rot"],2)
					for y in range(2):
						write_stream[2 + y] = new_ry[y]
				if "x" in spawner_keys:
					new_x = convert_int_to_arr(signed_to_unsigned(x["x"],2),2)
					for y in range(2):
						write_stream[4 + y] = new_x[y]
				if "y" in spawner_keys:
					new_y = convert_int_to_arr(signed_to_unsigned(x["y"],2),2)
					for y in range(2):
						write_stream[6 + y] = new_y[y]
				if "z" in spawner_keys:
					new_z = convert_int_to_arr(signed_to_unsigned(x["z"],2),2)
					for y in range(2):
						write_stream[8 + y] = new_z[y]
				if "cs_model" in spawner_keys:
					if new_type == 0x50:
						new_type = x["cs_model"] % 256
						write_stream[0xA] = new_type
				if "max_idle_speed" in spawner_keys:
					new_mis = x["max_idle_speed"] % 256
					write_stream[0xC] = new_mis
				if "max_aggro_speed" in spawner_keys:
					new_mas = x["max_aggro_speed"] % 256
					write_stream[0xD] = new_mas
				if "scale" in spawner_keys:
					new_scale = x["scale"] % 256
					write_stream[0xF] = new_scale
				if "aggro" in spawner_keys:
					new_aggro = x["aggro"] % 256
					write_stream[0x10] = new_aggro
				if "init_spawn_state" in spawner_keys:
					new_iss = x["init_spawn_state"] % 256
					write_stream[0x12] = new_iss
				if "spawn_trigger" in spawner_keys:
					new_spawn_trigger = x["spawn_trigger"] % 256
					write_stream[0x13] = new_spawn_trigger
				if "respawn_timer" in spawner_keys:
					new_respawn_timer = convert_int_to_arr(x["respawn_timer"],2)
					for y in range(2):
						write_stream[0x14 + y] = new_respawn_timer[y]
				spawner_data = {
					"stream": write_stream,
					"type": new_type
				}
				# print([hex(ele) for ele in spawner_data["stream"]])
				vanilla_spawners["character_spawners"].append(spawner_data)
			if x["action"] == "edit":
				for y in vanilla_spawners["character_spawners"]:
					if x["vanilla_index"] == y["vanilla_index"]:
						write_stream = y["stream"]
						new_type = 0;
					if "type" in spawner_keys:
						new_type = x["type"] % 256
						write_stream[0] = new_type
					if "y_rot" in spawner_keys:
						new_ry = convert_int_to_arr(x["y_rot"],2)
						for y in range(2):
							write_stream[2 + y] = new_ry[y]
					if "x" in spawner_keys:
						new_x = convert_int_to_arr(signed_to_unsigned(x["x"],2),2)
						for y in range(2):
							write_stream[4 + y] = new_x[y]
					if "y" in spawner_keys:
						new_y = convert_int_to_arr(signed_to_unsigned(x["y"],2),2)
						for y in range(2):
							write_stream[6 + y] = new_y[y]
					if "z" in spawner_keys:
						new_z = convert_int_to_arr(signed_to_unsigned(x["z"],2),2)
						for y in range(2):
							write_stream[8 + y] = new_z[y]
					if "max_idle_speed" in spawner_keys:
						new_mis = x["max_idle_speed"] % 256
						write_stream[0xC] = new_mis
					if "max_aggro_speed" in spawner_keys:
						new_mas = x["max_aggro_speed"] % 256
						write_stream[0xD] = new_mas
					if "scale" in spawner_keys:
						new_scale = x["scale"] % 256
						write_stream[0xF] = new_scale
					if "aggro" in spawner_keys:
						new_aggro = x["aggro"] % 256
						write_stream[0x10] = new_aggro
					if "init_spawn_state" in spawner_keys:
						new_iss = x["init_spawn_state"] % 256
						write_stream[0x12] = new_iss
					if "spawn_trigger" in spawner_keys:
						new_spawn_trigger = x["spawn_trigger"] % 256
						write_stream[0x13] = new_spawn_trigger
					if "respawn_timer" in spawner_keys:
						new_respawn_timer = convert_int_to_arr(x["respawn_timer"],2)
						for y in range(2):
							write_stream[0x14 + y] = new_respawn_timer[y]
					y["stream"] = write_stream
			if x["action"] == "delete":
				for y in vanilla_spawners["character_spawners"]:
					if x["vanilla_index"] == y["vanilla_index"]:
						vanilla_spawners["character_spawners"].remove(y)

	with open(output_file,"w+b") as fh:
		# print(vanilla_spawners)
		new_unknown_array_count = convert_int_to_arr(len(vanilla_spawners["unknown_array"]),2)
		fh.seek(0)
		fh.write(bytearray(new_unknown_array_count))
		write_location = 2;
		for x in vanilla_spawners["unknown_array"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += len(x["stream"])
		new_spawner_count = convert_int_to_arr(len(vanilla_spawners["character_spawners"]),2)
		fh.seek(write_location)
		fh.write(bytearray(new_spawner_count))
		write_location += 2
		for x in vanilla_spawners["character_spawners"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += len(x["stream"])