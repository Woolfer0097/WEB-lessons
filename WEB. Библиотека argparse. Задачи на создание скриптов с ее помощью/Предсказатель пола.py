import argparse


movies = {
    "melodrama": 0,
    "football": 100,
    "other": 50
}

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--cars', metavar='cars', nargs='?', default=50)
parser.add_argument('--barbie', metavar='barbie', nargs='?', default=50)
parser.add_argument('--movie', metavar='movie', nargs='?', default="other")


args = parser.parse_args()
barbie, cars, movie = int(args.barbie), int(args.cars), movies[args.movie]
if barbie > 100 or barbie < 0:
    barbie = 50
if cars > 100 or cars < 0:
    cars = 50
boy = int((100 - barbie + cars + movie) / 3)
girl = (100 - int(boy))
print(f"boy: {int(boy)}\ngirl: {round(girl)}")
