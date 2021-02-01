# MIDI System Exclusive (SysEx) Grammar

This grammar file maps the structure of the MIDI System Exclusive File Format. The MIDI SysEx File is a wrapper around manufacturer-specific data. Defining it facilitates parsing of the underlying MIDI data. Grammar files are written XML and can be loaded by the hex code and binary file analysis tools Synalize It! on [macOS](https://www.synalysis.net) and [Hexinator](https://hexinator.com) on Windows.

This grammar does not cover MIDI System Common or System Real Time Messages, and focuses on Non Real Time Universal System Exclusive Messages.

## Installation
1. Download and open the <a href="https://github.com/codemechanic/midi-sysex-grammar/blob/main/grammar/midi_sysex.grammar?raw=true" download>midi_sysex.grammar</a> in either Synalize It! or Hexinator.
2. Open a MIDI SysEx file.
3. Apply the MIDI Sysex grammar to the SysEx file.

## MIDI System Exclusive links
- <a href="https://www.midi.org/specifications-old/item/table-4-universal-system-exclusive-messages" target="_blank">MIDI 1.0 Universal System Exclusive Messages documentation</a> published by the MIDI Association
- Somascape's <a href="http://www.somascape.org/midi/tech/spec.html" target="_blank">Guide to the MIDI Software Specification</a>, specifically the section on <a href="http://www.somascape.org/midi/tech/spec.html#sysexmsgs" target="_blank">System Exclusive Messages</a>
- <a href="http://web.archive.org/web/20070813201804/www.borg.com/~jglatt/" target="_blank">MIDI Technical Fanatic's Brainwashing Center</a>


