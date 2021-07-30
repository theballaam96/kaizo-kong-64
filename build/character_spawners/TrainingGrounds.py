from spawner_modules import *
import os

CopyBin = "TrainingGrounds_Spawners_Copy.bin"

if os.path.exists(CopyBin):
	os.remove(CopyBin)

edits = {
	"spawners": [
		{
			"action": "add",
			"type": 0x3D,
			"x": 863,
			"y": 70,
			"z": 1619,
			"spawn_trigger": 0,
			"init_spawn_state": 2,
			"scale": 0x30,
			"aggro": 1,
			"max_idle_speed":35,
         	"max_aggro_sped":60,
		},
		{
			"action": "add",
			"type": 0x3E,
			"x": 790,
			"y": 70,
			"z": 1648,
			"spawn_trigger": 0,
			"init_spawn_state": 2,
			"scale": 0x30,
			"aggro": 1,
			"max_idle_speed":35,
         	"max_aggro_sped":60,
		},
		{
			"action": "add",
			"type": 0x3F,
			"x": 804,
			"y": 68,
			"z": 1709,
			"spawn_trigger": 0,
			"init_spawn_state": 2,
			"scale": 0x30,
			"aggro": 1,
			"max_idle_speed":35,
         	"max_aggro_sped":60,
		},
		{
			"action": "add",
			"type": 0x40,
			"x": 875,
			"y": 66,
			"z": 1690,
			"spawn_trigger": 0,
			"init_spawn_state": 2,
			"scale": 0x30,
			"aggro": 1,
			"max_idle_speed":35,
         	"max_aggro_sped":60,
		},
		{
			"action": "add",
			"type": 0x41,
			"x": 858,
			"y": 66,
			"z": 1747,
			"spawn_trigger": 0,
			"init_spawn_state": 2,
			"scale": 0x30,
			"aggro": 1,
			"max_idle_speed":35,
         	"max_aggro_sped":60,
		},
	],
}

with open("TrainingGrounds_Spawners.bin","rb") as fh:
	old_spawners = unpackCharacterSpawners(fh.read())
	writeSpawners(old_spawners,edits,CopyBin)