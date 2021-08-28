from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
# Create your views here.

#this is class based view
class ReviewView(View):
    #instead of View, you can use FormView and it will make the code simplified:
    #form_class=ReviewForm
    #template_name="reviews/review.html"
    #now we dont have to define get method, but what about form submission?
    #django automatically handles form submission
    #succes_url="/thank-you"
    #but this form does not know what to do with data, so we need to add extra method
    #we need to define form valid function
    #def form_valid(self,form):
        #form.save()
        #return super().form_valid(form)

    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


#def review(request):
#    if request.method=='POST':
#        form=ReviewForm(request.POST)
#
#        if form.is_valid():
#            print(form.cleaned_data)
#            #review=Review(
#            #    user_name=form.cleaned_data['user_name'],
#            #    review_text=form.cleaned_data['review_text'],
#            #    rating=form.cleaned_data['rating'])
#            #review.save()
#            form.save()
#            return HttpResponseRedirect("/thank-you")
    
#    #get he input page we are not in this if block
#    else:
#        form=ReviewForm()
#        return render(request,"reviews/review.html",{
#            "form":form
#        })

#def thank_you(request):
#    return render(request,"reviews/thank_you.html")

#this is class based view (templated), we dont need to define a get method
class ThankYouView(TemplateView):
    #def get(self,request):
    #    return render(request,"reviews/thank_you.html")
    template_name="reviews/thank_you.html"

class ReviewListView(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name="object_list"
    #No need to define get method because we are using ListView

    #def get_context_data(self, **kwargs):
    #   context=super().get_context_data(**kwargs)
    #    reviews=Review.objects.all()
    #    context["reviews"]=reviews
    #    return context

class SingleReviewView(DetailView):
    template_name="reviews/single_review.html"
    model=Review
    #No need to define get method because we are using DetailView

    #def get_context_data(self, **kwargs):
    #    context=super().get_context_data(**kwargs)
    #    review_id=kwargs["id"]
    #    selected_review=Review.objects.get(pk=review_id)
    #    context["reviews"]=selected_review
    #    return context