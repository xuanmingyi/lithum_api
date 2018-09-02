from utils import get_app
from views.tag import TagView

app = get_app()

app.add_url_rule('/v1/tag', view_func=TagView.as_view('tag'))


if __name__ == '__main__':
    app.run(debug=True)
