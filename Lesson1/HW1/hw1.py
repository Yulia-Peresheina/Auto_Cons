"""Написать функцию на Пайтон, которой передаются в качестве параметров команда и текст.
Функция должна возвращщать True, если команда успешно выполнена и текст найден в ее выводе и
 False в противном случае. Передаваться должна только одна строка,
 разбиение вывода использовать не нужно."""

import subprocess


def task_one(input_text):
    command, text, *other = input_text.split(";")
    text = text.strip()
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    if result.returncode == 0:
        if text in out:
            return True
    return False


if __name__ == "__main__":
    task_one("cat /etc/os-release; 222221")
    task_one("cat /etc/os-release; Jammy")

