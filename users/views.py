from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, Http404, reverse
from django.views.generic import UpdateView
from users.forms import RegisterForm, UserImageForm, ProfileImageForm
from django.contrib.auth import authenticate, login, logout
from users.email import send_register_mail
from django.contrib.auth.decorators import user_passes_test, login_required
from users.forms import AuthUser


def login_required(function=None, redirect_field_name='login', login_url='users:login'):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            send_register_mail(user)

            return redirect('users:login')
    return render(request, 'users/register.html', {'form': form, })


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            raise Http404('Email or password not provided!')
        user = authenticate(request, username=username, password=password)

        if user is None:
            raise Http404('Invalid credentials')
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'users/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def upload_view(request):
    if request.method == 'GET':
        form = UserImageForm()
    else:
        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'users/file_uploaded.html')

    return render(request, 'users/upload.html', {
        'form': form
    })

def contact_view(request):
    return render (request, 'contact.html')

@login_required
def stocks_view(request):
    return render (request, 'stocks.html')

@login_required
def profile_view(request):
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form
    })

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = AuthUser
    fields = ['first_name', 'last_name', 'phone_no', 'company']
    template_name = 'users/editprofile.html'

    def get_queryset(self):
        return AuthUser.objects.filter(is_active=True)

    def form_valid(self, form):
        print(form.errors)
        return super(UpdateProfileView, self).form_valid(form)

    def get_success_url(self):
        return reverse ('users:profile')