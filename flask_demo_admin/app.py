from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import db, Product

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Cấu hình CSDL SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo các thành phần
db.init_app(app)
admin = Admin(app, name='Quản trị sản phẩm', template_mode='bootstrap4')
admin.add_view(ModelView(Product, db.session))

# Tạo CSDL nếu chưa có
with app.app_context():
    db.create_all()

# Chạy Flask app
if __name__ == '__main__':
    app.run(debug=True)
