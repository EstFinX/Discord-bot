import random
def generate():
    symbols="ABCDEFGLMNOPQRSTUVWXYZ0123456789"
    password="".join(random.choices(symbols,k=10))
    print(password)
for i in range(100):
    
    generate()