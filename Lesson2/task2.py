import subprocess
import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test 1

    assert checkout('cd /home/yulia/tst; 7z a ../out/arx2', 'Everithing is OK'), 'Test 1 FAIL'


def test_step2():
    # test 2

    assert checkout('cd /home/yulia/out; 7z e arx2.7z -o/home/yulia/folder1 -y', 'Everithing is OK'),\
        'Test 2 FAIL'


def test_step3():
    # test 3

    assert checkout('cd /home/yulia/out; 7z t arx2.7z', 'Everithing is OK')