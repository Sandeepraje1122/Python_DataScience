import json

from config import *
class Product(db.Model):
    id = db.Column("prod_id",db.Integer,primary_key = True)
    name = db.Column("prod_name",db.String(50))
    qty = db.Column("prod_qty",db.Integer)
    price = db.Column("prod_price",db.Float)
    vendor = db.Column("prod_vendor",db.String(50))

db.create_all()

@app.route("/product/api/v1/<int:pid>",methods=["GET"])
def search_product(pid):
    print('search method called...')
    dbproduct = Product.query.filter_by(id=pid).first()
    if dbproduct:
        product = {"Product_ID":dbproduct.id,
                   "Product_NAME": dbproduct.name,
                   "Product_QTY": dbproduct.qty,
                   "Product_PRICE": dbproduct.price,
                   "Product_VEN": dbproduct.vendor,
                   }
        return json.dumps(product)
    else:
        return json.dumps({"ERROR":"Product for given ID was not Present"})

@app.route("product/api/v1/",methods=["POST"])
    def add_new_product():
       req_data=request.get_json()
       if req_data:
           name=req_data.get("name")
           if name.isalpha() and len(name)<=2:
               return json.dumps({"ERROR":"Invalid product Name"})

@app.route("product/api/v1/", methods=["GET"])
    def get_list_of_products()

@app.route("product/api/v1/<int:pid>",methods=["PATCH"])
    def update_product_qty():
        pass

@app.route("product/api/v1/<int:pid>", methods=["PUT"])
    def update_product():
        pass


@app.route("product/api/v1/<int:pid>", methods=["DELETE"])
    def delete_product():
        pass
