# Library commandline scripts

- ./rebuild.sh
- python3 library.py getAvailableBooks
- python3 library.py getAvgPages
- python3 library.py addCardholder --name 'MacKay Roy' --username mackayroy
- python3 library.py addBook --name 'Whispers in the Mist' --genre 'Mystery' --pages 137 --quality 'Good' --availability 1
- python3 library.py checkOutBook --username mackayroy --bookId --quality "Good"
- python3 library.py returnBook --username mackayroy --bookId
- python3 library.py getNewBooks --username 'mackayroy'
- python3 library.py mostPopular
- python3 library.py bestCarer
