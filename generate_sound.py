# generate_sound.py
# Run this ONCE to create the alert sound file

import numpy as np
import wave
import os
import struct

def create_beep(filename, frequency=1000, duration=0.5, volume=0.8):
    """Creates a beep .wav file"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # Create the beep wave
    t = np.linspace(0, duration, num_samples)
    wave_data = (np.sin(2 * np.pi * frequency * t) * volume * 32767).astype(np.int16)
    
    # Save as .wav file
    os.makedirs("sounds", exist_ok=True)
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)       # Mono
        f.setsampwidth(2)       # 2 bytes per sample
        f.setframerate(sample_rate)
        f.writeframes(wave_data.tobytes())
    
    print(f"✅ Sound created: {filename}")

# Generate the alert beep
create_beep("sounds/alert.wav", frequency=1000, duration=0.4)
print("Done! You can now run main.py")