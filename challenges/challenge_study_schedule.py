def study_schedule(permanence_period, target_time):
    best_time = 0

    try:
        for period in permanence_period:
            start, end = period
            if start <= target_time <= end:
                best_time += 1
    except TypeError:
        return None
    else:
        return best_time
