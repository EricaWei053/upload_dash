import threading
import subprocess
import webbrowser

import time

def run_dash():
    """
    Run dash application in this function
        and then open then dash url in the new window.
    :return: None
    """

    proc = subprocess.Popen(['python', './template/only_dash.py'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    t = threading.Thread(target=output_reader, args=(proc,))
    t.start()

    try:
        time.sleep(3)
        webbrowser.open('http://localhost:8050')
        # assert b'Directory listing' in resp.read()
        time.sleep(10)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=1)
            print('== subprocess exited with rc =%d', proc.returncode)
        except subprocess.TimeoutExpired:
            print('subprocess did not terminate in time')
    t.join()

    return None


# helper functions
def output_reader(proc):
    """
    Check if subprocess works correctly.
    :param proc: process
    :return: None
    """
    for line in iter(proc.stdout.readline, b''):
        print('got line: {0}'.format(line.decode('utf-8')), end='')


if __name__ == "__main__":
    run_dash()