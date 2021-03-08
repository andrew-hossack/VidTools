'''
 # @ Author: Andrew Hossack
 # @ Create Time: 2021-03-02 20:55:32
 # @ Description: Driver file for uploading TikTok videos.
        Feel free to build off of this as an example!
 '''

from vidtools.TikTokTools import TikTokTools
from vidtools.VideoTools import VideoTools
from vidtools.YouTubeTools import YouTubeTools

# NOTE This driver file is NOT COMPLETE!

if __name__ == "__main__":
    api = TikTokTools(verbosity=1)
    videotools = VideoTools()

    num_videos_requested = 3    # Max number of return videos
    max_length_seconds = 20     # Max length of videos
    videolist_parsed = api.get_video_list(num_videos_requested, max_length_seconds, buffer_len=10)

    for tiktok in videolist_parsed:
        # Get new video from list
        desc = tiktok['desc']
        downloadaddr = tiktok['video']['downloadAddr']
        author = tiktok['author']['nickname']
        print(f"Title: {desc} by {author}\nLink: {downloadaddr}")

        # Download Video
        videotools.video_downloader_from_url(downloadaddr)
        print(f'Done Downloading to {videotools._downloads_dir}\n')