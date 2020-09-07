"""
stem1402_python_final_p1_ken
Ken

"""



text = """Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.
Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural-language generation.
In the early days, many language-processing systems were designed by symbolic methods, i.e., the hand-coding of a set of rules, coupled with a dictionary lookup:[12][13] such as by writing grammars or devising heuristic rules for stemming.
More recent systems based on machine-learning algorithms have many advantages over hand-produced rules:
The learning procedures used during machine learning automatically focus on the most common cases, whereas when writing rules by hand it is often not at all obvious where the effort should be directed.
Automatic learning procedures can make use of statistical inference algorithms to produce models that are robust to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous input (e.g. with misspelled words or words accidentally omitted). Generally, handling such input gracefully with handwritten rules, or, more generally, creating systems of handwritten rules that make soft decisions, is extremely difficult, error-prone and time-consuming.
Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much more difficult task. In particular, there is a limit to the complexity of systems based on handwritten rules, beyond which the systems become more and more unmanageable. However, creating more data to input to machine-learning systems simply requires a corresponding increase in the number of man-hours worked, generally without significant increases in the complexity of the annotation process."""



def tfcalculator(string):
    list1 = list(string)
    word_count = dict()
    result = []

    while True:
        done = True
        for character in list1:
            # Remove all except spaces and letters so we can do split() later
            if not character.isalpha() and not character.isspace():
                done = False
                try:
                    while True: list1.remove(character)
                except:
                    pass
        if done: break

    string1 = "".join(list1)
    # case insensitive
    string2 = string1.casefold()



    list2 = string2.split()
    for word in list2:
        # If word isn't a key inside dictionary, it will add it automatically
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1


    # key= works by instead of looking at key, it looks at value
    for w in sorted(word_count, key=word_count.get, reverse=True):
        result += w, word_count[w]

    return result


print("Word frequency Calculator")
count = 1
print("---Top 3---\n")
for data in tfcalculator(text):
    print(data, "", end="")
    if count == 6: print("\n\n---Rest---")
    count += 1
    if count % 2 == 1:
        print("")


