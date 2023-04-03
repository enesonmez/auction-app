from app.model.repositories.offer_repository import OfferRepository
from app.model.services.user_service import UserService
from app.model.services.product_service import ProductService
from app.model.entities.offer import Offer


class OfferService:
    _offerrepository: OfferRepository = None
    _user_service: UserService = None
    _product_service: ProductService = None

    def __init__(self, offer_repoistory: OfferRepository, user_service: UserService, product_service: ProductService) -> None:
        self._offerrepository = offer_repoistory
        self._user_service = user_service
        self._product_service = product_service

    def get_all(self):
        return self._offerrepository.get_all()

    def add(self, offer: Offer) -> bool:
        user = self._user_service.get(id=offer.user_id)
        if not user:
            return False
        
        product = self._product_service.get(id=offer.product_id)
        if not product:
            return False
        
        max_price_offer = self._product_service.get_max_offer_product(product)  
        if max_price_offer and offer.price <= max_price_offer.price:
            return False
        
        self._offerrepository.add(offer)
        return True
