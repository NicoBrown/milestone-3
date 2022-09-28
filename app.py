"""
app.py
"""

#import dependencies
import os
from blueprints import app

if __name__ == '__main__':
    app.run(host=os.environ.get("hostaddr"),
            port=int(os.environ.get("port")),
            debug=True)
