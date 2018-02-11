from reports import *

text_file = open("wyniki.txt", "w")

answers = []

answers.append(str(count_games()))
answers.append("\n")
answers.append(str(decide()))
answers.append("\n")
answers.append(str(get_latest()))
answers.append("\n")
answers.append(str(count_by_genre()))
answers.append("\n")
answers.append(str(get_line_number_by_title()))
answers.append("\n")
answers.append(str(sort_abc()))
answers.append("\n")
answers.append(str(get_genres()))
answers.append("\n")
answers.append(str(when_was_top_sold_fps()))

text_file.writelines(answers)
text_file.close()
