# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff


def hide_password(password: str) -> str:
    hidden_pass = ""
    for i in password:
        hidden_pass += "*"
    return hidden_pass


def valid_password(password: str) -> bool:
    if len(password) < 3:
        return False
    else:
        return True


def same_password(password: str, confirmation: str) -> bool:
    if password != confirmation:
        return False
    else:
        return True


if __name__ == "__main__":
    while True:
        name = input("Please enter your name: ")
        password = input("Enter your password: ")
        valid_pass = valid_password(password)
        if not valid_pass:
            print("Password needs to be minimum 3 characters long!")
            continue
        confirmation = input("Confirm password: ")
        same_pass = same_password(password, confirmation)
        if not same_pass:
            print("Passwords do not match")
            continue
        if valid_password and same_password:
            print(f"Welcome {name},", end=" ")
            print(
                f"your password was changed and is securely stored as {hide_password(password)}, ({len(hide_password(password))} charecters)"
            )
            break
