from apigle.client import ApigleClient

API_KEY = "d0c77b28-ee50-420a-b697-576ce749b44f"
client = ApigleClient(API_KEY)

# /v1/search
print("search_v1:", client.search_v1(q="lofi music", pageToken=None))

# /v2/download
print("download:", client.download(
    video="QW8-UVmMm_Q?si=iWYXzmZ-tDb6Qpb7",
    type="mp4",
    resolution=360,
))

print("download_file:", client.download_file(
    video="QW8-UVmMm_Q?si=iWYXzmZ-tDb6Qpb7",
    output_path="asd.mp4",
    type="mp4",
    resolution=360,
))

# /v2/search
print("search_v2:", client.search_v2(
    q="ban",
    part="snippet",
    regionCode="US",
    maxResults=100,
    order="relevance",
    pageToken=None,
))

# /v2/videoComments
print("videoComments:", client.video_comments(
    videoId="kffacxfA7G4",
    part="snippet",
    maxResults=100,
))

# /v2/videoDetails
print("video_details:", client.video_details(
    id="XGGXlj6grzQ",
    part="contentDetails,snippet,statistics",
))

# /v2/channelDetails
print("channel_details:", client.channel_details(
    id="UCfM3zsQsOnfWNUppiycmBuw",
    part="snippet,statistics",
))

# /v2/channelVideos
print("channel_videos:", client.channel_videos(
    channelId="UCvgfXK4nTYKudb0rFR6noLA",
    part="snippet,id",
    order="date",
    maxResults=50,
    pageToken=None,
))

# /v2/playlistDetails
print("playlist_details:", client.playlist_details(
    id="PLqpXi64f6ul2Nzd5hHdHS4XuWa7ix8Rm-",
    part="snippet",
))

# /v2/playlistVideos
print("playlist_videos:", client.playlist_videos(
    playlistId="RDMM",
    part="snippet",
    maxResults=50,
    pageToken=None,
))

# /v2/trending
print("trending:", client.trending(
    part="snippet",
    videoCategoryId=1,
    regionCode="US",
    maxResults=50,
    pageToken=None,
))

# /v2/videoCategories
print("video_categories:", client.video_categories(
    part="snippet",
))

# /v2/i18nRegions
print("i18n_regions:", client.i18n_regions())
