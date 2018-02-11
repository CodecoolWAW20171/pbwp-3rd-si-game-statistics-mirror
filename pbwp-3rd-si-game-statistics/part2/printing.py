from reports import *

print(get_most_played(), "\n",
      round(sum_sold(),3), "\n",
      get_selling_avg(), "\n",
      count_longest_title(), "\n",
      get_date_avg(), "\n",
      get_game(file_name = "game_stat.txt", title = "Diablo III" ),
      "\n",
      count_grouped_by_genre(), "\n",
      get_date_ordered(), "\n")
