from gh_action import instroduction
from gh_action import own_runners
from gh_action import quickstart


def test_quickstart():
    assert quickstart() == "https://docs.github.com/en/free-pro-team@latest/actions/quickstart"


def test_own_runners():
    assert (
        own_runners()
        == "https://docs.github.com/en/free-pro-team@latest/actions/hosting-your-own-runners"
    )


def test_instroduction():
    assert (
        instroduction()
        == "https://docs.github.com/en/free-pro-team@latest/actions/learn-github-actions/"
        "introduction-to-github-actions"
    )
