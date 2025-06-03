import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    sqft = float(input('Введите sqft: '))
    baths = int(input('Введите baths: '))
    school_rating_mean = float(input('Введите school_rating_mean: '))
    school_distance_min = float(input('Введите school_distance_min: '))
    state_CA = float(input('Введите state_CA: '))
    r = requests.post('http://localhost:5000/predict', json=[baths, sqft, school_rating_mean, school_distance_min, state_CA])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)