from website import create_app

app = create_app()

if __name__ == "__main__":  # needed to ensure the Flask web server is only created IF this main.py file runs
    app.run(debug=True)  # debug = True causes the web server to re-run if any changes are made.
    # In production debug is not set to True
