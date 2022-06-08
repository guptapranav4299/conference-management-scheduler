from conference_scheduler import Conference, Track, Talk


def test():
    conf = Conference(name="Pfeffery Times", file="input.txt", starts_at="09:00", ends_at="17:00", lunch_at="12:00",
                      networking_at="17:00")
    conf.add_track("Track 1")
    conf.add_track("Track 2")
    conf.schedule()
    conf.list_tracks()


if __name__ == '__main__':
    test()
