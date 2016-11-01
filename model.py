from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dietary_Restriction(db.Model):
    """Dietary Restriction. i.e. Vegan, Gluten-Free, Organic"""

    __tablename___ = "dietary_restrictions"

    diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):

        return "<Dietary_Restriction diet_id={} name={}>".format(self.diet_id,
                                                                 self.name)


class Customer(db.Model):
    """Customer of Farm to Front Door"""

    __tablename___ = "customers"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    street_address = db.Column(db.String(100), nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)
    state = db.Column(db.String(2), nullable=True)
    phone = db.Column(db.String(30), nullable=True)

    def __repr__(self):

        return "<Customer id={}, first_name={}, last_name={}, email={}>".format(self.user_id,
                                                                                self.first_name,
                                                                                self.last_name,
                                                                                self.email)


class Customer_Restriction(db.Model):
    """Association table. Relates Customer class to Dietary_Restriction class."""

    __tablename__ = "customer_restrictions"

    cust_restr_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.user_id'), nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey('dietary_restrictions.diet_id'), nullable=False)

    def __repr__(self):

        return "<Customer_Restriction cust_restr_id={}, cust_id={}, diet_id={}>".format(self.cust_restr_id,
                                                                                        self.cust_id,
                                                                                        self.diet_id)


class Pickup(db.Model):
    """Pickup locations"""

    __tablename___ = "pickups"

    pickup_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    street_address = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(2), nullable=False)  # set CA default?

    def __repr__(self):

        return "<Pickup pickup_id={}, name={}, street_address={}, zipcode={}>".format(self.pickup_id,
                                                                                      self.name,
                                                                                      self.street_address,
                                                                                      self.zipcode)


class Icon(db.Model):
    """Icon for web usage"""

    __tablename__ = "icons"

    icon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    credit = db.Column(db.String(100), nullable=False)

    def __repr__(self):

        return "<Icon icon_id={} url={} credit={}>".format(self.icon_id,
                                                           self.url,
                                                           self.credit)


class Product(db.Model):
    """Product sold by Farm to Front Door"""

    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False)
    icon_id = db.Column(db.Integer, db.ForeignKey('icons.icon_id'), nullable=True)
    aisle = db.Column(db.String(50), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    img = db.Column(db.String(500), nullable=True)
    color = db.Column(db.String(10), nullable=True)

    def __repr__(self):

        return "<Product product_id={} name={} weight={} unit={} price={}>".format(self.product_id,
                                                                                   self.name,
                                                                                   self.weight,
                                                                                   self.unit,
                                                                                   self.price)


class Tag(db.Model):
    """Tag for products i.e. Certified Organic, Locally Grown"""

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):

        return "<Tag tag_id={} name={}>".format(self.tag_id, self.name)


class Product_Tag(db.Model):
    """Association table relating Tag class to Product class"""

    __tablename__ = "product_tags"

    prod_tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'), nullable=False)

    def __repr__(self):

        return "<Product_Tag prod_tag_id={} product_id={} tag_id={}>".format(self.prod_tag_id,
                                                                             self.product_id,
                                                                             self.tag_id)


class Recipe(db.Model):
    """Recipe pulled from Edamam API"""

    ___tablename___ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    url = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    img = db.Column(db.String(300), nullable=True)

    def __repr__(self):

        return "<Recipe name={} ingredients={} url={} img={}>".format()


class Customer_Recipe(db.Model):
    """Association table for Recipes each Customer has liked"""

    __tablename__ = "customer_recipes"

    cust_rec_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)

    def __repr__(self):

        return "<Customer_Recipe cust_rec_id={} customer_id={} recipe_id={}>".format(self.cust_rec_id,
                                                                                     self.customer_id,
                                                                                     self.recipe_id)


class Delivery(db.Model):
    """A delivery of incoming products, composed of Delivery-Quantities"""

    __tablename__ = "deliveries"

    delivery_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    vendor = db.Column(db.String(500), nullable=True)
    received_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):

        return "<Delivery delivery_id={} vendor={} received_at={}>".format(self.delivery_id,
                                                                           self.vendor,
                                                                           self.received_at)


class Delivery_Quantity(db.Model):
    """An amount of a certain product, in each delivery"""

    __tablename__ = "delivery_quantities"

    deliv_qty_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    product_qty = db.Column(db.Integer, nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey("deliveries.delivery_id"), nullable=False)

    def __repr__(self):

        return "<Delivery_Quantity deliv_qty_id={} product_id={} product_qty={} delivery_id={}>".format(self.deliv_qty_id,
                                                                                                        self.product_id,
                                                                                                        self.product_qty,
                                                                                                        self.delivery_id)


class Order(db.Model):
    """An order placed by a customer, composed of Order-Quantities"""

    __tablename__ = "order"

    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.user_id"), nullable=False)
    placed_at = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    pickup_id = db.Column(db.Integer, db.ForeignKey("pickups.pickup_id"), nullable=False)
    received_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):

        return "<Order order_id={} customer_id={} total={} placed_at={} received_at={}>".format(self.order_id,
                                                                                                self.customer_id,
                                                                                                self.total,
                                                                                                self.placed_at,
                                                                                                self.received_at)


class Order_Quantity(db.Model):
    """An amount of a certain product, in each order"""

    __tablename__ = "order_quantities"

    order_qty_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    product_qty = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable=False)

    def __repr__(self):

        return "<Order_Quantity order_qty_id={} product_id={} product_qty={} order_id={}>".format(self.order_qty_id,
                                                                                                  self.product_id,
                                                                                                  self.product_qty,
                                                                                                  self.order_id)