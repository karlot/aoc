import re
from enum import Enum

with open("input.txt") as file:
    lines = file.read().strip().splitlines()

# Test input
# lines = [
#     "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
#     "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
# ]

class RS(Enum):
    resting = 0
    flying = 1

class Reindeer:
    def __init__(self, name, speed=0, fly_time=0, rest_time=0) -> None:
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.state = RS.flying
        self.time = 0
        self.distance = 0
        self.points = 0
    
    def __repr__(self) -> str:
        return f"({self.name}, speed:{self.speed} km/s for {self.fly_time}, rest-time:{self.rest_time}, distance:{self.distance}, state:{self.state}, points:{self.points})"

    def tick(self) -> None:
        self.time += 1
        if self.state == RS.flying:
            # print(f"{self.name} currently flying, taking rest in {self.fly_time - self.time}")
            self.distance += self.speed
            if self.time == self.fly_time:
                # print(f"{self.name} started to take rest")
                self.state = RS.resting
                self.time = 0
        else: # Resting
            # print(f"{self.name} currently resting, starting to fly in {self.rest_time - self.time}")
            if self.time == self.rest_time:
                # print(f"{self.name} started to fly again")
                self.state = RS.flying
                self.time = 0

# Our almanac for the race
reindeers: dict[str,Reindeer] = {}
for line in lines:
    if m := re.match(r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$", line):
        name, speed, fly_time, rest_time = m.groups()
        reindeers[name] = Reindeer(name, int(speed), int(fly_time), int(rest_time))

def reset_race():
    for r in reindeers.values():
        r.time = r.distance = r.points = 0
        r.state = RS.flying

def max_distance():
    return max(r.distance for r in reindeers.values())

def max_points():
    return max(r.points for r in reindeers.values())

def race(time, use_points=False):
    for _ in range(time):
        for r in reindeers.values():
            r.tick()
        if use_points:
            lead_dist = max_distance()
            for r in reindeers.values():
                if r.distance == lead_dist:
                    r.points += 1
    return max_points() if use_points else max_distance()

#--------------------------------------------------------------------------------------------------
race_seconds = 2503

distance = race(race_seconds)
print(f"Part1: {distance}")

reset_race()

points = race(race_seconds, use_points=True)
print(f"Part2: {points}")
