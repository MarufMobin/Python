class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart ( self , item, price, quantity ):
        self.cart.append({ 'item': item, 'price': price, 'quantity' : quantity })

    def checkout( self, amount ):
        # print(self.cart)
        price = 0
        for item in self.cart:
            price += item['price'] * item['quantity']
        print(price)
        if amount < price:
            return f'Please give me more money { price - amount }'
        elif amount > price:
            return f'here are the items and extra money: { amount - price }'
        else :
            return f'Thank\'s a lot of Here are the items'  
        

shopping = Shopper('Maruf Mobin')
shopping.add_to_cart('TShirt', 400, 3 )
shopping.add_to_cart('Shoes', 899, 4 )
shopping.add_to_cart('Pants', 1400, 2 )

reply = shopping.checkout(7596)
print(reply)



    