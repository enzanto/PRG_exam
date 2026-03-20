# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff


def multiply_myself(target_value: int, multiplication: int) -> int:
    answer = target_value
    try:
        for i in range(multiplication - 1):
            answer *= target_value
        print(
            f"{target_value} multiplied by itself {multiplication} times is equal to {answer}"
        )
    except TypeError as e:
        print("Only integers allowed: ", e)
    except Exception as e:
        print("An error has occured: ", e)
    return answer


def min_max_length(user_list: list[int | float]) -> tuple:
    minimum = min(user_list)
    maximum = max(user_list)
    length = len(user_list)
    return (minimum, maximum, length)
