from pytubefix import YouTube
from pydub import AudioSegment
import eyed3
import os


def get_audio(link):
    """
    Downloads the audio from the URL to a m4a file
    """
    try:
        yt = YouTube(
                link,
                use_oauth=True,
                allow_oauth_cache=True
        )
        
        yt.title = input(str("Enter song name: "))
        print("Downloading...")    
    
        vid_stream = yt.streams.filter(only_audio=True).first()
                
        vid_stream.download(output_path=".")
        print("Downloaded!")
        return yt.title

    except Exception as e:
        print(f"An error has occurred: {e}")


def m4a_to_mp3(filename: str):
    """
    Converts the audio from m4a to mp3 since Spotify does not accept m4a files
    """
    print("Converting from m4a to mp3...")
    m4a_file = AudioSegment.from_file(filename + ".m4a", format="m4a")
    m4a_file.export(filename + ".mp3", format="mp3")
    print("Converted!")
    os.remove(filename + ".m4a")

def set_artist(filename: str, artist: str):
    """
    Gives the file a proper artist on Spotify so it is easier to search for
    """
    s = eyed3.load(filename + ".mp3")
    s.tag.artist = artist
    s.tag.save()


if __name__ == "__main__":
    # Directory is set in the Spotify app.
    home_dir = os.path.expanduser("~")
    music_dir = os.path.join(home_dir, "Music")
    os.chdir(music_dir)
    other_path = input("Would you like to use another directory [y/n]? ")
    if (other_path == "y"):
        new_path = input("Write path: ")
        os.chdir(new_path)
    url = input("URL: ")
    artist = input(str("Enter Artist: "))

    title = get_audio(url)
    m4a_to_mp3(title)
    set_artist(title, artist)

    
