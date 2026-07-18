from flask import Flask,request,render_template,flash,redirect,url_for
import csv
import os

app=Flask(__name__)
app.config['SECRET_KEY']='Aryan@2005'

if not (os.path.exists('users.csv')):
    with open('users.csv','w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=['id','email','password'])
        writer.writeheader()



@app.route('/',methods=['GET'])
def home():
    return render_template('register.html')



@app.route('/register',methods=['POST','GET'])
def register():
    email=request.form.get('email')
    password=request.form.get('password')

    with open('users.csv','r') as in_file,\
         open('users.csv','a',newline="") as out_file:
        reader=csv.DictReader(in_file)
        fieldnames=reader.fieldnames
        # print(int(in_file.readlines()[-1][0])+1)
        rows=list(reader)
        last_row=rows[-1]
        for user in rows:
            if user['email']==email:
                flash("User Already Exists")
                return render_template('login.html')
            
        # return render_template('register.html')
        
        writer=csv.DictWriter(out_file,fieldnames=fieldnames)
        
        print(last_row)
        inc_id=int(last_row['id'])+1
        writer.writerow({
            'id':inc_id,
            'email':email,
            'password':password
        })
        return redirect(url_for('player'))
    

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/choice' ,methods=['GET','POST'])
def choice():
    player_val1=request.form.get('O')
    player_val2=request.form.get('X')
    # print(player_val1,player_val2)
    
    if player_val1:
        return render_template('game.html',player=player_val1)

    return render_template('game.html', player=player_val2)

@app.route('/player',methods=['GET','POST'])
def player():
    return render_template('player.html')


@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)