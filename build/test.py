import gzip
from loading_zones.zoneextractor import *

with open("./../dk64.z64","rb") as fh:
	fh.seek(0x11811BC)
	a = fh.read(0x1E0)
	b = gzip.decompress(a)
	print(unpackLoadingZones(b))