from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

from tqdm import tqdm


def main():
    print(get_employees())
    print(calculate_salary())
    print('Current time: ', datetime.now())


if __name__ == '__main__':
    main()
    for i in tqdm(range(int(9e6))):
        pass
