
import win32com.client as wincl

# Initialize the SAPI.SpVoice object
spk = wincl.Dispatch("SAPI.SpVoice")

# Get the list of available voices
vcs = spk.GetVoices()

# Print the available voices
for i in range(vcs.Count):
    print(f"Voice {i}: {vcs.Item(i).GetAttribute('Name')}")

# Select a voice by index (change the index to choose a different voice)
selected_voice_index = 0  # Change this to the desired voice index

# Ensure the index is within the valid range
if 0 <= selected_voice_index < vcs.Count:
    spk.Voice = vcs.Item(selected_voice_index)
else:
    print("Selected voice index is out of range")

# Define the list of people names
names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

# Loop through each name in the list
for name in names:
    # Construct the shoutout message
    shoutout_message = f"Shoutout to {name}!"
    # Use the text-to-speech engine to speak the message
    spk.Speak(shoutout_message)

# Speak a final message
spk.Speak("Thank You")
