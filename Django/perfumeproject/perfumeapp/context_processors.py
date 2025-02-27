from adminpanelapp.models import * 

def categories_processor(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'category_data': categories}
