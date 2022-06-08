import datetime


class Talk:
    # Class modelling a Talk.

    def __init__(self, title="Generic Talk", duration=60, starts_at=None):
        super(Talk, self).__init__()
        self.title = title
        self.duration = duration
        self.starts_at = starts_at


class Track:
    """
    Class modelling a Track (Collection of talks and breaks)
    """

    def __init__(self, name, starts_at=None, ends_at=None, lunch_at=None, networking_at=None):
        super(Track, self).__init__()
        self.name = name
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.lunch_at = lunch_at
        self.networking_at = networking_at
        self.talks = []

    def add_talk(self, talk):
        self.talks.append(talk)

    def schedule_talk(self, start, end, talks):
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


class Conference:
    """
    Class to model Conference. Collection of tracks. The biggest entity in the given limited universe of discourse.
    """

    def __init__(self, name="Generic Conference", file=None, starts_at=None, ends_at=None, lunch_at=None,
                 networking_at=None):
        super(Conference, self).__init__()
        self.name = name
        self.tracks = []
        self.unassigned_talks = []
        self.starts_at = datetime.datetime.strptime(starts_at, "%H:%M")
        self.ends_at = datetime.datetime.strptime(ends_at, "%H:%M")
        self.lunch_at = datetime.datetime.strptime(lunch_at, "%H:%M")
        self.networking_at = datetime.datetime.strptime(networking_at, "%H:%M")
        if file:
            self.parse_input_file(file)

    def parse_input_file(self, file):
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

    def create_track(self, name):
        self.tracks.append(Track(name, starts_at=self.starts_at, ends_at=self.ends_at, lunch_at=self.lunch_at,
                                 networking_at=self.networking_at))

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
        for track in self.tracks:
            self.unassigned_talks = track.schedule_talk(self.starts_at, self.lunch_at, self.unassigned_talks)
            track.add_talk(Talk(title="Lunch", starts_at=self.lunch_at))
            self.unassigned_talks = track.schedule_talk(
                datetime.datetime.strptime(str(self.lunch_at.hour + 1) + ":" + str(self.lunch_at.minute), "%H:%M"),
                self.ends_at,
                self.unassigned_talks)
            track.add_talk(Talk(title="Netowrking Event", starts_at=self.networking_at))
        for talk in self.unassigned_talks:
            print("Unable to schedule: " + talk.title)
