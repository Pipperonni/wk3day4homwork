from main import Cart, Item, Shop
import unittest

class ShoppingCartTest(unittest.TestCase):

    def test_add_product(self):
        test_addeing = Shop()
        test_addeing.cart.add("milk", "2", "2.99")
        self.assertEqual(len(test_addeing.cart.items), 1)
        

    def test_product(self):
        product_test = Item("milk", "2", "2.99")
        self.assertEqual(product_test.name, "milk")
        self.assertEqual(product_test.quantity, "2")
        self.assertEqual(product_test.price, "2.99")

    def test_delete(self):
        del_test = Shop()
        del_test.cart.add("milk", "2", "2.99")
        del_test.cart.add("eggs", "5", "4.99")
        del_test.cart.add("bread", "3", "1.99")
        
        del_test.cart.delete("milk")
        self.assertEqual(len(del_test.cart.items), 2)
        


        


unittest.main()