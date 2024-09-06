import csv
from datetime import datetime

class SteamGame:
    def __init__(self, app_id, name, release_date, estimated_owners, peak_ccu, required_age, price, dlc_count, about_the_game, supported_languages, full_audio_languages, reviews, header_image, website, support_url, support_email, windows, mac, linux, metacritic_score, metacritic_url, user_score, positive, negative, score_rank, achievements, recommendations, notes, average_playtime_forever, median_playtime_forever, average_playtime_2_weeks, median_playtime_2_weeks, developers, publishers, categories, genres, tags, screenshots, movies):
        self.app_id = app_id
        self.name = name

        try:
            self.release_date = datetime.strptime(release_date, '%b %d, %Y') if release_date else None
        except ValueError:
            self.release_date = None
        self.estimated_owners = int(estimated_owners) if estimated_owners.isdigit() else 0
        self.peak_ccu = int(peak_ccu) if peak_ccu.isdigit() else 0
        self.required_age = int(required_age) if required_age.isdigit() else 0
        self.price = float(price)
        self.dlc_count = int(dlc_count) if dlc_count.isdigit() else 0
        self.about_the_game = about_the_game
        self.supported_languages = supported_languages.split(',') if supported_languages else []
        self.full_audio_languages = full_audio_languages.split(',') if full_audio_languages else []
        self.reviews = reviews
        self.header_image = header_image
        self.website = website
        self.support_url = support_url
        self.support_email = support_email
        self.windows = windows == 'True'
        self.mac = mac == 'True'
        self.linux = linux == 'True'
        self.metacritic_score = int(metacritic_score) if metacritic_score.isdigit() else None
        self.metacritic_url = metacritic_url
        self.user_score = float(user_score) if user_score else None
        self.positive = int(positive) if positive.isdigit() else 0
        self.negative = int(negative) if negative.isdigit() else 0
        self.score_rank = int(score_rank) if score_rank.isdigit() else None
        self.achievements = int(achievements) if achievements.isdigit() else 0
        self.recommendations = int(recommendations) if recommendations.isdigit() else 0
        self.notes = notes
        self.average_playtime_forever = int(average_playtime_forever) if average_playtime_forever.isdigit() else 0
        self.median_playtime_forever = int(median_playtime_forever) if median_playtime_forever.isdigit() else 0
        self.average_playtime_2_weeks = int(average_playtime_2_weeks) if average_playtime_2_weeks.isdigit() else 0
        self.median_playtime_2_weeks = int(median_playtime_2_weeks) if median_playtime_2_weeks.isdigit() else 0
        self.developers = developers.split(',') if developers else []
        self.publishers = publishers.split(',') if publishers else []
        self.categories = categories.split(',') if categories else []
        self.genres = genres.split(',') if genres else []
        self.tags = tags.split(',') if tags else []
        self.screenshots = screenshots.split(',') if screenshots else []
        self.movies = movies.split(',') if movies else []

class SteamGame:
    def __init__(self, row):
        self.app_id = row[0]
        self.name = row[1]
        try:
            self.release_date = datetime.strptime(row[2], '%b %d, %Y') if row[2] else None
        except ValueError:
            self.release_date = None
        self.price = float(row[6]) if row[6] else 0.0
        self.genres = row[34].split(',') if row[34] else []
        self.average_playtime_forever = int(row[30]) if row[30] else 0  # Campo para tempo médio de jogo

# Classe para gerenciar a análise de jogos
class SteamGames:
    def __init__(self, file_path):
        self.file_path = file_path
        self.games = []

    def load_games(self):
        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Pular o cabeçalho
            for row in reader:
                game = SteamGame(row)
                self.games.append(game)

    def get_games_percentage(self):
        total_games = len(self.games)
        if total_games == 0:
            return {"free": 0, "paid": 0}

        free_games = len([game for game in self.games if game.price == 0.00])
        paid_games = total_games - free_games

        free_percentage = (free_games / total_games) * 100
        paid_percentage = (paid_games / total_games) * 100

        return {"free": free_percentage, "paid": paid_percentage}

    def get_year_with_most_new_games(self):
        games_by_year = {}
        for game in self.games:
            if game.release_date:
                year = game.release_date.year
                if year not in games_by_year:
                    games_by_year[year] = 0
                games_by_year[year] += 1
        max_year = max(games_by_year, key=games_by_year.get)
        return [year for year, count in games_by_year.items() if count == games_by_year[max_year]]

    def get_most_common_genre(self):
        genres = {}
        for game in self.games:
            for genre in game.genres:
                genre = genre.strip()
                if genre not in genres:
                    genres[genre] = 0
                genres[genre] += 1
        max_genre = max(genres, key=genres.get)
        return max_genre

    def get_average_playtime(self):
        total_playtime = sum(game.average_playtime_forever for game in self.games)
        total_games = len(self.games)
        if total_games == 0:
            return 0
        return total_playtime / total_games