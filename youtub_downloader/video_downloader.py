from pytube import YouTube

# geting url of video
print("********** Program is started **********")
print()
print("Enter the url of video which you want to download")
print()
url=input("Enter the url : ")


# creating the youtube object
yt=YouTube(url)

# geting the tital of video
tital=yt.title
print()
print("Tital of video is : "+tital)

# geting the thumbnail
thumbnail=yt.thumbnail_url
print()
print("If you want to download the thumbnail of video")
print("link of thumbnail is : "+thumbnail)

# avalable streams
print()
streams=yt.streams.filter(progressive=True)
for index,stream in enumerate(streams):
    print(f"Press {index} to download ==> {stream}")

# downloading the video
num=int(input("Enter number which you want to download : "))
video=streams[num]

# geting the folder path
print()
print("Enter the path of folder where you want to download the video")
print()
path=input("Enter the path : ")
# changing path according to python
change_path=path.replace("\\","\\\\")
print()
print("********** downloading started **********")
print()
print("********** Please wait........ **********")
video.download(change_path)
print()
print("******* Downloading is complited *******")
print()
input("press Enter to exit ! ")