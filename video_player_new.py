"""A video player class."""
import pandas as pd
import operator
from src.video_playlist import Playlist # importing the necessary packages
from video_library import VideoLibrary
from src.video import Video


import enum
# will need to create a serparate class to run the stop/play functions
class video_state(enum.Enum):
    Playing = 1
    Pause = 2
    Stop = 3
    Continue = 4

class running_video:
    def __init__(self):
        self.video = None
        self.status = video_state.Stop

    def set_video(self, video, state):
        self.video = video
        self.set_status(state)

    def set_status(self, state):
        self.status = state

        if self.status == video_state.Playing:
            print("Playing video: " + self.video._title)
        elif self.status == video_state.Pause:
            print("Pausing video: " + self.video._title)
        elif self.status == video_state.Stop:
            print("Stopping video: " + self.video._title)
            self.video = None
        elif self.status == video_state.Continue:
            print("Continuing video: " + self.video._title)

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = True

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("here is a list of all videos")
        all_vids = self._video_library.get_all_videos()
        videos = []
        sorted_videos = []
        for vid in all_vids:
            tags = "["
            for tag in vid.tags:
                tags += tag + ""
            tags = tags.strip()
            tags += "]"
            videos += [f"{vid.title} ({vid.video_id}) {tags}"]
            sorted_videos = sorted(videos)
        for i in sorted_videos:
                print(i)
        # list_words = []
        # with open("videos.txt", "r") as d:
        #     lines = d.readlines()
        #     new_lines = sorted(lines)
        #     for i in new_lines:
        #         print(i)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video != None:

            if (video.flagged == None):
                if self.running_video.status != video_state.Stop:  # for avoiding the first time error print message from stop_video
                    self.stop_video()  # stopping the current video if playing

                self.running_video.set_video(video, video_state.Playing)
            else:
                print("Cannot play video: Video is currently flagged (reason: " + video.flagged + ")")

        else:
            print("Cannot play video: Video does not exist")
        # self.is_playing = is_playing
        # vids = self._video_library.get_video(video_id)
        # video_name = vids.title
        # print("playing video. {}".format(video_name))
        # return video_name





    def stop_video(self):


        """Stops the current video."""


        if self.video_under_process.status != video_state.Stop:
            self.video_under_process.set_status(video_state.Stop)

        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        # print("play_random_video needs implementation")
        videos = self._video_library.get_all_videos()

        # if all videos are marked as flagged them showing no video avaiilable for random function
        if len([x for x in videos if x.flagged == None]) == 0:
            print("No videos available")
            return

        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

        if self.video_under_process.video != None:
            if (self.video_under_process.status != video_state.Pause):
                self.video_under_process.set_status(video_state.Pause)
            else:
                print("Video already paused:", self.video_under_process.video._title)

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        if self.video_under_process.video != None:
            if self.video_under_process.status == video_state.Pause:
                self.video_under_process.set_status(video_state.Continue)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")
        """Resumes playing the current video."""


    def show_playing(self):
        if self.video_under_process.video != None:
            if self.video_under_process.status != video_state.Pause:
                print("Currently playing:", self.get_video_details(self.video_under_process.video))
            else:
                print("Currently playing:", self.get_video_details(self.video_under_process.video), "- PAUSED")

        else:
            print("No video is currently playing")
        """Displays video currently playing."""



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
