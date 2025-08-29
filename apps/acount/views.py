from django.shortcuts import render, redirect

from apps.acount.forms import ContactForm
#
# def contact_page_views(request):
#     return render(request, 'contact.html')


def contact_page_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.result = 1313
            contact.save()
            return redirect('home:contact')
        else:
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors,
                "form" : form,
            }
            return render(request, 'contact.html', context)

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})