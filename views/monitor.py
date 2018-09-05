from models import HostModel
from views import APIView
from validate import Validater, StringValidate, NumberValidate, ListValidate


class MonitorView(APIView):
    def get(self):
        validater = Validater()
        validater.add(StringValidate("search_text", default=""))
        search_text, = validater.run()
        hosts = HostModel.get()
        return {}