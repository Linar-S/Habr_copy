from blog_app.controllers.reaction import ReactionController


def change_reaction(request):
    return ReactionController(request).change()

