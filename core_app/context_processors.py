from .forms import FooterVragenForm

def footer_vragen_form_processor(request):
    return {
        'footer_vragen_form': FooterVragenForm()
    }
