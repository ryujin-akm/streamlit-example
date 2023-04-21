import streamlit as st
import sounddevice as sd
import soundfile as sf

def main():
    st.title("Audio Recorder and Transcriber")
    
    # Display instructions
    st.write("Click the button to start recording.")
    
    # Create button to start recording
    if st.button("Record"):
        # Record audio
        duration = 5  # seconds
        sample_rate = 44100  # Hz
        channels = 2  # stereo
        audio_file = "recording.wav"
        myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()
        sf.write(audio_file, myrecording, sample_rate)
        st.write("Recording finished.")
        st.audio(audio_file, format='audio/wav')
    
if __name__ == "__main__":
    main()

