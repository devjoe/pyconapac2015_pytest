# unit test case 1
def f(a, b):
    return a*b+1

def test_f():
    assert f(1, 1) == 2




# --------------------------------
# unit test case 2
class R1(object):
    def __init__(self, speaker_id):
        self.speaker_id = speaker_id
    def get_audience_number(self):
        return len(self.speaker_id)*10+1
    def timeout(self):
        self.speaker_id = "GG"

def test_R1():
    r1 = R1("excusemejoe")
    assert r1.get_audience_number() == 111
    r1.timeout()
    assert r1.speaker_id == "GG"
