def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    student_quantities = 0

    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        if (target_time >= period[0]) and (target_time <= period[1]):
            student_quantities += 1

    return student_quantities
