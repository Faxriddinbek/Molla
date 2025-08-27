from django.shortcuts import render, redirect

from apps.acount.forms import ContactForm

# def contact_page_views(request):
#     return render(request, 'contact.html')


def contact_page_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.result = 1313
            form.save()
            return redirect('acount:contact')
        else:
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors
            }
            return render(request, 'contact.html', context)

    else:
        return render(request, 'contact.html')