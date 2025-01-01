import subprocess
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from pathlib import Path

def clear_output_dir(output_dir):
    """Delete all files in the specified output directory."""
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"Directory '{output_dir}' does not exist.")

def download_youtube_video(youtube_url):

    output_dir = "work"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    clear_output_dir(output_dir)

    try:
        # Comando yt-dlp
        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o", f"{'work'}/%(title)s.%(ext)s",
            youtube_url
        ]
        
        # Ejecutar el comando
        print(f"Download from: {youtube_url}")
        subprocess.run(command, check=True)
        print("¡Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def get_latest_file(directory, extension):
    """Get the latest file by creation date with the given extension in a directory."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        raise FileNotFoundError(f"No files with extension {extension} found in {directory}.")
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


if __name__ == "__main__":
    print("")
    print("DOWNLOAD VIDEO FROM YOUTUBE - Suzdalenko Alexey was here 2024-31-12")
    print("")
    print("Example url https://youtu.be/E-u_uSJcWm0")
    print("")
    youtube_url = input("URL YouTube: ")
    download_youtube_video(youtube_url)
    merge_video_audio('work')
