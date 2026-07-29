from twttr import shorten
def main():
    test_shorten()

def test_shorten():
    assert shorten("cat") == "ct"
    assert shorten("TWItter") == "TWttr"
    assert shorten("cat!?") == "ct!?"
    assert shorten("cat12") == "ct12"


if __name__ == "__main__":
    main()
