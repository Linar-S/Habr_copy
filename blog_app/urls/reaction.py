from django.urls import path
from blog_app.views import change_reaction

reaction_urls= [
    path("reaction/change", change_reaction, name="change-reaction")
]
