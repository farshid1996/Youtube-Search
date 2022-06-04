# pip install scrapetube
# pip install py-youtube
import scrapetube
from py_youtube import Data
import pandas as pd
import os

keyword_input = str(input("What do you want to search ? "))
videos_number = int(input("How many videos to search ? "))


def get_statics(keyword="python", max_video=50):
    final_link = []
    final_data = []
    videos = scrapetube.get_search(keyword, limit=max_video, results_type="video")
    for video in videos:
        l1 = list(video['navigationEndpoint'].items())[1][1]
        l2 = l1['webCommandMetadata']['url']
        final = "https://www.youtube.com" + l2
        final_link.append(final)

    for links in final_link:
        data = Data(str(links)).data()
        channel = data['channel_name']
        subs = data['subscriber']
        title = data['title']
        views = data['views']
        publishdate = data['publishdate']
        likes = data['likes']

        dict2 = dict(
            Channel_name=channel,
            Subscriber=subs,
            Title=title,
            Link=links,
            Views=views,
            Publish_date=publishdate,
            Likes=likes
        )
        final_data.append(dict2)
    return final_data


Statics_Data_Frame = pd.DataFrame(get_statics(keyword_input, videos_number))

# Statics_Data_Frame.to_csv("youtube_channel_statics.csv", encoding="utf-8")
# Save CSV file in desktop
directory = "~/Desktop/" + str(keyword_input) + ".csv"
desktop = os.path.normpath(os.path.expanduser(directory))
Statics_Data_Frame.to_csv(desktop, encoding="utf-8")
