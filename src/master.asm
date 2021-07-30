.incasm "./../../Development/kaizo-kong-64/src/memory/functions.asm"

.org 0x805FC164
J  	 Start

.org 0x8000DE88
Start:
	JAL 	0x805FC2B0
	NOP

	Finish:
		J 		0x805FC15C
		NOP

.org 0x80000A30
LoadInAdditionalFile:
    JAL     @DMAFileTransfer
    ADDIU   a0, a0, 0x13F0
    .incasm "./../../Development/kaizo-kong-64/src/EndLoadingSpot.asm"
    LI      a2, 0x805DAE00
    JAL     @DMAFileTransfer       
    LUI     a0, 0x200 // 0x2000000
    J       0x80000734
    NOP