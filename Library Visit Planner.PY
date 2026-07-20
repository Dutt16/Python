Lending_period = input("Please enter the days of you having the book: ")
if Lending_period >= 10:
    print("Good, you still have a few days to read the book. Enjoy!")
elif Lending_period >= 15:
    print("Perfect, now you can return your book to the library. Thank You!")
else:
    print("Ohh, your book's return day has already past due so you will have to pay late fees. Good luck!")