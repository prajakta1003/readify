import os
from app.main import app

if __name__ == '__main__':
    # Change the current working directory to the build folder
    build_folder = os.path.join(os.path.dirname(__file__), 'build')
    os.chdir(build_folder)

    # Run the Flask app from the build folder
    app.run(debug=True)
