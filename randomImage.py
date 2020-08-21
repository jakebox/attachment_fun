import random, subprocess, glob
from pathlib import Path

HOME_FOLDER = "jake"
OPEN_LINK_IMAGES = False

messages_path = "/Users/" + HOME_FOLDER + "/Library/Messages/Attachments"

video_extns = ['mov', 'mp4', 'wmv', 'mpg']
image_extns = ['jpg', 'peg', 'png', 'gif', 'ebp', 'bmp', 'iff', 'svg']

class RandomAttachmenter():

    def __init__(self, messages_path):
    
        self.messages_path = messages_path
        # Create a list of paths to all iMessage attachment files
        self.media_files = glob.glob(self.messages_path + '/*/*/*/*', recursive=True)

    def open_media(self, media_path, file_type):

        if file_type == "video": 
            subprocess.call(["open", "-a", "QuickTime Player", media_path])
            return 1
        elif file_type == "image":
            subprocess.call(["open", "-a", "Preview", media_path])
            return 1
        else:
            return 0 # This should never happen

    def get_random_image(self):
        
        # Getting the path to a random media file from our list 
        media_path = self.media_files[random.randrange(len(self.media_files))]

        # Grab the file extension (.png, .mov, etc)
        media_extn = Path(media_path).suffix.lower()

        if media_extn[-3:] in video_extns:
            file_type = "video"
        elif media_extn[-3:] in image_extns or (media_extn == ".pluginpayloadattachment" and OPEN_LINK_IMAGES is True):
            file_type = "image"
        else:
            # Run again and try to find another file
            return self.get_random_image()
              
        return media_path, file_type

if __name__ == "__main__":
    obj = RandomAttachmenter(messages_path)
    media_path, file_type = obj.get_random_image()
    #print("\n" + media_path, file_type)
    obj.open_media(media_path, file_type)

