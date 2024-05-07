# Import necessary libraries
import cv2
import numpy as np
import moviepy.editor as mp

# Load the video file
video = cv2.VideoCapture('1.mp4')

# Initialize variables
frames = []
audio_segments = []

# Read frames from the video
while True:
    ret, frame = video.read()
    if not ret:
        break
    frames.append(frame)

# Convert frames to video
output = cv2.VideoWriter('D:/7th sem project/sample1', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frames[0].shape[1], frames[0].shape[0]))
for frame in frames:
    output.write(frame)
output.release()

# Extract audio from the video
clip = mp.VideoFileClip('1.mp4')
clip.audio.write_audiofile('audio.wav')

# Load the audio file
audio = mp.AudioFileClip('audio.wav')

# Detect audio segments with high intensity
audio_segments = audio.subclip(0, audio.duration).iter_segments()

# Generate highlight video
highlight = mp.concatenate_videoclips([mp.VideoFileClip('D:/7th sem project/sample1/high.mp4').subclip(segment[0], segment[1]) for segment in audio_segments])
highlight.write_videofile('D:/7th sem project/sample1/high.mp4', codec='libx264', audio_codec='aac')
