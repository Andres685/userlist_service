# routes.py
from flask import Blueprint, request, jsonify
from models import db, UserList

routes = Blueprint('routes', __name__)

@routes.route('/mark_as_not_watched', methods=['POST'])
def mark_as_not_watched():
    data = request.get_json()
    user_id = data.get('user_id')
    movie_title = data.get('movie_title')

    if not user_id or not movie_title:
        return jsonify({'message': 'Faltan datos (se requieren user_id y movie_title)'}), 400

    # Buscar entrada existente
    user_movie = UserList.query.filter_by(user_id=user_id, movie_title=movie_title).first()

    if user_movie:
        if not user_movie.watched:
            return jsonify({'message': 'Ya estaba marcada como no vista'}), 200
        user_movie.watched = False
    else:
        # Crear nueva entrada con watched=False
        new_entry = UserList(user_id=user_id, movie_title=movie_title, watched=False)
        db.session.add(new_entry)

    db.session.commit()
    return jsonify({'message': 'Película marcada como no vista'}), 200

@routes.route('/not_watched', methods=['GET'])
def get_not_watched_movies():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'Se requiere user_id'}), 400

    not_watched_movies = UserList.query.filter_by(user_id=user_id, watched=False).all()
    movies = [entry.movie_title for entry in not_watched_movies]
    return jsonify({'not_watched_movies': movies}), 200



@routes.route('/mark_as_watched', methods=['POST'])
def mark_as_watched():
    data = request.get_json()
    user_id = data.get('user_id')
    movie_title = data.get('movie_title')

    if not user_id or not movie_title:
        return jsonify({'message': 'Faltan datos (se requieren user_id y movie_title)'}), 400

    # Buscar entrada existente
    user_movie = UserList.query.filter_by(user_id=user_id, movie_title=movie_title).first()

    if user_movie:
        if user_movie.watched:
            return jsonify({'message': 'Ya estaba marcada como vista'}), 200
        user_movie.watched = True
    else:
        # Crear nueva entrada con watched=True
        new_entry = UserList(user_id=user_id, movie_title=movie_title, watched=True)
        db.session.add(new_entry)

    db.session.commit()
    return jsonify({'message': 'Película marcada como vista'}), 200
