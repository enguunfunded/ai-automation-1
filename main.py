import yt_dlp
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def download_youtube_video(url):
    ydl_opts = {
        'outtmpl': 'input/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def split_video(input_file, clip_length=30):
    output_dir = "output_shorts"
    os.makedirs(output_dir, exist_ok=True)
    video = VideoFileClip(input_file)
    total_duration = int(video.duration)
    for i in range(0, total_duration, clip_length):
        start = i
        end = min(i + clip_length, total_duration)
        clip = video.subclip(start, end)
        clip.write_videofile(
            f"{output_dir}/clip_{i//clip_length+1}.mp4",
            codec='libx264',
            audio_codec='aac'
        )
if __name__ == "__main__":
    url = input("📥 YouTube линк оруулна уу: ")
    downloaded_file = download_youtube_video(url)
    print("✅ Видео татагдлаа. Одоо тасдаж байна...")
    split_video(downloaded_file)
    print("🎉 Бүх клип бэлэн боллоо! `output_shorts/` хавтсаас шалгаарай.")
