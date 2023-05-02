from libqtile.command import lazy


# Define a function to toggle between the two most recently used groups
@lazy.function
def toggle_recent_groups():
    recent_groups = []  # Keep track of the two most recent groups

    def callback(qtile):
        current_group = qtile.current_group
        group_name = current_group.name

        # Add the current group to the recent_groups list if it's not there
        if group_name not in recent_groups:
            recent_groups.append(group_name)

        # Remove the oldest group if there are more than two groups in the list
        if len(recent_groups) > 2:
            recent_groups.pop(0)

        # Get the next group based on the current group and recent_groups list
        if len(recent_groups) == 2:
            if group_name == recent_groups[0]:
                next_group_name = recent_groups[1]
            else:
                next_group_name = recent_groups[0]
        else:
            next_group_name = group_name

        # Switch to the next group
        next_group = qtile.groups_map[next_group_name]
        qtile.current_screen.set_group(next_group)

    return callback
