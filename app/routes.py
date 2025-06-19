from flask import render_template, Blueprint, redirect, url_for, request, flash
from sqlalchemy import func
from datetime import datetime
from app.models import Visitor
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    visitors = Visitor.query.order_by(Visitor.visit_date.desc()).limit(50).all()
    total_visitors = Visitor.query.count()
    today_visitors = Visitor.query.filter(
        func.date(Visitor.visit_date) == datetime.now().date()
    ).count()
    monthly_visitors = Visitor.query.filter(
        func.to_char(Visitor.visit_date, 'YYYY-MM') == datetime.now().strftime('%Y-%m')
    ).count()

    return render_template('visitors.html',
                           visitors=visitors,
                           total_visitors=total_visitors,
                           today_visitors=today_visitors,
                           monthly_visitors=monthly_visitors)


@bp.route('/visitors')
def visitors():
    # Ова е опционално, ако сакаш посебен url за посетители
    return redirect(url_for('main.index'))


@bp.route('/visitor/add', methods=['GET', 'POST'])
def add_visitor():
    if request.method == 'POST':
        try:
            if not all([request.form.get('name'),
                        request.form.get('email'),
                        request.form.get('visit_date')]):
                flash('Please fill all required fields', 'danger')
                return render_template('add_visitor.html')

            if Visitor.query.filter_by(email=request.form['email']).first():
                flash('Email already exists!', 'danger')
                return render_template('add_visitor.html')

            visitor = Visitor(
                name=request.form['name'],
                email=request.form['email'],
                visit_date=datetime.strptime(request.form['visit_date'], '%Y-%m-%d').date(),
                ticket_type=request.form.get('ticket_type', 'regular')
            )

            db.session.add(visitor)
            db.session.commit()
            flash('Visitor added successfully!', 'success')
            return redirect(url_for('main.index'))  # Пренасочување на почетната страна

        except ValueError:
            db.session.rollback()
            flash('Invalid date format. Please use YYYY-MM-DD format.', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding visitor: {str(e)}', 'danger')

    return render_template('add_visitor.html')


@bp.route('/visitor/delete/<int:visitor_id>', methods=['POST'])
def delete_visitor(visitor_id):
    visitor = Visitor.query.get_or_404(visitor_id)
    try:
        db.session.delete(visitor)
        db.session.commit()
        flash('Visitor deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting visitor: {str(e)}', 'danger')
    return redirect(url_for('main.index'))
