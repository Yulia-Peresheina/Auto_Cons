import pytest
import yaml
from checout import checkout
import datetime


with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folder():
    yield checkout(f"mkdir -p {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_ext')}", "")
#   checkout(f"rm -r {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_ext')}", "")


@pytest.fixture()
def make_file():
    for i in range(data.get('count_file')):
        checkout(f"cd {data.get('folder_in')}; touch file{i+1}.txt", "")
        checkout(f"cd {data.get('folder_in')}; dd if=/dev/urandom of=file{i+1}.txt bs={data.get('size_file')} count=1 iflag=fullblock", '')


@pytest.fixture(autouse=True)
def log_info():
    with open('/proc/loadavg', encoding='utf-8') as f_r:
        data_loadavg = f_r.read()
    with open('stat.txt', 'a', encoding='utf-8') as f_w:
        dt_now = datetime.datetime.now()
        result = f'{dt_now} count_file = {data.get("count_file")} size_file = {data.get("size_file")} {data_loadavg = }\n'
        f_w.write(result)


