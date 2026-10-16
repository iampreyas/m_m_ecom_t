import difflib
PRODUCTS = [
    {"id": "p1", "name":"Oversized Black Hoodie","price":1899,"desc":"Cotton streetwear hoodie","img":""},
    {"id": "p2", "name":"Cargo Pant Olive","price":1499,"desc":"Relaxed tactical cargo","img":""},
    {"id": "p3", "name" :"Graphic Oversized Tee", "price":999,"desc":"Heavyweight cotton tee","category":"Tees","trend_score":91,"img":""}
]
class ProductRAGEngine:
    def search(self,q):
        matches =[p for p in PRODUCTS if q.lower() in p['name'].lower() or q.lower() in p['desc'].lower()]
        return matches if matches else [PRODUCTS[0]]