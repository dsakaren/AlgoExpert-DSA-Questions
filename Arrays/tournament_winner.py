def tournamentWinner(competitions, results):
    # Write your code here.
    points_dict = {}

    for i in range(len(competitions)):
        for j in range(len(competitions[i])):
            if competitions[i][j] not in points_dict:
                points_dict[competitions[i][j]] = 0

        if results[i] == 1:
            points_dict[competitions[i][0]] += 3
        else:
            points_dict[competitions[i][-1]] += 3

    return max(points_dict, key=points_dict.get)
