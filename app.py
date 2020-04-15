from resources.store import GLOBAL_STORE, StoreResource
from resources.ds import DSResource, NewDSResource, DSOperationResource, DSOperationResourceWithParam
from flask import Flask
from flask_restful import Api, Resource
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = Flask(__name__)
api = Api(app)

api.add_resource(DSOperationResource,
                 "/<string:data_structure>/<uuid:id>/<string:operation>")
api.add_resource(DSOperationResourceWithParam,
                 "/<string:data_structure>/<uuid:id>/<string:operation>/<string:param>")
api.add_resource(DSResource, "/<string:data_structure>/<uuid:id>")
api.add_resource(NewDSResource, "/<string:data_structure>/new")
api.add_resource(StoreResource, "/")


if __name__ == "__main__":
    app.run(load_dotenv=True, host=os.environ.get("FLASK_RUN_HOST"), port=os.environ.get(
        "FLASK_RUN_PORT"), debug=os.environ.get("FLASK_DEBUG"))
