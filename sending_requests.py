import requests
import data
import configuration

#Формируем заказ

def post_the_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATE_PATH,
                         json=data.orders_body)

#После формирования нового заказа фиксируем его трек-номер:

def get_the_new_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track_number})
