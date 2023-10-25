import csv
filepath = "PyPoll/Resources/election_data.csv"

#we want to open the file, after having shown the path.
fileopen = open(filepath, "r")

count = 0
candidates = []
candidate = []
countvote = []
percentvote = []

with open(filepath, "r") as poll:
    reader = csv.reader(poll, delimiter=",")
    header = next(reader)
    for row in reader:
        count = count + 1
        candidates.append(row[2])
    for a in set(candidates):
        candidate.append(a)
        total = candidates.count(a)
        countvote.append(total)
        percent = (total/count)*100
        percentvote.append(round(percent,3))

    winningcount = max(countvote)
    winner = candidate[countvote.index(winningcount)]

print("Election Results")
print("-----------------------")
print("Total Votes:" + str(count))
print("-----------------------")
for x in range(len(candidate)):
    print(candidate[x] + ": " + str(percentvote[x]) + "% (" + str(countvote[x]) + ")")
print("-----------------------")
print("Winner:" + winner)

with open('analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-----------------------\n")
    text.write("Total Votes:" + str(count) + "\n")
    text.write("-----------------------\n")
    for x in range(len(candidate)):
        text.write(candidate[x] + ": " + str(percentvote[x]) + "% (" + str(countvote[x]) + ")\n")
    text.write("-----------------------\n")
    text.write("Winner:" + winner + "\n")
