from flask.views import MethodView
from views import APIView
from flask import jsonify
from flask import request
from models import TagModel
import uuid
import datetime
from utils import get_db
import json

from validate import Validater, StringValidate, NumberValidate

class TagView(APIView):



    def get(self):
        # params
        validater = Validater()
        validater.add(NumberValidate("current_page", default=1, min=1))
        validater.add(NumberValidate("page_size", default=8, min=1))
        validater.add(StringValidate("search_text", ""))

        current_page, page_size, search_text = validater.run()

        # get

        if search_text:
            count = TagModel.query.filter(TagModel.name.like("%{0}%".format(search_text))).count()
            data = TagModel.query.filter(TagModel.name.like("%{0}%".format(search_text)))\
                .order_by(TagModel.id).limit(page_size).offset(page_size * (current_page - 1)).all()
        else:
            count = TagModel.query.count()
            data = TagModel.query.order_by(TagModel.id).limit(page_size).\
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

        tag= TagModel(name=name, color=color, tag_id=TagModel.geterate_tag_id(),
                    create_at=datetime.datetime.now())
        db.session.add(tag)
        db.session.commit()

        return None

    def put(self):
        db = get_db()
        data = json.loads(request.get_data())
        name = data.get("name")
        id = data.get("id")
        color = data.get("color")
        TagModel.query.filter(TagModel.tag_id==id).update({
            "name": name,
            "color": color,
            "update_at": datetime.datetime.now()
        })
        db.session.commit()
        return jsonify({"Code": 200,
                        "Message": "",
                        "Data": tag})

    def delete(self):
        return jsonify({})