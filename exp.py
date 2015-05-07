from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
now_time = datetime.now()

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
  return value.strftime(format)


@app.route("/home/<fname>/<lname>")
def jediname(fname,lname):
    return render_template('template.html',
                           my_string="I'm the jediname creator",
                           first=fname, last=lname,
                           curr_time=datetime.now())

if __name__ == "__main__":
  app.run(debug = True, host="0.0.0.0", port= 8080)