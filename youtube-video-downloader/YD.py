from yt_dlp import YoutubeDL
from sys import argv
import os

def main():
    if len(argv) < 3:
        print("Usage: python YD.py <YouTube_URL> <Local_Folder_Path>")
        return

    link = argv[1]
    local_folder_path = argv[2]

    # Create the download directory if it does not exist
    os.makedirs(local_folder_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(local_folder_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4'
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Video downloaded successfully to {local_folder_path}")
    except Exception as e:
        print(f"Failed to download video: {e}")

if __name__ == "__main__":
    main()
