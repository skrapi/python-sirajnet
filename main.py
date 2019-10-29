from textblob import Word
import numpy as np 
import argparse

def make_mine(yours, swap_rate):
    mine = []

    for string_word in yours:
        word_object = Word(string_word)

        if np.random.randint(swap_rate) == 0:
            meaning_count = len(word_object.synsets)
            if meaning_count > 0:
                meaning_selected = np.random.randint(meaning_count)
                synonym_count = len(word_object.synsets[meaning_selected].lemmas())
                mine += [word_object.synsets[meaning_selected].lemmas()[np.random.randint(synonym_count)].name()]
            else:
                mine += [string_word]
        else:
            mine += [string_word]

    return mine

parser = argparse.ArgumentParser()
parser.add_argument("--text", help="your original text", type=str, default="SaaS has dramatically lowered the intrinsic total cost of ownership for adopting software, solved scaling challenges and taken away the burden of issues with local hardware. ")
parser.add_argument("--chance", help="one in N swap chance", type=int, default=5)
args = parser.parse_args()

your_text = args.text.split()
my_text = make_mine(your_text, args.chance)

my_text = ' '.join(my_text)
print(my_text)