def open_or_senior(data):
    output = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output