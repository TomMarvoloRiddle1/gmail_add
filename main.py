import os
from dotenv import load_dotenv, dotenv_values


def new_entry(): #prompts string and uses .env to create new log

    load_dotenv()
    email = os.getenv("EMAIL_DOMAIN")
    pw = os.getenv("PASSWORD")

    prefix=input()

    new_user = (f"{prefix}@{email}:{pw}")
    return new_user


def all_logs(): #assigns .txt file to PyObject

    with open("sample.txt") as file:

        user_pass = [seta.splitlines() for seta in file]
        return(user_pass)


def main():

    new_logs = []
    lista = all_logs()

    for logs in lista:
        new_logs.append(logs)

    final_logs = []
    for profiles in new_logs:
        final_logs.append(profiles[0])

    new_user = new_entry()
    final_logs.append(new_user)


    # print(final_logs)
    for final_users in final_logs:
        with open("sample.txt", "w") as file:
            file.writelines(final_users)
        print(final_users)




main()
