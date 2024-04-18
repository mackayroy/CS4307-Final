import sqlite3
from datetime import datetime
import argparse
import random

conn = sqlite3.connect('libraryDB.db.db')
cursor = conn.cursor()

def bookSetUp():
    # CS4307-Final
    conditionOfBook = ["Good", "Very Good", "Poor", "Fair"]
    books = [
    {
    "title": "1984",
    "genre": "Dystopian fiction",
    "page_count": 328
    },
    {
    "title": "To Kill a Mockingbird",
    "genre": "Southern Gothic",
    "page_count": 281
    },
    {
    "title": "The Great Gatsby",
    "genre": "Jazz Age",
    "page_count": 180
    },
    {
    "title": "Pride and Prejudice",
    "genre": "Romance",
    "page_count": 279
    },
    {
    "title": "The Lord of the Rings",
    "genre": "High fantasy",
    "page_count": 1178 # Approximate for the complete trilogy
    },
    {
    "title": "Harry Potter and the Philosopher's Stone",
    "genre": "Fantasy",
    "page_count": 223
    },
    {
    "title": "Moby-Dick",
    "genre": "Adventure fiction",
    "page_count": 585 # Approximate
    },
    {
    "title": "The Catcher in the Rye",
    "genre": "Bildungsroman",
    "page_count": 277
    },
    {
    "title": "The Hobbit",
    "genre": "Fantasy",
    "page_count": 310
    },
    {
    "title": "Crime and Punishment",
    "genre": "Psychological fiction",
    "page_count": 551 # Approximate
    },
    {
    "title": "The Picture of Dorian Gray",
    "genre": "Gothic fiction",
    "page_count": 254
    },
    {
    "title": "Frankenstein",
    "genre": "Gothic fiction, Science fiction",
    "page_count": 280
    },
    {
    "title": "The Adventures of Huckleberry Finn",
    "genre": "Adventure fiction, Satire",
    "page_count": 366
    },
    {
    "title": "Anna Karenina",
    "genre": "Realist fiction, Tragedy",
    "page_count": 864 # Approximate
    },
    {
    "title": "Brave New World",
    "genre": "Dystopian fiction, Science fiction",
    "page_count": 288
    },
    {
    "title": "The Odyssey",
    "genre": "Epic poetry",
    "page_count": 384
    },
    {
    "title": "Don Quixote",
    "genre": "Parody, Satire",
    "page_count": 1056 # Approximate
    },
    {
    "title": "The Brothers Karamazov",
    "genre": "Philosophical fiction",
    "page_count": 796 # Approximate
    },
    {
    "title": "Wuthering Heights",
    "genre": "Gothic fiction, Romance",
    "page_count": 342
    },
    {
    "title": "The Count of Monte Cristo",
    "genre": "Adventure fiction, Historical fiction",
    "page_count": 1276 # Approximate
    },
    {
    "title": "Alice's Adventures in Wonderland",
    "genre": "Fantasy, Children's literature",
    "page_count": 192
    },
    {
    "title": "The Road",
    "genre": "Post-apocalyptic fiction",
    "page_count": 287
    },
    {
    "title": "War and Peace",
    "genre": "Historical fiction",
    "page_count": 1392 # Approximate
    },
    {
    "title": "Dracula",
    "genre": "Gothic fiction, Horror",
    "page_count": 488
    },
    {
    "title": "Les Misérables",
    "genre": "Historical fiction",
    "page_count": 1232 # Approximate
    },
    {
    "title": "The Canterbury Tales",
    "genre": "Poetry, Short stories",
    "page_count": 544
    },
    {
    "title": "The Handmaid's Tale",
    "genre": "Dystopian fiction",
    "page_count": 311
    },
    {
    "title": "One Hundred Years of Solitude",
    "genre": "Magical realism",
    "page_count": 417
    },
    {
    "title": "Slaughterhouse-Five",
    "genre": "Science fiction",
    "page_count": 275
    },
    {
    "title": "Gone with the Wind",
    "genre": "Historical fiction, Romance",
    "page_count": 1037 # Approximate
    },
    {
    "title": "The Name of the Wind",
    "genre": "Fantasy",
    "page_count": 662
    },
    {
    "title": "The Road to Serfdom",
    "genre": "Non-fiction, Economics",
    "page_count": 283
    },
    {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "genre": "Science fiction, Comedy",
    "page_count": 193
    },
    {
    "title": "The Alchemist",
    "genre": "Adventure fiction, Quest",
    "page_count": 163
    },
    {
    "title": "The Giver",
    "genre": "Dystopian fiction, Young adult",
    "page_count": 208
    },
    {
    "title": "Norwegian Wood",
    "genre": "Coming-of-age fiction",
    "page_count": 296
    },
    {
    "title": "The Bell Jar",
    "genre": "Semi-autobiographical novel",
    "page_count": 244
    },
    {
    "title": "Fahrenheit 451",
    "genre": "Dystopian fiction",
    "page_count": 158
    },
    {
    "title": "The Secret History",
    "genre": "Mystery, Psychological thriller",
    "page_count": 559
    },
    {
    "title": "The Martian",
    "genre": "Science fiction",
    "page_count": 369
    },
    {
    "title": "The Stranger",
    "genre": "Philosophical fiction",
    "page_count": 123
    },
    {
    "title": "The Girl with the Dragon Tattoo",
    "genre": "Crime fiction, Mystery",
    "page_count": 672
    },
    {
    "title": "The Road Less Traveled",
    "genre": "Psychology, Self-help",
    "page_count": 320
    },
    {
    "title": "The Shining",
    "genre": "Horror",
    "page_count": 447
    },
    {
    "title": "The Stand",
    "genre": "Post-apocalyptic fiction",
    "page_count": 1153
    },
    {
    "title": "The Goldfinch",
    "genre": "Bildungsroman",
    "page_count": 771
    },
    {
    "title": "The Da Vinci Code",
    "genre": "Mystery, Thriller",
    "page_count": 454
    },
    {
    "title": "The Night Circus",
    "genre": "Fantasy",
    "page_count": 512
    },
    {
    "title": "The Handmaid's Tale",
    "genre": "Dystopian fiction",
    "page_count": 311
    },
    {
    "title": "The Help",
    "genre": "Historical fiction",
    "page_count": 451
    },
    {
    "title": "The Kite Runner",
    "genre": "Historical fiction",
    "page_count": 371
    },
    {
    "title": "Life of Pi",
    "genre": "Adventure fiction",
    "page_count": 319
    },
    {
    "title": "The Book Thief",
    "genre": "Historical fiction",
    "page_count": 552
    },
    {
    "title": "The Hunger Games",
    "genre": "Dystopian fiction, Science fiction",
    "page_count": 374
    },
    {
    "title": "The Catcher Was a Spy",
    "genre": "Biography, Non-fiction",
    "page_count": 272
    },
    {
    "title": "The Color Purple",
    "genre": "Epistolary novel",
    "page_count": 304
    },
    {
    "title": "The Martian Chronicles",
    "genre": "Science fiction, Short stories",
    "page_count": 222
    },
    {
    "title": "The Girl on the Train",
    "genre": "Thriller, Mystery",
    "page_count": 316
    },
    {
    "title": "A Game of Thrones",
    "genre": "Epic fantasy",
    "page_count": 694
    },
    {
    "title": "Educated",
    "genre": "Memoir",
    "page_count": 334
    },
    {
    "title": "The Road",
    "genre": "Post-apocalyptic fiction",
    "page_count": 287
    },
    {
    "title": "The Godfather",
    "genre": "Crime fiction",
    "page_count": 448
    },
    {
    "title": "The Help",
    "genre": "Historical fiction",
    "page_count": 464
    },
    {
    "title": "Where the Crawdads Sing",
    "genre": "Mystery, Coming-of-age fiction",
    "page_count": 384
    },
    {
    "title": "The Thorn Birds",
    "genre": "Family saga, Romance",
    "page_count": 692
    },
    {
    "title": "The Road",
    "genre": "Post-apocalyptic fiction",
    "page_count": 287
    },
    {
    "title": "The Goldfinch",
    "genre": "Bildungsroman",
    "page_count": 771
    },
    {
    "title": "The Da Vinci Code",
    "genre": "Mystery, Thriller",
    "page_count": 454
    },
    {
    "title": "The Night Circus",
    "genre": "Fantasy",
    "page_count": 512
    },
    {
    "title": "The Help",
    "genre": "Historical fiction",
    "page_count": 451
    },{
    "title": "The Hobbit",
    "genre": "Fantasy",
    "page_count": 310
    },
    {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "genre": "Science fiction, Comedy",
    "page_count": 193
    },
    {
    "title": "The Silent Patient",
    "genre": "Psychological thriller",
    "page_count": 336
    },
    {
    "title": "Crazy Rich Asians",
    "genre": "Romantic comedy",
    "page_count": 527
    },
    {
    "title": "The Stand",
    "genre": "Post-apocalyptic fiction",
    "page_count": 1153
    },
    {
    "title": "The Nightingale",
    "genre": "Historical fiction",
    "page_count": 440
    },
    {
    "title": "The Martian",
    "genre": "Science fiction",
    "page_count": 369
    },
    {
    "title": "The Testaments",
    "genre": "Dystopian fiction",
    "page_count": 432
    },
    {
    "title": "Where the Crawdads Sing",
    "genre": "Mystery, Coming-of-age fiction",
    "page_count": 384
    },
    {
    "title": "Little Fires Everywhere",
    "genre": "Domestic fiction",
    "page_count": 338
    },
    {
    "title": "The Tattooist of Auschwitz",
    "genre": "Historical fiction",
    "page_count": 288
    },
    {
    "title": "The Silent Wife",
    "genre": "Psychological thriller",
    "page_count": 304
    },
    {
    "title": "The Girl with the Dragon Tattoo",
    "genre": "Crime fiction, Mystery",
    "page_count": 672
    },
    {
    "title": "The Night Circus",
    "genre": "Fantasy",
    "page_count": 512
    },
    {
    "title": "The Handmaid's Tale",
    "genre": "Dystopian fiction",
    "page_count": 311
    },
    {
    "title": "Gone Girl",
    "genre": "Mystery, Thriller",
    "page_count": 419
    },
    {
    "title": "Before We Were Yours",
    "genre": "Historical fiction",
    "page_count": 352
    },
    {
    "title": "The Help",
    "genre": "Historical fiction",
    "page_count": 451
    },
    {
    "title": "The Outsider",
    "genre": "Crime fiction, Horror",
    "page_count": 561
    },
    {
    "title": "Big Little Lies",
    "genre": "Mystery, Thriller",
    "page_count": 460
    },{
    "title": "The Catcher in the Rye",
    "genre": "Bildungsroman",
    "page_count": 277
    },
    {
    "title": "Sapiens: A Brief History of Humankind",
    "genre": "Non-fiction, History",
    "page_count": 443
    },
    {
    "title": "The Subtle Art of Not Giving a F*ck",
    "genre": "Self-help",
    "page_count": 224
    },
    {
    "title": "Educated",
    "genre": "Memoir",
    "page_count": 334
    },
    {
    "title": "Girl, Wash Your Face",
    "genre": "Self-help",
    "page_count": 240
    },
    {
    "title": "Atomic Habits",
    "genre": "Self-help",
    "page_count": 319
    },
    {
    "title": "Becoming",
    "genre": "Memoir",
    "page_count": 448
    },
    {
    "title": "Where the Crawdads Sing",
    "genre": "Mystery, Coming-of-age fiction",
    "page_count": 384
    },
    {
    "title": "Born a Crime",
    "genre": "Autobiography, Memoir",
    "page_count": 304
    },
    {
    "title": "The Silent Patient",
    "genre": "Psychological thriller",
    "page_count": 336
    },
    {
    "title": "The Alice Network",
    "genre": "Historical fiction",
    "page_count": 503
    },
    {
    "title": "The Nightingale",
    "genre": "Historical fiction",
    "page_count": 440
    },
    {
    "title": "The Tattooist of Auschwitz",
    "genre": "Historical fiction",
    "page_count": 288
    },
    {
    "title": "Before We Were Yours",
    "genre": "Historical fiction",
    "page_count": 352
    },
    {
    "title": "The Help",
    "genre": "Historical fiction",
    "page_count": 451
    },
    {
    "title": "The Book Thief",
    "genre": "Historical fiction",
    "page_count": 552
    },
    {
    "title": "All the Light We Cannot See",
    "genre": "Historical fiction",
    "page_count": 530
    },
    {
    "title": "The Night Circus",
    "genre": "Fantasy",
    "page_count": 512
    },
    {
    "title": "Circe",
    "genre": "Fantasy, Mythological fiction",
    "page_count": 400
    },
    {
    "title": "The Song of Achilles",
    "genre": "Historical fiction, Mythological fiction",
    "page_count": 352
    }
    ]

    for book in books:
        condition = random.choice(conditionOfBook)
        cursor.execute("INSERT INTO books (name,genre,pages,quality) VALUES (?,?,?,?)", (book["title"],book["genre"].spilt(",")[0],book["page_count"],condition))
        conn.commit()
