from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from front_end.core.commonClass import signUpLayer
from front_end.models import UserInfo
from front_end.core.get_medicines import GetMedicines
from django.http import JsonResponse
from front_end.models import MedicineUserData
from front_end.core.practo_layer import PractoLayer
from front_end.core.watson_layer import WatsonLayer

# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def signup_user(request):

    if request.method == "POST":
        if 'first_name' and 'last_name' and 'email' and 'password' and 'dob' and 'city' and 'address' and 'pin_code' and 'disease' in request.POST.keys():

            new_user = signUpLayer(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['dob'],
                        request.POST['disease'], request.POST['city'], request.POST['address'], request.POST['pin_code'])

            new_user.signup_user()

            new_user.new_user_create_id()

            user = authenticate(username=request.POST['email'].slice[0], password=request.POST['password'])

            return redirect('html/home.html', {
                'userObject' : user
            })

        else:
            #pass some error response in the form
            pass

    return render(request, 'html/signup.html')

def login_user(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'html/home.html', {'userObject' : UserInfo.objects.get(email__username=user.username)})
            else:
                return render(request, 'html/login.html', {"wrong_password_message": "You entered wrong password."})
        else:
            return render(request, 'html/login.html', {"wrong_password_message": "User Name does not exist."})

    else:
        return render(request, 'html/login.html')


def logout_user(request):
    logout(request)
    return redirect('../')

def home(request):

    user = request.user

    return render(request, 'html/home.html', {'userObject' : UserInfo.objects.get(email__username=user.username)})

def get_medicine_list(request):

    get_medicine = GetMedicines(request.GET['medicine_name'])

    return JsonResponse(get_medicine.search_medicines())

def send_medicine_data(request):

    if request.method == "POST":

        if 'course_time' and 'daily_dose' and 'medicine_name' and 'quantity' and 'reminder' in request.POST.keys():


            new_medicine_data = MedicineUserData()

            new_medicine_data.user_id = UserInfo.objects.get(email__username=str(request.user.username))
            new_medicine_data.name = request.POST['medicine_name']
            new_medicine_data.quantity = request.POST['quantity']
            new_medicine_data.course_time = request.POST['course_time']
            new_medicine_data.daily_dosage = request.POST['daily_dose']
            new_medicine_data.reminder_new = request.POST['reminder']

            new_medicine_data.save()

            return redirect('../home')


def practo_layer(request):

    symptom_name = request.GET['symptoms']
    city_name = request.GET['city_name']

    search_doctor = PractoLayer(symptom_name, city_name)

    doc_data = search_doctor.search_doctor()

def watson_endpoint(request):

    query = request.GET['query']

    watson_result = WatsonLayer(query)

    result = watson_result.return_watson_result()

    return render(request, 'html/results.html', {
        'disease_name' : result[0]['disease_name'],
        'body' : result[0]['body']
    })



