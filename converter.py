from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(url, output_path='output'):
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Download the video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    audio_file_path = video.download(output_path=output_path)

    # Convert to MP3
    base, ext = os.path.splitext(audio_file_path)
    mp3_file_path = f"{base}.mp3"
    audio = AudioSegment.from_file(audio_file_path)
    audio.export(mp3_file_path, format="mp3")

    # Remove the original audio file
    os.remove(audio_file_path)

    return mp3_file_path

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    mp3_file = download_youtube_video_as_mp3(url)
    print(f"Downloaded and converted video to {mp3_file}")
