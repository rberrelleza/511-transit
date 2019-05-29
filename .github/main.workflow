workflow "publish" {
  on = "push"
  resolves = ["upload"]
}

action "tag-filter" {
  uses = "actions/bin/filter@3c0b4f0e63ea54ea5df2914b4fabf383368cd0da"
  args = "tag v*"
}

action "check" {
  uses = "ross/python-actions/setup-py/3.7@627646f618c3c572358bc7bc4fc413beb65fa50f"
  args = "check"
  needs = "tag-filter"
}

action "sdist" {
  uses = "ross/python-actions/setup-py/3.7@627646f618c3c572358bc7bc4fc413beb65fa50f"
  args = "sdist"
  needs = "check"
}

action "upload" {
  uses = "ross/python-actions/twine@627646f618c3c572358bc7bc4fc413beb65fa50f"
  args = "upload ./dist/fiveoneone-*.tar.gz"
  secrets = ["TWINE_PASSWORD", "TWINE_USERNAME"]
  needs = "sdist"
}
