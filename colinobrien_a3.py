#colinobrien_a3.py
val=input("Let me help you choose a movie or show. Type in a number 1-10:")
out = " "
if val is 1:
    out="Star Wars: A New Hope"
elif val is 2:
    out="The Lord of the Rings: Two Towers"
elif val is 3:
    out="The Lord of the Rings: The Return of the King"
elif val is 4:
    out="The Dark Night"
elif val is 5:
    out="Rise of the Planet of the Apes"
elif val is 6:
    out="Dawn of the Planet of the Apes"
elif val is 7:
    out="War for the Planet of the Apes"
elif val is 8:
    out="Watchmen"
elif val is 9:
    out="Captain America: The First Avenger"
else: out="Iron Man"
fin_out=str.strip(out)
print("You should watch: " + fin_out)
