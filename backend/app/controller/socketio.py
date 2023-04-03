from flask_socketio import SocketIO, emit
from app.model.entities.offer import Offer

from app.model import offer_service, product_service

socket_io = SocketIO()


@socket_io.on('connect')
def test_connect():
    # product_price = product_service.get_all_by_max_price()
    # data = [i.serialize for i in product_price]
    # print(data)
    # emit('offer_announce', data, broadcast=True)
    print("connect")


@socket_io.on('offer')
def handle_offer(json):
    offer = Offer(json['user_id'], json['product_id'], json['price'])
    result = offer_service.add(offer)
    if result:
        product_price = product_service.get_all_by_max_price()
        data = [i.serialize for i in product_price]

        print('received json: ', data)
        emit('offer_announce', data, broadcast=True)
    else:
        return
