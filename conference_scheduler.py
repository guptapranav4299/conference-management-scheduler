import datetime
import os,sys

class Talk:

    def __init__(self, title="Generic Talk", duration=60, starts_at=None):
        self.title = title
        self.duration = duration
        self.starts_at = starts_at


class Track:

    def __init__(self, name, starts_at=None, ends_at=None, lunch_at=None, networking_at=None):
        self.name = name
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.lunch_time = lunch_at
        self.networking_time = networking_at
        self.talks = []

    def add_talk(self, talk):
        self.talks.append(talk)

    def schedule_talk(self, start, end, talks):
        try:
            """
            Schedules some talks for the duration between start and end, and returns the list
            of still unscheduled talks.
            """
            start_min = start.hour * 60 + start.minute
            end_min = end.hour * 60 + end.minute
            length = end_min - start_min
            current_length = 0
            for talk in talks:
                if current_length < length and current_length + talk.duration <= length:
                    talk.starts_at = datetime.datetime.strptime(
                        str(start.hour + current_length // 60) + ":" + str(current_length % 60),
                        "%H:%M")
                    self.talks.append(talk)
                    current_length += talk.duration
            return [talk for talk in talks if talk not in self.talks]
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            data = {
                "exception": str(e),
                "filename": str(fname),
                "line_no": str(exc_tb.tb_lineno),
            }
            raise Exception("Error in scheduling talk--->",data)


class Conference:

    def __init__(self, name="Generic Conference", file=None, starts_at=None, ends_at=None, lunch_at=None,
                 networking_at=None):
        self.name = name
        self.tracks = []
        self.unassigned_talks = []
        self.starts_at = datetime.datetime.strptime(starts_at, "%H:%M")
        self.ends_at = datetime.datetime.strptime(ends_at, "%H:%M")
        self.lunch_time = datetime.datetime.strptime(lunch_at, "%H:%M")
        self.networking_time = datetime.datetime.strptime(networking_at, "%H:%M")
        if file:
            status = self.parse_input_file(file)
        else:
            raise Exception("file object cannot be none for parsing")

    def parse_input_file(self, file):
        try:
            """
            Parses a file for input data and stores the parsed talks in unassigned_talks
            """
            inp = open(file, 'r')
            line = inp.readline()
            while line:
                inp_array = line.split()
                if inp_array[len(inp_array) - 1] == "lightning":
                    duration = 5
                else:
                    duration = int(inp_array[len(inp_array) - 1][:-3])
                title = " ".join(inp_array[:len(inp_array) - 1])
                self.unassigned_talks.append(Talk(title=title, duration=duration))
                line = inp.readline()
            inp.close()
            return True
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            data = {
                "exception": str(e),
                "filename": str(fname),
                "line_no": str(exc_tb.tb_lineno),
            }
            print("Error in parsing file--->",data)
            return False

    def create_track(self, name):
        self.tracks.append(Track(name, starts_at=self.starts_at, ends_at=self.ends_at, lunch_at=self.lunch_time,
                                 networking_at=self.networking_time))

    def list_tracks(self):
        """
        Prints information about the tracks
        """
        for track in self.tracks:
            print(track.name + ":")
            for talk in track.talks:
                print(datetime.datetime.strftime(talk.starts_at, "%I:%M %p") + " " + talk.title)

    def add_talk(self, name, duration):
        self.unassigned_talks.append(Talk(name, duration))

    def schedule_track(self):
        try:
            for track in self.tracks:
                self.unassigned_talks = track.schedule_talk(self.starts_at, self.lunch_time, self.unassigned_talks)
                track.add_talk(Talk(title="Lunch", starts_at=self.lunch_time))
                self.unassigned_talks = track.schedule_talk(
                    datetime.datetime.strptime(str(self.lunch_time.hour + 1) + ":" + str(self.lunch_time.minute), "%H:%M"),
                    self.ends_at,
                    self.unassigned_talks)
                track.add_talk(Talk(title="Netowrking Event", starts_at=self.networking_time))
            for talk in self.unassigned_talks:
                print("Unable to schedule: " + talk.title)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            data = {
                "exception": str(e),
                "filename": str(fname),
                "line_no": str(exc_tb.tb_lineno),
            }
            raise Exception("Error in scheduling tracks--->",data)
