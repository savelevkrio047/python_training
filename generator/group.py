from model.group import Group
from fixture.session import SessionHelper
from fixture.application import Application
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f ="data/groups.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
   symbols =  string.ascii_letters + string.digits + " "*10
   return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer", 20))
            for i in range(n)]
testdata1 = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 3)]
            for header in ["", random_string("header", 3)]
            for footer in ["", random_string("footer", 3)]]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
   # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))