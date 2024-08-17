from django.views import generic
from .models import Prod, Comment
from django.shortcuts import get_object_or_404
from .forms import Commentform


class Productview(generic.ListView):
    # model = Prod
    queryset = Prod.objects.filter(status=True)
    template_name = 'productions/lis.html'
    context_object_name = 'productss'


class Productdetailview(generic.DetailView):
    model = Prod
    template_name = 'productions/detail.html'
    context_object_name = 'productss'
    # form ersal nazar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = Commentform()
        return context


class Sendcomment(generic.CreateView):
    model = Comment
    # tamami creat view ha form niaz darand
    form_class = Commentform
    # fields = '__all__'
    # jahat save form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        prod_id = int(self.kwargs['pk'])
        prodd = get_object_or_404(Prod, id=prod_id)
        obj.prodd = prodd
        return super().form_valid(form)
