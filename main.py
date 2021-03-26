import os
import sys
import string
import random
from graph import Graph


# Initiates user menu for text files in the /texts/ directory.
def user_menu():
    b = True

    while b:
        print("Here is a list of the current text files available:")
        textfiles = os.listdir("texts/")

        for i, e in enumerate(textfiles, start=1):
            print("Text file ({}): {}".format(i, e))

        print("Please provide a number to select a text file."
              " The text will be scanned to construct a Markov Chain (MC). This"
              " model is then used to generate text.")
        try:
            v = int(input("Enter your choice: "))
        except ValueError:
            print("I'm sorry, that is not a valid choice. Please try again.")
            continue

        if 0 < v <= len(textfiles):
            print(f"You have chosen {v}.")
            graph = create_mc(textfiles[v - 1])
        else:
            print("That value is out of range. Please try again.")
            continue

        generatetext(graph)

        end = input("Input Y to choose another text file. Any other input will"
                    " terminate the program: ")
        if end.lower() == "y":
            continue
        else:
            b = False

        print("Thank you. Until next time.")


# Initiates menu for user provided command line argument
def arg_menu(filearg):
    mc = create_mc(filearg)
    generatetext(mc)
    response = input("Would you like to choose another text to create a"
                     " different model? Y/y will accept. Any other input will"
                     " exit: ")
    if response.lower() == "y":
        user_menu()
    else:
        print("Thank you, farewell.")


# Receives a string text input to remove all punctuation and capitalization.
# Returns a list of all the words in the string input.
def clean_text(text_data):
    text_data = text_data.translate(str.maketrans('', '', string.punctuation))
    text_data = ' '.join(text_data.split())
    text_data = text_data.lower()
    text_data = text_data.split(' ')
    return text_data


# Processes text and creates Graph object representation of Markov Chain.
# Returns the Graph object.
def create_mc(filename):
    if "texts/" not in filename:
        filename = "texts/" + filename
        filepath = os.path.realpath(filename)
    else:
        filepath = filename

    g = Graph()
    with open(filepath) as f:
        text_data = f.read()

    text_data = clean_text(text_data)

    g.add_vertex(text_data[0])

    for i in range(1, len(text_data)):
        g.add_edge(text_data[i - 1], text_data[i])

    print("The Markov Chain (MC) model has been created.")
    return g


# Receives a Graph object and integer as input to create and return a string of words.
def createstring(graph, wordcount):
    # Obtain a list of keys for each vertex. Establish the starting 'node' for
    # graph traversal.
    keylist = list(graph.get_vertices())
    currentvertex = graph.get_vertex(keylist[random.randrange(len(keylist))])
    markovtext = currentvertex.value

    # The currentvertex variable changes types. From vertex to string, then back to vertex,
    # to keep traversing the graph. Acquires string values based on adjacent
    # vertices and the edge weight values that connects them.
    for _ in range(wordcount - 1):
        adjacentvertices = list(currentvertex.get_links())
        currentvertex = random.choices(adjacentvertices, weights=currentvertex.get_weights())[0]
        markovtext += " " + currentvertex
        currentvertex = graph.get_vertex(currentvertex)

    return markovtext


# Receives a graph object as input. This graph is a Markov Chain model
# representation. The user is asked to provide an integer. Text containing
# an amount of words equal to this integer is created using the graph.
def generatetext(graph):
    tloop = True
    while tloop:
        try:
            word_count = int(input("How many words would you like to generate"
                                   " for your text?: "))
        except ValueError:
            print("I'm sorry, that isn't a valid input. Try again.")
            continue

        if word_count > 0:
            markovtext = createstring(graph, word_count)
            print(markovtext)

            more = input("Would you like to generate more text? Y/y will"
                         " accept. Any other input will decline: ")
            if more.lower() == "y":
                continue
            else:
                tloop = False
        else:
            print("Please enter an integer greater than 0 to produce text.")


def main():
    print("Greetings! Welcome to the text generator.")
    if len(sys.argv) < 2:
        print("No command line arguments detected.")
        user_menu()
    else:
        print("Accessing file... " + str(sys.argv[1]))
        arg_menu(sys.argv[1])


if __name__ == "__main__":
    main()
