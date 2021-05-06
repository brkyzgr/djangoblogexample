from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label= "Parola",widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget= forms.PasswordInput) # widget= forms.PasswordInput --> Bunun password şeklinde görünmesi için yazdık.
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrula",widget=forms.PasswordInput)
    
    def clean(self): # Bura parola ile confirm in eşit olup olmadığını sorgulayan fonksiyon
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor") # Eğer eşit değilse hata fırlattık.
        
        # Eğer password ile confirm aynıysa burdaki alanları sözlük yapısında döndürmek gerek. Çünkü bir sonraki sayfaya dönmek için.

        values = {
            "username" : username,
            "password" : password,
        }
        return values

        