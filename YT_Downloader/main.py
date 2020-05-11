import pytube

# for downloading multiple files Use list and Loop
link = input("Enter the Link of Youtube To download:")
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
# The video will be downloaded in the Current directory
print("Downloaded")

