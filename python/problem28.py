print("Become the programmer you're meant to be!")
class pizza :
    def __init__(self,ingredients):
        self.ingredients=ingredients
    def pizza_flavours(self,flavour):
        pizza_flavours_dict={"hawian":"name:hawian , ingredients:ham,pianapple", "metafestival":"name:metafestival ,ingredients:beef,metabal,bacon "}
        self.flavour=pizza_flavours_dict[flavour]
        print(self.flavour)        
p1=pizza(["backen","paramesan","ham"])
p1.orderno=1

p2=pizza(["olives","spinach","mushroom"])
p2.orderno=2
print(p1.ingredients)
print(p1.orderno)
print(p2.ingredients)
print(p2.orderno)

flavour=input()
p1.pizza_flavours(flavour)