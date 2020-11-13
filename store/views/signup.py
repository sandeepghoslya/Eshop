from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.costomer import Customer
from django.views import View


def validateCustomer(customer):
    error_message = None


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error': error_message, 'value': value}
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name be 4 char long'
        if not customer.last_name:
            error_message = "Lirst Name Required !!"
        elif len(customer.last_name) < 4:
            error_message = 'Last Name be 4 char long'
        if not customer.phone:
            error_message = "Phone number Required !!"
        elif len(customer.phone) < 11:
            error_message = 'Enter 10 number phone number'
        if not customer.password:
            error_message = "Password Required !!"
        elif len(customer.password) < 4:
            error_message = "Email Required !!"
        elif len(customer.email) < 4:
            error_message = "Email must be 4 character long"
        elif customer.isExists:
            error_message = 'Email Address Aleady Registe '
