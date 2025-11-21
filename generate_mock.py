import requests

API_KEY = "0408518476f66efbff48d2d5a5530635"
BASE = "https://api.themoviedb.org/3"
IMG_POSTER = "https://image.tmdb.org/t/p/w500"
IMG_BACKDROP = "https://image.tmdb.org/t/p/w1280"

# -------------------------------------------
#  Tus 300 títulos
# -------------------------------------------
titles = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "The Matrix",
    "Avatar",
    "Titanic",
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather Part II",
    "The Dark Knight Rises",
    "Fight Club",
    "Forrest Gump",
    "Pulp Fiction",
    "The Social Network",
    "The Wolf of Wall Street",
    "Joker",
    "The Avengers",
    "Avengers: Endgame",
    "Avengers: Infinity War",
    "Guardians of the Galaxy",
    "Iron Man",
    "Iron Man 2",
    "Iron Man 3",
    "Captain America: The Winter Soldier",
    "Captain America: Civil War",
    "Thor: Ragnarok",
    "Black Panther",
    "Doctor Strange",
    "Spider-Man: Homecoming",
    "Spider-Man: Far From Home",
    "Spider-Man: No Way Home",
    "Dune",
    "Dune: Part Two",
    "Mad Max: Fury Road",
    "Blade Runner 2049",
    "Blade Runner",
    "Oppenheimer",
    "The Hunger Games",
    "The Hunger Games: Catching Fire",
    "The Hunger Games: Mockingjay - Part 1",
    "The Hunger Games: Mockingjay - Part 2",
    "The Revenant",
    "The Martian",
    "Gravity",
    "Arrival",
    "Tenet",
    "Dunkirk",
    "The Prestige",
    "Memento",
    "Shutter Island",
    "Whiplash",
    "La La Land",
    "The Big Short",
    "The Hateful Eight",
    "Inglourious Basterds",
    "Django Unchained",
    "Kill Bill: Vol. 1",
    "Kill Bill: Vol. 2",
    "The Departed",
    "GoodFellas",
    "The Irishman",
    "Casino",
    "Scarface",
    "Heat",
    "Saving Private Ryan",
    "1917",
    "Hacksaw Ridge",
    "The Imitation Game",
    "The Theory of Everything",
    "Bohemian Rhapsody",
    "Elvis",
    "Rocketman",
    "The Curious Case of Benjamin Button",
    "Se7en",
    "Zodiac",
    "Gone Girl",
    "The Girl with the Dragon Tattoo",
    "The Butterfly Effect",
    "A Beautiful Mind",
    "The Truman Show",
    "The Pursuit of Happyness",
    "Cast Away",
    "The Terminal",
    "The Green Mile",
    "Catch Me If You Can",
    "The Pianist",
    "Schindler's List",
    "The Hurt Locker",
    "American Sniper",
    "Zero Dark Thirty",
    "The Bourne Identity",
    "The Bourne Supremacy",
    "The Bourne Ultimatum",
    "No Time to Die",
    "Skyfall",
    "Spectre",
    "Casino Royale",
    "John Wick",
    "John Wick: Chapter 2",
    "John Wick: Chapter 3 - Parabellum",
    "John Wick: Chapter 4",
    "Mission: Impossible - The Final Reckoning",
    "Mission: Impossible - Fallout",
    "Mission: Impossible - Rogue Nation",
    "Top Gun",
    "Top Gun: Maverick",
    "Fast & Furious",
    "Fast Five",
    "Furious 7",
    "The Fate of the Furious",
    "Baby Driver",
    "Drive",
    "The Equalizer",
    "The Equalizer 2",
    "The Accountant",
    "The Nice Guys",
    "Superbad",
    "The Hangover",
    "The Hangover Part II",
    "The Hangover Part III",
    "21 Jump Street",
    "22 Jump Street",
    "Deadpool",
    "Deadpool 2",
    "Logan",
    "X-Men: Apocalypse",
    "X2",
    "X-Men: First Class",
    "The Wolverine",
    "The Incredible Hulk",
    "Hulk",
    "Man of Steel",
    "Batman Begins",
    "The Batman",
    "The Flash",
    "Aquaman",
    "Wonder Woman",
    "Wonder Woman 1984",
    "Shazam!",
    "The Suicide Squad",
    "Suicide Squad",
    "Bird Box",
    "A Quiet Place",
    "A Quiet Place Part II",
    "The Conjuring",
    "The Conjuring 2",
    "The Conjuring: The Devil Made Me Do It",
    "Annabelle",
    "Annabelle: Creation",
    "Annabelle Comes Home",
    "Insidious",
    "Insidious: Chapter 2",
    "Insidious: The Red Door",
    "The Nun",
    "The Nun II",
    "The Ring",
    "The Grudge",
    "Paranormal Activity",
    "Barbarian",
    "Smile",
    "It",
    "It Chapter Two",
    "Hereditary",
    "Midsommar",
    "Get Out",
    "Us",
    "Nope",
    "Split",
    "Glass",
    "Unbreakable",
    "The Sixth Sense",
    "Old",
    "Shrek",
    "Shrek 2",
    "Shrek the Third",
    "Shrek Forever After",
    "Puss in Boots",
    "Puss in Boots: The Last Wish",
    "Kung Fu Panda",
    "Kung Fu Panda 2",
    "Kung Fu Panda 3",
    "How to Train Your Dragon",
    "How to Train Your Dragon 2",
    "How to Train Your Dragon: The Hidden World",
    "Toy Story",
    "Toy Story 2",
    "Toy Story 3",
    "Toy Story 4",
    "Cars",
    "Cars 2",
    "Cars 3",
    "Finding Nemo",
    "Finding Dory",
    "Up",
    "Inside Out",
    "Coco",
    "Ratatouille",
    "Monsters, Inc.",
    "Monsters University",
    "Elemental",
    "Frozen",
    "Frozen II",
    "Moana",
    "Encanto",
    "Zootopia",
    "The Lion King",
    "Aladdin",
    "Beauty and the Beast",
    "The Little Mermaid",
    "Mulan",
    "Tangled",
    "Big Hero 6",
    "Wreck-It Ralph",
    "Ralph Breaks the Internet",
    "The Lego Movie",
    "The Lego Batman Movie",
    "The Lego Movie 2: The Second Part",
    "Minions",
    "Despicable Me",
    "Despicable Me 2",
    "Despicable Me 3",
    "The Secret Life of Pets",
    "The Secret Life of Pets 2",
    "Sing",
    "Sing 2",
    "The Super Mario Bros. Movie",
    "Pokémon Detective Pikachu",
    "Sonic the Hedgehog",
    "Sonic the Hedgehog 2",
    "Ready Player One",
    "Pacific Rim",
    "Pacific Rim: Uprising",
    "Transformers",
    "Transformers: Revenge of the Fallen",
    "Transformers: Dark of the Moon",
    "Transformers: Age of Extinction",
    "Transformers: The Last Knight",
    "Bumblebee",
    "Jurassic Park",
    "The Lost World: Jurassic Park",
    "Jurassic Park III",
    "Jurassic World: Fallen Kingdom",
    "Jurassic World Dominion"
]
# --------------------------------------------

