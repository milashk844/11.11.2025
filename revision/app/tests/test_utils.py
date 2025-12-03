from app.utils.utils import is_valid_email
import pytest

# валідний email
def test_is_valid_email_1():
    assert is_valid_email("user@example.com")
    assert is_valid_email("name.surname@domain.org")
# декілька @
def test_is_valid_email_2():
    assert not is_valid_email('user@@example.com')
    assert not is_valid_email('user@number@2.com')
# відсутня крапка
def test_is_valid_email_3():
    assert not is_valid_email('user@examplecom')
    assert not is_valid_email('user@domain')
# порожній рядок
def test_is_valid_email_4():
    assert not is_valid_email('')

from app.utils.utils import avg

# нормальний список
def test_afg_1():
    values = [1.0, 2.0, 3.0, 4.0]
    assert avg(values) == 2.5
# в списку тільки 1 елемент
def test_afg_2():
    values = [10.0]
    assert avg(values) == 10.0
# негативні числа
def test_afg_3():
    values = [-1.0, -2.0, -3.0, -4.0]
    assert avg(values) == -2.5
# порожній список
def test_afg_4():
    with pytest.raises(ValueError):
        avg([])

from app.utils.utils import uah_to_usd

# звичайний кейс
def test_uah_to_usd_1():
    assert uah_to_usd(1000, 40) == 25.0
# неправильний курс
def test_uah_to_usd_2():
    with pytest.raises(ValueError):
        uah_to_usd(1000, 0)
# неправильна сума
def test_uah_to_usd_3():
    with pytest.raises(ValueError):
        uah_to_usd(0, 40)
# дуже великі значення
def test_uah_to_usd_4():
    result = uah_to_usd(1_000_000, 40)
    result == 25000.0
# точна робота з float
def test_uah_to_usd_5():
    result = uah_to_usd(1234.56, 36.6)
    # перевіряємо з допуском
    assert pytest.approx(result, 0.01) == 33.72