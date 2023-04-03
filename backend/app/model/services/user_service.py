from app.model.repositories.user_repository import UserRepository
from app.model.entities.user import User


from werkzeug.security import generate_password_hash


class UserService:
    _userrepository: UserRepository = None

    def __init__(self, user_repoistory: UserRepository) -> None:
        self._userrepository = user_repoistory

    def get_all(self):
        return self._userrepository.get_all()
    
    def get(self, **kwargs):
        return self._userrepository.get(**kwargs)

    def add(self, user: User) -> bool:
        is_exist_user = self._userrepository.get(email=user.email)

        if is_exist_user:
            return False
        
        user.password = generate_password_hash(user.password, method='sha256')
        self._userrepository.add(user)
        return True
        
