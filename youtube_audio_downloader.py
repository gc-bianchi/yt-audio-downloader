import os
import yt_dlp
from typing import List


def download_youtube_audio(
    video_urls_or_search_terms: List[str], output_directory: str
) -> bool:
    """
    Use a list of YouTube video URLs or search terms to download the audio from YouTube videos.

    :param video_urls_or_search_terms:  A list of YouTube video URLs or search terms.
    :param output_directory:            The directory where the downloaded audio files will be saved.
    :return:                            True if all downloads are successful, False if an error occurs.
    """

    try:
        download_options = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_directory, "%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        # replace print statements with logger
        with yt_dlp.YoutubeDL(download_options) as downloader:
            for term in video_urls_or_search_terms:
                print(f"Downloading audio for: {term}")
                downloader.download([term])
        print("All audio downloads completed successfully.")
        return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


####

video_urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
output_dir = "~/Desktop"
download_youtube_audio(video_urls, output_dir)
