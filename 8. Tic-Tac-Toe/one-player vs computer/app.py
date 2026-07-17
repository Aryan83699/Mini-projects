from flask import Flask,request,render_template

app=Flask(__name__)



@app.route('/',methods=['GET'])
def home():
    return render_template('register.html')



@app.route('/register',methods=['POST','GET'])
def register():
    # Handle registration logic here
    return render_template('register.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/choice' ,methods=['GET','POST'])
def choice():
    player_val1=request.form.get('O')
    player_val2=request.form.get('X')
    print(player_val1,player_val2)
    
    if player_val1:
        return render_template('game.html',player=player_val1)

    return render_template('game.html', player=player_val2)

@app.route('/verify',methods=['GET','POST'])
def verify():
    return render_template('player.html')


@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)