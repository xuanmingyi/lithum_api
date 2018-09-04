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
            "id": self.id,
            "tag_id": self.tag_id,
            "name": self.name,
            "color": self.color,
            "create_at": strftime(self.create_at),
            "update_at": strftime(self.update_at),
            "delete_at": strftime(self.delete_at)
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
