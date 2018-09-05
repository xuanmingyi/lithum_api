from utils import get_db, generate_id
import datetime


db = get_db()

def strftime(v):
    if not v:
        return ""
    return v.strftime("%Y-%m-%d %H:%M:%S")

class TagModel(db.Model):
    __tablename__ = "pytags"

    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.String(32))
    name = db.Column(db.String(32))
    color = db.Column(db.String(7))
    create_at = db.Column(db.TIMESTAMP(True))
    update_at = db.Column(db.TIMESTAMP(True))
    delete_at = db.Column(db.TIMESTAMP(True))


    def serialize(self):
        return {
            "id": self.tag_id,
            "name": self.name,
            "color": self.color,
            "create_at": strftime(self.create_at)
        }

    @staticmethod
    def geterate_tag_id():
        return 'tag-' + generate_id(8)

    @classmethod
    def create(cls, name, color):
        tag= cls(name=name, color=color, tag_id=TagModel.geterate_tag_id(),
                    create_at=datetime.datetime.now())
        db.session.add(tag)
        db.session.commit()

    @classmethod
    def update(cls, tag_id, *args, **kwargs):
        cls.query.filter(cls.tag_id==tag_id).update({
            "name": kwargs.get("name"),
            "color": kwargs.get("color"),
            "update_at": datetime.datetime.now()
        })
        db.session.commit()

    @classmethod
    def delete(cls, ids):
        for id in ids:
            tag = TagModel.query.filter_by(tag_id=id).first()
            db.session.delete(tag)
        db.session.commit()


class HostModel(object):
    @classmethod
    def get(cls):
        HOST_STATUS_MONITORED = 0
        HOST_STATUS_NOT_MONITORED = 1
        HOST_STATUS_TEMPLATE = 3
        HOST_STATUS_PROXY_ACTIVE = 5
        HOST_STATUS_PROXY_PASSIVE = 6

        HOST_AVAILABLE_UNKNOWN = 0
        HOST_AVAILABLE_TRUE = 1
        HOST_AVAILABLE_FALSE = 2

        hosts = {}
        sql = "select hostid, host, name, status, available from hosts where status != 3 and available in (1, 2);"
        results = db.engine.execute(sql)
        for row in results:
            name = row[2]
            hosts[name] = {}
            hosts[name]["hostid"] = row[0]
            hosts[name]["items"] = []
        for host in hosts:
            sql = "select itemid, name, status from items where hostid = {0}".format(hosts[host]["hostid"])
            items = db.engine.execute(sql)
            for item in items:
                hosts[host]["items"].append({
                    "itemid": item["itemid"],
                    "name": item["name"],
                    "status": item["status"]
                })
        return hosts