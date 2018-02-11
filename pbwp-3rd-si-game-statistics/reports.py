
# Report functions
def load(file_name):
    games = []
    text_file = open(file_name, "r")
    for line in text_file:
        games.append(line.split("\t"))
    return games

def count_games(file_name = "game_stat.txt"):
    games = load(file_name)
    return len(games)

def decide(file_name = "game_stat.txt", year = 2009):
    games = load(file_name)
    for game in games:
        if game[2] == str(year):
            return True
    return False

def get_latest(file_name = "game_stat.txt"):
    games = load(file_name)
    latest = 0
    for game in games:
        if int(game[2]) > latest:
            latest = int(game[2])
            title = game[0]
    return title

def count_by_genre(file_name = "game_stat.txt", genre = "RPG"):
    games = load(file_name)
    counter = 0
    for game in games:
        if game[3] == genre:
            counter += 1
    return counter

def get_line_number_by_title(file_name = "game_stat.txt", title = "Diablo III"):
    games = load(file_name)
    line_number = 1
    for game in games:
        if game[0] == title:
            return line_number
        line_number += 1
    raise ValueError

def sort_abc(file_name = "game_stat.txt"):
    games = load(file_name)
    titles = []
    for game in games:
        titles.append(game[0])
    return sorted(titles)

def get_genres(file_name = "game_stat.txt"):
    games = load(file_name)
    genres = []
    for game in games:
        if game[3] not in genres:
            genres.append(game[3])
    return genres

def when_was_top_sold_fps(file_name = "game_stat.txt"):
    games = load(file_name)
    sold_number = 0
    for game in games:
        if game[3] == "First-person shooter":
            if float(game[1]) > sold_number:
                sold_number = float(game[1])
                date = game[2]
    if sold_number == 0:
        raise ValueError
    return int(date)
