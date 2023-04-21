from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file):
    # Initialize recognizer
    r = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        
    # Transcribe audio
    try:
        text = r.recognize_google(audio)
        st.write("Transcription: ", text)
    except sr.UnknownValueError:
        st.write("Unable to transcribe audio")
        
def main():
    st.title("Audio Recorder and Transcriber")
    
    # Display instructions
    st.write("Click the button to start recording.")
    
    # Create button to start recording
    if st.button("Record"):
        # Initialize recognizer
        r = sr.Recognizer()
        
        # Record audio
        with sr.Microphone() as source:
            st.write("Recording...")
            audio = r.listen(source)
            st.write("Recording finished.")
        
        # Save audio file
        audio_file = "recording.wav"
        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())
            
        # Transcribe audio
        transcribe_audio(audio_file)
        


    with st.echo(code_location='below'):
        total_points = st.slider("Number of points in the spiral", 1, 5000, 2000)
        num_turns = st.slider("Number of turns in the spiral", 1, 120, 9)

        Point = namedtuple('Point', 'x y')
        data = []

        points_per_turn = total_points / num_turns

        for curr_point_num in range(total_points):
            curr_turn, i = divmod(curr_point_num, points_per_turn)
            angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
            radius = curr_point_num / total_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            data.append(Point(x, y))

        st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
            .mark_circle(color='#0068c9', opacity=0.5)
            .encode(x='x:Q', y='y:Q'))
    
if __name__ == "__main__":
    main()
