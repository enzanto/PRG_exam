# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff


world = ["d", "l", "r", "o", "w"]
hello = "hello "


def reverse_word(user_list: list[str]) -> str:
    reversed_list = []
    for i in user_list:
        reversed_list.insert(0, i)
    return "".join(reversed_list)  # returning the reversed list as a string


output_string = hello + reverse_word(world)  # making the first string
splitted_string = output_string.split(sep=" ")  # split the string to reverse
reversed_string_list = list(reversed(splitted_string))  # reversing the list
reversed_string = " ".join(reversed_string_list)  # joining it back together
print(output_string.title())
print("-" * 30)
print(reversed_string.upper())
