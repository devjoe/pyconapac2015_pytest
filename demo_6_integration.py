import bottle

class DB(object):
    def save(self, what):
        with open("db.data", "a") as f:
            f.write(str(what))
        return True
db = DB()

@bottle.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    bottle.run()

#-------------------------------------
# How to write unit test?
def test_index():
    assert index() == 'Hi!'



#-------------------------------------
# How to write unit test?


@bottle.route('/db')
def save_something_to_db():
    if db.save("+1"):
        return "Yo!"
    else:
        return "No!"

def test_save_something_to_db():
    assert save_something_to_db() == "Yo!"
