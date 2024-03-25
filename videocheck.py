#import packages
import pandas as pd

#create initial variables
remaining_videos = [i for i in range(1,290)]

#read logfile and create a list with the lines from the log
def readlog(logfile):
    with open(logfile, encoding='utf8') as file_object:
        videos_log = [line.strip('\n') for line in file_object.readlines()]
    return videos_log

#find the lines that indicate transitions and create a list of all the videos in the list.
def videocount(video_log):
    seen_videos = []
    for line in video_log:
        try:
            if line[0:32] == "VideoPlaybackManager.Transition:":
                line = line.replace('VideoPlaybackManager.Transition:', '')
                videos = line.split("->")
                seen_videos.append(int(videos[0]))
                seen_videos.append(int(videos[1]))
        except:
            pass
    return seen_videos

#load database from reddit (credits to u/Casinocaster) and validate from there.
def validate(seen_video_list):
    reddit_df = pd.read_excel('./data/videolist.xlsx')
    seen_df = reddit_df.loc[reddit_df['Video'].isin(seen_video_list)]
    remaining_df = reddit_df.loc[~reddit_df['Video'].isin(seen_video_list)]
    return seen_df, remaining_df

#create main function that returns a count of how many
def rvcounter(logfile):
    videoslog = readlog(logfile)
    seenvideos = videocount(videoslog)
    sv,rv = validate(seenvideos)
    remaining_count = len(rv)
    message = f"Immortality video count: \n {len(sv)} videos have been seen. \n {len(rv)} remain to be seen. The list of videos to be seen is the following: \n {list(rv.Video)}"
    print(f"{message}")