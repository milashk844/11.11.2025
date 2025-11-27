def is_valid_email(value: str) -> bool:
    """
    Повертає True, якщо email валідний:
    - містить один символ '@'
    - має домен з крапкою: example.com
    - не починається і не закінчується на '@' або '.'
    """
    if not isinstance(value, str):
        return False
    # має бути рівно один '@'
    if value.count('@') != 1:
        return False
    local, domain = value.split('@')
    # не може починатися або закінчуватися на '@' чи '.'
    if not local or not domain:
        return False
    if value[0] in ('@', '.') or value[-1] in ('@', '.'):
        return False
    # домен має містити крапку
    if '.' not in domain:
        return False
    # домен не може починатися або закінчуватися на '.'
    if domain[0] == '.' or domain[-1] == '.':
        return False
    return True

def avg(values: list[float]) -> float:
    """
    Повертає середнє значення списку.
    Якщо список порожній — підіймає ValueError.
    """
    if not values:  # якщо список порожній
        raise ValueError("Список не може бути порожнім")

    return sum(values) / len(values)

def uah_to_usd(amount: float, rate: float) -> float:
    """
    Конвертує гривні у долари.
    Якщо сума або курс <= 0 — підіймає ValueError.
    """

    if amount <= 0.0:
        raise ValueError('Сума не може дорівнювати 0!')
    if rate <= 0.0:
        raise ValueError('Курс не може дорівнювати 0!')

    return round(amount / rate, 2)  # округлення до 2 знаків після коми