from phew import logging, server, connect_to_wifi
from secret import ssid, password
from phew.template import render_template



ip = connect_to_wifi(ssid, password)


logging.info("server start at {}".format(ip))



@server.route("/", ['POST', 'GET'])
def index(request):
    print(request.method)
    if request.method == 'POST':
        content = request.form.get("content", None)
        return "update successful, refresh your page"
        

        
    return render_template("index.html")


@server.catchall()
def myCatch(request):
    return "no matching page", 404


server.run()
