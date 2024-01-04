import os
from mido import MidiFile

def get_midi_files(directory_path):
    midi_files =[]

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is a MIDI file
        if filename.lower().endswith('.mid'):
            midi_files.append(file_path)

    return midi_files

def get_attribute_vector(file_path, attribute):
    mid = MidiFile(file_path)
    vector = []
    for i, track in enumerate(mid.tracks):
        for msg in track:
            if hasattr(msg, attribute):
                vector.append(msg.note)

    return vector

# Function to load and explore a MIDI file
def explore_midi_file(file_path):
    # Load the MIDI file
    midi_file = MidiFile(file_path)

    # Display basic information
    print(f"MIDI File: {file_path}")
    print(f"Ticks per Beat: {midi_file.ticks_per_beat}")

    # Display information about each track
    for i, track in enumerate(midi_file.tracks):
        print(f"\nTrack {i + 1}:")
        print(f"  Name: {track.name}")
        print(f"  Messages Count: {len(track)}")
        print(f"  Messages:")
        for msg in track:
            print(f"    {msg}")

