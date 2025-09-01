import json
import csv
import requests

def get_json(url: str):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def get_productos():
    return get_json("https://fakestoreapi.com/products")

def get_producto_por_id(product_id: int):
    return get_json(f"https://fakestoreapi.com/products/{product_id}")

def guardar_json(productos, product= "productos.json"):
    with open(product, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4)

def guardar_csv(productos, filename="productos.csv"):
    campos = ["id", "title", "price", "description"]
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for producto in productos:
            writer.writerow({
                "id": producto["id"],
                "title": producto["title"],
                "price": producto["price"],
                "description": producto["description"]
            })

def main():
    productos = get_productos()      

    guardar_json(productos)
    guardar_csv(productos)

if __name__ == "__main__":
    main()