from flask import Flask,request,render_template
import datetime
import Data.BackEnd_Operations
import webbrowser


app = Flask(__name__)

   # Data_receive_ = Data.CreateFile.CRUD.read_specific_data(name, company)
   # return Data_receive_.to_html(header="true", table_id="table")
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/consulta_esp', methods=['GET','POST'])
def consulta_especifica():

    if request.method == 'POST':
        name = request.form.get('name')
        company = request.form.get('company')
        Data_receive_ = Data.BackEnd_Operations.CRUD.read_specific_data(name, company)
        return Data_receive_.to_html(header="true", table_id="table")
    return render_template('Search.html')

@app.route('/consulta_geral', methods=['GET'])
def consulta_geral():
    Data_receive = Data.BackEnd_Operations.view_all()
    return Data_receive.to_html(header="true", table_id="table")


@app.route('/inserir', methods = ['GET','POST'])
def inserir():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        company = request.form.get('company')
        amount = request.form.get('amount')
        Data.BackEnd_Operations.CRUD.create_data(id, name, company, datetime.datetime.now(), int(amount))
        return render_template('Insert_Sucess.html')
    return render_template('Insert.html')


@app.route('/remover', methods = ['GET','POST','DELETE'])
def remover():

    if request.method == 'POST':
        id = request.form.get('id')
        Data.BackEnd_Operations.CRUD.delete_data(id)
        return render_template('Delete_sucess.html')
    return render_template('Delete.html')

if __name__ == '__main__':
    app.run(debug=True)
