def calc_div(x, y):
    try:
        print(int(x) / int(y))
    # except Exception:
    #     print('something happened')
    # except (ZeroDivisionError, ValueError) as err:
    #     print(f'x: {x}, y: {y}')
    #     raise err
    # except (ZeroDivisionError, ValueError) as err:
    #     print('Some error happened!')
    #     print(err)
    except ZeroDivisionError:
        print('не дели на ноль!')
    except ValueError:
        print('Введен текст вместо числа')
    else:
        print('вычисление прошло успешно')
    finally:
        print('Вычисление завершено')


calc_div('3', '5')
calc_div('5', '0')
calc_div('5', 'cslkjdflsdkjf')
calc_div('5', '8')
