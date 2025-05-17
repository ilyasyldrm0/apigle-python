import os
from apigle.client import ApigleClient

API_KEY = "test-api-key"

client = ApigleClient(API_KEY)

def test_search_v1():
    result = client.search_v1(q="test")
    print("search_v1:", result)

def test_download():
    result = client.download(video="QW8-UVmMm_Q", type="mp4", resolution=360)
    print("download:", result)

def test_download_file():
    success = client.download_file(video="QW8-UVmMm_Q", output_path="test.mp4", type="mp4", resolution=360)
    print("download_file:", success)
    if os.path.exists("test.mp4"): os.remove("test.mp4")

def test_search_v2():
    result = client.search_v2(q="test")
    print("search_v2:", result)

def test_video_comments():
    result = client.video_comments(videoId="QW8-UVmMm_Q")
    print("video_comments:", result)

def test_video_details():
    result = client.video_details(id="QW8-UVmMm_Q")
    print("video_details:", result)

def test_channel_details():
    result = client.channel_details(id="UCsPGGyIGeuDn2YwuZ1yE_uQ")
    print("channel_details:", result)

def test_channel_videos():
    result = client.channel_videos(channelId="UCsPGGyIGeuDn2YwuZ1yE_uQ")
    print("channel_videos:", result)

def test_playlist_details():
    result = client.playlist_details(id="PLBCF2DAC6FFB574DE")
    print("playlist_details:", result)

def test_playlist_videos():
    result = client.playlist_videos(playlistId="PLBCF2DAC6FFB574DE")
    print("playlist_videos:", result)

def test_trending():
    result = client.trending()
    print("trending:", result)

def test_video_categories():
    result = client.video_categories()
    print("video_categories:", result)

def test_i18n_regions():
    result = client.i18n_regions()
    print("i18n_regions:", result)

if __name__ == "__main__":
    test_search_v1()
    test_download()
    test_download_file()
    test_search_v2()
    test_video_comments()
    test_video_details()
    test_channel_details()
    test_channel_videos()
    test_playlist_details()
    test_playlist_videos()
    test_trending()
    test_video_categories()
    test_i18n_regions()
