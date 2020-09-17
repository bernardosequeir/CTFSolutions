def stat(strg):
    runners_scores = strg.split(', ')
    hours_scores = []
    minutes_scores = []
    seconds_scores = []
    for score in runners_scores:
        split_values = score.split('|')
        hours_scores.append(int(split_values[0]))
        minutes_scores.append(int(split_values[1]))
        seconds_scores.append(int(split_values[2]))
    hours_scores.sort()
    minutes_scores.sort()
    seconds_scores.sort()
    range_str = calculate_range(hours_scores, minutes_scores, seconds_scores)
    mean_str = calculate_mean(hours_scores, minutes_scores, seconds_scores)
    median_str = calculate_median(hours_scores, minutes_scores, seconds_scores)

    return range_str + mean_str + median_str


def calculate_range(hours_scores, minutes_scores, seconds_scores):
    hours_range = hours_scores[-1] - hours_scores[0]
    minutes_range = minutes_scores[-1] - minutes_scores[0]
    seconds_range = seconds_scores[-1] - seconds_scores[0]
    range_string = "Range: " + \
        pad(hours_range) + "|" + pad(minutes_range) + \
        "|" + pad(seconds_range) + " "
    return range_string


def calculate_mean(hours_scores, minutes_scores, seconds_scores):
    hours_mean = round(sum(hours_scores) / len(hours_scores))
    minutes_mean = round(sum(minutes_scores) / len(minutes_scores))
    seconds_mean = round(sum(seconds_scores) / len(seconds_scores))
    mean_string = "Mean: " + \
        pad(hours_mean) + "|" + pad(minutes_mean) + \
        "|" + pad(seconds_mean) + " "
    return mean_string


def calculate_median(hours_scores, minutes_scores, seconds_scores):
    hours_median = hours_scores[round(len(hours_scores) / 2)]
    minutes_median = minutes_scores[round(len(hours_scores) / 2)]
    seconds_median = seconds_scores[round(len(hours_scores) / 2)]
    if(len(hours_scores) % 2 != 0):
        hours_median = round(hours_scores[round(
            len(hours_scores) / 2)] + hours_scores[round((len(hours_scores) / 2) + 1)] / 2)
        minutes_median = round(minutes_scores[round(
            len(minutes_scores) / 2)] + minutes_scores[round((len(minutes_scores) / 2) + 1)] / 2)
        seconds_median = round(seconds_scores[round(
            len(seconds_scores) / 2)] + seconds_scores[round((len(seconds_scores) / 2) + 1)] / 2)
    median_string = "Median: " + \
        pad(hours_median) + "|" + pad(minutes_median) + \
        "|" + pad(seconds_median)
    print(median_string)
    return median_string


def pad(num):
    if(num < 10):
        return "0" + str(num)
    return str(num)


if __name__ == "__main__":
    stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")
