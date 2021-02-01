#!/usr/bin/env python

# The map_id generic script is intended to be run from within the MIDI Sysex Grammar file

currentGrammar = currentMapper.getCurrentGrammar()
multiByteID = currentGrammar.getStructureByName("Multi Byte ID")
singleByteID = currentGrammar.getStructureByName("Single Byte ID")

currentPos = currentMapper.getCurrentOffset()
byteView = currentMapper.getCurrentByteView()
byte = byteView.readByte(currentPos)

if (byte == 0x00):
	currentMapper.mapStructure(multiByteID)
	debugLog("Multi Byte ID mapped at offset " + str(currentPos))
else:
	currentMapper.mapStructure(singleByteID)
	debugLog("Single Byte ID mapped at offset " + str(currentPos))
