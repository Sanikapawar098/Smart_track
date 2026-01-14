from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import CitizenProfile, Complaint
from .forms import CustomerRegistrationForm, CreateComplaintForm
from django.contrib.auth import authenticate, login
import datetime
from django.contrib.auth import logout as auth_logout


def home(request):
    return render(request, 'core_app/home.html')


@login_required
def citizen_dashboard(request):
    try:
        profile = request.user.citizenprofile
    except CitizenProfile.DoesNotExist:
        profile = None
    complaints = Complaint.objects.filter(customer=request.user)
    return render(request, 'core_app/citizen_dashboard.html', {'profile': profile, 'complaints': complaints})


def is_manager(user):
    return getattr(user, 'is_society_manager', False)


@login_required
def manager_dashboard(request):
    if not getattr(request.user, 'is_society_manager', False):
        return HttpResponseForbidden('Forbidden: manager access only')
    pending = Complaint.objects.filter(status=Complaint.STATUS_PENDING)
    return render(request, 'core_app/manager_dashboard.html', {'pending': pending})


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('core_app:citizen_dashboard')
            else:
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('core_app:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'core_app/register.html', {'form': form})


def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'core_app/complaint_list.html', {'complaints': complaints})


@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'core_app/complaint_detail.html', {'complaint': complaint})


@login_required
def create_complaint(request):
    if request.method == 'POST':
        form = CreateComplaintForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.customer = request.user
            comp.complaintDate = int(datetime.date.today().strftime('%Y%m%d'))
            comp.status = Complaint.STATUS_PENDING
            comp.save()
            messages.success(request, 'Complaint submitted.')
            return redirect('core_app:complaint_detail', pk=comp.pk)
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = CreateComplaintForm()
    return render(request, 'core_app/create_complaint.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('core_app:home')
