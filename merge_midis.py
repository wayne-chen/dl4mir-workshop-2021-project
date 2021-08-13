import midi
import pathlib

# wavpath = Path("~/Downloads/DSD100subset/Sources/Dev/081 - Patrick Talbot - Set Me Free")
wavpath = pathlib.Path("/Users/wichen/Downloads/")

filenames = ['drums.midi', 'guitar.midi', 'prediction.midi']

pattern = midi.Pattern()

for f in filenames:
    filepath = wavpath / f
    current_pattern = midi.read_midifile(str(filepath))
    for track in current_pattern:
        pattern.append(track)

midi.write_midifile('mixed.mid', pattern)
