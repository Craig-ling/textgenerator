import os
import string
import random
from graph import Graph, Vertex

# Initiates user menu for texts directory files
def user_menu():
    b = True

    while b:
        print("Here is a list of the current text files available:")
        textfiles = os.listdir("texts/")

        for i, e in enumerate(textfiles, start=1):
            print("Text file {}: {}".format(i, e))

        print('''Please provide a number to select a text file.
            The text will be scanned to construct a Markov Chain (MC). This model
            is then used to generate text.''')
        try:
            v = int(input("Enter your choice: "))
        except ValueError:
            print("I'm sorry, that is not a valid choice. Please try again")
            continue

        if v > 0 and v <= len(textfiles):
            print(f"You have chosen {v}")
            graph = create_mc(textfiles[v-1])
        else:
            print("That value is out of range. Please try again")
            continue

        print("The MC model has been created.")
        generatetext(graph)

        end = input('''Input Y to choose another text file. Any other input will
                    terminate the program.''')
        end.lower()
        if end == "y":
            continue
        else:
            b = False

        print("Thank you. Until next time")

# Initiates menu for user provided command line argument
def arg_menu(filearg):
    pass

# Processes text and creates Graph object representation of Markov Chain.
# Returns the Graph object.
def create_mc(filename):
    filepath = os.path.realpath(filename)
    g = Graph()
    with open(filepath) as f:
        text_data = f.read()

    text_data = text_data.translate(str.maketrans('', '', string.punctuation))
    text_data = ' '.join(text_data.split())
    text_data = text_data.lower()
    text_data = text_data.split(' ')

    g.add_vertex(text_data[0])

    for i in range(1, len(text_data)):
        g.add_edge(text_data[i-1], text_data[i])

    return g

# Generates text.
def generatetext(graph):
    tloop = True
    while(tloop):
        try:
            wordcount = int(input('''How many words do you desire to generate
                                  for your text?'''))
        except ValueError:
            print("I'm sorry, that isn't a valid input. Try again")
            continue

        if wordcount > 0:
            # Obtain a list of keys for each vertex. Establish the starting 'node' for
            # graph traversal.
            keylist = list(graph.get_vertices())
            currentvertex = graph.get_vertex(keylist[random.randrange(len(keylist))])
            markovtext = currentvertex.value

            # The currentvertex variable changes types. From vertex to string, then back to vertex, 
            # to keep traversing the graph. Acquires string values based on adjacent
            # vertices and the edge weight values that connects them.
            for _ in range(word_count):
                adjacentvertices = list(currentvertex.get_links())
                currentvertex = random.choices(adjacentvertices, weights=currentvertex.get_weights())[0]
                markovtext += " " + currentvertex
                currentvertex = graph.get_vertex(currentvertex)

            print(markovtext)

            more = input("Would you like to generate more text? y/n")
            more.lower()
            if more == "y":
                continue
            else:
                tloop = False


def main():
    print("Greetings! Welcome to the text generator.")

    if not len(sys.argv):
        print("No command line arguments detected.")
        user_menu()


if __name__ == "__main__":
    main()

