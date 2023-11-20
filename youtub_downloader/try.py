from pytube import YouTube


print("Enter the url of video which you want to download")
print()
url=input("Enter the url : ")


# creating the youtube object
yt=YouTube(url)


# avalable streams
print()
streams=yt.streams.filter(progressive=True)
for index,stream in enumerate(streams):
    print(f"Press {index} to download ==> {stream}")



