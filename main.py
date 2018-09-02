from utils import get_app
from views.tag import TagView

app = get_app()

app.add_url_rule('/v1/tag', view_func=TagView.as_view('tag'))

app.run(debug=True)