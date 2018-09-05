from models import TagModel
from views import APIView
from validate import Validater, StringValidate, NumberValidate, ListValidate



class TagView(APIView):

    def get(self):
        # params
        validater = Validater()
        validater.add(NumberValidate("current_page", default=1, min=1))
        validater.add(NumberValidate("page_size", default=8, min=1))
        validater.add(StringValidate("search_text", default=""))
        current_page, page_size, search_text = validater.run()

        # get
        query = TagModel.query
        if search_text:
            query.filter(TagModel.name.like("%{0}%".format(search_text)))

        count = query.count()
        data = query.order_by(TagModel.id).limit(page_size).\
                offset(page_size * (current_page - 1)).all()
        return { "count": count, "list": data}

    def post(self):
        # params
        validater = Validater()
        validater.add(StringValidate("name", required=True))
        validater.add(StringValidate("color", required=True))
        name, color = validater.run()
        # create
        TagModel.create(name=name, color=color)
        return None

    def put(self):
        # params
        validater = Validater()
        validater.add(StringValidate("id", required=True))
        validater.add(StringValidate("name", required=True))
        validater.add(StringValidate("color", required=True))
        tag_id, name, color = validater.run()

        # update
        TagModel.update(tag_id, **{"name": name, "color": color})
        return None


    def delete(self):
        validater = Validater()
        validater.add(ListValidate("ids", required=True))
        ids, = validater.run()

        TagModel.delete(ids)
        return None