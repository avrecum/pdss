from flask_restful import Resource
from constants import STACK, DEQUE, LIST, SET, KV
GLOBAL_STORE = {STACK: {}, DEQUE: {}, LIST: {}, SET: {}, KV: {}}


class StoreResource(Resource):
    def get(self):
        return str(GLOBAL_STORE)
