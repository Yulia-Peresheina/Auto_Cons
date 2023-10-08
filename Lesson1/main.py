import subprocess


def main():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        print(out)
        if 'Jammy' in out and '22.04.1' in out:
            print('Success')
    else:
        print("Fail")


if __name__ == "__main__":

    main()
