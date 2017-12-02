from flask import Flask
import router

app = Flask(__name__)

router.init(app)

app.run(port=8080, debug=True)