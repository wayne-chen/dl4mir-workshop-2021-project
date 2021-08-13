import mido
import pathlib

# wavpath = Path("~/Downloads/DSD100subset/Sources/Dev/081 - Patrick Talbot - Set Me Free")
wavpath = pathlib.Path("/Users/wichen/Downloads/")

filenames = ['drums.midi', 'guitar.midi', 'prediction.midi']

merged_midi = mido.MidiFile(type=1)

appended_filenames = []
[appended_filenames.append(mido.MidiFile(wavpath / f)) for f in filenames]
merged_midi.ticks_per_beat = appended_filenames[0].ticks_per_beat

for f in appended_filenames:
    merged_midi.tracks += f.tracks
merged_midi.save('merged.mid')
