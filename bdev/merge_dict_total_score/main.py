def merge(dict1, dict2):
    # let's not mutate arguments
    # get a set of unique keys
    keys = set(dict1.keys()).union(dict2.keys())

    # new results dict
    results = dict()

    # loop over keys and combine key/value pairs
    for key in keys:
        if key in dict2 and key in dict1 or key in dict2:
            results[key] = dict2[key]
        else:
            results[key] = dict1[key]

    return results


def total_score(score_dict):
    total_score = 0

    for value in score_dict.values():
        total_score += value

    return total_score
