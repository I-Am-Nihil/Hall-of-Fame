import moviepy.editor
from pathlib import Path

# In the bottom line, 
# add the video file that was previously placed in the folder with the code.
# There must also be an audio file in the folder, 
# the name of which will be the same as that of the video file.
video_file = Path('...')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')
