import yaml
import pytest
from checout import checkout


with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestsSeminar3Positive:
    def test_step4(self, make_folder, make_file):
        # test 4 тест на архивацию
        assert checkout(f'cd {data.get("folder_in")}; 7z a {data.get("folder_out")}archive', 'Everything is Ok'), 'Test 4 FAIL'

    def test_step5(self, make_folder):
        # test 5 тест на удаление файла
        assert checkout(f'cd {data.get("folder_out")}; 7z d ./archive.7z file1.txt', 'Everything is Ok'), 'Test 5 FAIL'

    def test_step6(self, make_folder):
        # test 6 тест на проверку команды вывода списка файлов
        assert checkout(f' 7z l {data.get("folder_out")}archive.7z', 'Listing archive'), 'Test 6 FAIL'

    def test_step7(self):
        # test 7 тест на извлечение файлов
        assert checkout(f'cd {data.get("folder_ext")}; 7z x {data.get("folder_out")}archive.7z', 'Everything is Ok'), 'Test 7 FAIL'



if __name__ == '__main__':
    pytest.main(["-vv"])
