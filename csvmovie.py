import csv
with open("csvmovies.csv","w") as f:
    write=csv.writer(f,delimiter=",")
    write.writerow(["Top Gun", "Risky Business", "Minority Report"])
    write.writerow(["Titanic", "The Revenant", "Inception"])
    write.writerow(["Training Day", "Man on Fire", "Flight"])
with open("csvmovies.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))