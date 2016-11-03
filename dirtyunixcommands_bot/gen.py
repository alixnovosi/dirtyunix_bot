import os
import random

from collections import defaultdict

HERE = os.path.abspath(os.path.dirname(__file__))
LEADER_FILE = os.path.join(HERE, "leader_cmds")
FOLLOWER_FILE = os.path.join(HERE, "follower_cmds")

GOOD_FILE = os.path.join(HERE, "good")


def gen_dict():
    """Generate dictionary from file."""

    dict = defaultdict(list)

    with open(GOOD_FILE) as f:

        for line in f:
            if line is None or line == "":
                break

            words = line.split()

            first = words[0]
            dict["$"].append(first)

            for i, word in enumerate(words[1:]):
                dict[words[i-1]].append(word)

                if i-2 > 0:
                    dict[tuple(words[i-2:i])].append(word)

    return dict


def gen_markov(dict=None):
    """Generate a tweet by markov-chaining."""
    if dict is None:
        dict = gen_dict()

    phrase = []
    last = random.choice([key for key in dict.keys() if len(key) > 1 and isinstance(key, tuple)])

    phrase.extend(last)

    for i in range(random.choice(range(7, 14))):

        options = dict[last]
        if options is None or options == []:
            break

        new = tuple([last[-1], random.choice(options)])

        phrase.extend(new)

        last = new

    return " ".join(phrase)


def gen_naive_random():
    """Generate a <= tweet-sized dirty command."""

    cmd = random_cmd()

    # Periodically staple some commands together.
    if random.choice(range(5)) == 2:
        second_cmd = random_cmd()

        return "; ".join([cmd, second_cmd])

    else:
        return cmd


def random_cmd():
    """Get a random dirty command."""
    leader = random_leader()
    following = random_followers()

    return " ".join([leader, following])


def random_leader():
    """Get random command from leader commands file."""
    return random_line(LEADER_FILE)


def random_followers():
    """Get random command(s) from leader commands file."""
    count = random.choice(range(2, 5))
    lines = []

    while count > 0:
        lines.append(random_line(FOLLOWER_FILE))
        count -= 1

    return " ".join(lines)


def random_line(file_path):
    """Get random line from a file."""
    # Fancy alg from http://stackoverflow.com/a/35579149 to avoid loading full file.
    line_num = 0
    selected_line = ""
    with open(file_path) as f:
        while 1:
            line = f.readline()
            if not line:
                break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line

    return selected_line.strip()

if __name__ == "__main__":
    dict = gen_dict()

    print("Rand")
    for i in range(8):
        print(gen_naive_random())

    # print()
    # print("markov")
    # for i in range(8):
    #     print(gen_markov(dict=dict))
