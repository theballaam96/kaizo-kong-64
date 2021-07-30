import subprocess
import os
import shutil
from pathlib import Path

newASMName = "master-copy.asm"
oldASMName = "master.asm"
ROMName = "kaizo-kong-64.z64"
pathExt = "../src/"
os.chdir("../src/")
if os.path.exists(newASMName):
    os.remove(newASMName)
shutil.copyfile(oldASMName, newASMName);
os.chdir("../Build/")

new_dir = "./../src/"
edited_lines = [];

with open("./../src/master-copy.asm", "r") as fh:
    asmlines = fh.readlines()
    for l in asmlines:
        if ".incasm" in l:
            split_line = l.split("/")
            src_found = False;
            new_line = ".incasm \"" + new_dir
            for s in split_line:
                if src_found:
                    new_line += s.replace("\n","").replace("\"","") + "/"
                if s == "src":
                    src_found = True;
            new_line = new_line[:-1] + "\"\n"
            edited_lines.append(new_line)
        else:
            edited_lines.append(l)

if os.path.exists("../src/master-copy.asm"):
    os.remove("../src/master-copy.asm")
with open("../src/master-copy.asm", "a") as fh:
    for e in edited_lines:
        fh.write(e)

result = subprocess.check_output(["lua", "-l", "loadASM", "-e", "loadASMPatch('../src/master-copy.asm')"])

def processBytePatch(addr, val):
    val = bytes([val])
    if addr >= 0x72C and addr < (0x72C + 8):
        diff = addr - 0x72C
        with open(ROMName, "r+b") as fh:
            fh.seek(0x132C + diff)
            fh.write(val)
        # print("Boot hook code")
    elif addr >= 0xA30 and addr < (0xA30 + 1696):
        diff = addr - 0xA30
        with open(ROMName, "r+b") as fh:
            fh.seek(0x1630 + diff)
            fh.write(val)
        # print("Expansion Pak Draw Code")
    elif addr >= 0xDE88 and addr < (0xDE88 + 3920):
        diff = addr - 0xDE88
        with open(ROMName, "r+b") as fh:
            fh.seek(0xEA88 + diff)
            fh.write(val)
        # print("Expansion Pak Picture")
    elif addr >= 0x5DAE00 and addr < (0x5DAE00 + 0x20000):
        diff = addr - 0x5DAE00
        with open(ROMName, "r+b") as fh:
            fh.seek(0x2000000 + diff)
            fh.write(val)
        # print("Heap Shrink Space")
    #else:
        #print("Attempt to write to address " + str(addr) + " with value " + str(val) + " failed")

foundHookBytes = [0];
def processHookInfo(addr,val):
    val = bytes([val])

def arrToInt(arr):
    total = 0;
    for x in arr:
        total = total * 256
        total = total + int.from_bytes(x,"big")
    return total

f = open("codeOutput.txt", "r")

highest_heapspace = 0;

for x in f:
    line = x
    segs = line.split(":")
    if int(segs[0]) < 0x5FAE00 and int(segs[0]) > highest_heapspace:
        highest_heapspace = int(segs[0])
    #processHookInfo(int(segs[0]),int(segs[1]))

if highest_heapspace > 0:
    new_end = (highest_heapspace - 0x5DAE00) + 0x2000000 + 1;
else:
    new_end = 0x2000001
if os.path.exists("../src/EndLoadingSpot.asm"):
  os.remove("../src/EndLoadingSpot.asm")
with open("../src/EndLoadingSpot.asm", "a") as fh:
    fh.write("LI    a1, " + str(hex(new_end)))

result = subprocess.check_output(["lua", "-l", "loadASM", "-e", "loadASMPatch('../src/master-copy.asm')"])
with open("codeOutput.txt","r") as f:
    for x in f:
        line = x
        segs = line.split(":")
        processBytePatch(int(segs[0]), int(segs[1]))
if os.path.exists("codeOutput.txt"):
    os.remove("codeOutput.txt")
if os.path.exists("../src/master-copy.asm"):
    os.remove("../src/master-copy.asm")