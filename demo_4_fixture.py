class DB(object):
    def __init__(self, setting_str):
        #...
        pass

def f(db):
    # get data from db & do something ..
    return True

# ---------------------------------------
# Write your test:
def test_f(db):
    assert f(db) == True




# problem: I am Lazy
# ------------------------------------
import pytest
@pytest.fixture
def mydb():
    db = DB("to_mydb")
    #setup your db
    return db



# ------------------------------------
@pytest.fixture(params=["to_mydb",
                        "to_yourdb"])
def db(request):
    db = DB(request.param)
    #setup your db
    return db
