from conference_scheduler import Conference


def main():
    conference = Conference(name="My Times", file="input.txt", starts_at="09:00", ends_at="17:00", lunch_at="12:00",
                      networking_at="17:00")
    conference.create_track("Track 1")
    conference.create_track("Track 2")
    conference.schedule_track()
    conference.list_tracks()


if __name__ == '__main__':
    main()
