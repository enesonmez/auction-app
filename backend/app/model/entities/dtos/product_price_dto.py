
class ProductPriceDto:
    id:str
    name:str
    image_url:str
    price: int
    full_name: str
    
    def __init__(self, id, name:str, image_url:str, price:int, full_name: str) -> None: 
        self.id = id
        self.name = name
        self.image_url = image_url
        self.price = price
        self.full_name = full_name

    @property
    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'image_url': self.image_url,
            'price': self.price,
            'email': self.full_name
        }