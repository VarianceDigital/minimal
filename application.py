from minimal import create_app
import os

os.environ["SESSION_SECRET"]="MySessionSecret" 

application = create_app()

