@app.route("/number/<int:n>")
def number(n):
    """
    Display 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)
