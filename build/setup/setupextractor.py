def arrToInt(arr):
	total = 0;
	for x in arr:
		total = (total * 256) + x;
	return total

def extractSetup(byte_string):
	model2_arr = []
	mystery_arr = []
	actor_arr = []
	modeltwo_count = arrToInt(list(byte_string[:4]))
	read_location = 4
	for x in range(modeltwo_count):
		byte_stream = byte_string[read_location:read_location + 0x30]
		_id = arrToInt(list(byte_string[read_location + 0x2A:read_location + 0x2C]))
		_type = arrToInt(list(byte_string[read_location + 0x28:read_location + 0x2A]))
		data = {
			"stream": byte_stream,
			"id": _id,
			"type": _type,
		}
		model2_arr.append(data)
		read_location += 0x30
	mystery_count = arrToInt(list(byte_string[read_location:read_location+4]))
	read_location += 4;
	for x in range(mystery_count):
		byte_stream = byte_string[read_location:read_location + 0x24]
		data = {
			"stream": byte_stream
		}
		mystery_arr.append(data)
		read_location += 0x24
	actor_count = arrToInt(list(byte_string[read_location:read_location+4]))
	read_location += 4;	
	for x in range(actor_count):
		byte_stream = byte_string[read_location:read_location + 0x38]
		_id = arrToInt(list(byte_string[read_location + 0x34:read_location + 0x36]))
		_type = arrToInt(list(byte_string[read_location + 0x32:read_location + 0x34])) + 16
		data = {
			"stream": byte_stream,
			"id": _id,
			"type": _type,
		}
		actor_arr.append(data)
		read_location += 0x38
	data = {
		"modeltwo": model2_arr,
		"actor_spawners": actor_arr,
		"mystery": mystery_arr
	}
	return data