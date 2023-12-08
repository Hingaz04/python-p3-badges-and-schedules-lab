def badge_maker(name):

    return f"Hello, my name is {name}."


def batch_badge_creator(speakers):

    return [badge_maker(name) for name in speakers]


def assign_rooms(speakers):

    room_assignments = []
    for index, name in enumerate(speakers, start=1):
        room_assignments.append(
            f"Hello, {name}! You'll be assigned to room {index}!")
    return room_assignments


def printer(speakers):

    badges = batch_badge_creator(speakers)
    for badge in badges:
        print(badge)

    room_assignments = assign_rooms(speakers)
    for assignment in room_assignments:
        print(assignment)
