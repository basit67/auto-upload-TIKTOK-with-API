import os
import requests

def main():
        # Your TikTok API key
    api_key = input("your_api_key_here: ")
    print(api_key)
    correctsapi = input("is you API is correct??: ").upper()
    
    if correctsapi == "YES" or correctsapi == "Y":
        print("make sure you have all you video which will be uploaded in current directory")
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
    else:
        print("make sure to enter correct API key and run this script again")
        quit

print("privacy policy:\nthis script is only use to upload all video on current directory and we are not using any of your data")
PPTAC = input("did you read and agree with privacy policy: ").upper()
print("term and condition:\nby using this script you will agreed to upload all your video in current directory to tiktok")
TAC = input("did you read and agree with term and condition: ").upper()
if PPTAC == "YES" or PPTAC == "Y" and TAC == "YES" or TAC == "Y" :
    main()

else:
    print("please read and agreed to our privacy policy, term and condition?")
    quit
