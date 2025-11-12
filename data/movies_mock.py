# data/movies_mock.py
# Mock extendido con muchas películas reales (usando posters de TMDb)

movies_mock = [
    # --- ACCIÓN ---
    {
        "id": 1,
        "title": "Inception",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg",
        "description": "A skilled thief leads a team into dreams to steal secrets.",
    },
    {
        "id": 2,
        "title": "The Dark Knight",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "description": "Batman faces the Joker in Gotham City.",
    },
    {
        "id": 3,
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg",
        "description": "In a post-apocalyptic wasteland, Max helps a rebel warrior.",
    },
    {
        "id": 4,
        "title": "Gladiator",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
        "description": "A betrayed Roman general fights for revenge and freedom.",
    },
    {
        "id": 5,
        "title": "John Wick",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg",
        "description": "An ex-hitman seeks vengeance after losing everything.",
    },
    {
        "id": 6,
        "title": "Avengers: Endgame",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/ulzhLuWrPK07P1YkdWQLZnQh1JL.jpg",
        "description": "The Avengers unite for one last stand.",
    },
    {
        "id": 7,
        "title": "Top Gun: Maverick",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg",
        "description": "Maverick faces the future while training a new generation of pilots.",
    },

    # --- CIENCIA FICCIÓN ---
    {
        "id": 8,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
        "description": "A team travels through a wormhole to save humanity.",
    },
    {
        "id": 9,
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "description": "A hacker discovers a shocking truth about his reality.",
    },
    {
        "id": 10,
        "title": "Blade Runner 2049",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/aMpyrCizvSztTu1Pe3YzKJRhfaJ.jpg",
        "description": "A young blade runner uncovers secrets about humanity's future.",
    },
    {
        "id": 11,
        "title": "Dune",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
        "description": "A noble family fights for control of the desert planet Arrakis.",
    },
    {
        "id": 12,
        "title": "Avatar",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg",
        "description": "A marine on an alien planet becomes torn between two worlds.",
    },

    # --- TERROR ---
    {
        "id": 13,
        "title": "The Conjuring",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg",
        "description": "Paranormal investigators face a haunted farmhouse.",
    },
    {
        "id": 14,
        "title": "Get Out",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/1SwAVYpuLj8KsHxllTF8Dt9dSSX.jpg",
        "description": "A young man uncovers disturbing secrets about his girlfriend's family.",
    },
    {
        "id": 15,
        "title": "Hereditary",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg",
        "description": "A family is haunted by sinister secrets after a tragedy.",
    },
    {
        "id": 16,
        "title": "It",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg",
        "description": "A group of kids face a terrifying entity in their town.",
    },
    {
        "id": 17,
        "title": "A Quiet Place",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg",
        "description": "A family must live in silence to survive deadly creatures.",
    },

    # --- ANIMACIÓN ---
    {
        "id": 18,
        "title": "Toy Story 4",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/w9kR8qbmQ01HwnvK4alvnQ2ca0L.jpg",
        "description": "Woody and Buzz embark on a new adventure.",
    },
    {
        "id": 19,
        "title": "Spider-Man: Into the Spider-Verse",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg",
        "description": "Teen Miles Morales becomes Spider-Man in another dimension.",
    },
    {
        "id": 20,
        "title": "Coco",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg",
        "description": "A boy journeys to the Land of the Dead to find his family.",
    },
    {
        "id": 21,
        "title": "Up",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/49L3Sjt5G6Z2Y4HhUZmM0t0EBQm.jpg",
        "description": "An old man and a young boy go on a floating house adventure.",
    },
    {
        "id": 22,
        "title": "Zootopia",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg",
        "description": "A rookie bunny cop and a cynical fox uncover a conspiracy.",
    },

    # --- COMEDIA ---
    {
        "id": 23,
        "title": "The Hangover",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/kfX8Ctin3fSZbdnjh6CXSNZUOVP.jpg",
        "description": "Four friends wake up from a bachelor party with no memory.",
    },
    {
        "id": 24,
        "title": "Superbad",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg",
        "description": "Two friends try to score alcohol for a party.",
    },
    {
        "id": 25,
        "title": "21 Jump Street",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/8v3UX3dp9w1uJbbzA1gNRIFTLm0.jpg",
        "description": "Two cops go undercover at a high school.",
    },
    {
        "id": 26,
        "title": "Ted",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/kfkyALvHMYTonkwB5d2BvvVSMo6.jpg",
        "description": "A man’s teddy bear comes to life, with chaotic results.",
    },

    # --- DRAMA ---
    {
        "id": 27,
        "title": "Forrest Gump",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg",
        "description": "A simple man witnesses key moments in history.",
    },
    {
        "id": 28,
        "title": "Fight Club",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg",
        "description": "An office worker starts an underground fight club.",
    },
    {
        "id": 29,
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/hBcY0fE9pfXzvVaY4GKarweriG2.jpg",
        "description": "A banker imprisoned for murder forms a lasting friendship.",
    },
    {
        "id": 30,
        "title": "The Godfather",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
        "description": "The aging patriarch of a crime family transfers power to his son.",
    },

    # --- ACCIÓN ---
    {
        "id": 31,
        "title": "Mission: Impossible – Fallout",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/AkJQpZp9WoNdj7pLYSj1L0RcMMN.jpg",
        "description": "Ethan Hunt and his team race against time after a mission gone wrong.",
    },
    {
        "id": 32,
        "title": "Die Hard",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/yFihWxQcmqcaBR31QM6Y8gT6aYV.jpg",
        "description": "An NYPD officer tries to save his wife during a terrorist takeover.",
    },
    {
        "id": 33,
        "title": "The Bourne Identity",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/sq4QyUoUTrdZRk9d9y0ZqDnF1rO.jpg",
        "description": "A man with amnesia searches for his identity while being hunted.",
    },
    {
        "id": 34,
        "title": "Casino Royale",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/mgKfXDXmCjT1v6u4V7u0OZ1Q1pB.jpg",
        "description": "James Bond earns his license to kill and faces a dangerous banker.",
    },
    {
        "id": 35,
        "title": "The Equalizer",
        "genre": "Action",
        "poster": "https://image.tmdb.org/t/p/w500/2eQfjqlvPAxd9aLDs8DvsKLnfed.jpg",
        "description": "A quiet man uses his mysterious skills to help those in need.",
    },

    # --- CIENCIA FICCIÓN ---
    {
        "id": 36,
        "title": "Tenet",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/k68nPLbIST6NP96JmTxmZijEvCA.jpg",
        "description": "A secret agent manipulates time to prevent World War III.",
    },
    {
        "id": 37,
        "title": "Ex Machina",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/9goPEdj1r5D3XyL2rHdLrYfM2fv.jpg",
        "description": "A programmer tests a humanoid AI in a high-tech facility.",
    },
    {
        "id": 38,
        "title": "Edge of Tomorrow",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/uUHvlkLavotfGsNtosDy8ShsIYF.jpg",
        "description": "A soldier relives the same day fighting aliens over and over again.",
    },
    {
        "id": 39,
        "title": "Oblivion",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/eO3r38fwnhb58M1YgcjQBd3VNcp.jpg",
        "description": "A drone repairman discovers shocking truths about his mission.",
    },
    {
        "id": 40,
        "title": "The Fifth Element",
        "genre": "Sci-Fi",
        "poster": "https://image.tmdb.org/t/p/w500/fPtlCO1yQtnoLHOwKtWz7db6RGU.jpg",
        "description": "A taxi driver becomes humanity’s unlikely savior in a futuristic city.",
    },

    # --- TERROR ---
    {
        "id": 41,
        "title": "The Nun",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/sFC1ElvoKGdHJIWRpNB3xWJ9lJA.jpg",
        "description": "A priest and a novice confront a demonic nun in Romania.",
    },
    {
        "id": 42,
        "title": "The Babadook",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/8rN3HvO7f1W3IHLFqG2u9Oha8Jf.jpg",
        "description": "A mother and son are haunted by a sinister storybook entity.",
    },
    {
        "id": 43,
        "title": "The Ring",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/tf1mUo47gUUSK6VKo4Tz1d8rQhI.jpg",
        "description": "A journalist investigates a cursed videotape that kills viewers.",
    },
    {
        "id": 44,
        "title": "Insidious",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/fw1D0ZxJ1R2B7tOaPcXQhI8zMOB.jpg",
        "description": "A family looks for help when their son becomes possessed.",
    },
    {
        "id": 45,
        "title": "Midsommar",
        "genre": "Horror",
        "poster": "https://image.tmdb.org/t/p/w500/lcb7P21oTZn3sUo3h1LU1c46VTN.jpg",
        "description": "A couple joins a mysterious midsummer festival in Sweden.",
    },

    # --- ANIMACIÓN ---
    {
        "id": 46,
        "title": "Finding Nemo",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg",
        "description": "A clownfish crosses the ocean to find his missing son.",
    },
    {
        "id": 47,
        "title": "Shrek",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/2yYP0PQjG8zVqturh1BAqu2Tixl.jpg",
        "description": "An ogre's peaceful life is interrupted by fairy tale creatures.",
    },
    {
        "id": 48,
        "title": "The Lion King",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/2bXbqYdUdNVa8VIWXVfclP2ICtT.jpg",
        "description": "A young lion prince flees after tragedy and returns to reclaim his throne.",
    },
    {
        "id": 49,
        "title": "Ratatouille",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/t3vaWRPSf6WjDSamIkKDs1iQWna.jpg",
        "description": "A rat who dreams of becoming a chef teams up with a young cook.",
    },
    {
        "id": 50,
        "title": "Frozen",
        "genre": "Animation",
        "poster": "https://image.tmdb.org/t/p/w500/195JvvmRocUjk5rhfQAoyQ5u8C.jpg",
        "description": "A princess sets out to find her sister whose powers trapped their kingdom in ice.",
    },

    # --- COMEDIA ---
    {
        "id": 51,
        "title": "The 40-Year-Old Virgin",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/qEJgXk7eKxT8YxQjYgKJmRZC2Lv.jpg",
        "description": "A man in his forties tries to lose his virginity with the help of friends.",
    },
    {
        "id": 52,
        "title": "Step Brothers",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/9pEPlfTGBUdKQUkV2TgbHZQKcqB.jpg",
        "description": "Two middle-aged men become stepbrothers and must live together.",
    },
    {
        "id": 53,
        "title": "Crazy Rich Asians",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/1XxL4LJ5WHdrcYcihEZUCgNCpAw.jpg",
        "description": "A woman discovers her boyfriend belongs to an ultra-rich family.",
    },
    {
        "id": 54,
        "title": "Pitch Perfect",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/8vRTe3oD3tSGL2YgnB0NccsJ8W7.jpg",
        "description": "A college student joins an all-girl a cappella group.",
    },
    {
        "id": 55,
        "title": "The Truman Show",
        "genre": "Comedy",
        "poster": "https://image.tmdb.org/t/p/w500/bd4xG7v5C1Z1oeYZ4PEx4CnJTHX.jpg",
        "description": "A man discovers his entire life is a TV show broadcast to the world.",
    },

    # --- DRAMA ---
    {
        "id": 56,
        "title": "Whiplash",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/oPxnRhyAIzJKGUEdSiwTJQBaSxL.jpg",
        "description": "A jazz drummer pushes himself to the limit under a ruthless instructor.",
    },
    {
        "id": 57,
        "title": "The Social Network",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/n0ybibhJtQ5icDqTp8eRytcIHJx.jpg",
        "description": "The story behind Facebook’s creation and its controversial founders.",
    },
    {
        "id": 58,
        "title": "La La Land",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
        "description": "A jazz musician and an actress fall in love in Los Angeles.",
    },
    {
        "id": 59,
        "title": "Joker",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
        "description": "A struggling comedian descends into madness and crime.",
    },
    {
        "id": 60,
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "poster": "https://image.tmdb.org/t/p/w500/bczFUdB6t2YJ1Jc0Xx7F5G9rVxE.jpg",
        "description": "A father struggles to build a better life for his son.",
    }
]
