import subprocess
import os
from pathlib import Path

def download_youtube_video(youtube_url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs('out', exist_ok=True)
    
    try:
        command = [
            "C:\python_exe\Scripts\yt-dlp.exe",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o", f"{output_dir}/%(epoch)s.%(ext)s",
            "-k",
            youtube_url
        ]
        print(f"Downloading from: {youtube_url}")
        subprocess.run(command, check=True)
        print("Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
        x = input("Press Enter to exit...")

def merge_video_audio(video_path, audio_path, output_path):
    """
    Merges video and audio using ffmpeg.
    """
    try:
        # Command to merge video and audio
        command = [
            "C:/ProgramData/chocolatey/bin/ffmpeg.exe",  # Full path to ffmpeg
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-strict", "experimental",
            output_path
        ]

        print(f"Merging video and audio into: {output_path}")
        subprocess.run(command, check=True)
        print("Merge complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error merging files: {e}")
        x = input("Press Enter to exit...")

def main():
    # Example usage
    print("Example: https://youtu.be/d73tiBBzvFM")
    youtube_url = input("Enter Short YouTube URL: ").strip()

    # Download video and audio
    output_dir = "downloads"
    download_youtube_video(youtube_url, output_dir)

    # Optional: merge video and audio
    try:
        # Locate the most recent video and audio files
        video_file = max(Path(output_dir).glob("*.mp4"), key=os.path.getctime)
        audio_file = max(Path(output_dir).glob("*.m4a"), key=os.path.getctime)
        output_file = f"out/{video_file.stem}_merged.mp4"

        merge_video_audio(str(video_file), str(audio_file), output_file)
    except Exception as e:
        print(f"Error during merge: {e}")
        x = input("Press Enter to exit...")

if __name__ == "__main__":
    main()
