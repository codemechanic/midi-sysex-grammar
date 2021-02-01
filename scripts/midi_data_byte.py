#!/usr/bin/env python

# The midi_data_byte custom data script is intended to be run from within the MIDI Sysex Grammar file

# MIDI Data Byte
#
# All bytes between the System Exclusive status byte and EOX (or the next status byte) must have zero in the top bit.
# MIDI Data Bytes range in value from 0 to 127.


def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	"""parseByteRange method"""

	processedBytes = 0
	firstBit = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (firstBit == 0):

		result = byteView.readUnsignedIntBits(bitPos+1, 7, ENDIAN_BIG)

		# return value to results
		value = Value()
		value.setString(str(result))
		results.addElement(element, 1, 0, value)
		processedBytes = 1
	
	return processedBytes


def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	"""fillByteRange method"""

	# get number edited by user
	number = value.getUnsigned()

	# verbose flag
	verbose = False

	# verbose info
	if verbose:
		debugLog("Input value: " + str(number))
		debugLog("byteArray length: " + str(byteArray.getLength()))
		debugLog("bitPos: " + str(bitPos))
		debugLog("bitLength: " + str(bitLength))

		# number in binary
		numBinary = '{0:08b}'.format(number)
		debugLog("Input value binary: " + str(numBinary))

		# number in hex
		numHex = str.format('0x{:02X}', int(str(number), 16))
		debugLog("Input value hex: " + str(numHex))

	if (number < 128):
		byteArray.deleteRange(bitPos/8, bitLength/16)
		byteArray.writeUnsignedIntBits(number, bitPos, 8, ENDIAN_BIG)
	else:
		debugLog("Input value out of range (0-127). Value not updated.")
