from flask_restful import Resource
from data_structures.stack import Stack
from uuid import uuid4
from data_structures.stack import Stack
from data_structures.deque import Deque
from data_structures.kv import KV
from data_structures.list import List
from data_structures.set import Set

from resources.store import GLOBAL_STORE
import copy
from flask import abort, request
from constants import STACK, DEQUE, SET, LIST, KV, DATA_STRUCTURES
from constants import operations as OP

# Resources to connect data structures to http requests


class NewDSResource(Resource):
    def get(self, data_structure):
        data_structure = str(data_structure).upper()
        if data_structure not in DATA_STRUCTURES:
            abort(400)
        uuid = str(uuid4())
        if(data_structure == STACK):
            GLOBAL_STORE.get(data_structure)[uuid] = Stack()
        elif(data_structure == DEQUE):
            GLOBAL_STORE.get(data_structure)[uuid] = Deque()
        elif(data_structure == SET):
            GLOBAL_STORE.get(data_structure)[uuid] = Set()
        elif(data_structure == KV):
            GLOBAL_STORE.get(data_structure)[uuid] = KV()
        elif(data_structure == LIST):
            GLOBAL_STORE.get(data_structure)[uuid] = List()
        return uuid, 201


class DSResource(Resource):
    def get(self, data_structure, id):
        try:
            stack = GLOBAL_STORE[str(id)]
        except KeyError:
            return None
        return stack.get()

    def delete(self, id):
        del GLOBAL_STORE[str(id)]
        return "OK", 200


class DSOperationResource(Resource):

    def get(self, data_structure, id, operation=None):
        if operation == None:
            operation == "get"
        data_structure = str(data_structure).upper()
        operation = str(operation).upper()
        if data_structure not in DATA_STRUCTURES:
            abort(400)
        try:
            ds = GLOBAL_STORE.get(data_structure).get(str(id))
        except:
            abort(404)
        if(ds == None):
            abort(400)
        if(operation == OP.CLONE):
            new_uuid = str(uuid4())
            print("we got here")
            try:
                GLOBAL_STORE.get(data_structure)[
                    new_uuid] = copy.deepcopy(ds)
                return new_uuid
            except KeyError:
                abort(404)
            except:
                abort(500)
        elif(operation == OP.GET):
            return str(ds)
        if data_structure == STACK:
            if(operation == OP.STACK.POP):
                return ds.pop()
            elif(operation == OP.STACK.PEEK):
                return ds.peek()
            elif(operation == OP.STACK.SIZE):
                return ds.size()
            elif(operation == OP.STACK.GET):
                return ds.get()
        elif data_structure == DEQUE:
            if(operation == OP.DEQUE.POP_BACK):
                return ds.pop_back()
            elif(operation == OP.DEQUE.POP_FRONT):
                return ds.pop_front()
            elif(operation == OP.DEQUE.BACK):
                return ds.back()
            elif(operation == OP.DEQUE.FRONT):
                return ds.front()
            elif(operation == OP.DEQUE.REVERSE):
                return ds.reverse()
            elif(operation == OP.DEQUE.SIZE):
                return ds.size()
            elif(operation == OP.DEQUE.ROTATE):
                return ds.rotate()
            elif(operation == OP.DEQUE.SORT):
                return ds.sort()
            elif(operation == OP.DEQUE.CLEAR):
                return ds.clear()
        elif data_structure == SET:
            try:
                other = GLOBAL_STORE.get(data_structure).get(
                    str(request.args.get("id")))
            except KeyError:
                other = None
            if(operation == OP.SET.IS_EMPTY):
                return ds.is_empty()
            elif(operation == OP.SET.SIZE):
                return ds.size()
            elif(operation == OP.SET.UNION):
                if other == None:
                    abort(400)
                return ds.union(other)
            elif(operation == OP.SET.APPLY_UNION):
                if other == None:
                    abort(400)
                return ds.apply_union(other)
            elif(operation == OP.SET.INTERSECTION):
                if other == None:
                    abort(400)
                return ds.intersection(other)
            elif(operation == OP.SET.APPLY_INTERSECTION):
                if other == None:
                    abort(400)
                return ds.apply_intersection(other)
            elif(operation == OP.SET.DIFFERENCE):
                if other == None:
                    abort(400)
                return ds.difference(other)
            elif(operation == OP.SET.APPLY_DIFFERENCE):
                if other == None:
                    abort(400)
                return ds.apply_difference(other)
            elif(operation == OP.SET.SYMMETRIC_DIFFERENCE):
                if other == None:
                    abort(400)
                return ds.symmetric_difference(other)
            elif(operation == OP.SET.APPLY_SYMMETRIC_DIFFERENCE):
                if other == None:
                    abort(400)
                return ds.apply_symmetric_difference(other)
            elif(operation == OP.SET.IS_SUBSET):
                if other == None:
                    abort(400)
                return ds.is_subset(other)
            elif(operation == OP.SET.IS_SUPERSET):
                if other == None:
                    abort(400)
                return ds.is_superset(other)
        elif data_structure == LIST:
            if(operation == OP.LIST.REVERSE):
                return ds.reverse()
            elif(operation == OP.LIST.SORT):
                return ds.sort()
            elif(operation == OP.LIST.SIZE):
                return ds.size()
        elif data_structure == KV:
            return None
        abort(400)

    def post(self, id, operation):
        data = request.form.get('data')
        operation = operation.lower()
        stack = GLOBAL_STORE.get(str(id))
        if stack == None:
            abort(404)
        if(operation == 'push') and data:
            stack.push(data)
        return stack.get()


class DSOperationResourceWithParam(Resource):
    def get(self, data_structure, id, operation, param):
        return None
