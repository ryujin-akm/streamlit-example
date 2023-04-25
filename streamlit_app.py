import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr
from os import path
from pydub import AudioSegment
import subprocess
import streamlit as st
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import yolov5
import torch

import streamlit as st
import wave
from audiorecorder import audiorecorder

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())

    # To save audio to a file:
    with wave.open("transcript.wav", "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(44100)
        wav_file.writeframes(audio.tobytes())
        st.success("Audio saved as transcript.wav")


    # st.title("Audio Recorder")
    # audio = audiorecorder("Click to record", "Recording...")

    # if len(audio) > 0:
    #     # To play audio in frontend:
    #     st.audio(audio.tobytes())

    #     # To save audio to a file:
    #     wav_file = open("audio.mp3", "wb")
    #     wav_file.write(audio.tobytes())
    #     print("---------------------We are HEre--------------------")


    # sound = AudioSegment.from_mp3("audio.mp3")
    # sound.export("transcript.wav", format="wav")

    # input_file = "audio.mp3"
    # output_file = "transcript.wav"

    # subprocess.run([
    #     "ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar", "44100",
    #     output_file
    # ], timeout=5)

    # res = subprocess.call('ls -al', shell=True) 
    # st.write(res)
    # convert mp3 file to wav
    # sound = AudioSegment.from_mp3("audio.mp3")
    # sound.export("transcript.wav", format="wav")
    print("---------------------We are HEhjgfre--------------------")

    # transcribe audio file
    AUDIO_FILE = "transcript.wav"

    # use the audio file as the audio source
    r = sr.Recognizer()
    # r.energy_threshold = 200
    with sr.AudioFile(AUDIO_FILE) as source:
        print("I am Here")
    #     audio_data = source.readframes(source.SAMPLE_RATE * 5)  # read audio data for 5 seconds
        # pad audio data to ensure its length is a multiple of sample width
    #     sample_width = source.SAMPLE_WIDTH
    #     audio_data += bytes(math.ceil(len(audio_data) / sample_width) * sample_width - len(audio_data))
    #     r.adjust_for_ambient_noise(source, duration=1)
    #     audio = r.record(source)
    #     r.adjust_for_ambient_noise(source,duration=1)
        audio = r.record(source)  # read the entire audio file
    #     text = recognize.recognize_google(audio, language='en-IN', show_all=True)
    #     print("Transcription: " + str(r.recognize_google(audio, language = 'en-IN', show_all=True)))
    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    except :
        print("Sphinx could not understand audio")

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except:
        print("Could not request results from Google Speech Recognition service")





    model = yolov5.load('fcakyon/yolov5s-v7.0')

    st.set_option('deprecation.showfileUploaderEncoding', False)

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

        def detect(model, image_path):
            # Load image
            img = Image.open(image_path)

            # Perform inference
            detections = model(img)

            # Get predicted class names and bounding boxes
            class_names = detections.names
            boxes = detections.xyxy[0]

            print(f"\n Boxes: {boxes}\n")
            print(f"\n Detections: {detections}")

            print(f"\nClass names: {class_names}\n")

            ##First we need to find the objects that were detected
            classes_detected = [class_names[detections.pred[0][i][5].to(torch.int).item()] for i in range(len(boxes))]
            print(f"The classes detected are: {classes_detected}")

            # Filter out the detections for objects we are interested in
            interested_classes = ['car', 'person']
            # interested_indices = [i for i, class_name in enumerate(class_names.values()) if class_name in interested_classes]
            # class_names_found = [name for i, name in enumerate(class_names.values()) if name in interested_classes]
            # label_we_can_show = list(set(interested_classes).intersection(classes_detected))
            lable_indices_we_can_show = [i for i, x in enumerate(classes_detected) if x in interested_classes]
            print(f"\n label _we_ can _show: {lable_indices_we_can_show}\n")
            print
            filtered_boxes = boxes[interested_indices]


            #########################################
            fontsize = 1  # starting font size

            # portion of image width you want text width to be
            img_fraction = 0.50

            # font = ImageFont.truetype("arial.ttf", fontsize)
            # font = ImageFont.truetype(r'/content/arial.ttf', 7)
            ###################

            # font = ImageFont.truetype(r'/content/arial.ttf', 70)



            # draw.text((10, 20), text, fill = "red", font = font)
            Draw bounding boxes for filtered detections
            draw = ImageDraw.Draw(img)
            annotated_img = Image.fromarray(img)
            draw = ImageDraw.Draw(annotated_img)



            # for i, box in enumerate(boxes):
            for i in lable_indices_we_can_show:
              box = boxes[i]
              draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline='red', width=3)
              text = classes_detected[i]
              draw.text((box[0], box[1]), text, fill='red', font = ImageFont.truetype('arial.ttf', 25))
              # draw.text([(box[0], box[1])],class_names[interested_indices[i]], fill='red', font = font)

            # Show and save annotated image
            img.show()
            img.save('annotated_image.jpg')
        #     import streamlit as st
        #     from PIL import Image

            # Load the image from a file
            image = Image.open('annotated_image.jpg')

            # Display the image
            st.image(image, caption='Your Object Detection Image')


            return detections

        if uploaded_file is not None:
            # Use PIL to open the file from bytes
            image = Image.open(uploaded_file)

            # Display the image
            st.image(image, caption="Uploaded image", use_column_width=True)

            # Save the image to disk
            filename = f"{uploaded_file.name.split('.')[0]}.png"
            image.save(filename, format="PNG")
            st.success(f"Saved {filename} to disk!")
            detect(model, filename)
