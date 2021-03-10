from bokeh.server.server import Server
from dashboards.main import main_dashboard

server = Server({'/': main_dashboard},port=8080)

# start timers and services and immediately return
server.start()

if __name__ == '__main__':
    print('Opening Bokeh application on http://localhost:8080/')

    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()