"""
16. Read the duration of an experiment in seconds and
    calculate the duration in Hours, Minutes and Seconds.
"""
experiment_seconds = int(input("Experiment duration (seconds): "))
hours = experiment_seconds // 3600 # One hours has 3600 seconds
left_over = experiment_seconds % 3600
minutes = left_over // 60
seconds = left_over % 60
print(f"{hours} hours, {minutes} minutes {seconds} seconds")
print(f"{hours}:{minutes}:{seconds}")