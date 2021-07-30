def writeZones(vanilla_zones,edits,output_file):
	edit_keys = edits.keys()
	if "zones" in edit_keys:
		for x in edits["zones"]:
			zone_keys = x.keys()
			if x["action"] == "add":
				write_stream = [];
				for y in range(0x38):
					write_stream.append(0)
				if "x" in zone_keys:
					new_x = convert_int_to_arr(signed_to_unsigned(x["x"],2),2)
					for y in range(2):
						write_stream[y] = new_x[y]
				if "y" in zone_keys:
					new_y = convert_int_to_arr(signed_to_unsigned(x["y"],2),2)
					for y in range(2):
						write_stream[2 + y] = new_y[y]
				if "z" in zone_keys:
					new_z = convert_int_to_arr(signed_to_unsigned(x["z"],2),2)
					for y in range(2):
						write_stream[4 + y] = new_z[y]
				if "radius" in zone_keys:
					new_radius = convert_int_to_arr(x["radius"],2)
					for y in range(2):
						write_stream[6 + y] = new_radius[y]
				if "height" in zone_keys:
					new_height = convert_int_to_arr(x["height"],2)
					for y in range(2):
						write_stream[8 + y] = new_height[y]
				if "activation_type" in zone_keys:
					new_activation_type = x["activation_type"]
					write_stream[0xC] = new_activation_type[0]
				new_type = convert_int_to_arr(x["type"],2)
				for y in range(2):
					write_stream[0x10 + y] = new_type[y]
				if "map" in zone_keys:
					new_map = convert_int_to_arr(x["map"],2)
					for y in range(2):
						write_stream[0x12 + y] = new_map[y]
				if "exit" in zone_keys:
					new_exit = convert_int_to_arr(x["exit"],2)
					for y in range(2):
						write_stream[0x14 + y] = new_exit[y]
				if "transition_type" in zone_keys:
					new_transition_type = convert_int_to_arr(x["transition_type"],2)
					for y in range(2):
						write_stream[0x16 + y] = new_transition_type[y]
				if "is_tied_cs" in zone_keys:
					new_is_tied_cs = convert_int_to_arr(x["is_tied_cs"],2)
					for y in range(2):
						write_stream[0x1A + y] = new_is_tied_cs[y]
				if "cs" in zone_keys:
					new_cs = convert_int_to_arr(x["cs"],2)
					for y in range(2):
						write_stream[0x1C + y] = new_cs[y]
				if "shift_camera_to_kong" in zone_keys:
					new_shift_camera_to_kong = convert_int_to_arr(x["shift_camera_to_kong"],2)
					for y in range(2):
						write_stream[0x1E + y] = new_shift_camera_to_kong[y]
				zone_data = {
					"stream": write_stream
				}
				vanilla_zones["zones"].append(zone_data)
			if x["action"] == "edit":
				for y in vanilla_zones["zones"]:
					if y["vanilla_index"] == x["vanilla_index"]:
						write_stream = y["stream"]
						if "x" in zone_keys:
							new_x = convert_int_to_arr(signed_to_unsigned(x["x"],2),2)
							for y in range(2):
								write_stream[y] = new_x[y]
						if "y" in zone_keys:
							new_y = convert_int_to_arr(signed_to_unsigned(x["y"],2),2)
							for y in range(2):
								write_stream[2 + y] = new_y[y]
						if "z" in zone_keys:
							new_z = convert_int_to_arr(signed_to_unsigned(x["z"],2),2)
							for y in range(2):
								write_stream[4 + y] = new_z[y]
						if "radius" in zone_keys:
							new_radius = convert_int_to_arr(x["radius"],2)
							for y in range(2):
								write_stream[6 + y] = new_radius[y]
						if "height" in zone_keys:
							new_height = convert_int_to_arr(x["height"],2)
							for y in range(2):
								write_stream[8 + y] = new_height[y]
						if "activation_type" in zone_keys:
							new_activation_type = x["activation_type"]
							write_stream[0xC] = new_activation_type[0]
						if "type" in zone_keys:
							new_type = convert_int_to_arr(x["type"],2)
							for y in range(2):
								write_stream[0x10 + y] = new_type[y]
						if "map" in zone_keys:
							new_map = convert_int_to_arr(x["map"],2)
							for y in range(2):
								write_stream[0x12 + y] = new_map[y]
						if "exit" in zone_keys:
							new_exit = convert_int_to_arr(x["exit"],2)
							for y in range(2):
								write_stream[0x14 + y] = new_exit[y]
						if "transition_type" in zone_keys:
							new_transition_type = convert_int_to_arr(x["transition_type"],2)
							for y in range(2):
								write_stream[0x16 + y] = new_transition_type[y]
						if "is_tied_cs" in zone_keys:
							new_is_tied_cs = convert_int_to_arr(x["is_tied_cs"],2)
							for y in range(2):
								write_stream[0x1A + y] = new_is_tied_cs[y]
						if "cs" in zone_keys:
							new_cs = convert_int_to_arr(x["cs"],2)
							for y in range(2):
								write_stream[0x1C + y] = new_cs[y]
						if "shift_camera_to_kong" in zone_keys:
							new_shift_camera_to_kong = convert_int_to_arr(x["shift_camera_to_kong"],2)
							for y in range(2):
								write_stream[0x1E + y] = new_shift_camera_to_kong[y]
			if x["action"] == "delete":
				for y in vanilla_zones["zones"]:
					if y["vanilla_index"] == x["vanilla_index"]:
						vanilla_zones["zones"].remove(y)
	with open(output_file,"w+b") as fh:
		new_zone_count = convert_int_to_arr(len(vanilla_zones["zones"]),2)
		fh.seek(0)
		fh.write(bytearray(new_zone_count))
		write_location = 2;
		for x in vanilla_spawners["zones"]:
			fh.seek(write_location)
			fh.write(bytearray(x["stream"]))
			write_location += 0x38