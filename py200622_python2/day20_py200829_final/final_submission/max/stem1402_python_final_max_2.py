"""
Final Exam: Part 2
"""

# 1.
print('Question 1:')

article = 'Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering,' \
          ' and artificial intelligence concerned with the interactions between computers and human (natural)' \
          ' languages, in particular how to program computers to process and analyze large amounts of natural' \
          ' language data. Challenges in natural language processing frequently involve speech recognition, natural' \
          ' language understanding, and natural-language generation. In the early days, many language-processing' \
          ' systems were designed by symbolic methods, i.e., the hand-coding of a set of rules, coupled with a' \
          ' dictionary lookup:[12][13] such as by writing grammars or devising heuristic rules for stemming. More' \
          ' recent systems based on machine-learning algorithms have many advantages over hand-produced rules: The' \
          ' learning procedures used during machine learning automatically focus on the most common cases, whereas' \
          ' when writing rules by hand it is often not at all obvious where the effort should be directed. Automatic' \
          ' learning procedures can make use of statistical inference algorithms to produce models that are robust' \
          ' to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous' \
          ' input (e.g. with misspelled words or words accidentally omitted). Generally, handling such input' \
          ' gracefully with handwritten rules, or, more generally, creating systems of handwritten rules that make' \
          ' soft decisions, is extremely difficult, error-prone and time-consuming. Systems based on automatically' \
          ' learning the rules can be made more accurate simply by supplying more input data. However, systems based' \
          ' on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is' \
          ' a much more difficult task. In particular, there is a limit to the complexity of systems based on' \
          ' handwritten rules, beyond which the systems become more and more unmanageable. However, creating more' \
          ' data to input to machine-learning systems simply requires a corresponding increase in the number of' \
          ' man-hours worked, generally without significant increases in the complexity of the annotation process.'


def term_frequency(text):
    new_text = text.split()

    # Remove unnecessary words. I don't know how to remove special characters.
    for i in new_text:
        # removed = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'been', 'of']
        removed = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'been', 'of', 'and', 'more', 'to',
                   'by', 'on']

        if i in removed:
            new_text.remove(i)

    # Find word count of every word
    word_count = {}

    for i in new_text:

        if i in word_count:
            pass
        else:
            word_count[i] = new_text.count(i)

    # Change the number into TF

    for i in word_count:
        word_count[i] = word_count[i] / len(text)

        # Find top 3

        values = sorted(word_count.items(), reverse=True, key=lambda x: x[1])

    print(word_count)
    print()
    print(f"3: {values[2]}, 2: {values[1]}, 1: {values[0]}")


term_frequency(article)


# 2.
print()
print('Question 2:')
teams = {'Robert_Master': (220, 340),
         'Montreal Sprite': (320, 270),
         'Smart Maker': (115, 405),
         'Nova Robert': (450, 380),
         '10 Stars': (100, 330)}


def team_ranking(team):
    # Find best score out of the given ones
    for i in team:
        if team[i][0] > team[i][1]:
            team[i] = team[i][0]
        else:
            team[i] = team[i][1]

    # Sort
    ranked_teams = sorted(team.items(), reverse=True, key=lambda x: x[1])

    # Print out the scores
    for i in range(3):
        print(f"#{i + 1}: {ranked_teams[i][0]} with {ranked_teams[i][1]} points")


team_ranking(teams)
