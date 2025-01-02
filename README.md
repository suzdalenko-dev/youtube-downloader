# YouTube Downloader Script

**Version**: 1.0.0  
**Released**: 2024-12-31  
**Author**: Suzdalenko Alexey  

---

## Description

This script allows users to download videos from YouTube in both video and audio formats.

## Features

- Download the best video and audio quality available.
- Merge video and audio into a single MP4 file.
- Automatically clean up intermediate files.
- Easy-to-use script for any YouTube URL.

---

## Requirements

Windows 10-11
---

## Installation



1. **Clone the Repository**:
   you need install "yt-dlp" and "ffmpeg" framework
   ```bash
   git clone https://github.com/your-repo/youtube-downloader.git
   cd youtube-downloader
   run start.exe













Comments:


pyinstaller --onefile start.py
pyinstaller --onefile --add-binary "C:/ProgramData/chocolatey/bin/ffmpeg.exe;." --add-binary "C:/python_exe/Scripts/yt-dlp.exe;." start.py


powerShell:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install ffmpeg