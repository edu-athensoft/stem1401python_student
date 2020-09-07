"""
Final exam p2
"""

# Problem 1

article = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, " \
          "and artificial intelligence concerned with the interactions between computers and human (natural) languages, " \
          "in particular how to program computers to process and analyze large amounts of natural language data. Challenges " \
          "in natural language processing frequently involve speech recognition, natural language understanding, " \
          "and natural-language generation. In the early days, many language-processing systems were designed by symbolic methods, " \
          "i.e., the hand-coding of a set of rules, coupled with a dictionary lookup:[12][13] such as by writing grammars " \
          "or devising heuristic rules for stemming. More recent systems based on machine-learning algorithms have many " \
          "advantages over hand-produced rules: The learning procedures used during machine learning automatically focus on " \
          "the most common cases, whereas when writing rules by hand it is often not at all obvious where the effort should be " \
          "directed. Automatic learning procedures can make use of statistical inference algorithms to produce models that are " \
          "robust to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous input " \
          "(e.g. with misspelled words or words accidentally omitted). Generally, handling such input gracefully with handwritten rules, " \
          "or, more generally, creating systems of handwritten rules that make soft decisions, is extremely difficult, error-prone and " \
          "time-consuming. Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. " \
          "However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much " \
          "more difficult task. In particular, there is a limit to the complexity of systems based on handwritten rules, beyond which the systems " \
          "become more and more unmanageable. However, creating more data to input to machine-learning systems simply requires a corresponding " \
          "increase in the number of man-hours worked, generally without significant increases in the complexity of the annotation process.".lower()

remove_words = ["the", "a", "an", "is", "are", "was", "were", "been", "of", "and", "in", "to", "then", "by", "on", "or", "be",\
                "that", "more"]
list_1 = []
tuple_1 = ()
article_keeper = ""

print("Problem 1 part 1")
article = list(filter(lambda x: x not in remove_words, article.split()))
article = list(filter(lambda x: ("(" or ")") not in x, article))
for i in range(len(article)):
    if article[i][-1] == "]":
        while article[i][-1] == "]":
            article[i] = article[i][:-4]
    if article[i][-1] not in "abcdefghijklmnopqrstuvwxyz":
        article[i] = article[i][:-1]
for i in range(len(article)):
    article_keeper = article[i]
    if article[i] == 0:
        continue
    else:
        print(f"{article[i]} {article.count(article[i])}")
    tuple_1 = (article[i], article.count(article[i]))
    list_1.append(tuple_1)
    for j in range(len(article)):
        if article[j] == article_keeper:
            article[j] = 0

print()
print()
print("Problem 1 part 2")
list_1.sort(key=lambda x: x[1])
for i in range(1, 4):
    print(f"{i}. {list_1[-i][0]}, {list_1[-i][1]}")



# Problem 2

print()
print()
print("Problem 2")
scores = [("Robert Master", 220, 340),
          ("Montreal Sprite", 320, 270),
          ("Smart Marker", 115, 405),
          ("Nova Robert", 450, 380),
          ("10 Stars", 100, 330)]

scores.sort(key=lambda x: x[1] + x[2])
scores.reverse()

for i in range(1, len(scores) + 1):
    print(f"{i}. {scores[i-1][0]}, {scores[i-1][1] + scores[i-1][2]}")












