from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from pytils.translit import slugify

from catalog.models import Product, Category


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Вот такие инструменты'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'date_of_creation', 'views_count', 'is_published', 'slug')

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.category.pk])

    def form_valid(self, form):
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = Category.objects.get(pk=self.kwargs.get('pk'))
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'date_of_creation', 'views_count', 'is_published', 'slug')
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.object.category.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category')
    template_name = 'catalog/blogpost_confirm_delete.html'

