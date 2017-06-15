from django.conf.urls import url
import polls.views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    url(r'^$', polls.views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', polls.views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', polls.views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', polls.views.vote, name='vote'),
]