def search_movie(title):
    url = f"{BASE}/search/movie?api_key={API_KEY}&query={title}"
    res = requests.get(url).json()
    return res["results"][0] if res.get("results") else None

def get_movie(movie_id):
    url = f"{BASE}/movie/{movie_id}?api_key={API_KEY}"
    return requests.get(url).json()

def format_runtime(minutes):
    if not minutes:
        return "Unknown"
    return f"{minutes//60}h {minutes%60}m"

movies = []   # LISTA FINAL
counter = 1

for title in titles:
    print(f"⏳ Buscando: {title}")
    result = search_movie(title)
    if not result:
        print(f"❌ No encontrado → {title}")
        continue

    movie = get_movie(result["id"])

    poster = IMG_POSTER + movie["poster_path"] if movie.get("poster_path") else ""
    backdrop = IMG_BACKDROP + movie["backdrop_path"] if movie.get("backdrop_path") else ""

    genre = movie["genres"][0]["name"] if movie.get("genres") else "Unknown"
    year = movie.get("release_date", "0000")[:4]
    runtime = format_runtime(movie.get("runtime"))
    description = movie.get("overview", "").replace('"', "'")

    movies.append({
        "id": counter,
        "title": title,
        "year": int(year),
        "runtime": runtime,
        "genre": genre,
        "description": description,
        "poster": poster,
        "backdrop": backdrop,
    })

    counter += 1
    print(f"✔️ Añadida: {title}")

# -----------------------------------------------
#   Crear archivo movies_mock.py formateado
# -----------------------------------------------

output = "movies_mock = [\n"

for m in movies:
    output += "    {\n"
    output += f'        "id": {m["id"]},\n'
    output += f'        "title": "{m["title"]}",\n'
    output += f'        "year": {m["year"]},\n'
    output += f'        "runtime": "{m["runtime"]}",\n'
    output += f'        "genre": "{m["genre"]}",\n'
    output += '        "description": (\n'
    output += f'            "{m["description"]}"\n'
    output += "        ),\n"
    output += f'        "poster": "{m["poster"]}",\n'
    output += f'        "backdrop": "{m["backdrop"]}",\n'
    output += "    },\n"

output += "]\n"

with open("movies_mock.py", "w", encoding="utf-8") as f:
    f.write(output)

print("\n🎉 Archivo 'movies_mock3.py' generado con éxito (LISTA).")
