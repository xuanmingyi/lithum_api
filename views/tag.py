from flask.views import MethodView
from flask import jsonify
from flask import request
from models import TagModel
import uuid
import datetime
from utils import get_db
import json


class TagView(MethodView):

    def get(self):
        current_page = int(request.args.get("currentPage", 1))
        page_size = int(request.args.get("pageSize", 8))
        search_text = request.args.get("searchText", "")
        if search_text:
            count = TagModel.query.filter(TagModel.name.like("%{0}%".format(search_text))).count()
            data = TagModel.query.filter(TagModel.name.like("%{0}%".format(search_text)))\
                .order_by(TagModel.id).limit(page_size).offset(page_size * (current_page - 1)).all()
        else:
            count = TagModel.query.count()
            data = TagModel.query.order_by(TagModel.id).limit(page_size).\
                offset(page_size * (current_page - 1)).all()
        return jsonify({"Code": 200,
                        "Message": "",
                        "Data": {
                            "Count": count,
                            "List": data
                        }})

    def post(self):
        db = get_db()
        data = json.loads(request.get_data())
        name = data.get("name")
        color = data.get("color")
        tag = TagModel(name=name, color=color, tag_id=str(uuid.uuid4()), create_at=datetime.datetime.now())
        db.session.add(tag)
        db.session.commit()
        return jsonify({"Code": 200,
                        "Message": "",
                        "Data": None})

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