from app.model.repositories.product_repository import ProductRepository
from app.model.entities.product import Product
from app.model.entities.dtos.product_price_dto import ProductPriceDto

class ProductService:
    _productrepository: ProductRepository = None

    def __init__(self, product_repoistory: ProductRepository) -> None:
        self._productrepository = product_repoistory

    def get_all(self) -> ProductPriceDto:
        return self._productrepository.get_all()
    
    def get(self, **kwargs):
        return self._productrepository.get(**kwargs)

    def add(self, product: Product) -> bool:
        self._productrepository.add(product)
        return True
    
    def get_max_offer_product(self, product:Product):
        return self._productrepository.get_max_offer_product(product)
    
    def get_all_by_max_price(self):
        return self._productrepository.get_all_max_offer_product()
