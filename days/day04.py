import numpy as np

# Event from the guards
class Event:
    def __init__(self, yy, mm, dd, h, m, guard_id, event):
        self.yy = yy
        self.mm = mm
        self.dd = dd
        self.h = h
        self.m = m
        self.guard_id = guard_id
        self.event = event

    def __repr__(self):
        return f"[{self.yy} - {self.mm} - {self.dd} | {self.h}:{self.m}] Guard: {self.guard_id} Event: {self.event}"

    def __lt__(self, other):
        return ((int(self.yy), int(self.mm), int(self.dd), int(self.h), int(self.m)) <
                (int(other.yy), int(other.mm), int(other.dd), int(other.h), int(other.m)))

def process_data(input_data):
    events = []

    # process every line
    for line in input_data.split("\n"):
        year = line[1:5]
        month = line[6:8]
        day = line[9:11]
        hour = line[12:14]
        minute = line[15:17]
        if "Guard" in line.split(" "):
            guard = int(line.split(' ')[3][1:])
            event = "start_shift"
        elif "wakes" in line.split(" "):
            guard = -1
            event = "wake_up"
        else:
            guard = -1
            event = "fall_asleep"

        events.append(Event(year, month, day, hour, minute, guard, event))

    events.sort()

    guards_sleeping = {}
    current_guard = -1

    # go over all the events, if guard changes, we note that, if someone awakens we register the sleeping time
    for i, e in enumerate(events):
        if e.guard_id != -1:
            current_guard = e.guard_id
            if e.guard_id not in guards_sleeping: guards_sleeping[e.guard_id] = [0] * 60
        elif e.event == "wake_up":
            for m in range(int(events[i - 1].m), int(e.m)):
                guards_sleeping[current_guard][m] += 1

    return guards_sleeping

def solve_part1(input_data):
    # grid of 1000x1000 inches
    guards_sleeping = process_data(input_data)

    # extract the guard with the highest sum of the entire sleeping schedule
    most_sleeping = max(guards_sleeping, key=lambda gid: sum(guards_sleeping[gid]))
    # and find the highest minute in that array
    most_minute = guards_sleeping[most_sleeping].index(max(guards_sleeping[most_sleeping]))

    return most_minute * most_sleeping

def solve_part2(input_data):
    guards_sleeping = process_data(input_data)

    # just iterate over all guards cumulative schedules and find max minute
    max_guard = None
    max_minute = None
    max_count = 0

    for guard, minutes in guards_sleeping.items():
        for minute, count in enumerate(minutes):
            if count > max_count:
                max_count = count
                max_guard = guard
                max_minute = minute

    return max_guard*max_minute
