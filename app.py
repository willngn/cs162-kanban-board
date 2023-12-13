from src import app
if __name__ == '__main__':
    # change port number to account for availability and app visibility
    app.run(debug=True, port=5001)