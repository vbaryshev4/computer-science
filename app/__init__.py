from flask import Flask
import router

app = Flask(__name__)

router.init(app)
