"""
Final exam p2
"""

import re

# Problem 1

article = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and
    artificial intelligence concerned with the interactions between computers and human (natural) languages, in
    particular how to program computers to process and analyze large amounts of natural language data.
    Challenges in natural language processing frequently involve speech recognition, natural language understanding, 
    and natural-language generation.
    In the early days, many language-processing systems were designed by symbolic methods, i.e., the hand-coding of 
    a set of rules, coupled with a dictionary lookup:[12][13] such as by writing grammars or devising heuristic rules 
    for stemming.
    More recent systems based on machine-learning algorithms have many advantages over hand-produced rules:
    The learning procedures used during machine learning automatically focus on the most common cases, whereas when 
    writing rules by hand it is often not at all obvious where the effort should be directed.
    Automatic learning procedures can make use of statistical inference algorithms to produce models that are robust 
    to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous input 
    (e.g. with misspelled words or words accidentally omitted). Generally, handling such input gracefully with 
    handwritten rules, or, more generally, creating systems of handwritten rules that make soft decisions, is 
    extremely difficult, error-prone and time-consuming.
    Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. 
    However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the 
    rules, which is a much more difficult task. In particular, there is a limit to the complexity of systems based on 
    handwritten rules, beyond which the systems become more and more unmanageable. However, creating more data to input 
    to machine-learning systems simply requires a corresponding increase in the number of man-hours worked, generally 
    without significant increases in the complexity of the annotation process.
"""

remove_words = ["the", "a", "an", "is", "are", "was", "were", "been", "of", "and", "in", "to", "then", "by", "on", "or", "be",\
                "that", "more"]
reg = re.compile("[^a-z ]")
article = reg.sub("", article.lower())
article = list(filter(lambda x: x not in remove_words, article.split()))
list_1 = article
dict_1 = {}

for i in list_1:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

for i in dict_1:
    print(f"{i} {dict_1[i]}")
print()
print()
dict_1 = sorted(dict_1.items(), key=lambda x: x[1])
for i in range(1, 4):
    print(f"{i}. {dict_1[-i][0]} {dict_1[-i][1]}")


# Problem 2

print()
print()
print("Problem 2")
scores = [("Robert Master", 220, 340),
          ("Montreal Sprite", 320, 270),
          ("Smart Marker", 115, 405),
          ("Nova Robert", 450, 380),
          ("10 Stars", 100, 330)]

scores.sort(key=lambda x: max(x[1], x[2]))

for i in range(1, len(scores) + 1):
    print(f"{i}. {scores[-i][0]} {max(scores[-i][1], scores[-i][2])}")