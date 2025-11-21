movies_mock = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "runtime": "2h 28m",
        "genre": "Action",
        "description": (
            "Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets is offered a chance to regain his old life as payment for a task considered to be impossible: 'inception', the implantation of another person's idea into a target's subconscious."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ii8QGacT3MXESqBckQlyrATY0lT.jpg",
    },
    {
        "id": 2,
        "title": "The Dark Knight",
        "year": 2008,
        "runtime": "2h 32m",
        "genre": "Drama",
        "description": (
            "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/dqK9Hag1054tghRQSqLSfrkvQnA.jpg",
    },
    {
        "id": 3,
        "title": "Interstellar",
        "year": 2014,
        "runtime": "2h 49m",
        "genre": "Adventure",
        "description": (
            "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5XNQBqnBwPA9yT0jZ0p3s8bbLh0.jpg",
    },
    {
        "id": 4,
        "title": "The Matrix",
        "year": 1999,
        "runtime": "2h 16m",
        "genre": "Action",
        "description": (
            "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/p96dm7sCMn4VYAStA6siNz30G1r.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/tlm8UkiQsitc8rSuIAscQDCnP8d.jpg",
    },
    {
        "id": 5,
        "title": "Avatar",
        "year": 2009,
        "runtime": "2h 42m",
        "genre": "Action",
        "description": (
            "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gKY6q7SjCkAU6FqvqWybDYgUKIF.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7JNzw1tSZZEgsBw6lu0VfO2X2Ef.jpg",
    },
    {
        "id": 6,
        "title": "Titanic",
        "year": 1997,
        "runtime": "3h 14m",
        "genre": "Drama",
        "description": (
            "101-year-old Rose DeWitt Bukater tells the story of her life aboard the Titanic, 84 years later. A young Rose boards the ship with her mother and fiancé. Meanwhile, Jack Dawson and Fabrizio De Rossi win third-class tickets aboard the ship. Rose tells the whole story from Titanic's departure through to its death—on its first and last voyage—on April 15, 1912."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xXCuto8YVp5RFqBJ7yKmVmLOWpF.jpg",
    },
    {
        "id": 7,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "runtime": "2h 22m",
        "genre": "Drama",
        "description": (
            "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg",
    },
    {
        "id": 8,
        "title": "The Godfather",
        "year": 1972,
        "runtime": "2h 55m",
        "genre": "Drama",
        "description": (
            "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
    },
    {
        "id": 9,
        "title": "The Godfather Part II",
        "year": 1974,
        "runtime": "3h 22m",
        "genre": "Drama",
        "description": (
            "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ecBRkXerAZqRRUfR8Lt3L3Dh6J5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
    },
    {
        "id": 10,
        "title": "The Dark Knight Rises",
        "year": 2012,
        "runtime": "2h 45m",
        "genre": "Action",
        "description": (
            "Following the death of District Attorney Harvey Dent, Batman assumes responsibility for Dent's crimes to protect the late attorney's reputation and is subsequently hunted by the Gotham City Police Department. Eight years later, Batman encounters the mysterious Selina Kyle and the villainous Bane, a new terrorist leader who overwhelms Gotham's finest. The Dark Knight resurfaces to protect a city that has branded him an enemy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hr0L2aueqlP2BYUblTTjmtn0hw4.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/c3OHQncTAnKFhdOTX7D3LTW6son.jpg",
    },
    {
        "id": 11,
        "title": "Fight Club",
        "year": 1999,
        "runtime": "2h 19m",
        "genre": "Drama",
        "description": (
            "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground 'fight clubs' forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5TiwfWEaPSwD20uwXjCTUqpQX70.jpg",
    },
    {
        "id": 12,
        "title": "Forrest Gump",
        "year": 1994,
        "runtime": "2h 22m",
        "genre": "Comedy",
        "description": (
            "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/67HggiWaP9ZLv5sPYmyRV37yAJM.jpg",
    },
    {
        "id": 13,
        "title": "Pulp Fiction",
        "year": 1994,
        "runtime": "2h 34m",
        "genre": "Thriller",
        "description": (
            "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vQWk5YBFWF4bZaofAbv0tShwBvQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg",
    },
    {
        "id": 14,
        "title": "The Social Network",
        "year": 2010,
        "runtime": "2h 1m",
        "genre": "Drama",
        "description": (
            "In 2003, Harvard undergrad and computer programmer Mark Zuckerberg begins work on a new concept that eventually turns into the global social network known as Facebook. Six years later, Mark is one of the youngest billionaires ever, but his unprecedented success leads to both personal and legal complications when he ends up on the receiving end of two lawsuits, one involving his former friend."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/n0ybibhJtQ5icDqTp8eRytcIHJx.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/65D7t8wgZFpjOTvIp1HQvHFY0fC.jpg",
    },
    {
        "id": 15,
        "title": "The Wolf of Wall Street",
        "year": 2013,
        "runtime": "3h 0m",
        "genre": "Crime",
        "description": (
            "A New York stockbroker refuses to cooperate in a large securities fraud case involving corruption on Wall Street, corporate banking world and mob infiltration. Based on Jordan Belfort's autobiography."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/kW9LmvYHAaS9iA0tHmZVq8hQYoq.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7Nwnmyzrtd0FkcRyPqmdzTPppQa.jpg",
    },
    {
        "id": 16,
        "title": "Joker",
        "year": 2019,
        "runtime": "2h 2m",
        "genre": "Crime",
        "description": (
            "During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gZWl93sf8AxavYpVT1Un6EF3oCj.jpg",
    },
    {
        "id": 17,
        "title": "The Avengers",
        "year": 2012,
        "runtime": "2h 23m",
        "genre": "Science Fiction",
        "description": (
            "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!"
        ),
        "poster": "https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg",
    },
    {
        "id": 18,
        "title": "Avengers: Endgame",
        "year": 2019,
        "runtime": "3h 1m",
        "genre": "Adventure",
        "description": (
            "After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos' actions and restore order to the universe once and for all, no matter what consequences may be in store."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bR8ISy1O9XQxqiy0fQFw2BX72RQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9wXPKruA6bWYk2co5ix6fH59Qr8.jpg",
    },
    {
        "id": 19,
        "title": "Avengers: Infinity War",
        "year": 2018,
        "runtime": "2h 29m",
        "genre": "Adventure",
        "description": (
            "As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment - the fate of Earth and existence itself has never been more uncertain."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mDfJG3LC3Dqb67AZ52x3Z0jU0uB.jpg",
    },
    {
        "id": 20,
        "title": "Guardians of the Galaxy",
        "year": 2014,
        "runtime": "2h 1m",
        "genre": "Action",
        "description": (
            "Light years from Earth, 26 years after being abducted, Peter Quill finds himself the prime target of a manhunt after discovering an orb wanted by Ronan the Accuser."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/uLtVbjvS1O7gXL8lUOwsFOH4man.jpg",
    },
    {
        "id": 21,
        "title": "Iron Man",
        "year": 2008,
        "runtime": "2h 6m",
        "genre": "Action",
        "description": (
            "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/cKvDv2LpwVEqbdXWoQl4XgGN6le.jpg",
    },
    {
        "id": 22,
        "title": "Iron Man 2",
        "year": 2010,
        "runtime": "2h 4m",
        "genre": "Adventure",
        "description": (
            "With the world now aware of his dual life as the armored superhero Iron Man, billionaire inventor Tony Stark faces pressure from the government, the press and the public to share his technology with the military. Unwilling to let go of his invention, Stark, with Pepper Potts and James 'Rhodey' Rhodes at his side, must forge new alliances – and confront powerful enemies."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6WBeq4fCfn7AN0o21W9qNcRF2l9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7lmBufEG7P7Y1HClYK3gCxYrkgS.jpg",
    },
    {
        "id": 23,
        "title": "Iron Man 3",
        "year": 2013,
        "runtime": "2h 10m",
        "genre": "Action",
        "description": (
            "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/qhPtAc1TKbMPqNvcdXSOn9Bn7hZ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/4TSqtluelcWByj8YZdqwzQVjI0O.jpg",
    },
    {
        "id": 24,
        "title": "Captain America: The Winter Soldier",
        "year": 2014,
        "runtime": "2h 16m",
        "genre": "Action",
        "description": (
            "After the cataclysmic events in New York with The Avengers, Steve Rogers, aka Captain America is living quietly in Washington, D.C. and trying to adjust to the modern world. But when a S.H.I.E.L.D. colleague comes under attack, Steve becomes embroiled in a web of intrigue that threatens to put the world at risk. Joining forces with the Black Widow, Captain America struggles to expose the ever-widening conspiracy while fighting off professional assassins sent to silence him at every turn. When the full scope of the villainous plot is revealed, Captain America and the Black Widow enlist the help of a new ally, the Falcon. However, they soon find themselves up against an unexpected and formidable enemy—the Winter Soldier."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tVFRpFw3xTedgPGqxW0AOI8Qhh0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/1RWLMyC9KcFfcaoViMiJGSSZzzr.jpg",
    },
    {
        "id": 25,
        "title": "Captain America: Civil War",
        "year": 2016,
        "runtime": "2h 27m",
        "genre": "Adventure",
        "description": (
            "Following the events of Age of Ultron, the collective governments of the world pass an act designed to regulate all superhuman activity. This polarizes opinion amongst the Avengers, causing two factions to side with Iron Man or Captain America, which causes an epic battle between former allies."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rAGiXaUfPzY7CDEyNKUofk3Kw2e.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/kvRT3GwcnqGHzPjXIVrVPhUix7Z.jpg",
    },
    {
        "id": 26,
        "title": "Thor: Ragnarok",
        "year": 2017,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "Thor is imprisoned on the other side of the universe and finds himself in a race against time to get back to Asgard to stop Ragnarok, the destruction of his home-world and the end of Asgardian civilization, at the hands of a powerful new threat, the ruthless Hela."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6G2fLCVm9fiLyHvBrccq6GSe2ih.jpg",
    },
    {
        "id": 27,
        "title": "Black Panther",
        "year": 2018,
        "runtime": "2h 15m",
        "genre": "Action",
        "description": (
            "King T'Challa returns home to the reclusive, technologically advanced African nation of Wakanda to serve as his country's new leader. However, T'Challa soon finds that he is challenged for the throne by factions within his own country as well as without. Using powers reserved to Wakandan kings, T'Challa assumes the Black Panther mantle to join with ex-girlfriend Nakia, the queen-mother, his princess-kid sister, members of the Dora Milaje (the Wakandan 'special forces') and an American secret agent, to prevent Wakanda from being dragged into a world war."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/b6ZJZHUdMEFECvGiDpJjlfUWela.jpg",
    },
    {
        "id": 28,
        "title": "Doctor Strange",
        "year": 2016,
        "runtime": "1h 55m",
        "genre": "Fantasy",
        "description": (
            "After his career is destroyed, a brilliant but arrogant surgeon gets a new lease on life when a sorcerer takes him under her wing and trains him to defend the world against evil."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xf8PbyQcR5ucXErmZNzdKR0s8ya.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3zvZ699gMW2RhWc0GisIukzq0Ls.jpg",
    },
    {
        "id": 29,
        "title": "Spider-Man: Homecoming",
        "year": 2017,
        "runtime": "2h 13m",
        "genre": "Action",
        "description": (
            "Following the events of Captain America: Civil War, Peter Parker, with the help of his mentor Tony Stark, tries to balance his life as an ordinary high school student in Queens, New York City, with fighting crime as his superhero alter ego Spider-Man as a new threat, the Vulture, emerges."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/fn4n6uOYcB6Uh89nbNPoU2w80RV.jpg",
    },
    {
        "id": 30,
        "title": "Spider-Man: Far From Home",
        "year": 2019,
        "runtime": "2h 9m",
        "genre": "Action",
        "description": (
            "Peter Parker and his friends go on a summer trip to Europe. However, they will hardly be able to rest - Peter will have to agree to help Nick Fury uncover the mystery of creatures that cause natural disasters and destruction throughout the continent."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/4q2NNj4S5dG2RLF9CpXsej7yXl.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/vamhMTvh9m9zFHDoR0v1nRtf6T4.jpg",
    },
    {
        "id": 31,
        "title": "Spider-Man: No Way Home",
        "year": 2021,
        "runtime": "2h 28m",
        "genre": "Action",
        "description": (
            "Peter Parker is unmasked and no longer able to separate his normal life from the high-stakes of being a super-hero. When he asks for help from Doctor Strange the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/tyQo080tijexyUHBvWPwQt26bZa.jpg",
    },
    {
        "id": 32,
        "title": "Dune",
        "year": 2021,
        "runtime": "2h 35m",
        "genre": "Science Fiction",
        "description": (
            "Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wYMbnrdRCREjNLwFlG5SLWzBjui.jpg",
    },
    {
        "id": 33,
        "title": "Dune: Part Two",
        "year": 2024,
        "runtime": "2h 47m",
        "genre": "Science Fiction",
        "description": (
            "Follow the mythic journey of Paul Atreides as he unites with Chani and the Fremen while on a path of revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe, Paul endeavors to prevent a terrible future only he can foresee."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xOMo8BRK7PfcJv9JCnx7s5hj0PX.jpg",
    },
    {
        "id": 34,
        "title": "Mad Max: Fury Road",
        "year": 2015,
        "runtime": "2h 1m",
        "genre": "Action",
        "description": (
            "An apocalyptic story set in the furthest reaches of our planet, in a stark desert landscape where humanity is broken, and most everyone is crazed fighting for the necessities of life. Within this world exist two rebels on the run who just might be able to restore order."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hA2ple9q4qnwxp3hKVNhroipsir.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/uT895WNwm0aIJRtGizcQhrejWUo.jpg",
    },
    {
        "id": 35,
        "title": "Blade Runner 2049",
        "year": 2017,
        "runtime": "2h 44m",
        "genre": "Science Fiction",
        "description": (
            "Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. K's discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for 30 years."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mVr0UiqyltcfqxbAUcLl9zWL8ah.jpg",
    },
    {
        "id": 36,
        "title": "Blade Runner",
        "year": 1982,
        "runtime": "1h 58m",
        "genre": "Science Fiction",
        "description": (
            "In the smog-choked dystopian Los Angeles of 2019, blade runner Rick Deckard is called out of retirement to terminate a quartet of replicants who have escaped to Earth seeking their creator for a way to extend their short life spans."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/63N9uy8nd9j7Eog2axPQ8lbr3Wj.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/cFZRtb1Q4whERknfYtj7Fjsvxpg.jpg",
    },
    {
        "id": 37,
        "title": "Oppenheimer",
        "year": 2023,
        "runtime": "3h 1m",
        "genre": "Drama",
        "description": (
            "The story of J. Robert Oppenheimer's role in the development of the atomic bomb during World War II."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ycnO0cjsAROSGJKuMODgRtWsHQw.jpg",
    },
    {
        "id": 38,
        "title": "The Hunger Games",
        "year": 2012,
        "runtime": "2h 22m",
        "genre": "Science Fiction",
        "description": (
            "In a dystopian society where the Capitol forces each district to send two young tributes to fight to the death in a televised spectacle, a girl volunteers to take her sister’s place, setting the stage for a struggle of survival and defiance."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/yXCbOiVDCxO71zI7cuwBRXdftq8.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3sndNmvdF0R8AeyCmVoNv8LKtNy.jpg",
    },
    {
        "id": 39,
        "title": "The Hunger Games: Catching Fire",
        "year": 2013,
        "runtime": "2h 26m",
        "genre": "Adventure",
        "description": (
            "After surviving the Hunger Games, Katniss and Peeta struggle with the consequences of their victory as unrest spreads across Panem. Forced back into the spotlight, they become symbols of hope and resistance while the Capitol prepares a new and deadly challenge that will change the future of the nation forever."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vrQHDXjVmbYzadOXQ0UaObunoy2.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/eHaazLxM5LRMh0ySkVy7SK6wUWt.jpg",
    },
    {
        "id": 40,
        "title": "The Hunger Games: Mockingjay - Part 1",
        "year": 2014,
        "runtime": "2h 3m",
        "genre": "Science Fiction",
        "description": (
            "After surviving the Quarter Quell, Katniss finds herself in the hidden stronghold of District 13, where the rebellion against the Capitol is gaining momentum. Struggling with the weight of becoming the symbol of resistance, she must navigate fragile alliances while trying to protect those she loves. As propaganda battles rage and Panem moves closer to full-scale war, Katniss is forced to confront the true cost of revolution."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/4FAA18ZIja70d1Tu5hr5cj2q1sB.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/lV1P1Q5gLDXVG1ZYCxZHStkcQC3.jpg",
    },
    {
        "id": 41,
        "title": "The Hunger Games: Mockingjay - Part 2",
        "year": 2015,
        "runtime": "2h 17m",
        "genre": "Action",
        "description": (
            "As the war between the Capitol and the districts reaches its peak, Katniss Everdeen embarks on a perilous mission to liberate Panem and confront President Snow. Joined by a team of trusted allies, she navigates deadly traps, shifting loyalties, and the heavy cost of rebellion, determined to bring freedom to her people and end the Hunger Games once and for all."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/lImKHDfExAulp16grYm8zD5eONE.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/qVgLMRVNB5bHU0inmRa0ueShacN.jpg",
    },
    {
        "id": 42,
        "title": "The Revenant",
        "year": 2015,
        "runtime": "2h 37m",
        "genre": "Western",
        "description": (
            "In the 1820s, a frontiersman, Hugh Glass, sets out on a path of vengeance against those who left him for dead after a bear mauling."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ji3ecJphATlVgWNY0B0RVXZizdf.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mNQtUJv1F3u0uSKILFrGjIHqkxx.jpg",
    },
    {
        "id": 43,
        "title": "The Martian",
        "year": 2015,
        "runtime": "2h 21m",
        "genre": "Drama",
        "description": (
            "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/3ndAx3weG6KDkJIRMCi5vXX6Dyb.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/sq8oUjbBvKkqv9h0Ns5rQbbquhZ.jpg",
    },
    {
        "id": 44,
        "title": "Gravity",
        "year": 2013,
        "runtime": "1h 31m",
        "genre": "Science Fiction",
        "description": (
            "Dr. Ryan Stone, a brilliant medical engineer, is on her first Shuttle mission, with veteran astronaut Matt Kowalsky in command of his last flight before retiring. But on a seemingly routine spacewalk, disaster strikes. The Shuttle is destroyed, leaving Stone and Kowalsky completely alone-tethered to nothing but each other and spiraling out into the blackness of space. The deafening silence tells them they have lost any link to Earth and any chance for rescue. As fear turns to panic, every gulp of air eats away at what little oxygen is left. But the only way home may be to go further out into the terrifying expanse of space."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/kZ2nZw8D681aphje8NJi8EfbL1U.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/a2n6bKD7qhCPCAEALgsAhWOAQcc.jpg",
    },
    {
        "id": 45,
        "title": "Arrival",
        "year": 2016,
        "runtime": "1h 56m",
        "genre": "Drama",
        "description": (
            "Taking place after alien crafts land around the world, an expert linguist is recruited by the military to determine whether they come in peace or are a threat."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/pEzNVQfdzYDzVK0XqxERIw2x2se.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hNCqkXbWd40eftqSdjq8TmV7Mqr.jpg",
    },
    {
        "id": 46,
        "title": "Tenet",
        "year": 2020,
        "runtime": "2h 30m",
        "genre": "Action",
        "description": (
            "Armed with only one word - Tenet - and fighting for the survival of the entire world, the Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aCIFMriQh8rvhxpN1IWGgvH0Tlg.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yY76zq9XSuJ4nWyPDuwkdV7Wt0c.jpg",
    },
    {
        "id": 47,
        "title": "Dunkirk",
        "year": 2017,
        "runtime": "1h 47m",
        "genre": "War",
        "description": (
            "The story of the miraculous evacuation of Allied soldiers from Belgium, Britain, Canada and France, who were cut off and surrounded by the German army from the beaches and harbour of Dunkirk between May 26th and June 4th 1940 during World War II."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/b4Oe15CGLL61Ped0RAS9JpqdmCt.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ddIkmH3TpR6XSc47jj0BrGK5Rbz.jpg",
    },
    {
        "id": 48,
        "title": "The Prestige",
        "year": 2006,
        "runtime": "2h 10m",
        "genre": "Drama",
        "description": (
            "A mysterious story of two magicians whose intense rivalry leads them on a life-long battle for supremacy -- full of obsession, deceit and jealousy with dangerous and deadly consequences."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bdN3gXuIZYaJP7ftKK2sU0nPtEA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yCnJT53HMXAK87xzPAdjdYhZ3JE.jpg",
    },
    {
        "id": 49,
        "title": "Memento",
        "year": 2000,
        "runtime": "1h 53m",
        "genre": "Mystery",
        "description": (
            "Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife's killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fKTPH2WvH8nHTXeBYBVhawtRqtR.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7Wev9JMo6R5XAfz2KDvXb7oPMmy.jpg",
    },
    {
        "id": 50,
        "title": "Shutter Island",
        "year": 2010,
        "runtime": "2h 18m",
        "genre": "Drama",
        "description": (
            "World War II soldier-turned-U.S. Marshal Teddy Daniels investigates the disappearance of a patient from a hospital for the criminally insane, but his efforts are compromised by troubling visions and a mysterious doctor."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/nrmXQ0zcZUL8jFLrakWc90IR8z9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rbZvGN1A1QyZuoKzhCw8QPmf2q0.jpg",
    },
    {
        "id": 51,
        "title": "Whiplash",
        "year": 2014,
        "runtime": "1h 47m",
        "genre": "Drama",
        "description": (
            "Under the direction of a ruthless instructor, a talented young drummer begins to pursue perfection at any cost, even his humanity."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7fn624j5lj3xTme2SgiLCeuedmO.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/1kuYEvLkX2nTkbfzN6X0w0xQFQU.jpg",
    },
    {
        "id": 52,
        "title": "La La Land",
        "year": 2016,
        "runtime": "2h 9m",
        "genre": "Comedy",
        "description": (
            "Mia, an aspiring actress, serves lattes to movie stars in between auditions and Sebastian, a jazz musician, scrapes by playing cocktail party gigs in dingy bars, but as success mounts they are faced with decisions that begin to fray the fragile fabric of their love affair, and the dreams they worked so hard to maintain in each other threaten to rip them apart."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nlPCdZlHtRNcF6C9hzUH4ebmV1w.jpg",
    },
    {
        "id": 53,
        "title": "The Big Short",
        "year": 2015,
        "runtime": "2h 11m",
        "genre": "Comedy",
        "description": (
            "The men who made millions from a global economic meltdown."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/scVEaJEwP8zUix8vgmMoJJ9Nq0w.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/l2Lqkfjq1k5pG2gZXD4qSiyrJ0.jpg",
    },
    {
        "id": 54,
        "title": "The Hateful Eight",
        "year": 2015,
        "runtime": "3h 8m",
        "genre": "Drama",
        "description": (
            "Bounty hunters seek shelter from a raging blizzard and get caught up in a plot of betrayal and deception."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/jIywvdPjia2t3eKYbjVTcwBQlG8.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7gfDVfaw0VaIkUGiEH13o3TIC7A.jpg",
    },
    {
        "id": 55,
        "title": "Inglourious Basterds",
        "year": 2009,
        "runtime": "2h 33m",
        "genre": "Drama",
        "description": (
            "In Nazi-occupied France during World War II, a group of Jewish-American soldiers known as 'The Basterds' are chosen specifically to spread fear throughout the Third Reich by scalping and brutally killing Nazis. The Basterds, lead by Lt. Aldo Raine soon cross paths with a French-Jewish teenage girl who runs a movie theater in Paris which is targeted by the soldiers."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7sfbEnaARXDDhKm0CZ7D7uc2sbo.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hwNtEmmugU5Yd7hpfprNWI0DGIn.jpg",
    },
    {
        "id": 56,
        "title": "Django Unchained",
        "year": 2012,
        "runtime": "2h 45m",
        "genre": "Drama",
        "description": (
            "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7oWY8VDWW7thTzWh3OKYRkWUlD5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5Lbm0gpFDRAPIV1Cth6ln9iL1ou.jpg",
    },
    {
        "id": 57,
        "title": "Kill Bill: Vol. 1",
        "year": 2003,
        "runtime": "1h 51m",
        "genre": "Action",
        "description": (
            "An assassin is shot by her ruthless employer, Bill, and other members of their assassination circle – but she lives to plot her vengeance."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/v7TaX8kXMXs5yFFGR41guUDNcnB.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/p3WiF8qYS7Qp17YRYgrFh7gf9P9.jpg",
    },
    {
        "id": 58,
        "title": "Kill Bill: Vol. 2",
        "year": 2004,
        "runtime": "2h 16m",
        "genre": "Action",
        "description": (
            "The Bride unwaveringly continues on her roaring rampage of revenge against the band of assassins who had tried to kill her and her unborn child. She visits each of her former associates one-by-one, checking off the victims on her Death List Five until there's nothing left to do … but kill Bill."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2yhg0mZQMhDyvUQ4rG1IZ4oIA8L.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/pgG6tzJzC8mjGqhaT8IWwEk00xf.jpg",
    },
    {
        "id": 59,
        "title": "The Departed",
        "year": 2006,
        "runtime": "2h 31m",
        "genre": "Drama",
        "description": (
            "To take down South Boston's Irish Mafia, the police send in one of their own to infiltrate the underworld, not realizing the syndicate has done likewise. While an undercover cop curries favor with the mob kingpin, a career criminal rises through the police ranks. But both sides soon discover there's a mole among them."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/nT97ifVT2J1yMQmeq20Qblg61T.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6WRrGYalXXveItfpnipYdayFkQB.jpg",
    },
    {
        "id": 60,
        "title": "GoodFellas",
        "year": 1990,
        "runtime": "2h 25m",
        "genre": "Drama",
        "description": (
            "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gILte6Zd7m1YneIr6MVhh30S9pr.jpg",
    },
    {
        "id": 61,
        "title": "The Irishman",
        "year": 2019,
        "runtime": "3h 29m",
        "genre": "Crime",
        "description": (
            "Pennsylvania, 1956. Frank Sheeran, a war veteran of Irish origin who works as a truck driver, accidentally meets mobster Russell Bufalino. Once Frank becomes his trusted man, Bufalino sends him to Chicago with the task of helping Jimmy Hoffa, a powerful union leader related to organized crime, with whom Frank will maintain a close friendship for nearly twenty years."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/mbm8k3GFhXS0ROd9AD1gqYbIFbM.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/1RDto0tLo8Fhq7OcwgDaM7nECb7.jpg",
    },
    {
        "id": 62,
        "title": "Casino",
        "year": 1995,
        "runtime": "2h 59m",
        "genre": "Crime",
        "description": (
            "In Las Vegas, two best friends--a casino executive and a Mafia enforcer--compete for a gambling empire and a fast-living, fast-loving socialite."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gziIkUSnYuj9ChCi8qOu2ZunpSC.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/iZGiMD0p1M2AOmzKknFo5bkuz94.jpg",
    },
    {
        "id": 63,
        "title": "Scarface",
        "year": 1983,
        "runtime": "2h 50m",
        "genre": "Action",
        "description": (
            "After getting a green card in exchange for assassinating a Cuban government official, Tony Montana stakes a claim on the drug trade in Miami. Viciously murdering anyone who stands in his way, Tony eventually becomes the biggest drug lord in the state, controlling nearly all the cocaine that comes through Miami. But increased pressure from the police, wars with Colombian drug cartels and his own drug-fueled paranoia serve to fuel the flames of his eventual downfall."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/iQ5ztdjvteGeboxtmRdXEChJOHh.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/sctvs9cUwJD15qlTlrsh2BXsK75.jpg",
    },
    {
        "id": 64,
        "title": "Heat",
        "year": 1995,
        "runtime": "2h 50m",
        "genre": "Crime",
        "description": (
            "Obsessive master thief Neil McCauley leads a top-notch crew on various daring heists throughout Los Angeles while determined detective Vincent Hanna pursues him without rest. Each man recognizes and respects the ability and the dedication of the other even though they are aware their cat-and-mouse game may end in violence."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/umSVjVdbVwtx5ryCA2QXL44Durm.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5JaR6UEoCJJLtLpqFOVMY4O4R7P.jpg",
    },
    {
        "id": 65,
        "title": "Saving Private Ryan",
        "year": 1998,
        "runtime": "2h 49m",
        "genre": "Drama",
        "description": (
            "As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held territory and bringing the boy home."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/uqx37cS8cpHg8U35f9U5IBlrCV3.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rW2xRFlJRbTnBJlQTSjQmjevIwb.jpg",
    },
    {
        "id": 66,
        "title": "1917",
        "year": 2019,
        "runtime": "1h 59m",
        "genre": "War",
        "description": (
            "At the height of the First World War, two young British soldiers must cross enemy territory and deliver a message that will stop a deadly attack on hundreds of soldiers."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/iZf0KyrE25z1sage4SYFLCCrMi9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/2WgieNR1tGHlpJUsolbVzbUbE1O.jpg",
    },
    {
        "id": 67,
        "title": "Hacksaw Ridge",
        "year": 2016,
        "runtime": "2h 19m",
        "genre": "Drama",
        "description": (
            "WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people and becomes the first Conscientious Objector in American history to receive the Congressional Medal of Honor."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/wuz8TjCIWR2EVVMuEfBnQ1vuGS3.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/vDKRMZGFTKP9nQolzeSB1rB1w6p.jpg",
    },
    {
        "id": 68,
        "title": "The Imitation Game",
        "year": 2014,
        "runtime": "1h 53m",
        "genre": "History",
        "description": (
            "Based on the real life story of legendary cryptanalyst Alan Turing, the film portrays the nail-biting race against time by Turing and his brilliant team of code-breakers at Britain's top-secret Government Code and Cypher School at Bletchley Park, during the darkest days of World War II."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/zSqJ1qFq8NXFfi7JeIYMlzyR0dx.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gLQoJ9P79g501oEEtrN8zMlCPpx.jpg",
    },
    {
        "id": 69,
        "title": "The Theory of Everything",
        "year": 2014,
        "runtime": "2h 3m",
        "genre": "Drama",
        "description": (
            "The Theory of Everything is the extraordinary story of one of the world’s greatest living minds, the renowned astrophysicist Stephen Hawking, who falls deeply in love with fellow Cambridge student Jane Wilde."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/kJuL37NTE51zVP3eG5aGMyKAIlh.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ke3lanTAgCqPMpOyutIfXzYih2s.jpg",
    },
    {
        "id": 70,
        "title": "Bohemian Rhapsody",
        "year": 2018,
        "runtime": "2h 15m",
        "genre": "Music",
        "description": (
            "Singer Freddie Mercury, guitarist Brian May, drummer Roger Taylor and bass guitarist John Deacon take the music world by storm when they form the rock 'n' roll band Queen in 1970. Hit songs become instant classics. When Mercury's increasingly wild lifestyle starts to spiral out of control, Queen soon faces its greatest challenge yet – finding a way to keep the band together amid the success and excess."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/lHu1wtNaczFPGFDTrjCSzeLPTKN.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7mmXWuBeNJiBO0NIOUWOuFve4Tb.jpg",
    },
    {
        "id": 71,
        "title": "Elvis",
        "year": 2022,
        "runtime": "2h 39m",
        "genre": "Drama",
        "description": (
            "The life story of Elvis Presley as seen through the complicated relationship with his enigmatic manager, Colonel Tom Parker."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/qBOKWqAFbveZ4ryjJJwbie6tXkQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rLo9T9jEg67UZPq3midjLnTUYYi.jpg",
    },
    {
        "id": 72,
        "title": "Rocketman",
        "year": 2019,
        "runtime": "2h 1m",
        "genre": "Music",
        "description": (
            "The story of Elton John's life, from his years as a prodigy at the Royal Academy of Music through his influential and enduring musical partnership with Bernie Taupin."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/f4FF18ia7yTvHf2izNrHqBmgH8U.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/isnJGDrfR9dIrHMsPTvHtJaGEpc.jpg",
    },
    {
        "id": 73,
        "title": "The Curious Case of Benjamin Button",
        "year": 2008,
        "runtime": "2h 46m",
        "genre": "Drama",
        "description": (
            "Born under unusual circumstances, Benjamin Button springs into being as an elderly man in a New Orleans nursing home and ages in reverse. Twelve years after his birth, he meets Daisy, a child who flits in and out of his life as she grows up to be a dancer. Though he has all sorts of unusual adventures over the course of his life, it is his relationship with Daisy, and the hope that they will come together at the right time, that drives Benjamin forward."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/26wEWZYt6yJkwRVkjcbwJEFh9IS.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/dgMdsBbGXp9h6sLsfqsM3texzym.jpg",
    },
    {
        "id": 74,
        "title": "Se7en",
        "year": 1995,
        "runtime": "2h 7m",
        "genre": "Crime",
        "description": (
            "Two homicide detectives are on a desperate hunt for a serial killer whose crimes are based on the 'seven deadly sins' in this dark and haunting film that takes viewers from the tortured remains of one victim to the next. The seasoned Det. Somerset researches each sin in an effort to get inside the killer's mind, while his novice partner, Mills, scoffs at his efforts to unravel the case."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/191nKfP0ehp3uIvWqgPbFmI4lv9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hkKTtlHjiVUW5XRfkQfl3FmJUfX.jpg",
    },
    {
        "id": 75,
        "title": "Zodiac",
        "year": 2007,
        "runtime": "2h 37m",
        "genre": "Crime",
        "description": (
            "The Zodiac murders cause the lives of Paul Avery, David Toschi and Robert Graysmith to intersect."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6YmeO4pB7XTh8P8F960O1uA14JO.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3zCPI4JFc54xvLaJ71oI2KoP3az.jpg",
    },
    {
        "id": 76,
        "title": "Gone Girl",
        "year": 2014,
        "runtime": "2h 29m",
        "genre": "Mystery",
        "description": (
            "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ts996lKsxvjkO2yiYG0ht4qAicO.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/iWak7wT0j6ycCc8lKr4NBz9c7n5.jpg",
    },
    {
        "id": 77,
        "title": "The Girl with the Dragon Tattoo",
        "year": 2011,
        "runtime": "2h 38m",
        "genre": "Thriller",
        "description": (
            "Disgraced journalist Mikael Blomkvist investigates the disappearance of a weary patriarch's niece from 40 years ago. He is aided by the pierced, tattooed, punk computer hacker named Lisbeth Salander. As they work together in the investigation, Blomkvist and Salander uncover immense corruption beyond anything they have ever imagined."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/8bokS83zGdhaXgN9tjidUKmAftW.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/dNFbrnF0mIBm0rClbfEFWTtsgMP.jpg",
    },
    {
        "id": 78,
        "title": "The Butterfly Effect",
        "year": 2004,
        "runtime": "1h 53m",
        "genre": "Science Fiction",
        "description": (
            "A young man struggles to access sublimated childhood memories. He finds a technique that allows him to travel back into the past, to occupy his childhood body and change history. However, he soon finds that every change he makes has unexpected consequences."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ea5iv7TWMh18fOKoRGgmtcg85Gx.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yriYPLqyFqPW0QXaegT1KmWXk9a.jpg",
    },
    {
        "id": 79,
        "title": "A Beautiful Mind",
        "year": 2001,
        "runtime": "2h 15m",
        "genre": "Drama",
        "description": (
            "From the heights of notoriety to the depths of depravity, John Forbes Nash Jr. experiences it all. As a brilliant but socially awkward mathematician, he made a groundbreaking discovery early in his career and stands on the brink of international acclaim. But as the handsome and arrogant Nash accepts secret work in cryptography, he becomes entangled in a mysterious conspiracy. His life takes a nightmarish turn and he soon finds himself on a painful and harrowing journey of self-discovery."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rEIg5yJdNOt9fmX4P8gU9LeNoTQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hCJFWTPghXCwwSpvPpAoIB8318Q.jpg",
    },
    {
        "id": 80,
        "title": "The Truman Show",
        "year": 1998,
        "runtime": "1h 43m",
        "genre": "Comedy",
        "description": (
            "An insurance salesman begins to suspect that his whole life is actually some sort of reality TV show."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rmiG2uwcNoGFmBKMoa1pIcf514L.jpg",
    },
    {
        "id": 81,
        "title": "The Pursuit of Happyness",
        "year": 2006,
        "runtime": "1h 57m",
        "genre": "Drama",
        "description": (
            "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional career."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/lBYOKAMcxIvuk9s9hMuecB9dPBV.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5jhG1lTgV0MS6tDkBMQSSitttTT.jpg",
    },
    {
        "id": 82,
        "title": "Cast Away",
        "year": 2000,
        "runtime": "2h 23m",
        "genre": "Adventure",
        "description": (
            "Chuck Noland, a top international manager for FedEx, and Kelly, a Ph.D. student, are in love and heading towards marriage. Then Chuck's plane to Malaysia crashes at sea during a terrible storm. He's the only survivor, and finds himself marooned on a desolate island. With no way to escape, Chuck must find ways to survive in his new home."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7lLJgKnAicAcR5UEuo8xhSMj18w.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ioqaIhJSkwa9DGRHGtOOUTiGRs2.jpg",
    },
    {
        "id": 83,
        "title": "The Terminal",
        "year": 2004,
        "runtime": "2h 8m",
        "genre": "Comedy",
        "description": (
            "An Eastern European tourist unexpectedly finds himself stranded in JFK airport, and must take up temporary residence there."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/cPB3ZMM4UdsSAhNdS4c7ps5nypY.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/zt3cmdZr3t0K64gzpwIc4LXiuDu.jpg",
    },
    {
        "id": 84,
        "title": "The Green Mile",
        "year": 1999,
        "runtime": "3h 9m",
        "genre": "Fantasy",
        "description": (
            "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/o0lO84GI7qrG6XFvtsPOSV7CTNa.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/b6HWTOxn1xevvyHU2K9ICvaRU6g.jpg",
    },
    {
        "id": 85,
        "title": "Catch Me If You Can",
        "year": 2002,
        "runtime": "2h 21m",
        "genre": "Drama",
        "description": (
            "A true story about Frank Abagnale Jr. who, before his 19th birthday, successfully conned millions of dollars worth of checks as a Pan Am pilot, doctor, and legal prosecutor. An FBI agent makes it his mission to put him behind bars. But Frank not only eludes capture, he revels in the pursuit."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sdYgEkKCDPWNU6KnoL4qd8xZ4w7.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/eS3xZQ1C8lt6mm4K5lTmjbYn2HE.jpg",
    },
    {
        "id": 86,
        "title": "The Pianist",
        "year": 2002,
        "runtime": "2h 30m",
        "genre": "Drama",
        "description": (
            "The true story of pianist Władysław Szpilman's experiences in Warsaw during the Nazi occupation. When the Jews of the city find themselves forced into a ghetto, Szpilman finds work playing in a café; and when his family is deported in 1942, he stays behind, works for a while as a laborer, and eventually goes into hiding in the ruins of the war-torn city."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2hFvxCCWrTmCYwfy7yum0GKRi3Y.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/1XqIhsqnAozznGhxlGdI0GPcCro.jpg",
    },
    {
        "id": 87,
        "title": "Schindler's List",
        "year": 1993,
        "runtime": "3h 15m",
        "genre": "Drama",
        "description": (
            "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/zb6fM1CX41D9rF9hdgclu0peUmy.jpg",
    },
    {
        "id": 88,
        "title": "The Hurt Locker",
        "year": 2008,
        "runtime": "2h 11m",
        "genre": "Drama",
        "description": (
            "During the Iraq War, a Sergeant recently assigned to an army bomb squad is put at odds with his squad mates due to his maverick way of handling his work."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/io2dfBJhasvGbgkCX9cCGVOiA99.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nKieVGBCZQfcylwO7mOMPaug8f2.jpg",
    },
    {
        "id": 89,
        "title": "American Sniper",
        "year": 2014,
        "runtime": "2h 13m",
        "genre": "War",
        "description": (
            "U.S. Navy SEAL Chris Kyle takes his sole mission—protect his comrades—to heart and becomes one of the most lethal snipers in American history. His pinpoint accuracy not only saves countless lives but also makes him a prime target of insurgents. Despite grave danger and his struggle to be a good husband and father to his family back in the States, Kyle serves four tours of duty in Iraq. However, when he finally returns home, he finds that he cannot leave the war behind."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/i1U46OwMc6vlm7OoSUKfqUH615e.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rl95VDEP3nsUQmGzE0S1S7y6T0N.jpg",
    },
    {
        "id": 90,
        "title": "Zero Dark Thirty",
        "year": 2012,
        "runtime": "2h 37m",
        "genre": "Thriller",
        "description": (
            "A chronicle of the decade-long hunt for al-Qaeda terrorist leader Osama bin Laden after the September 2001 attacks, and his death at the hands of the Navy S.E.A.L. Team 6 in May, 2011."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/wNSdSSxowM3WIqmPJNg3RagYbwP.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/evPzxMacNWsjkUKQO4NXKe5Rl6a.jpg",
    },
    {
        "id": 91,
        "title": "The Bourne Identity",
        "year": 2002,
        "runtime": "1h 59m",
        "genre": "Action",
        "description": (
            "Wounded to the brink of death and suffering from amnesia, Jason Bourne is rescued at sea by a fisherman. With nothing to go on but a Swiss bank account number, he starts to reconstruct his life, but finds that many people he encounters want him dead. However, Bourne realizes that he has the combat and mental skills of a world-class spy—but who does he work for?"
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aP8swke3gmowbkfZ6lmNidu0y9p.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/kJaRWmy1BGq3pHyE94LOTteiHer.jpg",
    },
    {
        "id": 92,
        "title": "The Bourne Supremacy",
        "year": 2004,
        "runtime": "1h 48m",
        "genre": "Action",
        "description": (
            "A CIA operation to purchase classified Russian documents is blown by a rival agent, who then shows up in the sleepy seaside village where Bourne and Marie have been living. The pair run for their lives and Bourne, who promised retaliation should anyone from his former life attempt contact, is forced to once again take up his life as a trained assassin to survive."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7IYGiDrquvX3q7e9PV6Pejs6b2g.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/fE7RqvVHbGHjBC9NjIjlLh2t4zK.jpg",
    },
    {
        "id": 93,
        "title": "The Bourne Ultimatum",
        "year": 2007,
        "runtime": "1h 55m",
        "genre": "Action",
        "description": (
            "Bourne is brought out of hiding once again by reporter Simon Ross who is trying to unveil Operation Blackbriar, an upgrade to Project Treadstone, in a series of newspaper columns. Information from the reporter stirs a new set of memories, and Bourne must finally uncover his dark past while dodging The Company's best efforts to eradicate him."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/15rMz5MRXFp7CP4VxhjYw4y0FUn.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/qiBILuWhv7ipF0pxiEqIJdkQzj8.jpg",
    },
    {
        "id": 94,
        "title": "No Time to Die",
        "year": 2021,
        "runtime": "2h 43m",
        "genre": "Action",
        "description": (
            "Bond has left active service and is enjoying a tranquil life in Jamaica. His peace is short-lived when his old friend Felix Leiter from the CIA turns up asking for help. The mission to rescue a kidnapped scientist turns out to be far more treacherous than expected, leading Bond onto the trail of a mysterious villain armed with dangerous new technology."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/iUgygt3fscRoKWCV1d0C7FbM9TP.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/x9td0NQha0t44K2qgcMipLOGjVi.jpg",
    },
    {
        "id": 95,
        "title": "Skyfall",
        "year": 2012,
        "runtime": "2h 23m",
        "genre": "Action",
        "description": (
            "When Bond's latest assignment goes gravely wrong, agents around the world are exposed and MI6 headquarters is attacked. While M faces challenges to her authority and position from Gareth Mallory, the new Chairman of the Intelligence and Security Committee, it's up to Bond, aided only by field agent Eve, to locate the mastermind behind the attack."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/d0IVecFQvsGdSbnMAHqiYsNYaJT.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/qB2eFmGEh5YCzhXUpz7As2PaDCh.jpg",
    },
    {
        "id": 96,
        "title": "Spectre",
        "year": 2015,
        "runtime": "2h 28m",
        "genre": "Action",
        "description": (
            "A cryptic message from Bond’s past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to reveal the terrible truth behind SPECTRE."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/zj8ongFhtWNsVlfjOGo8pSr7PQg.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/8lBViysvNJBPkl6zG1LVAaW3qhj.jpg",
    },
    {
        "id": 97,
        "title": "Casino Royale",
        "year": 2006,
        "runtime": "2h 24m",
        "genre": "Adventure",
        "description": (
            "Le Chiffre, a banker to the world's terrorists, is scheduled to participate in a high-stakes poker game in Montenegro, where he intends to use his winnings to establish his financial grip on the terrorist market. M sends Bond—on his maiden mission as a 00 Agent—to attend this game and prevent Le Chiffre from winning. With the help of Vesper Lynd and Felix Leiter, Bond enters the most important poker game in his already dangerous career."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/lMrxYKKhd4lqRzwUHAy5gcx9PSO.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mXFmGlMCgTIOyHaGmQG1Hb6Rv2m.jpg",
    },
    {
        "id": 98,
        "title": "John Wick",
        "year": 2014,
        "runtime": "1h 41m",
        "genre": "Action",
        "description": (
            "Ex-hitman John Wick comes out of retirement to track down the gangsters that took everything from him."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ff2ti5DkA9UYLzyqhQfI2kZqEuh.jpg",
    },
    {
        "id": 99,
        "title": "John Wick: Chapter 2",
        "year": 2017,
        "runtime": "2h 2m",
        "genre": "Action",
        "description": (
            "John Wick is forced out of retirement by a former associate looking to seize control of a shadowy international assassins’ guild. Bound by a blood oath to aid him, Wick travels to Rome and does battle against some of the world’s most dangerous killers."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hXWBc0ioZP3cN4zCu6SN3YHXZVO.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/r17jFHAemzcWPPtoO0UxjIX0xas.jpg",
    },
    {
        "id": 100,
        "title": "John Wick: Chapter 3 - Parabellum",
        "year": 2019,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "Super-assassin John Wick returns with a $14 million price tag on his head and an army of bounty-hunting killers on his trail. After killing a member of the shadowy international assassin’s guild, the High Table, John Wick is excommunicado, but the world’s most ruthless hit men and women await his every turn."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ziEuG1essDuWuC5lpWUaw1uXY2O.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/vVpEOvdxVBP2aV166j5Xlvb5Cdc.jpg",
    },
    {
        "id": 101,
        "title": "John Wick: Chapter 4",
        "year": 2023,
        "runtime": "2h 50m",
        "genre": "Action",
        "description": (
            "With the price on his head ever increasing, John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe and forces that turn old friends into foes."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vZloFAK7NmvMGKE7VkF5UHaz0I.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7I6VUdPj6tQECNHdviJkUHD2u89.jpg",
    },
    {
        "id": 102,
        "title": "Mission: Impossible - The Final Reckoning",
        "year": 2025,
        "runtime": "2h 50m",
        "genre": "Action",
        "description": (
            "Ethan Hunt and team continue their search for the terrifying AI known as the Entity — which has infiltrated intelligence networks all over the globe — with the world's governments and a mysterious ghost from Hunt's past on their trail. Joined by new allies and armed with the means to shut the Entity down for good, Hunt is in a race against time to prevent the world as we know it from changing forever."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/z53D72EAOxGRqdr7KXXWp9dJiDe.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xPNDRM50a58uvv1il2GVZrtWjkZ.jpg",
    },
    {
        "id": 103,
        "title": "Mission: Impossible - Fallout",
        "year": 2018,
        "runtime": "2h 27m",
        "genre": "Action",
        "description": (
            "When an IMF mission ends badly, the world is faced with dire consequences. As Ethan Hunt takes it upon himself to fulfill his original briefing, the CIA begin to question his loyalty and his motives. The IMF team find themselves in a race against time, hunted by assassins while trying to prevent a global catastrophe."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/AkJQpZp9WoNdj7pLYSj1L0RcMMN.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5jnoAA74Qwb5w6B9FMvnc20n6Ie.jpg",
    },
    {
        "id": 104,
        "title": "Mission: Impossible - Rogue Nation",
        "year": 2015,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "Ethan and team take on their most impossible mission yet—eradicating 'The Syndicate', an International and highly-skilled rogue organization committed to destroying the IMF."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fRJLXQBHK2wyznK5yZbO7vmsuVK.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/vYIUN5rrCncHFY8WvcuXQlM4hk5.jpg",
    },
    {
        "id": 105,
        "title": "Top Gun",
        "year": 1986,
        "runtime": "1h 50m",
        "genre": "Action",
        "description": (
            "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xUuHj3CgmZQ9P2cMaqQs4J0d4Zc.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jILeJ60zPpIjjJHGSmIeY4eO30t.jpg",
    },
    {
        "id": 106,
        "title": "Top Gun: Maverick",
        "year": 2022,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "After more than thirty years of service as one of the Navy’s top aviators, and dodging the advancement in rank that would ground him, Pete “Maverick” Mitchell finds himself training a detachment of TOP GUN graduates for a specialized mission the likes of which no living pilot has ever seen."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/AaV1YIdWKnjAIAOe8UUKBFm327v.jpg",
    },
    {
        "id": 107,
        "title": "Fast & Furious",
        "year": 2010,
        "runtime": "0h 2m",
        "genre": "Action",
        "description": (
            "A balls to the wall action film about Fast, the fastest person alive, who is also named Fast."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/p8c0a159yKnpciQCFsR8BaC23po.jpg",
        "backdrop": "",
    },
    {
        "id": 108,
        "title": "Fast Five",
        "year": 2011,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "Former cop Brian O'Conner partners with ex-con Dom Toretto on the opposite side of the law. Since Brian and Mia Toretto broke Dom out of custody, they've blown across many borders to elude authorities. Now backed into a corner in Rio de Janeiro, they must pull one last job in order to gain their freedom."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gEfQjjQwY7fh5bI4GlG0RrBu7Pz.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/c9CSkUqJirHFfRe4rptYpGDcy5w.jpg",
    },
    {
        "id": 109,
        "title": "Furious 7",
        "year": 2015,
        "runtime": "2h 19m",
        "genre": "Action",
        "description": (
            "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ktofZ9Htrjiy0P6LEowsDaxd3Ri.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ehzI1mVcnHqB58NqPyQwpMqcVoz.jpg",
    },
    {
        "id": 110,
        "title": "The Fate of the Furious",
        "year": 2017,
        "runtime": "2h 16m",
        "genre": "Action",
        "description": (
            "When a mysterious woman seduces Dom into the world of crime and a betrayal of those closest to him, the crew face trials that will test them as never before."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/dImWM7GJqryWJO9LHa3XQ8DD5NH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3IJ8kG8i84PncXkSovu0PaZQfjM.jpg",
    },
    {
        "id": 111,
        "title": "Baby Driver",
        "year": 2017,
        "runtime": "1h 53m",
        "genre": "Action",
        "description": (
            "After being coerced into working for a crime boss, a young getaway driver finds himself taking part in a heist doomed to fail."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tYzFuYXmT8LOYASlFCkaPiAFAl0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/oVD3ClJBoomSQHtnJPAlMfes8YD.jpg",
    },
    {
        "id": 112,
        "title": "Drive",
        "year": 2011,
        "runtime": "1h 40m",
        "genre": "Drama",
        "description": (
            "Driver is a skilled Hollywood stuntman who moonlights as a getaway driver for criminals. Though he projects an icy exterior, lately he's been warming up to a pretty neighbor named Irene and her young son, Benicio. When Irene's husband gets out of jail, he enlists Driver's help in a million-dollar heist. The job goes horribly wrong, and Driver must risk his life to protect Irene and Benicio from the vengeful masterminds behind the robbery."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/602vevIURmpDfzbnv5Ubi6wIkQm.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/oeEiUwvqHxWT0XqD3YlViaiJOVD.jpg",
    },
    {
        "id": 113,
        "title": "The Equalizer",
        "year": 2014,
        "runtime": "2h 12m",
        "genre": "Thriller",
        "description": (
            "McCall believes he has put his mysterious past behind him and dedicated himself to beginning a new, quiet life. But when he meets Teri, a young girl under the control of ultra-violent Russian gangsters, he can’t stand idly by – he has to help her. Armed with hidden skills that allow him to serve vengeance against anyone who would brutalize the helpless, McCall comes out of his self-imposed retirement and finds his desire for justice reawakened. If someone has a problem, if the odds are stacked against them, if they have nowhere else to turn, McCall will help. He is The Equalizer."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/9u4yW7yPA0BQ2pv9XwiNzItwvp8.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wNAfVj1ObGNye5fQM4tJXJGtU0.jpg",
    },
    {
        "id": 114,
        "title": "The Equalizer 2",
        "year": 2018,
        "runtime": "2h 1m",
        "genre": "Action",
        "description": (
            "Robert McCall, who serves an unflinching justice for the exploited and oppressed, embarks on a relentless, globe-trotting quest for vengeance when his former partner is murdered."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/cQvc9N6JiMVKqol3wcYrGshsIdZ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/55eNvuXNumZ3oDmtcsJvzGhKyLZ.jpg",
    },
    {
        "id": 115,
        "title": "The Accountant",
        "year": 2016,
        "runtime": "2h 8m",
        "genre": "Crime",
        "description": (
            "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fceheXB5fC4WrLVuWJ6OZv9FXYr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/dTGECn8He16tZeBHQTLf6rVydE8.jpg",
    },
    {
        "id": 116,
        "title": "The Nice Guys",
        "year": 2016,
        "runtime": "1h 56m",
        "genre": "Comedy",
        "description": (
            "A private eye investigates the apparent suicide of a fading porn star in 1970s Los Angeles and uncovers a conspiracy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/clq4So9spa9cXk3MZy2iMdqkxP2.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xLRiuFeZkV9vwGMdA5AUzq1PeUn.jpg",
    },
    {
        "id": 117,
        "title": "Superbad",
        "year": 2007,
        "runtime": "1h 53m",
        "genre": "Comedy",
        "description": (
            "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/giYuvpmpZbwkT3NtX4WdNYqGhxw.jpg",
    },
    {
        "id": 118,
        "title": "The Hangover",
        "year": 2009,
        "runtime": "1h 40m",
        "genre": "Comedy",
        "description": (
            "When three friends finally come to after a raucous night of bachelor-party revelry, they find a baby in the closet and a tiger in the bathroom. But they can't seem to locate their best friend, Doug – who's supposed to be tying the knot. Launching a frantic search for Doug, the trio perseveres through a nasty hangover to try to make it to the church on time."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/A0uS9rHR56FeBtpjVki16M5xxSW.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/iuRVt8tFiXDPGgzavhuSa3QHRxD.jpg",
    },
    {
        "id": 119,
        "title": "The Hangover Part II",
        "year": 2011,
        "runtime": "1h 42m",
        "genre": "Comedy",
        "description": (
            "The Hangover crew heads to Thailand for Stu's wedding. After the disaster of a bachelor party in Las Vegas last year, Stu is playing it safe with a mellow pre-wedding brunch. However, nothing goes as planned and Bangkok is the perfect setting for another adventure with the rowdy group."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/cKZu0Fdkj7dmwbfMpgDqVVCkLJQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/aGmsekNU5cMOkJMpbdRutkvmVMl.jpg",
    },
    {
        "id": 120,
        "title": "The Hangover Part III",
        "year": 2013,
        "runtime": "1h 40m",
        "genre": "Comedy",
        "description": (
            "This time, there's no wedding. No bachelor party. What could go wrong, right? But when the Wolfpack hits the road, all bets are off."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vtxuPWkdllLNLVyGjKYa267ntuH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/o8ZS811VjYbBi4pRYwILLdWCVey.jpg",
    },
    {
        "id": 121,
        "title": "21 Jump Street",
        "year": 2012,
        "runtime": "1h 49m",
        "genre": "Action",
        "description": (
            "When cops Schmidt and Jenko join the secret Jump Street unit, they use their youthful appearances to go undercover as high school students. They trade in their guns and badges for backpacks, and set out to shut down a dangerous drug ring. But, as time goes on, Schmidt and Jenko discover that high school is nothing like it was just a few years earlier -- and, what's more, they must again confront the teenage terror and anxiety they thought they had left behind."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/8v3Sqv9UcIUC4ebmpKWROqPBINZ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/d1ACwtoBygLKkGjCq9LUXnmcki.jpg",
    },
    {
        "id": 122,
        "title": "22 Jump Street",
        "year": 2014,
        "runtime": "1h 52m",
        "genre": "Crime",
        "description": (
            "After making their way through high school (twice), big changes are in store for officers Schmidt and Jenko when they go deep undercover at a local college. But when Jenko meets a kindred spirit on the football team, and Schmidt infiltrates the bohemian art major scene, they begin to question their partnership. Now they don't have to just crack the case - they have to figure out if they can have a mature relationship. If these two overgrown adolescents can grow from freshmen into real men, college might be the best thing that ever happened to them."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/850chzYHYbT3IISl6Q7dbBuFP2B.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/kdyYOwpKvvD2fSbwfnMM2YPAzfq.jpg",
    },
    {
        "id": 123,
        "title": "Deadpool",
        "year": 2016,
        "runtime": "1h 48m",
        "genre": "Action",
        "description": (
            "The origin story of former Special Forces operative turned mercenary Wade Wilson, who, after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/3E53WEZJqP6aM84D8CckXx4pIHw.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rFj9IKlL75B2pXhZA60jkNWvxeW.jpg",
    },
    {
        "id": 124,
        "title": "Deadpool 2",
        "year": 2018,
        "runtime": "2h 0m",
        "genre": "Action",
        "description": (
            "Wisecracking mercenary Deadpool battles the evil and powerful Cable and other bad guys to save a boy's life."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/to0spRl1CMDvyUbOnbb4fTk3VAd.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3P52oz9HPQWxcwHOwxtyrVV1LKi.jpg",
    },
    {
        "id": 125,
        "title": "Logan",
        "year": 2017,
        "runtime": "2h 17m",
        "genre": "Action",
        "description": (
            "In the near future, a weary Logan cares for an ailing Professor X in a hideout on the Mexican border. But Logan's attempts to hide from the world and his legacy are upended when a young mutant arrives, pursued by dark forces."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fnbjcRDYn6YviCcePDnGdyAkYsB.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/4DZxWNSAyksN6N3JkvpJ53Yq6zU.jpg",
    },
    {
        "id": 126,
        "title": "X-Men: Apocalypse",
        "year": 2016,
        "runtime": "2h 24m",
        "genre": "Action",
        "description": (
            "After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ikA8UhYdTGpqbatFa93nIf6noSr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/2ex2beZ4ssMeOduLD0ILzXKCiep.jpg",
    },
    {
        "id": 127,
        "title": "X2",
        "year": 2003,
        "runtime": "2h 13m",
        "genre": "Adventure",
        "description": (
            "Professor Charles Xavier and his team of genetically gifted superheroes face a rising tide of anti-mutant sentiment led by Col. William Stryker. Storm, Wolverine and Jean Grey must join their usual nemeses—Magneto and Mystique—to unhinge Stryker's scheme to exterminate all mutants."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bWMw0FMsY8DICgrQnrTSWbzEgtr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/loixNIKBURXfPcND4noz7E8FqCS.jpg",
    },
    {
        "id": 128,
        "title": "X-Men: First Class",
        "year": 2011,
        "runtime": "2h 12m",
        "genre": "Action",
        "description": (
            "Before Charles Xavier and Erik Lensherr took the names Professor X and Magneto, they were two young men discovering their powers for the first time. Before they were arch-enemies, they were closest of friends, working together with other mutants (some familiar, some new), to stop the greatest threat the world has ever known."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hNEokmUke0dazoBhttFN0o3L7Xv.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mCinjxmq2tRDzSgc8QcuRkV8yTo.jpg",
    },
    {
        "id": 129,
        "title": "The Wolverine",
        "year": 2013,
        "runtime": "2h 6m",
        "genre": "Action",
        "description": (
            "Wolverine faces his ultimate nemesis - and tests of his physical, emotional, and mortal limits - in a life-changing voyage to modern-day Japan."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/t2wVAcoRlKvEIVSbiYDb8d0QqqS.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/bEAQfLTykGg232kJogBlxRYaRqU.jpg",
    },
    {
        "id": 130,
        "title": "The Incredible Hulk",
        "year": 2008,
        "runtime": "1h 54m",
        "genre": "Science Fiction",
        "description": (
            "Scientist Bruce Banner scours the planet for an antidote to the unbridled force of rage within him: the Hulk. But when the military masterminds who dream of exploiting his powers force him back to civilization, he finds himself coming face to face with a new, deadly foe."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/gKzYx79y0AQTL4UAk1cBQJ3nvrm.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jPu8yiadqgzwFPGKJmGo637ASVP.jpg",
    },
    {
        "id": 131,
        "title": "Hulk",
        "year": 2003,
        "runtime": "2h 18m",
        "genre": "Science Fiction",
        "description": (
            "Bruce Banner, a genetics researcher with a tragic past, suffers massive radiation exposure in his laboratory that causes him to transform into a raging green monster when he gets angry."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/UllIft2jLSBaay3zQyMV4GNdfy.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gJws6mK1RxPVPeL0MpxUzahLFBf.jpg",
    },
    {
        "id": 132,
        "title": "Man of Steel",
        "year": 2013,
        "runtime": "2h 23m",
        "genre": "Action",
        "description": (
            "A young boy learns that he has extraordinary powers and is not of this earth. As a young man, he journeys to discover where he came from and what he was sent here to do. But the hero in him must emerge if he is to save the world from annihilation and become the symbol of hope for all mankind."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/dksTL9NXc3GqPBRHYHcy1aIwjS.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/69EFgWWPFWbRNHmQgYdSnyJ94Ge.jpg",
    },
    {
        "id": 133,
        "title": "Batman Begins",
        "year": 2005,
        "runtime": "2h 20m",
        "genre": "Drama",
        "description": (
            "Driven by tragedy, billionaire Bruce Wayne dedicates his life to uncovering and defeating the corruption that plagues his home, Gotham City.  Unable to work within the system, he instead creates a new identity, a symbol of fear for the criminal underworld - The Batman."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sPX89Td70IDDjVr85jdSBb4rWGr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ew5FcYiRhTYNJAkxoVPMNlCOdVn.jpg",
    },
    {
        "id": 134,
        "title": "The Batman",
        "year": 2022,
        "runtime": "2h 57m",
        "genre": "Crime",
        "description": (
            "In his second year of fighting crime, Batman uncovers corruption in Gotham City that connects to his own family while facing a serial killer known as the Riddler."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rvtdN5XkWAfGX6xDuPL6yYS2seK.jpg",
    },
    {
        "id": 135,
        "title": "The Flash",
        "year": 2023,
        "runtime": "2h 24m",
        "genre": "Action",
        "description": (
            "When his attempt to save his family inadvertently alters the future, Barry Allen becomes trapped in a reality in which General Zod has returned and there are no Super Heroes to turn to. In order to save the world that he is in and return to the future that he knows, Barry's only hope is to race for his life. But will making the ultimate sacrifice be enough to reset the universe?"
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rktDFPbfHfUbArZ6OOOKsXcv0Bm.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yF1eOkaYvwiORauRCPWznV9xVvi.jpg",
    },
    {
        "id": 136,
        "title": "Aquaman",
        "year": 2018,
        "runtime": "2h 23m",
        "genre": "Action",
        "description": (
            "Half-human, half-Atlantean Arthur Curry is taken on the journey of his lifetime to discover if he is worth of being a king."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ufl63EFcc5XpByEV2Ecdw6WJZAI.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9QusGjxcYvfPD1THg6oW3RLeNn7.jpg",
    },
    {
        "id": 137,
        "title": "Wonder Woman",
        "year": 2017,
        "runtime": "2h 21m",
        "genre": "Action",
        "description": (
            "An Amazon princess comes to the world of Man in the grips of the First World War to confront the forces of evil and bring an end to human conflict."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/v4ncgZjG2Zu8ZW5al1vIZTsSjqX.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/AaABt75ZzfMGrscUR2seabz4PEX.jpg",
    },
    {
        "id": 138,
        "title": "Wonder Woman 1984",
        "year": 2020,
        "runtime": "2h 31m",
        "genre": "Action",
        "description": (
            "A botched store robbery places Wonder Woman in a global battle against a powerful and mysterious ancient force that puts her powers in jeopardy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/egg7KFi18TSQc1s24RMmR9i2zO6.jpg",
    },
    {
        "id": 139,
        "title": "Shazam!",
        "year": 2019,
        "runtime": "2h 12m",
        "genre": "Action",
        "description": (
            "A boy is given the ability to become an adult superhero in times of need with a single magic word."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xnopI5Xtky18MPhK40cZAGAOVeV.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/o7JVhqMmrex1TPbmuxl8YXVlcfl.jpg",
    },
    {
        "id": 140,
        "title": "The Suicide Squad",
        "year": 2021,
        "runtime": "2h 12m",
        "genre": "Action",
        "description": (
            "Supervillains Harley Quinn, Bloodsport, Peacemaker and a collection of nutty cons at Belle Reve prison join the super-secret, super-shady Task Force X as they are dropped off at the remote, enemy-infused island of Corto Maltese."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/q61qEyssk2ku3okWICKArlAdhBn.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jlGmlFOcfo8n5tURmhC7YVd4Iyy.jpg",
    },
    {
        "id": 141,
        "title": "Suicide Squad",
        "year": 2016,
        "runtime": "2h 2m",
        "genre": "Action",
        "description": (
            "From DC Comics comes the Suicide Squad, an antihero team of incarcerated supervillains who act as deniable assets for the United States government, undertaking high-risk black ops missions in exchange for commuted prison sentences."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sk3FZgh3sRrmr8vyhaitNobMcfh.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wAk0yKrhAmvsoMvlKs4QImhvK5X.jpg",
    },
    {
        "id": 142,
        "title": "Bird Box",
        "year": 2018,
        "runtime": "2h 4m",
        "genre": "Horror",
        "description": (
            "Five years after an ominous unseen presence drives most of society to suicide, a survivor and her two children make a desperate bid to reach safety."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rGfGfgL2pEPCfhIvqHXieXFn7gp.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/pDKFL1zcHzEpmz4MJA5JJnRbJeD.jpg",
    },
    {
        "id": 143,
        "title": "A Quiet Place",
        "year": 2018,
        "runtime": "1h 31m",
        "genre": "Horror",
        "description": (
            "A family is forced to live in silence while hiding from creatures that hunt by sound."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nIrDm42dy5PaXtUAzUfPmxM4mQm.jpg",
    },
    {
        "id": 144,
        "title": "A Quiet Place Part II",
        "year": 2021,
        "runtime": "1h 36m",
        "genre": "Science Fiction",
        "description": (
            "Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown, they realize that the creatures that hunt by sound are not the only threats that lurk beyond the sand path."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/4q2hz2m8hubgvijz8Ez0T2Os2Yv.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/am782sUaTOGcEPEdUUjybwUZP1f.jpg",
    },
    {
        "id": 145,
        "title": "The Conjuring",
        "year": 2013,
        "runtime": "1h 52m",
        "genre": "Horror",
        "description": (
            "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse. Forced to confront a powerful entity, the Warrens find themselves caught in the most terrifying case of their lives."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/aQCCpAIdWAp6wyFgjMry4okwrZo.jpg",
    },
    {
        "id": 146,
        "title": "The Conjuring 2",
        "year": 2016,
        "runtime": "2h 14m",
        "genre": "Horror",
        "description": (
            "Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by malicious spirits."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/zEqyD0SBt6HL7W9JQoWwtd5Do1T.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ev5Ti7Q0REkoVLO7PkKaq1yZYQE.jpg",
    },
    {
        "id": 147,
        "title": "The Conjuring: The Devil Made Me Do It",
        "year": 2021,
        "runtime": "1h 51m",
        "genre": "Horror",
        "description": (
            "Paranormal investigators Ed and Lorraine Warren encounter what would become one of the most sensational cases from their files. The fight for the soul of a young boy takes them beyond anything they'd ever seen before, to mark the first time in U.S. history that a murder suspect would claim demonic possession as a defense."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/rQfX2xx8TUoNvyk892yKWNikJaM.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6Z0FhoZM56YkuXhvklMTpc7rc5u.jpg",
    },
    {
        "id": 148,
        "title": "Annabelle",
        "year": 2014,
        "runtime": "1h 39m",
        "genre": "Horror",
        "description": (
            "A couple begins to experience terrifying supernatural occurrences involving a vintage doll shortly after their home is invaded by satanic cultists."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/yLsuU2P2SpDYFwtZQ7dtfVAf6TE.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/eLPXcqgJPCEOf2cMwyTEXejRhrC.jpg",
    },
    {
        "id": 149,
        "title": "Annabelle: Creation",
        "year": 2017,
        "runtime": "1h 50m",
        "genre": "Horror",
        "description": (
            "Several years after the tragic death of their little girl, a doll maker and his wife welcome a nun and several girls from a shuttered orphanage into their home, soon becoming the target of the doll maker's possessed creation—Annabelle."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tb86j8jVCVsdZnzf8I6cIi65IeM.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/o8u0NyEigCEaZHBdCYTRfXR8U4i.jpg",
    },
    {
        "id": 150,
        "title": "Annabelle Comes Home",
        "year": 2019,
        "runtime": "1h 46m",
        "genre": "Horror",
        "description": (
            "Determined to keep Annabelle from wreaking more havoc, demonologists Ed and Lorraine Warren bring the possessed doll to the locked artifacts room in their home, placing her “safely” behind sacred glass and enlisting a priest’s holy blessing. But an unholy night of horror awaits as Annabelle awakens the evil spirits in the room, who all set their sights on a new target—the Warrens' ten-year-old daughter, Judy, and her friends."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/qWsHMrbg9DsBY3bCMk9jyYCRVRs.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jB98SrdXAYSbiprjIwc7WfVCuCV.jpg",
    },
    {
        "id": 151,
        "title": "Insidious",
        "year": 2011,
        "runtime": "1h 42m",
        "genre": "Horror",
        "description": (
            "A family discovers that dark spirits have invaded their home after their son inexplicably falls into an endless sleep. When they reach out to a professional for help, they learn things are a lot more personal than they thought."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tmlDFIUpGRKiuWm9Ixc6CYDk4y0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yZP6GyrgzdpjH1AxPHlb8ACLkiA.jpg",
    },
    {
        "id": 152,
        "title": "Insidious: Chapter 2",
        "year": 2013,
        "runtime": "1h 46m",
        "genre": "Horror",
        "description": (
            "The haunted Lambert family seeks to uncover the mysterious childhood secret that has left them dangerously connected to the spirit world."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/w5JjiB3O1CLDXbTJe1QpU5RHmlU.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/i9oyhCYxIYH2082J0Rc3a3jQjRB.jpg",
    },
    {
        "id": 153,
        "title": "Insidious: The Red Door",
        "year": 2023,
        "runtime": "1h 47m",
        "genre": "Horror",
        "description": (
            "To put their demons to rest once and for all, Josh Lambert and a college-aged Dalton Lambert must go deeper into The Further than ever before, facing their family's dark past and a host of new and more horrifying terrors that lurk behind the red door."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/d07phJqCx6z5wILDYqkyraorDPi.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/i2GVEvltEu3BXn5crBSxgKuTaca.jpg",
    },
    {
        "id": 154,
        "title": "The Nun",
        "year": 2018,
        "runtime": "1h 36m",
        "genre": "Horror",
        "description": (
            "A priest with a dark past and a novice nearing her final vows are sent by the Vatican to Romania to investigate a nun's death and face a demonic force."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sFC1ElvoKGdHJIWRpNB3xWJ9lJA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/cMnVmutb5mVgIBeiMOncAbwNjvG.jpg",
    },
    {
        "id": 155,
        "title": "The Nun II",
        "year": 2023,
        "runtime": "1h 50m",
        "genre": "Horror",
        "description": (
            "In 1956 France, a priest is violently murdered, and Sister Irene begins to investigate. She once again comes face-to-face with a powerful evil."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/5gzzkR7y3hnY8AD1wXjCnVlHba5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/aX3Od8NVLgM7pMYgRpTPkwSrbSC.jpg",
    },
    {
        "id": 156,
        "title": "The Ring",
        "year": 2002,
        "runtime": "1h 55m",
        "genre": "Horror",
        "description": (
            "Rachel Keller is a journalist investigating a videotape that may have killed four teenagers. There is an urban legend about this tape: the viewer will die seven days after watching it. Rachel tracks down the video... and watches it. Now she has just seven days to unravel the mystery of the Ring so she can save herself and her son."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/AeRpUynJKDpJveklBJipOYrVxCS.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6tuNQ16hC4Qp7wjTweKzUnnLBkI.jpg",
    },
    {
        "id": 157,
        "title": "The Grudge",
        "year": 2004,
        "runtime": "1h 32m",
        "genre": "Horror",
        "description": (
            "An American nurse living and working in Tokyo is exposed to a mysterious supernatural curse, one that locks a person in a powerful rage before claiming their life and spreading to another victim."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/5AGB8FVELnhMMw3nO372sw1xp58.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yefSD6lp3jOBYkBeY5QxRRKTJME.jpg",
    },
    {
        "id": 158,
        "title": "Paranormal Activity",
        "year": 2007,
        "runtime": "1h 26m",
        "genre": "Horror",
        "description": (
            "After a young, middle-class couple moves into what seems like a typical suburban house, they become increasingly disturbed by a presence that may or may not be demonic but is certainly the most active in the middle of the night."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tmclkEpjeo4Zu564gf3KrwIOuKw.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wfCdJ0MD1hYJzlaHulolNw5pYtR.jpg",
    },
    {
        "id": 159,
        "title": "Barbarian",
        "year": 2022,
        "runtime": "1h 42m",
        "genre": "Horror",
        "description": (
            "In town for a job interview, a young woman arrives at her Airbnb late at night only to find that it has been mistakenly double-booked and a strange man is already staying there. Against her better judgement, she decides to stay the night anyway."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/idT5mnqPcJgSkvpDX7pJffBzdVH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/b5Sq1p2qnLNlaU9XOwjNNdbWmkP.jpg",
    },
    {
        "id": 160,
        "title": "Smile",
        "year": 2022,
        "runtime": "1h 55m",
        "genre": "Horror",
        "description": (
            "After witnessing a bizarre, traumatic incident involving a patient, Dr. Rose Cotter starts experiencing frightening occurrences that she can't explain."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aPqcQwu4VGEewPhagWNncDbJ9Xp.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/kMZIMqEXO5MFd5Y1Ha2jZZF4pvF.jpg",
    },
    {
        "id": 161,
        "title": "It",
        "year": 2017,
        "runtime": "2h 15m",
        "genre": "Horror",
        "description": (
            "In a small town in Maine, seven children known as The Losers Club come face to face with life problems, bullies and a monster that takes the shape of a clown called Pennywise."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rAQcPrEaPzDRVNX7XX5TWyxCGFN.jpg",
    },
    {
        "id": 162,
        "title": "It Chapter Two",
        "year": 2019,
        "runtime": "2h 49m",
        "genre": "Horror",
        "description": (
            "27 years after overcoming the malevolent supernatural entity Pennywise, the former members of the Losers' Club, who have grown up and moved away from Derry, are brought back together by a devastating phone call."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/zfE0R94v1E8cuKAerbskfD3VfUt.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6LVSrgm83UYWlrLTCVGmWhFKYO0.jpg",
    },
    {
        "id": 163,
        "title": "Hereditary",
        "year": 2018,
        "runtime": "2h 8m",
        "genre": "Horror",
        "description": (
            "Following the death of the Leigh family matriarch, Annie and her children uncover disturbing secrets about their heritage. Their daily lives are not only impacted, but they also become entangled in a chilling fate from which they cannot escape, driving them to the brink of madness."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hjlZSXM86wJrfCv5VKfR5DI2VeU.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gJbTXKNTL6O7r7PzF6ZRkJGBlPp.jpg",
    },
    {
        "id": 164,
        "title": "Midsommar",
        "year": 2019,
        "runtime": "2h 27m",
        "genre": "Horror",
        "description": (
            "Several friends travel to Sweden to study as anthropologists a summer festival that is held every ninety years in the remote hometown of one of them. What begins as a dream vacation in a place where the sun never sets, gradually turns into a dark nightmare as the mysterious inhabitants invite them to participate in their disturbing festive activities."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/7LEI8ulZzO5gy9Ww2NVCrKmHeDZ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/aAM3cQmYGjjLQ24m0F0RWfjKQ57.jpg",
    },
    {
        "id": 165,
        "title": "Get Out",
        "year": 2017,
        "runtime": "1h 44m",
        "genre": "Mystery",
        "description": (
            "Chris and his girlfriend Rose go upstate to visit her parents for the weekend. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/bBQHALHRAaaORlPNXv7fNcRXYdx.jpg",
    },
    {
        "id": 166,
        "title": "Us",
        "year": 2019,
        "runtime": "1h 56m",
        "genre": "Horror",
        "description": (
            "Husband and wife Gabe and Adelaide Wilson take their kids to their beach house expecting to unplug and unwind with friends. But as night descends, their serenity turns to tension and chaos when some shocking visitors arrive uninvited."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ux2dU1jQ2ACIMShzB3yP93Udpzc.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/sC0b8iPUHfZdD8kseLiHw3N8gkp.jpg",
    },
    {
        "id": 167,
        "title": "Nope",
        "year": 2022,
        "runtime": "2h 10m",
        "genre": "Horror",
        "description": (
            "Residents in a lonely gulch of inland California bear witness to an uncanny, chilling discovery."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/AcKVlWaNVVVFQwro3nLXqPljcYA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yRutvYkM3OP8N9oqqfjSK1VC7fs.jpg",
    },
    {
        "id": 168,
        "title": "Split",
        "year": 2017,
        "runtime": "1h 57m",
        "genre": "Horror",
        "description": (
            "Though Kevin has evidenced 23 personalities to his trusted psychiatrist, Dr. Fletcher, there remains one still submerged who is set to materialize and dominate all the others. Compelled to abduct three teenage girls led by the willful, observant Casey, Kevin reaches a war for survival among all of those contained within him — as well as everyone around him — as the walls between his compartments shatter apart."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/lli31lYTFpvxVBeFHWoe5PMfW5s.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9pkZesKMnblFfKxEhQx45YQ2kIe.jpg",
    },
    {
        "id": 169,
        "title": "Glass",
        "year": 2019,
        "runtime": "2h 9m",
        "genre": "Thriller",
        "description": (
            "In a series of escalating encounters, former security guard David Dunn uses his supernatural abilities to track Kevin Wendell Crumb, a disturbed man who has twenty-four personalities. Meanwhile, the shadowy presence of Elijah Price emerges as an orchestrator who holds secrets critical to both men."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/svIDTNUoajS8dLEo7EosxvyAsgJ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/rzsMWXQ7GaN60wIpg3yf01iBmXy.jpg",
    },
    {
        "id": 170,
        "title": "Unbreakable",
        "year": 2000,
        "runtime": "1h 46m",
        "genre": "Thriller",
        "description": (
            "An ordinary man makes an extraordinary discovery when a train accident leaves his fellow passengers dead — and him unscathed. The answer to this mystery could lie with the mysterious Elijah Price, a man who suffers from a disease that renders his bones as fragile as glass."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/mLuehrGLiK5zFCyRmDDOH6gbfPf.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/A7CYNTa3fWyU0t207XiecgriQv5.jpg",
    },
    {
        "id": 171,
        "title": "The Sixth Sense",
        "year": 1999,
        "runtime": "1h 47m",
        "genre": "Mystery",
        "description": (
            "Following an unexpected tragedy, child psychologist Malcolm Crowe meets a nine year old boy named Cole Sear, who is hiding a dark secret."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vOyfUXNFSnaTk7Vk5AjpsKTUWsu.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6TjllWT3cGrPFyqDXurVZ3L8bBi.jpg",
    },
    {
        "id": 172,
        "title": "Old",
        "year": 2021,
        "runtime": "1h 48m",
        "genre": "Thriller",
        "description": (
            "A group of families on a tropical holiday discover that the secluded beach where they are staying is somehow causing them to age rapidly – reducing their entire lives into a single day."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/vclShucpUmPhdAOmKgf3B3Z4POD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/32yqxyLlWcO81UCx51Jfq9aeJdA.jpg",
    },
    {
        "id": 173,
        "title": "Shrek",
        "year": 2001,
        "runtime": "1h 30m",
        "genre": "Animation",
        "description": (
            "It ain't easy bein' green -- especially if you're a likable (albeit smelly) ogre named Shrek. On a mission to retrieve a gorgeous princess from the clutches of a fire-breathing dragon, Shrek teams up with an unlikely compatriot -- a wisecracking donkey."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/iB64vpL3dIObOtMZgX3RqdVdQDc.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/40Wtp7kMG6mZ4d5T1jfrd8qrvD4.jpg",
    },
    {
        "id": 174,
        "title": "Shrek 2",
        "year": 2004,
        "runtime": "1h 32m",
        "genre": "Animation",
        "description": (
            "Shrek, Fiona, and Donkey set off to Far, Far Away to meet Fiona's mother and father, the Queen and King. But not everyone is happily ever after. Shrek and the King find it difficult to get along, and there's tension in the marriage. The Fairy Godmother discovers that Fiona has married Shrek instead of her son Prince Charming and plots to destroy their marriage."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2yYP0PQjG8zVqturh1BAqu2Tixl.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/8ohobj5lAIbl5XWw11FywS3IRrS.jpg",
    },
    {
        "id": 175,
        "title": "Shrek the Third",
        "year": 2007,
        "runtime": "1h 33m",
        "genre": "Fantasy",
        "description": (
            "The King of Far Far Away has died and Shrek and Fiona are to become King & Queen. However, Shrek wants to return to his cozy swamp and live in peace and quiet, so when he finds out there is another heir to the throne, they set off to bring him back to rule the kingdom."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/n4SexGGQzI26E269tfpa80MZaGV.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wvXxKpFGXvQJRB0nvvfURhRD3C0.jpg",
    },
    {
        "id": 176,
        "title": "Shrek Forever After",
        "year": 2010,
        "runtime": "1h 33m",
        "genre": "Comedy",
        "description": (
            "A bored and domesticated Shrek pacts with deal-maker Rumpelstiltskin to get back to feeling like a real ogre again, but when he's duped and sent to a twisted version of Far Far Away—where Rumpelstiltskin is king, ogres are hunted, and he and Fiona have never met—he sets out to restore his world and reclaim his true love."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6HrfPZtKcGmX2tUWW3cnciZTaSD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/uzzTystB8lL0mRDII5Sfs5HxgkI.jpg",
    },
    {
        "id": 177,
        "title": "Puss in Boots",
        "year": 2011,
        "runtime": "1h 30m",
        "genre": "Animation",
        "description": (
            "Long before he even met Shrek, the notorious fighter, lover and outlaw Puss in Boots becomes a hero when he sets off on an adventure with the tough and street smart Kitty Softpaws and the mastermind Humpty Dumpty to save his town. This is the true story of The Cat, The Myth, The Legend... The Boots."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/n4UkIqNYSTr4DPoHCVfLrL8mbre.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/6Pr9bECfj5k4KIYmT7np0xCXt3U.jpg",
    },
    {
        "id": 178,
        "title": "Puss in Boots: The Last Wish",
        "year": 2022,
        "runtime": "1h 43m",
        "genre": "Animation",
        "description": (
            "Puss in Boots discovers that his passion for adventure has taken its toll: He has burned through eight of his nine lives, leaving him with only one life left. Puss sets out on an epic journey to find the mythical Last Wish and restore his nine lives."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/kuf6dutpsT0vSVehic3EZIqkOBt.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jr8tSoJGj33XLgFBy6lmZhpGQNu.jpg",
    },
    {
        "id": 179,
        "title": "Kung Fu Panda",
        "year": 2008,
        "runtime": "1h 30m",
        "genre": "Animation",
        "description": (
            "When the Valley of Peace is threatened, lazy Po the panda discovers his destiny as the 'chosen one' and trains to become a kung fu hero, but transforming the unsleek slacker into a brave warrior won't be easy. It's up to Master Shifu and the Furious Five -- Tigress, Crane, Mantis, Viper and Monkey -- to give it a try."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/wWt4JYXTg5Wr3xBW2phBrMKgp3x.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ahTluOLnlwJlW3oRX4SB9lOey7C.jpg",
    },
    {
        "id": 180,
        "title": "Kung Fu Panda 2",
        "year": 2011,
        "runtime": "1h 31m",
        "genre": "Animation",
        "description": (
            "Po and his friends fight to stop a peacock villain from conquering China with a deadly new weapon, but first the Dragon Warrior must come to terms with his past."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/mtqqD00vB4PGRt20gWtGqFhrkd0.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/7BdxZXbSkUiVeCRXKD3hi9KYeWm.jpg",
    },
    {
        "id": 181,
        "title": "Kung Fu Panda 3",
        "year": 2016,
        "runtime": "1h 35m",
        "genre": "Animation",
        "description": (
            "While Po and his father are visiting a secret panda village, an evil spirit threatens all of China, forcing Po to form a ragtag army to fight back."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/oajNi4Su39WAByHI6EONu8G8HYn.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/A6shbaUPorZatoVbDdJgknxe3CZ.jpg",
    },
    {
        "id": 182,
        "title": "How to Train Your Dragon",
        "year": 2025,
        "runtime": "2h 5m",
        "genre": "Fantasy",
        "description": (
            "On the rugged isle of Berk, where Vikings and dragons have been bitter enemies for generations, Hiccup stands apart, defying centuries of tradition when he befriends Toothless, a feared Night Fury dragon. Their unlikely bond reveals the true nature of dragons, challenging the very foundations of Viking society."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/q5pXRYTycaeW6dEgsCrd4mYPmxM.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/vHTFrcqJoCi1is3XN0PZe2LSnI2.jpg",
    },
    {
        "id": 183,
        "title": "How to Train Your Dragon 2",
        "year": 2014,
        "runtime": "1h 42m",
        "genre": "Fantasy",
        "description": (
            "Five years have passed since Hiccup and Toothless united the dragons and Vikings of Berk. Now, they spend their time charting unmapped territories. During one of their adventures, the pair discover a secret cave that houses hundreds of wild dragons -- and a mysterious dragon rider. Hiccup and Toothless find themselves at the center of a battle to protect Berk from a power-hungry warrior."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/d13Uj86LdbDLrfDoHR5aDOFYyJC.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5MnP0h7RcUCeX7gpxMYoMScmfq7.jpg",
    },
    {
        "id": 184,
        "title": "How to Train Your Dragon: The Hidden World",
        "year": 2019,
        "runtime": "1h 44m",
        "genre": "Animation",
        "description": (
            "As Hiccup fulfills his dream of creating a peaceful dragon utopia, Toothless’ discovery of an untamed, elusive mate draws the Night Fury away. When danger mounts at home and Hiccup’s reign as village chief is tested, both dragon and rider must make impossible decisions to save their kind."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xvx4Yhf0DVH8G4LzNISpMfFBDy2.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/h3KN24PrOheHVYs9ypuOIdFBEpX.jpg",
    },
    {
        "id": 185,
        "title": "Toy Story",
        "year": 1995,
        "runtime": "1h 21m",
        "genre": "Family",
        "description": (
            "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3Rfvhy1Nl6sSGJwyjb0QiZzZYlB.jpg",
    },
    {
        "id": 186,
        "title": "Toy Story 2",
        "year": 1999,
        "runtime": "1h 32m",
        "genre": "Animation",
        "description": (
            "Andy heads off to Cowboy Camp, leaving his toys to their own devices. Things shift into high gear when an obsessive toy collector named Al McWhiggen, owner of Al's Toy Barn kidnaps Woody. Andy's toys mount a daring rescue mission, Buzz Lightyear meets his match and Woody has to decide where he and his heart truly belong."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/yFWQkz2ynjwsazT6xQiIXEUsyuh.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/tPK1kSevALeVGPfDFv1pwyHnoJ9.jpg",
    },
    {
        "id": 187,
        "title": "Toy Story 3",
        "year": 2010,
        "runtime": "1h 42m",
        "genre": "Animation",
        "description": (
            "Woody, Buzz, and the rest of Andy's toys haven't been played with in years. With Andy about to go to college, the gang find themselves accidentally left at a nefarious day care center. The toys must band together to escape and return home to Andy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/AbbXspMOwdvwWZgVN0nabZq03Ec.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wE5JGzujfvDPMIfFjJyrhXFjZLc.jpg",
    },
    {
        "id": 188,
        "title": "Toy Story 4",
        "year": 2019,
        "runtime": "1h 40m",
        "genre": "Family",
        "description": (
            "Woody has always been confident about his place in the world and that his priority is taking care of his kid, whether that's Andy or Bonnie. But when Bonnie adds a reluctant new toy called 'Forky' to her room, a road trip adventure alongside old and new friends will show Woody how big the world can be for a toy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/w9kR8qbmQ01HwnvK4alvnQ2ca0L.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/m67smI1IIMmYzCl9axvKNULVKLr.jpg",
    },
    {
        "id": 189,
        "title": "Cars",
        "year": 2006,
        "runtime": "1h 57m",
        "genre": "Animation",
        "description": (
            "Lightning McQueen, a hotshot rookie race car driven to succeed, discovers that life is about the journey, not the finish line, when he finds himself unexpectedly detoured in the sleepy Route 66 town of Radiator Springs. On route across the country to the big Piston Cup Championship in California to compete against two seasoned pros, McQueen gets to know the town's offbeat characters."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2Touk3m5gzsqr1VsvxypdyHY5ci.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/sd4xN5xi8tKRPrJOWwNiZEile7f.jpg",
    },
    {
        "id": 190,
        "title": "Cars 2",
        "year": 2011,
        "runtime": "1h 46m",
        "genre": "Animation",
        "description": (
            "Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventure of his own: international espionage."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/okIz1HyxeVOMzYwwHUjH2pHi74I.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/4BS8tgBNWg2jPiDlBwM2iJe1xB7.jpg",
    },
    {
        "id": 191,
        "title": "Cars 3",
        "year": 2017,
        "runtime": "1h 42m",
        "genre": "Animation",
        "description": (
            "Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen is suddenly pushed out of the sport he loves. To get back in the game, he will need the help of an eager young race technician with her own plan to win, inspiration from the late Fabulous Hudson Hornet, and a few unexpected turns. Proving that #95 isn't through yet will test the heart of a champion on Piston Cup Racing’s biggest stage!"
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fyy1nDC8wm553FCiBDojkJmKLCs.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/86TlYSntBzD4pxLNM6U3GoOfGdD.jpg",
    },
    {
        "id": 192,
        "title": "Finding Nemo",
        "year": 2003,
        "runtime": "1h 40m",
        "genre": "Animation",
        "description": (
            "Nemo, an adventurous young clownfish, is unexpectedly taken from his Great Barrier Reef home to a dentist's office aquarium. It's up to his worrisome father Marlin and a friendly but forgetful fish Dory to bring Nemo home -- meeting vegetarian sharks, surfer dude turtles, hypnotic jellyfish, hungry seagulls, and more along the way."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/eCynaAOgYYiw5yN5lBwz3IxqvaW.jpg",
    },
    {
        "id": 193,
        "title": "Finding Dory",
        "year": 2016,
        "runtime": "1h 37m",
        "genre": "Adventure",
        "description": (
            "Dory is reunited with her friends Nemo and Marlin in the search for answers about her past. What can she remember? Who are her parents? And where did she learn to speak Whale?"
        ),
        "poster": "https://image.tmdb.org/t/p/w500/3UVe8NL1E2ZdUZ9EDlKGJY5UzE.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/o11rDwFa7nZMVI57Mm3C44YwmmF.jpg",
    },
    {
        "id": 194,
        "title": "Up",
        "year": 2009,
        "runtime": "1h 36m",
        "genre": "Animation",
        "description": (
            "Carl Fredricksen spent his entire life dreaming of exploring the globe and experiencing life to its fullest. But at age 78, life seems to have passed him by, until a twist of fate (and a persistent 8-year old Wilderness Explorer named Russell) gives him a new lease on life."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/mFvoEwSfLqbcWwFsDjQebn9bzFe.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hGGC9gKo7CFE3fW07RA587e5kol.jpg",
    },
    {
        "id": 195,
        "title": "Inside Out",
        "year": 2015,
        "runtime": "1h 35m",
        "genre": "Animation",
        "description": (
            "When 11-year-old Riley moves to a new city, her Emotions team up to help her through the transition. Joy, Fear, Anger, Disgust and Sadness work together, but when Joy and Sadness get lost, they must journey through unfamiliar places to get back home."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jJKZaTBNenlFclQyjrnvzkRmvWE.jpg",
    },
    {
        "id": 196,
        "title": "Coco",
        "year": 2017,
        "runtime": "1h 45m",
        "genre": "Family",
        "description": (
            "Despite his family’s baffling generations-old ban on music, Miguel dreams of becoming an accomplished musician like his idol, Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events. Along the way, he meets charming trickster Hector, and together, they set off on an extraordinary journey to unlock the real story behind Miguel's family history."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wSJHuSD7ojzoXifWjOAjxV7UpEL.jpg",
    },
    {
        "id": 197,
        "title": "Ratatouille",
        "year": 2007,
        "runtime": "1h 51m",
        "genre": "Animation",
        "description": (
            "Remy, a resident of Paris, appreciates good food and has quite a sophisticated palate. He would love to become a chef so he can create and enjoy culinary masterpieces to his heart's delight. The only problem is, Remy is a rat. When he winds up in the sewer beneath one of Paris' finest restaurants, the rodent gourmet finds himself ideally placed to realize his dream."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/t3vaWRPSf6WjDSamIkKDs1iQWna.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xgDj56UWyeWQcxQ44f5A3RTWuSs.jpg",
    },
    {
        "id": 198,
        "title": "Monsters, Inc.",
        "year": 2001,
        "runtime": "1h 32m",
        "genre": "Animation",
        "description": (
            "Lovable Sulley and his wisecracking sidekick Mike Wazowski are the top scare team at Monsters, Inc., the scream-processing factory in Monstropolis. When a little girl named Boo wanders into their world, it's the monsters who are scared silly, and it's up to Sulley and Mike to keep her out of sight and get her back home."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/wFSpyMsp7H0ttERbxY7Trlv8xry.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/sDTnMOJ3H5wI38OxObmCtK7wfd5.jpg",
    },
    {
        "id": 199,
        "title": "Monsters University",
        "year": 2013,
        "runtime": "1h 44m",
        "genre": "Animation",
        "description": (
            "A look at the relationship between Mike and Sulley during their days at Monsters University — when they weren't necessarily the best of friends."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/y7thwJ7z5Bplv6vwl6RI0yteaDD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hmAOMwVeJfdWXgK1Ikyl2eYkE99.jpg",
    },
    {
        "id": 200,
        "title": "Elemental",
        "year": 2023,
        "runtime": "1h 42m",
        "genre": "Family",
        "description": (
            "In a city where fire, water, land and air residents live together, a fiery young woman and a go-with-the-flow guy will discover something elemental: how much they have in common."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/4Y1WNkd88JXmGfhtWR7dmDAo1T2.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/4fLZUr1e65hKPPVw0R3PmKFKxj1.jpg",
    },
    {
        "id": 201,
        "title": "Frozen",
        "year": 2013,
        "runtime": "1h 42m",
        "genre": "Animation",
        "description": (
            "Young princess Anna of Arendelle dreams about finding true love at her sister Elsa’s coronation. Fate takes her on a dangerous journey in an attempt to end the eternal winter that has fallen over the kingdom. She's accompanied by ice delivery man Kristoff, his reindeer Sven, and snowman Olaf. On an adventure where she will find out what friendship, courage, family, and true love really means."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/itAKcobTYGpYT8Phwjd8c9hleTo.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/u2bZhH3nTf0So0UIC1QxAqBvC07.jpg",
    },
    {
        "id": 202,
        "title": "Frozen II",
        "year": 2019,
        "runtime": "1h 43m",
        "genre": "Family",
        "description": (
            "Elsa, Anna, Kristoff and Olaf head far into the forest to learn the truth about an ancient mystery of their kingdom."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/mINJaa34MtknCYl5AjtNJzWj8cD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/AoSZyb37ljMAxw0RdeQEBHKtgcc.jpg",
    },
    {
        "id": 203,
        "title": "Moana",
        "year": 2026,
        "runtime": "Unknown",
        "genre": "Family",
        "description": (
            "In Ancient Polynesia, when a terrible curse incurred by Maui reaches the island of an impetuous Chieftain, his willful daughter answers the Ocean's call to seek out the demigod to set things right."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2B2XvBZFSOrGt7nptyNoBSFPhfb.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ogv0eTxwCVcrfKYsl2GKH4hNHJL.jpg",
    },
    {
        "id": 204,
        "title": "Encanto",
        "year": 2021,
        "runtime": "1h 42m",
        "genre": "Animation",
        "description": (
            "The tale of an extraordinary family, the Madrigals, who live hidden in the mountains of Colombia, in a magical house, in a vibrant town, in a wondrous, charmed place called an Encanto. The magic of the Encanto has blessed every child in the family—every child except one, Mirabel. But when she discovers that the magic surrounding the Encanto is in danger, Mirabel decides that she, the only ordinary Madrigal, might just be her exceptional family's last hope."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/4j0PNHkMr5ax3IA8tjtxcmPU3QT.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/3G1Q5xF40HkUBJXxt2DQgQzKTp5.jpg",
    },
    {
        "id": 205,
        "title": "Zootopia",
        "year": 2016,
        "runtime": "1h 49m",
        "genre": "Animation",
        "description": (
            "Determined to prove herself, Officer Judy Hopps, the first bunny on Zootopia's police force, jumps at the chance to crack her first case - even if it means partnering with scam-artist fox Nick Wilde to solve the mystery."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9tOkjBEiiGcaClgJFtwocStZvIT.jpg",
    },
    {
        "id": 206,
        "title": "The Lion King",
        "year": 1994,
        "runtime": "1h 29m",
        "genre": "Family",
        "description": (
            "Young lion prince Simba, eager to one day become king of the Pride Lands, grows up under the watchful eye of his father Mufasa; all the while his villainous uncle Scar conspires to take the throne for himself. Amid betrayal and tragedy, Simba must confront his past and find his rightful place in the Circle of Life."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/q00H8EqULYSK74lgevMkhmGGLHn.jpg",
    },
    {
        "id": 207,
        "title": "Aladdin",
        "year": 1992,
        "runtime": "1h 32m",
        "genre": "Animation",
        "description": (
            "In the boorish city of Agrabah, kind-hearted street urchin Aladdin and Princess Jasmine fall in love, although she can only marry a prince. He and power-hungry Grand Vizier Jafar vie for a magic lamp that can fulfill their wishes."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/eLFfl7vS8dkeG1hKp5mwbm37V83.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nenJjvfe2Eq8uBMXFJnWj5mw4bi.jpg",
    },
    {
        "id": 208,
        "title": "Beauty and the Beast",
        "year": 1991,
        "runtime": "1h 24m",
        "genre": "Romance",
        "description": (
            "Follow the adventures of Belle, a bright young woman who finds herself in the castle of a prince who's been turned into a mysterious beast. With the help of the castle's enchanted staff, Belle soon learns the most important lesson of all -- that true beauty comes from within."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/hUJ0UvQ5tgE2Z9WpfuduVSdiCiU.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/fW4ZCoEZRBqLAJGFQ2g5AdAfPQR.jpg",
    },
    {
        "id": 209,
        "title": "The Little Mermaid",
        "year": 2023,
        "runtime": "2h 15m",
        "genre": "Adventure",
        "description": (
            "The youngest of King Triton’s daughters, and the most defiant, Ariel longs to find out more about the world beyond the sea, and while visiting the surface, falls for the dashing Prince Eric. With mermaids forbidden to interact with humans, Ariel makes a deal with the evil sea witch, Ursula, which gives her a chance to experience life on land, but ultimately places her life – and her father’s crown – in jeopardy."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ym1dxyOk4jFcSl4Q2zmRrA5BEEN.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/lAs4Y5a8Pi86xDwuv8cx2prOVI2.jpg",
    },
    {
        "id": 210,
        "title": "Mulan",
        "year": 1998,
        "runtime": "1h 28m",
        "genre": "Animation",
        "description": (
            "To save her father from certain death in the army, a young woman secretly enlists in his place and becomes one of China's greatest heroines in the process."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bj3iSjLlkwHtJrPmvHXa8P7edI9.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/mUYV0ZdsDEliGaQahcQH1F3grsP.jpg",
    },
    {
        "id": 211,
        "title": "Tangled",
        "year": 2010,
        "runtime": "1h 40m",
        "genre": "Animation",
        "description": (
            "Feisty teenager Rapunzel, who has long and magical hair, wants to go and see sky lanterns on her eighteenth birthday, but she's bound to a tower by her overprotective mother. She strikes a deal with Flynn Rider, a charming wanted thief, and the duo set off on an action-packed escapade."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/ym7Kst6a4uodryxqbGOxmewF235.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/cWczNud8Y8i8ab0Z4bxos4myWYO.jpg",
    },
    {
        "id": 212,
        "title": "Big Hero 6",
        "year": 2014,
        "runtime": "1h 42m",
        "genre": "Adventure",
        "description": (
            "A special bond develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/2mxS4wUimwlLmI1xp6QW6NSU361.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ie6jboaxL8WYJO3TWt9JZdvnHzL.jpg",
    },
    {
        "id": 213,
        "title": "Wreck-It Ralph",
        "year": 2012,
        "runtime": "1h 41m",
        "genre": "Family",
        "description": (
            "Wreck-It Ralph is the 9-foot-tall, 643-pound villain of an arcade video game named Fix-It Felix Jr., in which the game's titular hero fixes buildings that Ralph destroys. Wanting to prove he can be a good guy and not just a villain, Ralph escapes his game and lands in Hero's Duty, a first-person shooter where he helps the game's hero battle against alien invaders. He later enters Sugar Rush, a kart racing game set on tracks made of candies, cookies and other sweets. There, Ralph meets Vanellope von Schweetz who has learned that her game is faced with a dire threat that could affect the entire arcade, and one that Ralph may have inadvertently started."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/zWoIgZ7mgmPkaZjG0102BSKFIqQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/riKyo85CmJU48ZaSMLpuDNTZHuE.jpg",
    },
    {
        "id": 214,
        "title": "Ralph Breaks the Internet",
        "year": 2018,
        "runtime": "1h 52m",
        "genre": "Family",
        "description": (
            "Video game bad guy Ralph and fellow misfit Vanellope von Schweetz must risk it all by traveling to the World Wide Web in search of a replacement part to save Vanellope's video game, Sugar Rush. In way over their heads, Ralph and Vanellope rely on the citizens of the internet — the netizens — to help navigate their way, including an entrepreneur named Yesss, who is the head algorithm and the heart and soul of trend-making site BuzzzTube."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/iVCrhBcpDaHGvv7CLYbK6PuXZo1.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/qDQEQbgP3v7B9IYLAUcYexNrVYP.jpg",
    },
    {
        "id": 215,
        "title": "The Lego Movie",
        "year": 2014,
        "runtime": "1h 40m",
        "genre": "Animation",
        "description": (
            "An ordinary Lego mini-figure, mistakenly thought to be the extraordinary MasterBuilder, is recruited to join a quest to stop an evil Lego tyrant from conquering the universe."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/oQeusrfyFx6DiSANOXKV3dc2G0g.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5N2mfRrvJUnCVpsMIebfosEyo1i.jpg",
    },
    {
        "id": 216,
        "title": "The Lego Batman Movie",
        "year": 2017,
        "runtime": "1h 44m",
        "genre": "Animation",
        "description": (
            "A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/snGwr2gag4Fcgx2OGmH9otl6ofW.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/eoMushgujydxFplE9yPZ54lwOvo.jpg",
    },
    {
        "id": 217,
        "title": "The Lego Movie 2: The Second Part",
        "year": 2019,
        "runtime": "1h 47m",
        "genre": "Action",
        "description": (
            "It's been five years since everything was awesome and the citizens are facing a huge new threat: LEGO DUPLO® invaders from outer space, wrecking everything faster than they can rebuild."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/QTESAsBVZwjtGJNDP7utiGV37z.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/nLvDo1F9xQD4VdFNgtipti7lKYD.jpg",
    },
    {
        "id": 218,
        "title": "Minions",
        "year": 2015,
        "runtime": "1h 31m",
        "genre": "Family",
        "description": (
            "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/dr02BdCNAUPVU07aOodwPYv6HCf.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wKrxeY6lbu7KFBsWVcMH6M8avwr.jpg",
    },
    {
        "id": 219,
        "title": "Despicable Me",
        "year": 2010,
        "runtime": "1h 35m",
        "genre": "Family",
        "description": (
            "Villainous Gru lives up to his reputation as a despicable, deplorable and downright unlikable guy when he hatches a plan to steal the moon from the sky. But he has a tough time staying on task after three orphans land in his care."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/9lOloREsAhBu0pEtU0BgeR1rHyo.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/2XSeKDmIa2KxaiJy4J9e8FrIZhk.jpg",
    },
    {
        "id": 220,
        "title": "Despicable Me 2",
        "year": 2013,
        "runtime": "1h 38m",
        "genre": "Animation",
        "description": (
            "Gru is recruited by the Anti-Villain League to help deal with a powerful new super criminal."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/oyMPJJZoOpLHgJoFPUOn6DgkbWJ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/fOipappvgVtUbbHOtmCkHzcwJjC.jpg",
    },
    {
        "id": 221,
        "title": "Despicable Me 3",
        "year": 2017,
        "runtime": "1h 30m",
        "genre": "Action",
        "description": (
            "Gru and his wife Lucy must stop former '80s child star Balthazar Bratt from achieving world domination."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6t3YWl7hrr88lCEFlGVqW5yV99R.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ftRkFtAGuHngHnLiOxktq0aCVMF.jpg",
    },
    {
        "id": 222,
        "title": "The Secret Life of Pets",
        "year": 2016,
        "runtime": "1h 26m",
        "genre": "Family",
        "description": (
            "The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bc3rCMgP4bbxNqGQCRlpJyU8otF.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/c1Ywtvlqls6tPBZ3BqbPtBwHyng.jpg",
    },
    {
        "id": 223,
        "title": "The Secret Life of Pets 2",
        "year": 2019,
        "runtime": "1h 26m",
        "genre": "Family",
        "description": (
            "Max the terrier must cope with some major life changes when his owner gets married and has a baby. When the family takes a trip to the countryside, nervous Max has numerous run-ins with canine-intolerant cows, hostile foxes and a scary turkey. Luckily for Max, he soon catches a break when he meets Rooster, a gruff farm dog who tries to cure the lovable pooch of his neuroses."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/s9xg4V5EDKiphgIksVJ9gewBM11.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/zDIievPXqjfjLogXFqnnopU0OkK.jpg",
    },
    {
        "id": 224,
        "title": "Sing",
        "year": 2016,
        "runtime": "1h 48m",
        "genre": "Family",
        "description": (
            "A koala named Buster recruits his best friend to help him drum up business for his theater by hosting a singing competition."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/xviEKU073QAzeFRzWDdW9xDHPbB.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/z9ft5HYHzWcasR6SGcgeluxTznB.jpg",
    },
    {
        "id": 225,
        "title": "Sing 2",
        "year": 2021,
        "runtime": "1h 50m",
        "genre": "Family",
        "description": (
            "Buster and his new cast now have their sights set on debuting a new show at the Crystal Tower Theater in glamorous Redshore City. But with no connections, he and his singers must sneak into the Crystal Entertainment offices, run by the ruthless wolf mogul Jimmy Crystal, where the gang pitches the ridiculous idea of casting the lion rock legend Clay Calloway in their show. Buster must embark on a quest to find the now-isolated Clay and persuade him to return to the stage."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aWeKITRFbbwY8txG5uCj4rMCfSP.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/ztiFxuG0gC6wQ8y7JZFYbCQyN4Y.jpg",
    },
    {
        "id": 226,
        "title": "The Super Mario Bros. Movie",
        "year": 2023,
        "runtime": "1h 33m",
        "genre": "Family",
        "description": (
            "While working underground to fix a water main, Brooklyn plumbers—and brothers—Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9n2tJBplPbgR2ca05hS5CKXwP2c.jpg",
    },
    {
        "id": 227,
        "title": "Pokémon Detective Pikachu",
        "year": 2019,
        "runtime": "1h 45m",
        "genre": "Action",
        "description": (
            "In a world where people collect pocket-size monsters (Pokémon) to do battle, a boy comes across an intelligent monster who seeks to be a detective."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/uhWvnFgg3BNlcUz0Re1HfQqIcCD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/yXybBEC45p84D0Ky7GmQQYrclVr.jpg",
    },
    {
        "id": 228,
        "title": "Sonic the Hedgehog",
        "year": 2020,
        "runtime": "1h 39m",
        "genre": "Action",
        "description": (
            "Powered with incredible speed, Sonic The Hedgehog embraces his new home on Earth. That is, until Sonic sparks the attention of super-uncool evil genius Dr. Robotnik. Now it’s super-villain vs. super-sonic in an all-out race across the globe to stop Robotnik from using Sonic’s unique power for world domination."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/aQvJ5WPzZgYVDrxLX4R6cLJCEaQ.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/stmYfCUGd8Iy6kAMBr6AmWqx8Bq.jpg",
    },
    {
        "id": 229,
        "title": "Sonic the Hedgehog 2",
        "year": 2022,
        "runtime": "2h 3m",
        "genre": "Action",
        "description": (
            "After settling in Green Hills, Sonic is eager to prove he has what it takes to be a true hero. His test comes when Dr. Robotnik returns, this time with a new partner, Knuckles, in search for an emerald that has the power to destroy civilizations. Sonic teams up with his own sidekick, Tails, and together they embark on a globe-trotting journey to find the emerald before it falls into the wrong hands."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6DrHO1jr3qVrViUO6s6kFiAGM7.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/xuLA0pii2IMJW2puT7EvJtgpg0H.jpg",
    },
    {
        "id": 230,
        "title": "Ready Player One",
        "year": 2018,
        "runtime": "2h 20m",
        "genre": "Adventure",
        "description": (
            "When the creator of a popular video game system dies, a virtual contest is created to compete for his fortune."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/pU1ULUq8D3iRxl1fdX2lZIzdHuI.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/5a7lMDn3nAj2ByO0X1fg6BhUphR.jpg",
    },
    {
        "id": 231,
        "title": "Pacific Rim",
        "year": 2013,
        "runtime": "2h 11m",
        "genre": "Action",
        "description": (
            "Using massive piloted robots to combat the alien threat, earth's survivors take the fight to the invading alien force lurking in the depths of the Pacific Ocean. Nearly defenseless in the face of the relentless enemy, the forces of mankind have no choice but to turn to two unlikely heroes who now stand as earth's final hope against the mounting apocalypse."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/8wo4eN8dWKaKlxhSvBz19uvj8gA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9X7Im1YuBhyHYVD8r7CAONPJR5k.jpg",
    },
    {
        "id": 232,
        "title": "Pacific Rim: Uprising",
        "year": 2018,
        "runtime": "1h 51m",
        "genre": "Action",
        "description": (
            "It has been ten years since The Battle of the Breach and the oceans are still, but restless. Vindicated by the victory at the Breach, the Jaeger program has evolved into the most powerful global defense force in human history. The PPDC now calls upon the best and brightest to rise up and become the next generation of heroes when the Kaiju threat returns."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/nFWhttU8PM50t25NPdy7PE7rv3G.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/oMaj75G2WFw66xI1TREg1hrToSg.jpg",
    },
    {
        "id": 233,
        "title": "Transformers",
        "year": 2007,
        "runtime": "2h 24m",
        "genre": "Adventure",
        "description": (
            "Young teenager Sam Witwicky becomes involved in the ancient struggle between two extraterrestrial factions of transforming robots – the heroic Autobots and the evil Decepticons. Sam holds the clue to unimaginable power and the Decepticons will stop at nothing to retrieve it."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/1P7w3AImoEOWJX7nn3fdaKDfEQA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/77P56ZcL8M9Cw7FIptMIGjhNJoj.jpg",
    },
    {
        "id": 234,
        "title": "Transformers: Revenge of the Fallen",
        "year": 2009,
        "runtime": "2h 30m",
        "genre": "Science Fiction",
        "description": (
            "Sam Witwicky leaves the Autobots behind for a normal life. But when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers' war."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/pLBb0whOzVDtJvyD4DPeQyQNOqp.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/bH1bhjn37uA1zOPvyHbzJSvza7v.jpg",
    },
    {
        "id": 235,
        "title": "Transformers: Dark of the Moon",
        "year": 2011,
        "runtime": "2h 34m",
        "genre": "Action",
        "description": (
            "The Autobots continue to work for NEST, now no longer in secret. But after discovering a strange artifact during a mission in Chernobyl, it becomes apparent to Optimus Prime that the United States government has been less than forthright with them."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/28YlCLrFhONteYSs9hKjD1Km0Cj.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/x2sSPVVKFt20vzHDwOWJK1UUfSj.jpg",
    },
    {
        "id": 236,
        "title": "Transformers: Age of Extinction",
        "year": 2014,
        "runtime": "2h 45m",
        "genre": "Science Fiction",
        "description": (
            "As humanity picks up the pieces after the battle of Chicago, a shadowy group reveals itself in an attempt to control the direction of history…while an ancient, powerful new menace sets Earth in its crosshairs. With help from Cade Yeager, Optimus Prime and the Autobots rise to meet their most fearsome challenge yet."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/jyzrfx2WaeY60kYZpPYepSjGz4S.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/wxr4Z6E83h14CogsZOzDm1vuDX3.jpg",
    },
    {
        "id": 237,
        "title": "Transformers: The Last Knight",
        "year": 2017,
        "runtime": "2h 34m",
        "genre": "Action",
        "description": (
            "Humans and Transformers are at war. Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth. Saving our world falls upon the shoulders of an unlikely alliance: Cade Yeager; Bumblebee; an English Lord; and an Oxford Professor."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/s5HQf2Gb3lIO2cRcFwNL9sn1o1o.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/1n00NlOGRFZVs8coBxyZLm5l4EC.jpg",
    },
    {
        "id": 238,
        "title": "Bumblebee",
        "year": 2018,
        "runtime": "1h 53m",
        "genre": "Action",
        "description": (
            "On the run in the year 1987, Bumblebee finds refuge in a junkyard in a small Californian beach town. Charlie, on the cusp of turning 18 and trying to find her place in the world, discovers Bumblebee, battle-scarred and broken.  When Charlie revives him, she quickly learns this is no ordinary yellow VW bug."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/fw02ONlDhrYjTSZV8XO6hhU3ds3.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/hMANgfPHR1tRObNp2oPiOi9mMlz.jpg",
    },
    {
        "id": 239,
        "title": "Jurassic Park",
        "year": 1993,
        "runtime": "2h 7m",
        "genre": "Adventure",
        "description": (
            "A wealthy entrepreneur secretly creates a theme park featuring living dinosaurs drawn from prehistoric DNA. Before opening day, he invites a team of experts and his two eager grandchildren to experience the park and help calm anxious investors. However, the park is anything but amusing as the security systems go off-line and the dinosaurs escape."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/bRKmwU9eXZI5dKT11Zx1KsayiLW.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/jzt9HuhIAdH9qp0K2MA1m5V8sgq.jpg",
    },
    {
        "id": 240,
        "title": "The Lost World: Jurassic Park",
        "year": 1997,
        "runtime": "2h 9m",
        "genre": "Adventure",
        "description": (
            "Four years after Jurassic Park's genetically bred dinosaurs ran amok, multimillionaire John Hammond shocks chaos theorist Ian Malcolm by revealing that he has been breeding more beasties at a secret location. Malcolm, his paleontologist ladylove and a wildlife videographer join an expedition to document the lethal lizards' natural behavior in this action-packed thriller."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/6fSkhv35nPSw9hwPVCMINQFG1WD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/A4rYaPdzgocCjQ0n9LUSYUxyvpS.jpg",
    },
    {
        "id": 241,
        "title": "Jurassic Park III",
        "year": 2001,
        "runtime": "1h 32m",
        "genre": "Adventure",
        "description": (
            "In need of funds for research, Dr. Alan Grant accepts a large sum of money to accompany Paul and Amanda Kirby on an aerial tour of the infamous Isla Sorna. It isn't long before all hell breaks loose and the stranded wayfarers must fight for survival as a host of new -- and even more deadly -- dinosaurs try to make snacks of them."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/oQXj4NUfS3r3gHXtDOzcJgj1lLc.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/8v8x4vVbRgrsdU3M4drnD7HQbfe.jpg",
    },
    {
        "id": 242,
        "title": "Jurassic World: Fallen Kingdom",
        "year": 2018,
        "runtime": "2h 9m",
        "genre": "Action",
        "description": (
            "Three years after Jurassic World was destroyed, Isla Nublar now sits abandoned. When the island's dormant volcano begins roaring to life, Owen and Claire mount a campaign to rescue the remaining dinosaurs from this extinction-level event."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/x8cLgs0uXlb9rmpuVIxopoRGnCr.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/gBmrsugfWpiXRh13Vo3j0WW55qD.jpg",
    },
    {
        "id": 243,
        "title": "Jurassic World Dominion",
        "year": 2022,
        "runtime": "2h 27m",
        "genre": "Adventure",
        "description": (
            "Four years after Isla Nublar was destroyed, dinosaurs now live—and hunt—alongside humans all over the world. This fragile balance will reshape the future and determine, once and for all, whether human beings are to remain the apex predators on a planet they now share with history's most fearsome creatures."
        ),
        "poster": "https://image.tmdb.org/t/p/w500/jbAvCACjLf1ZG0unB2tdmx5HAf1.jpg",
        "backdrop": "https://image.tmdb.org/t/p/w1280/9eAn20y26wtB3aet7w9lHjuSgZ3.jpg",
    },
]
