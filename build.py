import shutil
import os

def create_build_folder():
    # Create a 'build' folder if it doesn't exist
    build_folder = os.path.join(os.path.dirname(__file__), 'build')
    if not os.path.exists(build_folder):
        os.makedirs(build_folder)

def copy_templates():
    # Copy templates to the 'build' folder
    templates_src = os.path.join(os.path.dirname(__file__), './app/templates')
    templates_dest = os.path.join(os.path.dirname(__file__), 'build', 'templates')
    shutil.copytree(templates_src, templates_dest)

def copy_static():
    # Copy the 'static' folder to the 'build' folder
    static_src = os.path.join(os.path.dirname(__file__), './app/static')
    static_dest = os.path.join(os.path.dirname(__file__), 'build', 'static')
    shutil.copytree(static_src, static_dest)

def main():
    create_build_folder()
    copy_templates()
    copy_static()

if __name__ == '__main__':
    main()
