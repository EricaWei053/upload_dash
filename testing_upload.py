
import subprocess as cmd



def process(fn):

    cp = cmd.run("pytest -v -s ./tests/test_dash.py --app template.only_dash", check=True, shell=True)
    print(cp)


    cp = cmd.run("git add .", check=True, shell=True)
    print("Git add: ")
    print(cp)

    message = "update the repository"

    cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
    print("Git commit: ")
    print(cp)

    cp = cmd.run("git push -u origin main -f", check=True, shell=True)
    print("Git push: ")
    print(cp)


if __name__ == "__main__":
    process('template.dash_only')