# add import lines like so - one for each module
# makes import more intuitive for end-user
# allows them to access modules afterwards, like:
#   import {{cookiecutter.project_slug}}
#   x = {{cookiecutter.project_slug}}.foo.func()
import {{cookiecutter.project_slug}}.foo as foo
