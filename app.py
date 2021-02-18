from flask import Flask, send_file
from flask import jsonify
from flask import request

# from queriesHive import QueriesHive
# from queriesHive import QueriesHive

app = Flask(__name__)

tableToo = {"ools": [
           {"ID": '563e6w53we',
            "Date Create": '18-03-2020',
            "Kama": 'jkl',
            "Last_i": '127.0.0.1',
            "Birth_Date": '18-08-2020',
            "Last_Date": '18-08-2020',
            "ID_Family": 'sd',
            ">Op_Name": 'jkld jklsd jkl',
            "Aad_Name": 'dsddfsfdf',
            "Ik": '568789',
            "Omp": '123',
            "Unit": 'dsedef',
            "Comments": 'sdadsd',
            "Insertion_Time": '03-2020'
            },
            {"ID": '563e6w53we',
             "Date Create": '18-03-2020',
             "Kama": 'jkl',
             "Last_i": '127.0.0.1',
             "Birth_Date": '18-08-2020',
             "Last_Date": '18-08-2020',
             "ID_Family": 'sd',
             ">Op_Name": 'jkld jklsd jkl',
             "Aad_Name": 'dsddfsfdf',
             "Ik": '568789',
             "Omp": '123',
             "Unit": 'dsedef',
             "Comments": 'sdadsd',
             "Insertion_Time": '03-2020'
             }
            ]}

@app.route('/', methods=['GET'])
def hello_user():
    return jsonify({'message': 'Hello, User!'})


@app.route('/table', methods=['GET'])
# get All Table - select * from tabletoo
def return_all():
    print(request.headers)
    # all_table = QueriesHive("ool Table").get_all_table()
    all_table = tableToo
    return jsonify({'tableToo': all_table})


# with variable in the route
@app.route('/admin/table', methods=['GET'])
# select * from tableToo where column =/> value
def return_by_value():
    dict = request.args.to_dict()
    query = ""
    if "date_insertion" in dict:
        query = query + " date_insertion > '" + request.args.get('date_insertion') + "' "
    for k, v in dict.items():
        if query != "":
            query = query + "AND "
        query = query + " " + k + " = '" + request.args.get(k) + "' "
    # filter_table = QueriesHive("ool Table").get_query_by_value(query)
    filter_table = tableToo[0]
    return jsonify({'tableToo': filter_table})


@app.route('/admin/table', methods=['POST'])
def add_one():
    # TODO - check if works with args
    # TODO - decide what require in the columns
    dict_add = request.args.to_dict()
    # add_row_to_table = QueriesHive("ool Table").add_row(dict_add, tableToo)
    tableToo.append(dict_add)
    # TODO - Returns a html page that says the line was added successfully

    # req_data = request.get_json()
    # values = "'" + req_data['date_insertion'] + "', " + req_data['hoolid'].upper() + "', " + req_data[
    #   'hooltype'].upper() + "', " + req_data['name'] + "', " + req_data['tik'] + "', " + req_data['opN'] + "', " + \
    #       req_data['kamaN'] + "', " + req_data['comp'] + "', " + req_data['unit'] + "', " + req_data['comments']

    return jsonify({'quarks': tableToo})


@app.route('/admin/table', methods=['PUT'])
def edit_one(name):
    dict_edit = request.args.to_dict()
    # update_row_in_table = QueriesHive("ool Table").update_row(dict_edit)
    # TODO show what return from update_row_in_table
    html_file = "Succeeded/failed"
    return jsonify({'quarks': html_file})


@app.route('/admin/table', methods=['DELETE'])
def delete_one(name):
    req_data = request.get_json()
    # delete_row_in_table = QueriesHive("ool Table").delete_row(req_data['hoolid'].upper())
    # TODO show what return from delete_row_in_table
    html_file = "Succeeded/failed"
    return jsonify({'quarks': html_file})


# get all ool of on
@app.route('/on/<string:name_on>', methods=['GET'])
# select * from tableToo where column =/> value
def return_by_value_on():
    on = request.args['on']
    # TODO - print request.args['on'] to see if get the on name
    query = "on ='" + on + "'"
    # all_ool_by_on = QueriesHive("ool Table").get_query_by_value(query)
    all_ool_by_on = tableToo[1]
    return jsonify({'tableToo': all_ool_by_on})



@app.route('/coding.PNG')
def logo():
    def get_image():
        filename = 'images\\coding.PNG'
        return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
