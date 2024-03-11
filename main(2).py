import telebot
import re
import asyncio
from telebot import types

bot = telebot.TeleBot('7180862451:AAFVQOZ-0q7XR31BDuyZOQMrHKzHtI82n0Q')

def clean_movie_name(movie_name):
    return re.sub(r'[^A-Za-z0-9]+', '', movie_name)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cy = types.InlineKeyboardMarkup(row_width=1)
    uy = types.InlineKeyboardButton('مطور البوت 🤖', url='t.me/yonnr')
    cy.add(uy)
    yr=[uy]

    bot.send_message(message.chat.id, """*> اهلا عزيزي في بوت Top 250 Movies 🎬

> ارسل اسماء افلامك لتعرف كم فيلم شاهدت من قائمة افضل 250 على موقع IMDB 📒

> رجاء ارسل اسماء افلام ك قائمة برسالة واحدة, مثال:

the godfather/12 angry men/se7en...........

> واذا كان اسم الفيلم اقصر من 4 احرف اكتب معه سنة انتاج الفيلم، مثال:

up 2009/ran 1985/m 1931........*""", reply_markup=cy, parse_mode= 'Markdown')


@bot.message_handler(func=lambda message: True)
def count_watched_movies(message):
    movie_names_list = [clean_movie_name(movie.strip().lower()) for movie in message.text.split('/')]

    all_movies = [
      "The Shawshank Redemption",
      "The Godfather",
      "The Godfather: Part II The Godfather 2",
      "The Dark Knight",
      "12 Angry Men",
      "Schindler's List",
      "The Lord of the Rings: The Return of the King",
      "Pulp Fiction",
      "The Lord of the Rings: The Fellowship of the Ring",
      "Dune: Part Two Dune 2",
      "The Good, the Bad and the Ugly",
      "Forrest Gump",
      "The Lord of the Rings: The Two Towers",
      "Fight Club",
      "Inception",
      "Star Wars: Episode V - The Empire Strikes Back",
      "The Matrix",
      "Goodfellas",
      "One Flew Over the Cuckoo's Nest",
      "Se7en",
      "It's a Wonderful Life",
      "Interstellar",
      "Seven Samurai",
      "The Silence of the Lambs",
      "Saving Private Ryan",
      "City of God",
      "Life Is Beautiful",
      "The Green Mile",
      "Terminator 2: Judgment Day",
      "Star Wars: Episode IV - A New Hope",
      "Back to the Future",
      "Spirited Away",
      "The Pianist",
      "Spider-Man: Across the Spider-Verse",
      "Parasite",
      "Psycho",
      "Gladiator",
      "The Lion King",
      "Léon: The Professional",
      "The Departed",
      "American History X",
      "Whiplash",
      "The Prestige",
      "Grave of the Fireflies",
      "Harakiri",
      "The Usual Suspects",
      "Casablanca",
      "The Intouchables",
      "Cinema Paradiso",
      "Modern Times",
      "Rear Window",
      "Once Upon a Time in the West",
      "Alien",
      "12th Fail",
      "City Lights",
      "Apocalypse Now",
      "Django Unchained",
      "Memento",
      "WALL·E : wall.e",
      "Raiders of the Lost Ark",
      "The Lives of Others",
      "Sunset Blvd.",
      "Paths of Glory",
      "Avengers: Infinity War",
      "Spider-Man: Into the Spider-Verse",
      "The Shining",
      "Witness for the Prosecution",
      "The Great Dictator",
      "Aliens",
      "Inglourious Basterds",
      "The Dark Knight Rises",
      "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
      "American Beauty",
      "Oldboy",
      "Coco",
      "Amadeus",
      "Toy Story",
      "The Boat",
      "Braveheart",
      "Avengers: Endgame",
      "Joker",
      "Princess Mononoke",
      "Good Will Hunting",
      "Your Name.",
      "Once Upon a Time in America",
      "Oppenheimer",
      "High and Low",
      "3 Idiots",
      "Singin' in the Rain",
      "Capernaum",
      "Requiem for a Dream",
      "Come and See",
      "Toy Story 3",
      "Star Wars: Episode VI - Return of the Jedi",
      "Eternal Sunshine of the Spotless Mind",
      "The Hunt",
      "2001: A Space Odyssey",
      "Reservoir Dogs",
      "Ikiru",
      "Lawrence of Arabia",
      "The Apartment",
      "North by Northwest",
      "Citizen Kane",
      "M 1931",
      "Vertigo",
      "Double Indemnity",
      "Scarface",
      "Incendies",
      "Amélie",
      "Full Metal Jacket",
      "A Clockwork Orange",
      "Heat",
      "Up 2009",
      "To Kill a Mockingbird",
      "The Sting",
      "A Separation",
      "Indiana Jones and the Last Crusade",
      "Die Hard",
      "Metropolis",
      "Hamilton",
      "Like Stars on Earth",
      "Snatch",
      "L.A. Confidential",
      "Bicycle Thieves",
      "1917",
      "Taxi Driver",
      "Downfall",
      "Dangal",
      "For a Few Dollars More",
      "Batman Begins",
      "The Wolf of Wall Street",
      "Some Like It Hot",
      "The Kid",
      "Green Book",
      "The Father",
      "Top Gun: Maverick",
      "Judgment at Nuremberg",
      "All About Eve",
      "The Truman Show",
      "There Will Be Blood",
      "Shutter Island",
      "Casino",
      "Ran 1985",
      "Jurassic Park",
      "The Sixth Sense",
      "Pan's Labyrinth",
      "Unforgiven",
      "A Beautiful Mind",
      "No Country for Old Men",
      "The Thing",
      "The Treasure of the Sierra Madre",
      "Kill Bill: Vol. 1",
      "Yojimbo",
      "Monty Python and the Holy Grail",
      "The Great Escape",
      "Finding Nemo",
      "Rashomon",
      "Howl's Moving Castle",
      "The Elephant Man",
      "Prisoners",
      "Chinatown",
      "Dial M for Murder",
      "Gone with the Wind",
      "V for Vendetta",
      "Lock, Stock and Two Smoking Barrels",
      "The Secret in Their Eyes",
      "Raging Bull",
      "Inside Out",
      "Three Billboards Outside Ebbing, Missouri",
      "Trainspotting",
      "The Bridge on the River Kwai",
      "Spider-Man: No Way Home",
      "Poor Things",
      "Fargo",
      "Klaus",
      "Warrior",
      "Catch Me If You Can",
      "Godzilla Minus One",
      "Gran Torino",
      "My Neighbor Totoro",
      "Million Dollar Baby",
      "Harry Potter and the Deathly Hallows: Part 2",
      "Children of Heaven",
      "12 Years a Slave",
      "Blade Runner",
      "Before Sunrise",
      "The Grand Budapest Hotel",
      "Ben-Hur : ben hur",
      "Barry Lyndon",
      "Gone Girl",
      "The Gold Rush",
      "Hacksaw Ridge",
      "In the Name of the Father",
      "Memories of Murder",
      "Dead Poets Society",
      "On the Waterfront",
      "The General",
      "The Deer Hunter",
      "Wild Tales",
      "Mad Max: Fury Road",
      "Sherlock Jr.",
      "Monsters, Inc.",
      "The Third Man",
      "Wild Strawberries",
      "The Wages of Fear",
      "Jaws",
      "How to Train Your Dragon",
      "Mary and Max",
      "Mr. Smith Goes to Washington",
      "Ford v Ferrari",
      "Ratatouille",
      "The Seventh Seal",
      "Tokyo Story",
      "Room",
      "The Big Lebowski",
      "Rocky",
      "Logan",
      "Spotlight",
      "Hotel Rwanda",
      "Platoon",
      "The Terminator",
      "The Passion of Joan of Arc",
      "Before Sunset",
      "La haine",
      "The Best Years of Our Lives",
      "Jai Bhim",
      "The Exorcist",
      "Rush",
      "Pirates of the Caribbean: The Curse of the Black Pearl",
      "Network",
      "Stand by Me",
      "The Wizard of Oz",
      "The Incredibles",
      "Hachi: A Dog's Tale",
      "Into the Wild",
      "The Handmaiden",
      "My Father and My Son",
      "To Be or Not to Be",
      "The Sound of Music",
      "The Grapes of Wrath",
      "Groundhog Day",
      "The Battle of Algiers",
      "Amores Perros",
      "Rebecca",
      "Cool Hand Luke",
      "The Iron Giant",
      "The Help",
      "It Happened One Night",
      "The 400 Blows",
      "Dances with Wolves"

    ]

    cleaned_all_movies = [clean_movie_name(movie.lower()) for movie in all_movies]
    watched_count = sum(1 for movie in cleaned_all_movies if movie in movie_names_list)
    
    if watched_count == 0:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
  > اغلق التلجرام واذهب شاهد الافلام.🐎*""" , parse_mode= 'Markdown')
    if 1 <= watched_count <= 11:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم
> لماذا انت على قيد الحياة؟☠*""" , parse_mode= 'Markdown')

    if 12 <= watched_count <= 24:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم
> الطريق طويل لكنك تستطيع.💪🏻*""" , parse_mode= 'Markdown')
    if 25 <= watched_count <= 74:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
> استمرررر يا بطل تستطيع.🦁*""" , parse_mode= 'Markdown')

    if 75 <= watched_count <= 124:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
> الحنكة تناديك من بعيد.🗣*""" , parse_mode= 'Markdown')
    if 125 <= watched_count <= 174:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
> وحش قربت للحنكة.🦾*""" , parse_mode= 'Markdown')
    if 175 <= watched_count <= 199:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
> محنك جيد وتقدر على الافضل.🧑🏻‍🏫*""" , parse_mode= 'Markdown')
    if 175 <= watched_count <= 199:
      bot.send_message(message.chat.id,f"""*> شاهدت {watched_count} فيلم 
> محنك Max و راقي و مذهل.🦸🏻‍♂️*""" , parse_mode= 'Markdown')


if __name__ == '__main__':
  bot.polling(none_stop=True)