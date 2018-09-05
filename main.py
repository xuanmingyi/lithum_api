from utils import get_app
from views.tag import TagView
from views.host import HostView

app = get_app()
app.add_url_rule("/v1/tag", view_func=TagView.as_view("tag"))
app.add_url_rule("/v1/host", view_func=HostView.as_view("host"))

if __name__ == '__main__':
    app.run(debug=True)
