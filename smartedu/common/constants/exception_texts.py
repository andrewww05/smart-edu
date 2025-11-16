class ExceptionText:
    UNEXPECTED_ERROR = 'Виникла непередбачувана помилка'
    UNEXPECTED_ERROR_DETAILED = staticmethod(lambda err : f'Виникла непередбачувана помилка: {err}')
    WRONG_CREDENTIALS = 'Невірні облікові дані'