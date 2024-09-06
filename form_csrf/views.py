from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    return render(request, 'form_csrf/hello.html')


def form_view(request):
    if request.method == 'POST':
        # Print the raw POST data (request body)
        print(request.body)  # This prints the raw POST data
        print(request.POST)   # This prints parsed form data as a dictionary
        
        # Access individual form fields
        name = request.POST.get('name')

        print(f"Name: {name}")

        # Return a response
        return HttpResponse(f"Name: {name}")
    import time; time.sleep(5)
    return render(request, 'form_csrf/login.html')