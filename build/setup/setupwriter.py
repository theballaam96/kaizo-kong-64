from n64lib import *

def writeSetup(vanilla_setup,edits,output_file):
	for x in vanilla_setup["actor_spawners"]:
		x["stream"] = list(x["stream"])
	for x in vanilla_setup["modeltwo"]:
		x["stream"] = list(x["stream"])
	for x in vanilla_setup["mystery"]:
		x["stream"] = list(x["stream"])
	edit_keys = edits.keys()
	if "actors" in edit_keys:
		for x in edits["actors"]:
			actor_keys = x.keys();
			if x["action"] == "add":
				new_actor = [];
				for y in range(0x38):
					new_actor.append(0)
				new_id = convert_int_to_arr(x["id"],2)
				for y in range(2): 
					new_actor[0x34 + y] = new_id[y]
				new_type = convert_int_to_arr(x["type"]-16,2)
				for y in range(2):
					new_actor[0x32 + y] = new_type[y]
				if "x" in actor_keys:
					actor_x = int(float_to_hex(x["x"]),16)
					write_bytes = convert_int_to_arr(actor_x,4)
					for z in range(4):
						new_actor[z] = write_bytes[z]
				if "y" in actor_keys:
					actor_y = int(float_to_hex(x["y"]),16)
					write_bytes = convert_int_to_arr(actor_y,4)
					for z in range(4):
						new_actor[4 + z] = write_bytes[z]
				if "z" in actor_keys:
					actor_z = int(float_to_hex(x["z"]),16)
					write_bytes = convert_int_to_arr(actor_z,4)
					for z in range(4):
						new_actor[8 + z] = write_bytes[z]
				if "rot_x" in actor_keys:
					actor_rx = int(float_to_hex(x["rot_x"]),16)
					write_bytes = convert_int_to_arr(actor_rx,4)
					for z in range(4):
						new_actor[0x30 + z] = write_bytes[z]
				if "scale" in actor_keys:
					actor_scale = int(float_to_hex(x["scale"]),16)
					write_bytes = convert_int_to_arr(actor_scale,4)
					for z in range(4):
						new_actor[0xC + z] = write_bytes[z]
				data = {
					"stream": new_actor,
					"id": new_id,
					"type": new_type,
				}
				vanilla_setup["actor_spawners"].append(data)
			elif x["action"] == "edit":
				for y in vanilla_setup["actor_spawners"]:
					if y["id"] == x["id"]:
						write_stream = y["stream"]
						# Edits
						if "x" in actor_keys:
							actor_x = int(float_to_hex(x["x"]),16)
							write_bytes = convert_int_to_arr(actor_x,4)
							for z in range(4):
								write_stream[z] = write_bytes[z]
						if "y" in actor_keys:
							actor_y = int(float_to_hex(x["y"]),16)
							write_bytes = convert_int_to_arr(actor_y,4)
							for z in range(4):
								write_stream[4 + z] = write_bytes[z]
						if "z" in actor_keys:
							actor_z = int(float_to_hex(x["z"]),16)
							write_bytes = convert_int_to_arr(actor_z,4)
							for z in range(4):
								write_stream[8 + z] = write_bytes[z]
						y["stream"] = write_stream

			elif x["action"] == "delete":
				for y in vanilla_setup["actor_spawners"]:
					if y["id"] == x["id"]:
						vanilla_setup["actor_spawners"].remove(y)

	if "modeltwo" in edit_keys:
		for x in edits["modeltwo"]:
			modeltwo_keys = x.keys()
			if x["action"] == "add":
				new_obj = [];
				for y in range(0x30):
					new_obj.append(0)
				new_id = convert_int_to_arr(x["id"],2)
				for y in range(2): 
					new_obj[0x2A + y] = new_id[y]
				new_type = convert_int_to_arr(x["type"],2)
				for y in range(2):
					new_obj[0x28 + y] = new_type[y]
				if "x" in modeltwo_keys:
					obj_x = int(float_to_hex(x["x"]),16)
					write_bytes = convert_int_to_arr(obj_x,4)
					for y in range(4):
						new_obj[y] = write_bytes[y]
				if "y" in modeltwo_keys:
					obj_y = int(float_to_hex(x["y"]),16)
					write_bytes = convert_int_to_arr(obj_y,4)
					for y in range(4):
						new_obj[y + 4] = write_bytes[y]
				if "z" in modeltwo_keys:
					obj_z = int(float_to_hex(x["z"]),16)
					write_bytes = convert_int_to_arr(obj_z,4)
					for y in range(4):
						new_obj[y + 8] = write_bytes[y]
				if "scale" in modeltwo_keys:
					obj_scale = int(float_to_hex(x["scale"]),16)
					write_bytes = convert_int_to_arr(obj_scale,4)
					for y in range(4):
						new_obj[y + 0xC] = write_bytes[y]
				if "rot_x" in modeltwo_keys:
					obj_rx = int(float_to_hex(x["rot_x"]),16)
					write_bytes = convert_int_to_arr(obj_rx,4)
					for y in range(4):
						new_obj[y + 0x18] = write_bytes[y]
				if "rot_y" in modeltwo_keys:
					obj_ry = int(float_to_hex(x["rot_y"]),16)
					write_bytes = convert_int_to_arr(obj_ry,4)
					for y in range(4):
						new_obj[y + 0x1C] = write_bytes[y]
				if "rot_z" in modeltwo_keys:
					obj_rz = int(float_to_hex(x["rot_z"]),16)
					write_bytes = convert_int_to_arr(obj_rz,4)
					for y in range(4):
						new_obj[y + 0x20] = write_bytes[y]
				data = {
					"stream": new_obj,
					"id": new_id,
					"type": new_type,
				}
				vanilla_setup["modeltwo"].append(data)
			elif x["action"] == "edit":
				for z in vanilla_setup["modeltwo"]:
					if x["id"] == z["id"]:
						write_stream = z["stream"]
						if "x" in modeltwo_keys:
							obj_x = int(float_to_hex(x["x"]),16)
							write_bytes = convert_int_to_arr(obj_x,4)
							for y in range(4):
								write_stream[y] = write_bytes[y]
						if "y" in modeltwo_keys:
							obj_y = int(float_to_hex(x["y"]),16)
							write_bytes = convert_int_to_arr(obj_y,4)
							for y in range(4):
								write_stream[y + 4] = write_bytes[y]
						if "z" in modeltwo_keys:
							obj_z = int(float_to_hex(x["z"]),16)
							write_bytes = convert_int_to_arr(obj_z,4)
							for y in range(4):
								write_stream[y + 8] = write_bytes[y]
						if "scale" in modeltwo_keys:
							obj_scale = int(float_to_hex(x["scale"]),16)
							write_bytes = convert_int_to_arr(obj_scale,4)
							for y in range(4):
								write_stream[y + 0xC] = write_bytes[y]
						if "rot_x" in modeltwo_keys:
							obj_rx = int(float_to_hex(x["rot_x"]),16)
							write_bytes = convert_int_to_arr(obj_rx,4)
							for y in range(4):
								write_stream[y + 0x18] = write_bytes[y]
						if "rot_y" in modeltwo_keys:
							obj_ry = int(float_to_hex(x["rot_y"]),16)
							write_bytes = convert_int_to_arr(obj_ry,4)
							for y in range(4):
								write_stream[y + 0x1C] = write_bytes[y]
						if "rot_z" in modeltwo_keys:
							obj_rz = int(float_to_hex(x["rot_z"]),16)
							write_bytes = convert_int_to_arr(obj_rz,4)
							for y in range(4):
								write_stream[y + 0x20] = write_bytes[y]
						z["stream"] = write_stream
			elif x["action"] == "delete":
				for y in vanilla_setup["modeltwo"]:
					if y["id"] == x["id"]:
						vanilla_setup["modeltwo"].remove(y)

	with open(output_file,"w+b") as fh:
		new_m2_count = convert_int_to_arr(len(vanilla_setup["modeltwo"]),4)
		fh.seek(0)
		fh.write(bytearray(new_m2_count))
		write_location = 4;
		for x in vanilla_setup["modeltwo"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += 0x30
		new_my_count = convert_int_to_arr(len(vanilla_setup["mystery"]),4)
		fh.seek(write_location)
		fh.write(bytearray(new_my_count))
		write_location += 4
		for x in vanilla_setup["mystery"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += 0x24
		new_ac_count = convert_int_to_arr(len(vanilla_setup["actor_spawners"]),4)
		fh.seek(write_location)
		fh.write(bytearray(new_ac_count))
		write_location += 4
		for x in vanilla_setup["actor_spawners"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += 0x38

		