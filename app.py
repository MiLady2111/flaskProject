import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# connection = sqlite3.connect('db.db')
# cursor = connection.cursor()


def execute_query(query):
    # conn = sqlite3.connect('db.db')
    # vse chto vnuri
    # conn.close()
    with sqlite3.connect('db.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def get_by_id(table, record_id):
    return execute_query(
        f"SELECT * FROM {table} WHERE id={record_id}"
    )[0]


@app.route('/')
def recipes_list():
    recipes = execute_query("SELECT * FROM recipes")
    return render_template('index.html',
                           recipes=recipes, get_by_id=get_by_id)


# @app.route('/<int:pk>/')
# def recipe_detail(pk):
#     recipes = execute_query(f"SELECT * FROM recipes WHERE name={pk}")
#     return render_template('index.html',
#                            recipes=recipes, get_by_id=get_by_id)
#
#
# @app.route('/add/recipe/', methods=['GET', 'POST'])
# def add_recipe():
#     if request.method == 'POST':
#         execute_query(
#             f"INSERT INTO name (name) VALUES ('{request.form['name']}')"
#             f"INSERT INTO ingredients (name) VALUES ('{request.form['ingredients']}')"
#             f"INSERT INTO recipe_preparation (name) VALUES ('{request.form['recipe_preparation']}')"
#         )
#         return redirect('/')
#     return render_template('add_recipe.html')
#
#
# @app.route('/remove_recipe/', methods=['POST'])
# def remove_recipe():
#     execute_query(
#         f"DELETE FROM recipes WHERE id={request.form['id']}"
#     )
#     return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


