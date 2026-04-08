from flask import Flask, render_template, request, redirect

app = Flask(__name__)


films = []


@app.route('/', methods=['POST','GET'])
def add_film():
    if request.method == 'POST':
        film = request.form.get('film')
        director = request.form.get('director')
        year = int(request.form.get('year'))
        rating = int(request.form.get('rating'))
        if year <= 1750:
            return redirect('/')
        if rating <= 0:
            return redirect('/')
        if film and director and year and rating:
            choice = {
                'Название' : film,
                'Жанр' : director,
                'Дата' : year,
                'Рейтинг' : rating
            }
            films.append(choice)
            print(films)
    return render_template('Films.html')

@app.route('/movies')
def show_films():
    film_delete = request.args.get('delete')
    if film_delete:
        if film_delete in films:
            films.remove(film_delete)
            return redirect('/')
    return render_template('movies.html',films=films)

# users = []
#
# @app.route('/', methods=['POST','GET'])
# def reg():
#     if request.method == 'POST':
#         first_name = request.form.get('first_name')
#         last_name= request.form.get('last_name')
#         age = int(request.form.get('age'))
#         if age <= 0:
#             return redirect('/')
#         if first_name and last_name and age:
#             user = {
#                 'Имя': first_name,
#                 'Фамилия': last_name,
#                 'Возраст': age
#             }
#             print(user)
#             users.append(user)
#             print(users)
#             return redirect('/users')
#     return render_template('register.html')
#
# @app.route('/users')
# def show_users():
#
#     return render_template('users.html',users=users)





if __name__ == '__main__':
     app.run(debug=True)


















