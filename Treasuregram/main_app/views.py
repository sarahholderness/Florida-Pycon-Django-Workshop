from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'treasures': treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",
    'https://s3.amazonaws.com/courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png'),
    Treasure("Fool's Gold", 0.00, 'pyrite', "Fool's Falls, CO",
    'https://s3.amazonaws.com/courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png'),
    Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA',
    'https://s3.amazonaws.com/courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png'),
]
