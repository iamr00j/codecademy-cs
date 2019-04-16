letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0
#print(letter_to_points)
def score_word(word):
  point_total = 0
  for letters in word:
    point_total += letter_to_points.get(letters,0)
  return point_total
#brownie_points = print(score_word("BROWNIE"))

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "LexiCon": ["ERASER", "BELLY", "HUSKY"], "ProfReader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for players, word in player_to_words.items():
  player = players
  words = word
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

