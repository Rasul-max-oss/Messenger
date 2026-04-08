# from flask import Flask, render_template, request, redirect
#
# app = Flask(__name__)
#
# telephone = {}
#
# @app.route('/', methods=['GET', 'POST'])
# def calls():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         number = request.form.get('number')
#         if name and number:
#             telephone[name] = number
#             print(telephone)
#         return redirect('/')
#     number_deleate = request.args.get('delete')
#     if number_deleate in telephone:
#         del telephone[number_deleate]
#     return render_template('calls.html', telephone=telephone)
#
#
#
#
# # items = []
# #
# # pairs = {}
# #
# # @app.route('/index2',methods=['GET','POST'])
# # def index2():
# #     if request.method == 'POST':
# #         key = request.form.get('key')
# #         value = request.form.get('value')
# #         if key and value:
# #             pairs[key] = value
# #             print(pairs)
# #         return redirect('/index2')
# #     return render_template('index2.html',pairs=pairs)
# #
# #
# #
# #
# # @app.route('/',methods=['GET','POST'])
# # def index():
# #     if request.method == 'POST':
# #         new_item = request.form.get('item')
# #         if new_item:
# #             items.append(new_item)
# #             return redirect('/')
# #     item_to_Delete = request.args.get('delete')
# #     if item_to_Delete:
# #         if item_to_Delete in items:
# #             items.remove(item_to_Delete)
# #             return redirect('/')
# #     return render_template('index.html',items=items)
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
