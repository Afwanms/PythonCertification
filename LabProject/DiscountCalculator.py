def apply_discount(price, discount):
    if not isinstance(price,(int,float)):
        return('The price should be a number')
    elif not isinstance(discount,(int,float)):
        return('The discount should be a number')
    elif  price <= 0:
        return('The price should be greater than 0')
    elif discount < 0 or discount > 100:
        return('The discount should be between 0 and 100')
    else:
        return(price * ((100-discount)/100))

print(apply_discount('string', 30))
print(apply_discount(90,'string'))
print(apply_discount(-90,90))
print(apply_discount(9, -20))
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(50, 100))
print(apply_discount(74.5, 20.0))