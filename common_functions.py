import random

def get_random_quote():
    quotes = [
        "Życie jest jak jazda na rowerze. Żeby utrzymać równowagę, musisz być w ciągłym ruchu.",
        "Jedyną drogą do osiągnięcia niemożliwego jest uwierzyć, że jest możliwe.",
        "Sukces to suma małych wysiłków, powtarzanych dzień po dniu.",
        "Nie licz dni, spraw by dni się liczyły.",
        "Najlepszym sposobem przewidzenia przyszłości jest jej tworzenie."
    ]
    return random.choice(quotes)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)