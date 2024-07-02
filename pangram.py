number = input("write down a number: ")
pangram = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0
}
for i in number:
    if i in pangram:
        pangram[i] += 1
Pangram = True     
for count in pangram.values():
    if count == 0:
        Pangram = False
if Pangram:
    print("entered number is a Pangram")
else:
    print("entered number is not a Pangram")

