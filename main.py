from tqdm import tqdm
import os
import moviepy.editor as mp

input_folder = "./input_folder"
output_folder = "./output_folder"

def batch_convert_mp4_to_mp3(input_folder, output_folder):
    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(".mp4"):
            try:
                input_file = os.path.join(input_folder, filename)
                output_file = os.path.join(output_folder, filename.split(".")[0] + ".mp3")
        #import -mp MoviePy
                video = mp.VideoFileClip(input_file)
                audio = video.audio
                audio.write_audiofile(output_file)

                video.close()
                audio.close()

            except Exception as e:
                print(f"Error converting file: {filename}. Error: {e}")

batch_convert_mp4_to_mp3(input_folder, output_folder)
