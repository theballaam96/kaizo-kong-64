from setup_modules import *
import os

CopyBin = "TrainingGrounds_Copy.bin"

if os.path.exists(CopyBin):
	os.remove(CopyBin)

edits = {
	"actors": [
		{
			"id": 0x5,
			"action": "edit",
			"x": 2483.292,
			"y": 354.9,
			"z": 1030.948,
		},
		{
			"id": 0x3,
			"action": "edit",
			"x": 653.765,
			"y": 113.783,
			"z": 526.157,
		},
		{
			"id": 0x6,
			"action": "edit",
			"x": 1375.67,
			"y": 194.667,
			"z": 1278.047,
		},
		{
			"id": 0x4,
			"action": "edit",
			"x": 1485.812,
			"y": 93.273,
			"z": 1644.573,
		},
		{
			"id": 0x0,
			"action": "edit",
			"x": 1603.583,
			"y": 300.794,
			"z": 1114.266,
		},
		{
			"id": 0x1,
			"action": "edit",
			"x": 1791.365,
			"y": 280.044,
			"z": 1137.398,
		},
		{
			"id": 0x9,
			"action": "edit",
			"x": 2504.635,
			"y": 211,
			"z": 923.765,
		},
		{
			"id": 0x100,
			"action": "add",
			"type": 133,
			"x": 1485.812,
			"y": 84.123,
			"z": 1644.573,
			"scale": 7,
		},
		{
			"id": 0x101,
			"action": "add",
			"type": 21,
			"x": 919.77,
			"y": 67.052,
			"z": 1773.638,
			"scale": 2
		}
	],
	"modeltwo": [
		{
			"id": 0x7,
			"action": "delete",
		},
		{
			"id": 0x1,
			"action": "delete",
		},
		{
			"id": 0x11,
			"action": "delete",
		},
		{
			"id": 0x10,
			"action": "delete",
		},
		{
			"id": 0xF,
			"action": "delete",
		},
		{
			"id": 0xD,
			"action": "delete",
		},
		{
			"id": 0xC,
			"action": "delete",
		},
		{
			"id": 0xB,
			"action": "delete",
		},
		{
			"id": 0xA,
			"action": "delete",
		},
		{
			"id": 0x9,
			"action": "delete",
		},
		{
			"id": 0x8,
			"action": "delete",
		},
		{
			"id": 0x39,
			"action": "edit",
			"x": 600,
			"y": 155,
			"z": 1873.238,
			"scale": 0.5,
		},
		{
			"id": 0x100,
			"action": "add",
			"type": 0x188,
			"scale": 1,
			"x": 2497.233,
			"y": 191,
			"z": 1036.381,
		},
		{
			"id": 0x101,
			"action": "add",
			"type": 0x188,
			"scale": 0.8,
			"x": 2497.233,
			"y": 242,
			"z": 1000.385
		}
	]
}

with open("TrainingGrounds.bin","rb") as fh:
	old_setup = extractSetup(fh.read())
	writeSetup(old_setup,edits,CopyBin)