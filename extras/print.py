
from rich import print as rprint


def printme(title, body):
    """helper function to print items to console"""
    rprint(
        f" ====  [bold spring_green2]{title}  start [/bold spring_green2] ===")
    if type(body) == list:
        for item in body:
            rprint(item)
    else:
        rprint(body)        
    rprint(
        f" ====  [bold spring_green2]{title} end [/bold spring_green2]=====")


# rprint(
#         f"attr c[/bold spring_green2]"
#         f" doesn't exist in class [bold yellow] ggo [bold yellow] ")
