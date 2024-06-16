team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
tiam_time = team1_time + team2_time
time_avg = round(tiam_time / tasks_total, 1)
if (score1 > score2 or score1 == score2) and team1_time < team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif (score1 < score2 or score1 == score2) and team1_time > team2_time:
    challenge_result = "Победа команды Волшебники Данных!!"
else:
    challenge_result = "Ничья!"
print("B команде Мастера кода участников %s!" %(team1_num ))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда Волшебники Данных решила задач; {}!".format(score2))
print("Волшебники Данных решили задачи за {} с!".format(team2_time))
print(f"Команды решили {score1} и {score2} задачи!")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!")
