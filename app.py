from flask import Flask,request


app=Flask(__name__)
#
# @app.route('/')
# def admin():
#     return 'welcome most students'
# @app.route("/success",methods=['POST'])
# def success_data():
#     data=request.get_json()
#     name=data['name']
#     model=data['model']
#     doors=data['doors']
#     return ({"name":name,"model":model,"doors":doors})
# @app.route("/user",methods=['GET'])
# def user():
#     data = request.get_json()
#     name = data['name']
#     model = data['model']
#     doors = data['doors']
#     return ({"name": name, "model": model, "doors": doors})
# @app.route("/delete",methods=['DELETE'])
# def name_delete():
#     data = request.get_json()
#     name = data['name']
#     model = data['model']
#     doors = data['doors']
#     return f'success_data : {success_data} succefully deleted'
# @app.route('/date')
# def get_current_data():
#     data={
#         "name":"venkat",
#         "age":22,
#         "position":"bad"
#     }
#     return data

# @app.route("/login",methods=['GET','POST'])
# def get_json_data():
#     data=request.json["key"]
#     return data
@app.route("/login",methods=['GET','POST'])
def get_json_data():
    data=request.json["key"]
    return data


if __name__ =='__main__':
    app.run(debug=True)

