import sending_requests

#Подкользин Михаил, 10-я когорта - Финальный проект. Инженер по тестированию плюс.
#Пробуем получить заказ по его трек-номеру

def get_track_number():
    track_number = sending_requests.post_the_new_order()
    return track_number.json() ["track"]

#Проверяем, что ответ пришёл с кодом "200"
def test_create_orders_track():
    track_number = get_track_number()
    get_response = sending_requests.get_the_new_order(track_number)
    assert get_response.status_code == 200