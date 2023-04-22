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

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())


    input_file = "audio.mp3"
    output_file = "transcript.wav"

# subprocess.run([
#     "ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar", "44100",
#     output_file
# ])

# convert mp3 file to wav
sound = AudioSegment.from_mp3("audio.mp3")
sound.export("transcript.wav", format="wav")
print("---------------------We are HEre--------------------")
# transcribe audio file
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

    print("Transcription: " + r.recognize_google(audio))



model = yolov5.load('fcakyon/yolov5s-v7.0')

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     def detect(model, image_path):
#         # Load image
#         img = Image.open(image_path)

#         # Perform inference
#         detections = model(img)

#         # Get predicted class names and bounding boxes
#         class_names = detections.names
#         boxes = detections.xyxy[0]

#         print(f"\n Boxes: {boxes}\n")
#         print(f"\n Detections: {detections}")

#         print(f"\nClass names: {class_names}\n")

#         ##First we need to find the objects that were detected
#         classes_detected = [class_names[detections.pred[0][i][5].to(torch.int).item()] for i in range(len(boxes))]
#         print(f"The classes detected are: {classes_detected}")

#         # Filter out the detections for objects we are interested in
#         interested_classes = ['car', 'person']
#         # interested_indices = [i for i, class_name in enumerate(class_names.values()) if class_name in interested_classes]
#         # class_names_found = [name for i, name in enumerate(class_names.values()) if name in interested_classes]
#         # label_we_can_show = list(set(interested_classes).intersection(classes_detected))
#         lable_indices_we_can_show = [i for i, x in enumerate(classes_detected) if x in interested_classes]
#         print(f"\n label _we_ can _show: {lable_indices_we_can_show}\n")
        # print
        # filtered_boxes = boxes[interested_indices]


        # #########################################
        # fontsize = 1  # starting font size

        # # portion of image width you want text width to be
        # img_fraction = 0.50

        # # font = ImageFont.truetype("arial.ttf", fontsize)
        # # font = ImageFont.truetype(r'/content/arial.ttf', 7)
        # ###################

        # # font = ImageFont.truetype(r'/content/arial.ttf', 70)



        # # draw.text((10, 20), text, fill = "red", font = font)
        # Draw bounding boxes for filtered detections
#         draw = ImageDraw.Draw(img)
        # annotated_img = Image.fromarray(img)
        # draw = ImageDraw.Draw(annotated_img)



#         # for i, box in enumerate(boxes):
#         for i in lable_indices_we_can_show:
#           box = boxes[i]
#           draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline='red', width=3)
#           text = classes_detected[i]
#           draw.text((box[0], box[1]), text, fill='red', font = ImageFont.truetype('arial.ttf', 25))
#           # draw.text([(box[0], box[1])],class_names[interested_indices[i]], fill='red', font = font)

#         # Show and save annotated image
#         img.show()
#         img.save('annotated_image.jpg')
#     #     import streamlit as st
#     #     from PIL import Image

#         # Load the image from a file
#         image = Image.open('annotated_image.jpg')

#         # Display the image
#         st.image(image, caption='Your Object Detection Image')


#         return detections

#     if uploaded_file is not None:
#         # Use PIL to open the file from bytes
#         image = Image.open(uploaded_file)

#         # Display the image
#         st.image(image, caption="Uploaded image", use_column_width=True)

#         # Save the image to disk
#         filename = f"{uploaded_file.name.split('.')[0]}.png"
#         image.save(filename, format="PNG")
#         st.success(f"Saved {filename} to disk!")
#         detect(model, filename)
