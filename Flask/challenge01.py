from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() :
    user = {
        'user_name1' : 'Hak',
        'user_name2' : 'Hak',
        'user_name3' : 'Hak'
    }
    # rendering 할 html 파일명 입력
    # html 로 넘겨줄 데이터 입력
    return render_template('index.html', user= user)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = '8080', debug=True) #debug = True 해주면 껏다켯다 안해도 반영됨 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user list</title>
</head>
<body>
    <h1>User, list</h1>
    {% for i, v in user.items() %}<br>
    {{i}} : {{v}}
    {% endfor %}
</body>
</html>
```
