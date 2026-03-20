# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff

import os

devices = [
    ["device", "type", "dateadded", "IP Address"],
    ["computer", "pc", "1591259971", "192.168.100.1"],
    ["android phone", "phone", "1591259971", "192.168.100.3"],
    ["samsung phone", "phone", "1591259971", "192.168.100.4"],
]

csvfile = "device.csv"


def csv_writer(csvfile: str, content: list[str] | str) -> None:
    mode = "w"
    file = None
    try:
        if os.path.exists(csvfile):
            mode = "a"
        else:
            mode = "w"
        file = open(csvfile, mode)
        if isinstance(content, list):
            for line in content:
                file.writelines(line + "\n")
        elif isinstance(content, str):
            file.write(content)
    except FileNotFoundError as e:
        print("File was not found: ", e)
    except Exception as e:
        print("an error occured", e)

    finally:
        if file != None:
            file.close()
            print("File saved and closed")


def list_to_csv(input_list: list) -> list[str] | None:
    sanitized_list = []
    try:
        for items in input_list:
            new_string = ",".join(items)
            sanitized_list.append(new_string)
        return sanitized_list
    except Exception as e:
        print("An error has occured: ", e)


sanitized_strings = list_to_csv(devices)

csv_writer(csvfile, sanitized_strings)
