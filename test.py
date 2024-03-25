from videocheck import readlog, videocount, validate, rvcounter

#Example 1: See how many videos you have seen, how many you have remaining and which ones they are.

rvcounter("./data/Testlog.log")

#Example 2: Get a dataframe of your remaining videos and export it to an excel file.

log = readlog("./data/Testlog.log")
seenvideos = videocount(log)
seendf, remainingdf = validate(seenvideos)
remainingdf.to_excel("test_remaining_video_info.xlsx")

#Example 3: Check to  see if the seen videos list is accurate.

log = readlog("./data/Testlog.log")
seenvideos = videocount(log)
seendf, remainingdf = validate(seenvideos)
print(seendf)