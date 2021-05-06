from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User # Bu şekilde user modelini dahil ettik.
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

def register(request):
    # 1.yöntem:
    """
    if request.method == "POST":

        form = RegisterForm(request.POST)
       
        if form.is_valid(): # Clean metodunu sadece is_valid fonsksiyonuyla çağrılır. Ve bu değerlerin eşitliği sağlanırsa değerleri döndürür.
            # Alttakiyle username ve password bilgilerini aldık.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # Aşağıdaki kod sayesinde veri tabanına username ve password u kaydettik.
            newUser = User (username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser) # Bu sayede hem sisteme kayıt oldu hemde sayfaya giriş yaptı.
            
            return redirect("index")
        context = {
            "form" : form 
        }
        return render(request,"register.html",context)
        
    else:
        form = RegisterForm()
        context = {
            "form" : form 
        }
        return render(request,"register.html",context)
    """    
    # 2.yöntem:
    form = RegisterForm(request.POST or None) # Bu şekilde if şartı kullanmadan post ve get mi olduğunu kontrol edebiliriz.
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
           
            newUser = User (username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser) 
            messages.success(request,"Başarıyla Kayıt Oldunuz...")
            
            return redirect("index")
    context = {
        "form" : form 
    }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        # Aşağıda authenticate eğer none dönerse aşağıdaki sorguya göre çalışır.
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı...")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")