import gh_action


def test_quickstart():
    assert gh_action.quickstart() == "https://docs.github.com/en/free-pro-team@latest/actions/quickstart"


def test_own_runners():
    assert gh_action.own_runners() == "https://docs.github.com/en/free-pro-team@latest/actions/hosting-your-own-runners"


def test_instroduction():
    assert gh_action.instroduction() == "https://docs.github.com/en/free-pro-team@latest/actions/learn-github-actions/introduction-to-github-actions"
