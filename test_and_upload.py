import subprocess as cmd


def test_and_upload_for_create(create_n_clicks, user_id, signal_id, signal_description, github):

    # 0.1 git pull, update files from github first
    try:
        cp = cmd.run(f"git pull origin main", check=True, shell=True)
        print(cp)
    except:
        print("Update with github failed.")
        return 'Create: Update with github failed.'

    # 0.2. Process link to be raw data link

    # db_access.insert_signal(user_id, signal_id, signal_description)
    contents_list = github.split('/')
    raw_link = None
    if "github.com" not in contents_list or 'blob' not in contents_list:
        print("The provided github link is invalid. ")
        return "Create: The provided github link is invalid."
    else:
        github_idx = contents_list.index("github.com")
        raw_lists = contents_list[github_idx + 1:]
        raw_lists.remove('blob')

        raw_lists.insert(0, "https://raw.githubusercontent.com")
        raw_link = "/".join(raw_lists)
        print(raw_link)

    # 1. download from github link and modify the filename as we need
    try:
        cp = cmd.run(f"wget -O user{user_id}_signal{signal_id}.html {raw_link}", check=True, shell=True)
        print(cp)
    except:
        print("Download file failed.")
        return 'Create: Download file failed.'

    # 3. upload to github
    try:
        cp = cmd.run("git add .", check=True, shell=True)
        print("Git add: ")
        print(cp)
        cp = cmd.run(f"git commit -m 'upload user file'", check=True, shell=True)
        print("Git commit: ")
        print(cp)

        cp = cmd.run("git push origin main", check=True, shell=True)
        print("Git push: ")
        print(cp)
        # db_access.insert_signal(user_id, signal_id, signal_description)
        return 'Create: Pass!'

    except:
        print("Didn't upload to github. ")
        return "Create: Upload to github failed."

'''
def test_and_upload_for_modify(modify_n_clicks, user_id, signal_id, signal_description, github):
    # 1. download from github link and modify the filename as we need
    try:
        cp = cmd.run(f"wget -O user{user_id}_signal{signal_id}.html {github}", check=True, shell=True)
        print(cp)
    except:
        print("Download file failed.")
        return False

    # 2. Modify name to be user{user_id}_signal{signal_id}.html
    user_fn = github.split('/')[-1]
    try:
        cp = cmd.run(f"mv {user_fn} user{user_id}_signal{signal_id}.html", check=True, shell=True)
        print(cp)
    except:
        print("Change filename failed.")
        return False

    # 3. upload to github
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
        return True

    except:
        print("Didn't upload to github. ")
        return False
'''


test_and_upload_for_create(1, 2, 1, "test", "https://github.com/weiluntsai0116/"
                                            "dashboard.github.io/blob/main/user1_signal1.html")
