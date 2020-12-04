import subprocess as cmd


def process(fn):

    try:
        cp = cmd.run(f"pytest -s ./tests/test_dash.py --app {fn}", check=True, shell=True)
        print(cp)
    except:
        print("Input dash file can't be compiled successfully.")
        exit(2)
        # return False

    try:
        cp = cmd.run("git add .", check=True, shell=True)
        print("Git add: ")
        print(cp)
        cp = cmd.run(f"git commit -m update user file", check=True, shell=True)
        print("Git commit: ")
        print(cp)

        cp = cmd.run("git push -u origin main -f", check=True, shell=True)
        print("Git push: ")
        print(cp)

    except:
        print("Didn't upload to github. ")
        exit(2)
        # return False


def update_proc(github):

    user_id = 10
    signal_id = 2
    try:
        cp = cmd.run(f"wget -O user{user_id}_signal{signal_id}.html {github}", check=True, shell=True)
        print(cp)
    except:
        print("Download file failed.")

    ''' 
    user_fn = github.split('/')[-1]
    print(user_fn)
    try:
        cp = cmd.run(f"mv {user_fn} user{user_id}_signal{signal_id}.html", check=True, shell=True)
        print(cp)
    except:
        print("Change filename failed.")
    '''
    try:
        cp = cmd.run("git add .", check=True, shell=True)
        print("Git add: ")
        print(cp)
        cp = cmd.run(f"git commit -m 'update user file'", check=True, shell=True)
        print("Git commit: ")
        print(cp)

        cp = cmd.run("git push -u origin main -f", check=True, shell=True)
        print("Git push: ")
        print(cp)

    except:
        print("Didn't upload to github. ")
        # return False

if __name__ == "__main__":
    update_proc("https://github.com/weiluntsai0116/dashboard.github.io/blob/main/user1_signal0.html")
    #process("template.only_dash")
