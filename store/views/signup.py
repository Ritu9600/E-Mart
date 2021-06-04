from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            phone=phone)
        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required!!!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must contain minimum of 4 characters"
        elif (not customer.last_name):
            error_message = "Last Name Required!!!"
        elif len(customer.last_name) < 3:
            error_message = "Last Name must contain minimum of 4 characters"
        elif (not customer.email):
            error_message = "Enter the Email Address"
        elif len(customer.email) < 5:
            error_message = "Last Name must contain minimum of 4 characters"
        elif (not customer.password):
            error_message = "Enter your Password!"
        elif len(customer.password) < 6:
            error_message = "Password must contain minimum of 6 characters"
        elif (not customer.phone):
            error_message = "Enter a valid Phone number"
        elif len(customer.phone) < 5:
            error_message = "Phone Number must contain minimum of 10 characters"
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        return error_message
