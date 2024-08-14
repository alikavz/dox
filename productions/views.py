from django.views import generic
from .models import Prod


class Productview(generic.ListView):
    # model = Prod
    queryset = Prod.objects.filter(status=True)
    template_name = 'productions/lis.html'
    context_object_name = 'productss'


class Productdetailview(generic.DetailView):
    model = Prod
    template_name = 'productions/detail.html'
    context_object_name = 'productss'
