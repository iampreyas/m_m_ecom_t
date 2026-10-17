import difflib
PRODUCTS = [
    {"id": "p1", "name":"Oversized Black Hoodie","price":1899,"desc":"Cotton streetwear hoodie","category":"Hoodies","trend_score":94,"img":""},
    {"id": "p2", "name":"Cargo Pant Olive","price":1499,"desc":"Relaxed tactical cargo","category":"Bottoms","trend_score":88,"img":""},
    {"id": "p3", "name" :"Graphic Oversized Tee", "price":999,"desc":"Heavyweight cotton tee","category":"Tees","trend_score":91,"img":""}
]
class ProductRAGEngine:
    def search(self,q="",category="All"):
        q_clean=q.lower()
        matches=PRODUCTS
        if category != "All":
            matches =[p for p in matches if p['category']==category]
        if q_clean:
            matches=[p for p in matches if q_clean in p['name'].lower() or q_clean in p['desc'].lower()]
        return matches