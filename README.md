# MIDI System Exclusive (Sysex) Grammar

This grammar file maps the structure of the MIDI System Exclusive File Format. The MIDI Sysex File is a wrapper around manufacturer-specific data. Defining this structure facilitates parsing of the MIDI data it contains.

Grammars are stored as XML and support both Python and Lua scripting languages. They are powerful in that they can export to C structs as well as inherit structures from object oriented languages. Grammars are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows.

This grammar does not cover MIDI System Common or System Real Time Messages, and focuses on Non Real Time Universal System Exclusive Messages.


## Usage
1. Download and open the <a href="https://github.com/codemechanic/midi-sysex-grammar/blob/main/grammar/midi_sysex.grammar?raw=true">midi_sysex.grammar</a> in either Synalize It! or Hexinator.
2. Open a MIDI Sysex file. If you don't have one available you can download a sample Sysex file (like <a href="https://github.com/codemechanic/midi-sysex-grammar/blob/main/sysex/test.syx?raw=true">test_1.syx</a>) that is provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.

![Synalize It! screenshot](https://github.com/codemechanic/midi-sysex-grammar/blob/main/images/screenshot_1.png?raw=true)


## Manufacturer and synthesizer specific grammars
* [OSCar MIDI System Exclusive Grammar](https://github.com/codemechanic/oscar-sysex-grammar)


## MIDI System Exclusive links
* <a href="https://www.midi.org/specifications-old/item/table-4-universal-system-exclusive-messages">MIDI 1.0 Universal System Exclusive Messages documentation</a> published by the MIDI Association
* Somascape's <a href="http://www.somascape.org/midi/tech/spec.html">Guide to the MIDI Software Specification</a>, specifically the section on <a href="http://www.somascape.org/midi/tech/spec.html#sysexmsgs">System Exclusive Messages</a>
* <a href="http://web.archive.org/web/20070813201804/www.borg.com/~jglatt/">MIDI Technical Fanatic's Brainwashing Center</a>
