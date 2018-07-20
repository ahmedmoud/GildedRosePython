from flask import Flask,redirect
from flask import render_template

from db import *
from gilded_rose import *
app = Flask (__name__)


@app.route('/')
def index():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * from products")
	data = cursor.fetchall()
	mysql.init_app(app)
	return  render_template("index.html",products=data)

@app.route('/update')
def update():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * from products")
	data = cursor.fetchall()
	items = []
	for product in data:
		product_object = Item(product[1],product[2],product[3])
		Gilded_object = GildedRose(product_object)
		updated_product_object = Gilded_object.update_quality()    
		conn = mysql.connect()
		cursor = conn.cursor()
		query = "UPDATE products  SET name="+"'"+updated_product_object.name+"'"+", quality="+str(updated_product_object.quality)+",sell_in="+str(updated_product_object.sell_in)+" WHERE id="+str(product[0])
		cursor.execute(query)
		conn.commit()
	mysql.init_app(app)
	return  redirect("/")



if __name__ == "__main__":
   app.run()

