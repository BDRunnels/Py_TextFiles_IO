# OLD WAY OF DOING IT (open(file, r for read))
# jabber = open('Jabberwocky.txt', 'r')  # r stands for read.
#
# for line in jabber:
#     # print(line, end="")  # gets rid of newline character (/n) after each line
#     print(line.rstrip())  # strips whitespace characters, does SAME AS ABOVE
#     # print(len(line))
#
# jabber.close()

# NEW WAY using 'with' statement (auto closes file, like try with resources in Java)

                # 1)
# with open("Jabberwocky.txt", "r") as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#
#     # Three Methods for Reading from File (just like for loop above)
#     lines = jabber.readlines()  # returns a list containing strings
#
# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end="")  # do processing in reverse order

                # 2)
# with open("Jabberwocky.txt") as jabber:
#     text = jabber.read()  # returns string, NOT list
#
# print(text)
# for char in reversed(text):
#     print(char, end="")

                # 3)
with open("Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break

print("*" * 80)

with open("Jabberwocky.txt", encoding="utf-8") as jabber:
    for line in jabber:
        print(line.rstrip())
