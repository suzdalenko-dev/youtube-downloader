import subprocess
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

def download_youtube_video(youtube_url):

    output_dir = "work"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Comando yt-dlp
        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o", f"{'work'}/%(epoch)s.%(ext)s",
            youtube_url
        ]
        
        # Ejecutar el comando
        print(f"Download from: {youtube_url}")
        subprocess.run(command, check=True)
        print("¡Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        x = input("")

def get_latest_file(directory, extension):
    """Get the latest file by creation date with the given extension in a directory."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        raise FileNotFoundError(f"No files with extension {extension} found in {directory}.")
        x = input("")
    return max(files, key=os.path.getctime)

def merge_video_audio(output_dir):
    try:
        # Get the latest video and audio files
        video_file = get_latest_file(output_dir, ".mp4")
        audio_file = get_latest_file(output_dir, ".m4a")

        print(f"Latest video file: {video_file}")
        print(f"Latest audio file: {audio_file}")

        # Load the video and audio files
        video = VideoFileClip(video_file)
        audio = AudioFileClip(audio_file)

        # Combine video and audio
        video = CompositeVideoClip([video])
        video.audio = audio

        # Extract the base name of the video file (without extension)
        video_name = os.path.splitext(os.path.basename(video_file))[0]

        # Define output file
        output_file = os.path.join(os.getcwd(), f"{video_name}.mp4")

        # Write the output to a file
        video.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Files merged successfully: {output_file}")
    except Exception as e:
        print(f"Error merging files: {e}")
        x = input("")

if __name__ == "__main__":
    try:
        print("")
        print("DOWNLOAD VIDEO FROM YOUTUBE - Suzdalenko Alexey was here 2024-31-12")
        print("")
        print("Example url https://youtu.be/XwTYKFeyiB0")
        print("")
        youtube_url = input("URL YouTube: ")
        download_youtube_video(youtube_url)
        merge_video_audio('work')
    except Exception as e:
        print(f"Error: {e}")
        x = input("")