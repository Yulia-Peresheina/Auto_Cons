
import pytest
from checout import checkout

folder_in = '/home/yulia/folder_in/'
folder_out = '/home/yulia/folder_out/'
folder_ext = '/home/yulia/folder_ext/'


#def test_step1():
#def test_step2():
    # test 2



#def test_step3():
    # test 3



def test_step4():
    # test 4 тест на архивацию
    assert checkout(f'cd {folder_in}; 7z a {folder_out}archive', 'Everything is Ok'), 'Test 4 FAIL'


def test_step5():
    # test 5 тест на удаление файла
    assert checkout(f'cd {folder_out}; 7z d ./archive.7z fail1.txt', 'Everything is Ok'), 'Test 5 FAIL'


def test_step6():
    # test 6 тест на проверку команды вывода списка файлов
    assert checkout(f' 7z l {folder_out}archive.7z', 'fail2.txt'), 'Test 6 FAIL'


def test_step7():
    # test 7 тест на извлечение файлов
    assert checkout(f'cd {folder_ext}; 7z x {folder_out}archive.7z', 'Everything is Ok'), 'Test 7 FAIL'


