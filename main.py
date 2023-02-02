import os
import requests

# Your TikTok API key
api_key = "your_api_key_here"

# The endpoint for uploading videos
upload_endpoint = "https://api.tiktok.com/v1/video/upload"

# Iterate over all videos in the directory
for filename in os.listdir():
    if filename.endswith(".mp4"):
        # Set the video title as the name of the video
        video_title = filename

        # Read the video data
        with open(filename, "rb") as f:
            video_data = f.read()

        # Upload the video
        response = requests.post(upload_endpoint, headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "video/mp4",
            "X-TikTok-Video-Title": video_title
        }, data=video_data)

        # Check the response status code
        if response.status_code != 200:
            print("Failed to upload video:", filename)
        else:
            print("Successfully uploaded video:", filename)
