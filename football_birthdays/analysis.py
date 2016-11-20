




f = open('fb_players.txt', 'r')
w = open('fb_cleaned.txt', 'w')

for line in f:
	line = line.replace("[", "")
	line = line.replace("]", "")
	line = line.replace("'", "")
	line = line[3:]
	line = line.replace("(", "")
	line = line.replace(")", "")
	if len(line) > 7:
		w.write(line)
f.close()
w.close()
