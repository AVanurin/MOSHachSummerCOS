def status_to_str(code: int):
    if code == 0:
        return "Готовиться к регистрации"
    elif code == 1:
        return "Находится в обработке"
    elif code == 2:
        return "Успешно  завершена"
    elif code == 4:
        return "Закрыта"
    else:
        return "Принудительно закрыта"