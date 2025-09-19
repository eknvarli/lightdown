from lightdown.core import App

app = App()

@app.route('/')
def index():
    return ('index.md', {
        'title':'LightDown App!',
        'message':'This is an example.'
    })

if __name__ == '__main__':
    app.run()