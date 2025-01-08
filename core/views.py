from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, About, Contact, Testimonial

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm

# Create your views here.

class Home(ListView):
    model = Project
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Default context (Project list)
        context['about'] = About.objects.first()  # Example: First About object
        context['testimonials'] = Testimonial.objects.all()
        context['contact'] = Contact.objects.all()   # All Testimonials
        return context
    
class ProjectView(DetailView):
    model = Project
    template_name = 'core/project.html'  # You can customize this template as needed
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can also add other context here if necessary
        return context
    


class ContactView(FormView):
    template_name = 'core/contact.html'  # ফর্ম রেন্ডার করার টেমপ্লেট
    form_class = ContactForm  # কোন ফর্ম ব্যবহার করা হবে
    success_url = reverse_lazy('contact')  # সাবমিটের পর কোথায় রিডাইরেক্ট করবে

    def form_valid(self, form):
        # ফর্মটি যদি বৈধ হয়, তাহলে ডেটা সেভ করুন
        form.save()
        return super().form_valid(form)
    
    
