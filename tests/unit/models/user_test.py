from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', "Username does not match that given in the constructor argument.")
        self.assertEqual(user.password, 'abcd', "Password does not match that given in the constructor argument.")
