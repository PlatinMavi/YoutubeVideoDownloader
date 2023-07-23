from pytube import YouTube

def get_available_resolutions(yt):
    resolutions = set()
    for stream in yt.streams:
        if stream.resolution:
            resolutions.add(stream.resolution)
    return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        resolutions = get_available_resolutions(yt)

        print("Available Resolutions:")
        for i, resolution in enumerate(resolutions, start=1):
            print(f"{i}. {resolution}")
        choice = int(input("Enter the number corresponding to your preferred resolution: "))

        video_stream = yt.streams.filter(res=resolutions[choice - 1]).first()
        video_stream.download(output_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
video_url = input("Video Link: ")
download_video(video_url, "C:/Users/PC/Desktop/Youtube")