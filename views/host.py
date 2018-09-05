from models import TagModel, HostModel
from views import APIView
from validate import Validater, StringValidate, NumberValidate, ListValidate


class HostView(APIView):
    def get(self):
        HostModel.get()
        return {}

    def post(self):
        return {}

    def put(self):
        return {}

    def delete(self):
        return {}