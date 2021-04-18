from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User ,Admin
from .forms import login_form

# Create your views here.


def slogin(request):
    if request.method == 'POST':
        form=login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                s_data=User.objects.get(name=username,password=password)
                request.session['student'] = s_data.pk
                return render(request,'user/profile.html',{"data":s_data})
            except:
                messages.error(request,'User Does Not Exit !')
    else:
        try:
            if request.session['student']:
                id = request.session['student']
                s_data = User.objects.get(id=id)
                return render(request, 'user/profile.html', {"data": s_data})
        except:
            form=login_form()
            return render(request,'user/ulogin.html',{'form':form})
        form = login_form()
    return render(request, 'user/ulogin.html', {'form': form})


def s_regitser(request):
    return  render(request,'user/uregister.html')


def regitser(request):
    name = request.POST.get("name")
    dob = request.POST.get("dob")
    password = request.POST.get("password")
    image = request.FILES['image']
    phone = request.POST.get("phone")
    User(name=name, dob=dob, password=password, image=image, phone=phone,mark=0).save()
    return redirect('s_login')


def s_edit(request):
    id=request.session['student']
    s_data=User.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        # dob = request.POST.get('dob')
        # photo = request.FILES['photo']
        User.objects.filter(id=id).update(name=name,phone=mob)
        messages.success(request, 'Successfully Profile Updated refresh the page')
        return render(request, 'user/profile.html', {"data": s_data})
    return render(request, 'user/s_edit.html', {"data": s_data})


def s_logout(request):
    del request.session['student']
    return redirect('s_login')


def a_login(request):
    if request.method =='POST':
        form=login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                a_data=Admin.objects.get(name=username,password=password)
                request.session['admin']=a_data.pk
                s_data=User.objects.all()
                return render(request,'admin/a_profile.html',{'data':s_data,'data1':a_data})
            except:
                messages.error(request, 'User Does Not Exit !')
    else:
        try:
            if request.session['admin']:
                return redirect('a_profile')
        except:
            form = login_form()
            return render(request, 'admin/a_login.html', {'form': form})
        form = login_form()
    return render(request,'admin/a_login.html', {'form': form})


def a_regitser(request):
    return render(request,'admin/a_register.html')


def asucessregitser(request):
    name = request.POST.get("name")
    dob = request.POST.get("dob")
    password = request.POST.get("password")
    image = request.FILES['image']
    phone = request.POST.get("phone")
    Admin(name=name, dob=dob, password=password, image=image, phone=phone).save()
    return redirect('a_login')


def a_logout(request):
    del request.session['admin']
    return redirect('a_login')


def s_update(request,pk):
    id = request.session['admin']
    a_data = Admin.objects.get(id=id)
    s_data = User.objects.all()
    if request.method == 'POST':
        object= User.objects.get(id=pk)
        # name = request.POST['name']
        # mob = request.POST['mob']
        # dob = request.POST['dob']
        # photo = request.FILES['photo']
        mark=request.POST['mark']
        User.objects.filter(id=object.id).update(mark=mark)
        messages.success(request, 'Successfully Profile Updated')
        return render(request, 'admin/a_profile.html', {'data': s_data, 'data1': a_data})
    s_data = User.objects.get(id=pk)
    return render(request, 'admin/a_update.html', {'data': s_data})