from itertools import count


def countnow(places):
    for i in places.values():
        if len(i) > 5:
            print(i)

d = {1: "DELHI", 2: "LONDON", 3: "PARIS", 4: "NEW YORK", 5: "DUBAI"}
countnow(d)