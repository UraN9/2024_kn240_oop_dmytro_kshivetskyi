#!/c/Users/Dmytro/AppData/Local/Programs/Python/Python313/python
from sys import argv
import argparse

def call_help():
    print("Ми викликали Help для нашої програми")

def display_version():
    print("Ми вивели версію")

if __name__ == "__main__":
    if False:#if argv[0] == "./__main__.py":
        print(f"Запустились, на першій позиції стоїть {argv[1]}")
        print(f"А на другій позиції {argv[2]}")
    
    #Якщо передали не всі аргументи, програма буде падати
    #І нам потрібні винятки
    #Тому придумали бібліотеку argparse

    parser = argparse.ArgumentParser(
        prog="Тестова програма", 
        description="Експерементуємо з агрументами")
    parser.add_argument("-hh", action="store_true", help="Наш тестовий ключ")
    parser.add_argument("-v", "--version", action="store_true", help="Ми додали нашу Версію")
    args = parser.parse_args()

    #print (parser.print_help())

    if args.hh:
        call_help()

    if args.version:
        display_version()