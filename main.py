from app import create_app

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(debug=True)