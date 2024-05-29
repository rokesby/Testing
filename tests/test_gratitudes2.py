from lib.gratitudes import Gratitudes

def test_do_nothing():
    myGratitude = Gratitudes()
    result = myGratitude.format()
    assert result == "Be grateful for: "


def test_one_gratitde():
    myGratitude = Gratitudes()
    myGratitude.add("Good weather")
    result = myGratitude.format()
    assert result == "Be grateful for: Good weather"


def test_two_gratitde():
    myGratitude = Gratitudes()
    myGratitude.add("Good weather")
    myGratitude.add("Good company")
    result = myGratitude.format()
    assert result == "Be grateful for: Good weather, Good company"


def test_empty_gratitude():
    myGratitude = Gratitudes()
    myGratitude.add("Good weather")
    myGratitude.add(" ")
    result = myGratitude.format()
    assert result == "Be grateful for: Good weather,  "