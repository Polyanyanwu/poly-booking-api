""" Views for the api functions """

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator
from .models import FacilityCode, RoomType
from .forms import FacilityCodeForm, RoomTypeForm


@login_required
@transaction.atomic
def maintain_facility_code(request):
    """ Maintain Facility Codes """
    # check that user is staff

    if not request.user.is_staff:
        messages.error(request,
                       "You are not authorized to perform this transaction")
        return redirect('/')

    facilities = FacilityCode.objects.all().order_by('name')
    use_instance = True
    if facilities.count() == 0:
        use_instance = False
        form = FacilityCodeForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            id_sent = request.POST.get('name_selected')
            facility = get_object_or_404(FacilityCode, id=id_sent)
            form = FacilityCodeForm(instance=facility)
            request.session['current_rec'] = id_sent
        elif 'create_new_record' in request.POST:
            form = FacilityCodeForm()
            request.session['current_rec'] = ""
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = FacilityCodeForm(instance=facilities[0])
                request.session['current_rec'] = facilities[0].id
            HttpResponseRedirect('api/facility_code.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            facility = get_object_or_404(FacilityCode, id=id_sent)
            name = facility.name
            facility.delete()
            request.session['current_rec'] = ""
            messages.success(request,
                             ('Facility ' + name +
                              ' was successfully deleted!'))
            if facilities.count():
                form = FacilityCodeForm(instance=facilities[0])
        elif 'save_record' in request.POST:

            if request.session.get('current_rec'):
                # editing a record which id was put in session
                facility_id = int(request.session.get('current_rec'))
                facility = FacilityCode.objects.get(pk=facility_id)
                form = FacilityCodeForm(request.POST, instance=facility)
            else:
                form = FacilityCodeForm(request.POST)
            if form.is_valid():
                new_rec = form.save()
                # put the newly saved record in edit mood to prevent
                # creating a new record again if the save key is pressed twice
                request.session['current_rec'] = new_rec.id
                messages.success(request,
                                 ('Your Facility was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if facilities.count():
            form = FacilityCodeForm(instance=facilities[0])
    paginator = Paginator(facilities, 15)  # Show 15 records
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'api/facility_code.html', {
        'form': form,
        'data': page_obj,
    })
