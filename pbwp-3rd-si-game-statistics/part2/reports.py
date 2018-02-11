def load(file_name):
    games = []
    text_file = open(file_name, "r")
    for line in text_file:
        games.append(line.split("\t"))
    for game in games:
        game[4] = game[4][:-1]
    return games

def get_most_played(file_name = "game_stat.txt"):
    sold_copies = 0
    games = load(file_name)

    for game in games:
        if float(game[1]) > sold_copies:
            sold_copies = float(game[1])
            title = game[0]
    return title

def sum_sold(file_name = "game_stat.txt"):
    games = load(file_name)
    sum = 0
    for game in games:
        sum += float(game[1])
    return sum

def get_selling_avg(file_name = "game_stat.txt"):
    games = load(file_name)
    sum = 0
    amount = 0
    for game in games:
        sum += float(game[1])
        amount += 1
    return sum/amount

def count_longest_title(file_name = "game_stat.txt"):
    games = load(file_name)
    longest = 0
    for game in games:
        if len(game[0]) > longest:
            longest = len(game[0])
    return longest

def get_date_avg(file_name = "game_stat.txt"):
    games = load(file_name)
    sum_date = 0
    for game in games:
        sum_date += int(game[2])
    output = sum_date / len(games)
    if output > int(output):
        return int(output) + 1
    return output

def get_game(file_name, title):
    games = load(file_name)
    for game in games:
        if game[0] == title:
            game[1] = float(game[1])
            game[2] = int(game[2])
            return game
    raise ValueError

def count_grouped_by_genre(file_name = "game_stat.txt"):
    games = load(file_name)
    genres = {}
    for game in games:
        if game[3] not in genres.keys():
            genres[game[3]] = 1
        else:
            genres[game[3]] += 1
    return genres

def get_date_ordered(file_name = "game_stat.txt"):
    games = load(file_name)
    ordered = []
    output = []
    for game in games:
        ordered.append((game[0], game[2]))
    ordered = sorted(ordered, key = lambda x: x[0])
    ordered = sorted(ordered, key=lambda x: x[1], reverse = True)
    for item in ordered:
        output.append(item[0])
    return output
