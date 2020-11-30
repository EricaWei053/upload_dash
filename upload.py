
import subprocess as cmd

def upload():
    cp = cmd.run("git add .", check=True, shell=True)
    print("Git add: ")
    print(cp)

    response = input("Do you want to use the default message for this commit?([y]/n)\n")
    message = "update the repository"
    if response.startswith('n'):
        message = input("What message you want?\n")

    cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
    print("Git commit: ")
    print(cp)

    cp = cmd.run("git push -u origin main -f", check=True, shell=True)
    print("Git push: ")
    print(cp)


if __name__ == "__main__":
    upload()
