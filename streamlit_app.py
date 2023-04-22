# import streamlit as st
# from audiorecorder import audiorecorder

# st.title("Audio Recorder")
# audio = audiorecorder("Click to record", "Recording...")

# if len(audio) > 0:
#     # To play audio in frontend:
#     st.audio(audio.tobytes())
    
#     # To save audio to a file:
#     wav_file = open("audio.mp3", "wb")
#     wav_file.write(audio.tobytes())

import streamlit as st
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Use PIL to open the file from bytes
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption="Uploaded image", use_column_width=True)

    # Save the image to disk
    filename = f"{uploaded_file.name.split('.')[0]}.png"
    image.save(filename, format="PNG")
    st.success(f"Saved {filename} to disk!")
