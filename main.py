import os
import requests

def main():
    # Your TikTok API key
    api_key = input("Enter your API key: ")
    print(api_key)
    correct_api = input("Is your API key correct? [Y/N]: ").upper()
    # Your TikTok Client Secret
    print("make sure to enter correct info")
    client_secret = input("Enter your Client Secret: ")
    # Your TikTok Client Key
    client_key = input("Enter your Client Key: ")
    
    if correct_api == "YES" or correct_api == "Y":
        print("Make sure you have all the videos which will be uploaded in the current directory.")
        
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
                    "X-TikTok-Client-Secret": client_secret,
                    "X-TikTok-Client-Key": client_key,
                    "X-TikTok-Video-Title": video_title
                }, data=video_data)

                # Check the response status code
                if response.status_code != 200:
                    print("Failed to upload video:", filename)
                else:
                    print("Successfully uploaded video:", filename)
    else:
        print("Make sure to enter the correct API key and run the script again.")
        quit

print("Privacy policy: This script is only used to upload all videos in the current directory and we are not using any of your data.")
PPTAC = input("Have you read and agreed with the privacy policy? [Y/N]: ").upper()
print("Terms and Conditions: By using this script, you agree to upload all your videos in the current directory to TikTok.")
TAC = input("Have you read and agreed with the terms and conditions? [Y/N]: ").upper()
if PPTAC == "YES" or PPTAC == "Y" and TAC == "YES" or TAC == "Y":
    main()
else:
    print("Please read and agree to our privacy policy and terms and conditions.")
    quit
