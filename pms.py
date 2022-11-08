from flask import*
import pymysql

app=Flask(__name__)

@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="pharmacy")
        cu=db.cursor()
        sql="select * from user"
        cu.execute(sql)
        data=cu.fetchall()
        return render_template('index1.html',d=data)
    except Exception as e:
        print("Error:",e)

@app.route('/user')
def form():
    return render_template('form1.html')

@app.route('/store',methods=['POST','GET'])
def store():

    pro=request.form['Product_name']
    mfg=request.form['Mfg']
    exp=request.form['Exp']
    pr=request.form['Price']

    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="pharmacy")
        cu=db.cursor()
        sql="insert into user(Product_name,Mfg,Exp,Price)values('{}','{}','{}','{}')".format(pro,mfg,exp,pr)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="pharmacy")
        cu=db.cursor()
        sql="delete from user where id={}".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)

@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="pharmacy")
        cu=db.cursor()
        sql="select * from user where id={}".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('editform1.html',d=data)
    except Exception as e:
        print("Error:",e)
    
        
@app.route('/update/<rid>',methods=['POST','GET'])    
def update(rid):
    i=request.form['Id']
    pro=request.form['Product_name']
    mfg=request.form['Mfg']
    exp=request.form['Exp']
    pr=request.form['Price']

    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="pharmacy")
        cu=db.cursor()
        sql="update user SET Id='{}',Product_name='{}',Mfg='{}',Exp='{}',Price='{}' where id='{}'".format(i,pro,mfg,exp,pr,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')

    except Exception as e:
        print("Error:",e)





app.run(debug=True)
