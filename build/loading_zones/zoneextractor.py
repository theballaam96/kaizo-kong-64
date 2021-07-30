from n64lib import *

def unpackLoadingZones(data):
	zones = []
	zone_count = arrToInt(list(data[:2]))
	read_header = 2
	print(zone_count)
	for x in range(zone_count):
		stream = list(data[read_header:read_header + 0x3A])
		vanilla_index = x
		x_pos = unsigned_to_signed(arrToInt(list(data[read_header:read_header + 2])),2)
		y_pos = unsigned_to_signed(arrToInt(list(data[read_header + 2:read_header + 4])),2)
		z_pos = unsigned_to_signed(arrToInt(list(data[read_header + 4:read_header + 6])),2)
		radius = arrToInt(list(data[read_header + 6:read_header + 8]))
		height = unsigned_to_signed(arrToInt(list(data[read_header + 8:read_header + 0xA])),2)
		activation_type = arrToInt(list(data[read_header + 0xC:read_header + 0xD]))
		zone_type = arrToInt(list(data[read_header + 0x10:read_header + 0x12]))
		_map = arrToInt(list(data[read_header + 0x12:read_header + 0x14]))
		_exit = arrToInt(list(data[read_header + 0x14:read_header + 0x16]))
		transition = arrToInt(list(data[read_header + 0x16:read_header + 0x18]))
		is_tied = arrToInt(list(data[read_header + 0x1A:read_header + 0x1C]))
		cutscene = arrToInt(list(data[read_header + 0x1C:read_header + 0x1E]))
		shift_camera_to_kong = arrToInt(list(data[read_header + 0x1E:read_header + 0x20]))
		zone_data = {
			"stream": stream,
			"vanilla_index": vanilla_index,
			"x": x_pos,
			"y": y_pos,
			"z": z_pos,
			"radius": radius,
			"height": height,
			"activation_type": activation_type,
			"type": zone_type,
			"map": _map,
			"exit": _exit,
			"transition_type": transition,
			"is_tied_cs": is_tied,
			"cs": cutscene,
			"shift_camera_to_kong": shift_camera_to_kong,
		}
		zones.append(zone_data)
		read_header += 0x38
	zone_data = {
		"zones": zones
	}
	return zone_data