from um import count

def test_count_correct():
    assert count("um, um") == 2
    assert count("um, hola, como estás um") == 2
    assert count("um") == 1

def test_count_inwords():
    assert count("bum in an album") == 0
    assert count("pum, sonó la bomba") == 0
    assert count("me gusta el bombombum") == 0

def test_count_spaces():
    assert count(" um ") == 1
    assert count("um  um ") == 2

def test_count_case():
    assert count(" UM ") == 1
    assert count("UM  UM ") == 2




