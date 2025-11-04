from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Booking, db

sales_routes = Blueprint('sales', __name__)

@sales_routes.route('/api/sales-data')
@jwt_required()
def sales_data():
    range_type = request.args.get('range', 'month')

    # --- Replace with real grouping logic ---
    if range_type == 'day':
        data = [{"label": "2025-09-29", "sales": 100}]
    elif range_type == 'week':
        data = [{"label": "Week 1", "sales": 700}]
    elif range_type == 'month':
        data = [{"label": "2025-09", "sales": 2500}]
    else:  # overall
        total = db.session.query(db.func.sum(Booking.amount)).scalar() or 0
        data = [{"label": "Total", "sales": total}]
    return jsonify(data)
