# MIDI System Exclusive (SysEx) Grammar

This grammar file maps the structure of the MIDI System Exclusive File Format. The MIDI SysEx File is a wrapper around manufacturer-specific data. Defining it facilitates parsing of the underlying MIDI data. Grammar files are written XML and can be loaded by the hex code and binary file analysis tools Synalize It! on [macOS](https://www.synalysis.net) and [Hexinator](https://hexinator.com) on Windows.

Note that this grammar does not cover MIDI System Common or System Real Time Messages, and focuses on Non Real Time Universal System Exclusive Messages.

## Installation

1. Download and open the [midi_sysex.grammar](https://github.com/codemechanic/midi-sysex-grammar/blob/main/grammar/midi_sysex.grammar) in either Synalize It! or Hexinator.

2. Open a MIDI SysEx file.

3. Apply the MIDI Sysex grammar to the SysEx file.

## MIDI System Exclusive links

- The official [MIDI 1.0 Universal System Exclusive Messages documentation](https://www.midi.org/specifications-old/item/table-4-universal-system-exclusive-messages) published by the MIDI Association

- [Somascape's Guide to the MIDI Software Specification](http://www.somascape.org/midi/tech/spec.html), specifically the section on [System Exclusive Messages](http://www.somascape.org/midi/tech/spec.html#sysexmsgs)

- The [MIDI Technical Fanatic's Brainwashing Center](http://web.archive.org/web/20070813201804/www.borg.com/~jglatt/)


