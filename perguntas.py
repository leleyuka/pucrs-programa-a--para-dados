from programa import SteamGames

steam_games = SteamGames('steam_games_sample.csv')
steam_games.load_games()


percentages = steam_games.get_games_percentage()
print("Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?")
print(f"Resposta: Gratuitos: {percentages['free']:.2f}%, Pagos: {percentages['paid']:.2f}%\n")

years = steam_games.get_year_with_most_new_games()
print("Pergunta 2: Qual o ano com o maior número de novos jogos?")
print(f"Resposta: {years}\n")

common_genre = steam_games.get_most_common_genre()
print("Pergunta 3: Qual é o gênero de jogo mais comum na plataforma?")
print(f"Resposta: {common_genre}\n")

print(f"Pergunta 4: Qual o tempo médio de jogo (em horas)?")
print(f"Resposta: {steam_games.get_average_playtime():.2f} horas\n")