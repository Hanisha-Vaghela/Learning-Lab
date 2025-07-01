from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login,logout
from sample.models import User,Tutorials, Certificate , VideoTutorial
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
import io

def generate_certificate(request):
        username = request.COOKIES.get('user_username')
        if request.method == 'POST':
            username = request.COOKIES.get('user_username')
            name = request.POST.get('name')
            course = request.POST.get('course')
            completion_date = request.POST.get('completion_date')
            
            # Store in session for preview
            request.session['certificate_data'] = {
                'name': name,
                'course': course,
                'completion_date': completion_date
            }
            
            return redirect('preview_certificate')
        
        return render(request, 'certificate.html',{'username':username})

def preview_certificate(request):
    if not request.session.get('certificate_data'):
        return redirect('generate_certificate')
    
    context = request.session['certificate_data']
    return render(request, 'certificate_preview.html', context)

def save_certificate(request):
    if request.method == 'POST' and request.session.get('certificate_data'):
        data = request.session['certificate_data']
        
        # Save to database
        Certificate.objects.create(
            name=data['name'],
            course=data['course'],
            completion_date=data['completion_date']
        )
        
        # Clear session data
        del request.session['certificate_data']
        
        return redirect('success')
    
    return redirect('generate_certificate')

def download_certificate_pdf(request):
    if not request.session.get('certificate_data'):
        return redirect('generate_certificate')
    
    # print("Hello")
    data = request.session['certificate_data']
    template = get_template('certificate_pdf.html')
    print(template)

    html = template.render({**data,'pdf_landscape': True })
    # print(html)
    result = io.BytesIO()
    # print(result)
    # pdf = pisa.pisaDocument(open("certificate_PDF.html","r"),open('mypdf.pdf')'wb')
    pdf = pisa.pisaDocument(io.StringIO(html), result)
    # print("result")
    
    if not pdf.err:
        print("H")
        print(result)
        response = HttpResponse(pdf.getvalue(), content_type='application/pdf')
        print(response)
        response['Content-Disposition'] = f'attachment; filename="{data["name"]}_{data["course"]}_certificate.pdf"'
        return response
    
    return HttpResponse('Error generating PDF', status=400)

def success(request):
    return render(request, "success.html")

def code(request):
    return render(request,"code.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def broh_code(request):
    return render(request,"broh_code.html")

def codewith_mosh(request):
    return render(request,"codewith_mosh.html")

def shraddha_khapra(request):
    return render(request,"shraddha_khapra.html")

def login(request):
    return render(request, "login.html")

def f_course(request):
    return render(request,"f_cours.html")

def report(request):
    return render(request,"report.html")

def contact_tutor(request):
    return render(request,"contact_tutor.html")

def loginsubmit(request):
    email = request.GET.get("email")
    password = request.GET.get("password")

    # add data isLogin true in cookie

    myuser = get_object_or_404(User, email=email)


    if myuser and myuser.password == password:
        response = redirect("/")  # Redirect to the homepage after login
        response.set_cookie("user_email", myuser.email, max_age=3600)  # Store email in cookie
        response.set_cookie("user_username",myuser.username, max_age=3600)

        return response
    else:
        return render(request, "login.html", {"error": "Invalid credentials"})

def logout_view(request):
    response = redirect("/")  # Redirect to home after logout
    response.delete_cookie("user_email")  # Remove cookie
    response.delete_cookie("user_username")
    return response

   
def signup(request):
    return render(request, "signup.html")

def submit(request):
    username = request.GET.get("username")
    email = request.GET.get("email")
    password = request.GET.get("password")

    # Check if the user already exists
    existing_user = User.objects.filter(email=email).first()
    if existing_user:
        return render(request, "signup.html", {"error": "Email already registered!"})

    # Create new user
    new_user = User(username=username, email=email, password=password)
    new_user.save()

    # Set cookie and redirect to homepage
    # add data isLogin true in cookie 

    response = redirect("/")
    response.set_cookie("user_email", new_user.email, max_age=3600)  # Cookie expires in 1 hour
    response.set_cookie("user_username",new_user.username, max_age=3600)
    return response


# @login_required
def profile(request):
    username = request.COOKIES.get('user_username')
    email = request.COOKIES.get('user_email')
    return render(request, "profile.html", {'username': username,'email':email})

def tutorials(request,topic=None):
    tutorials = Tutorials.objects.all()

    python = tutorials[0]
    html = tutorials[1]
    css = tutorials[2]
    js = tutorials[3]
    c = tutorials[4]
    c_sharp = tutorials[5]

    if topic == 'python':
        return render(request, "tutorials.html", {"tutorial": python})
    elif topic == 'html':
        return render(request, "tutorials.html", {"tutorial": html})
    elif topic == 'css':
        return render(request, "tutorials.html", {"tutorial": css})
    elif topic == 'js':
        return render(request, "tutorials.html", {"tutorial": js})
    elif topic == 'c':
        return render(request, "tutorials.html", {"tutorial": c})
    elif topic == 'c_sharp':
        return render(request, "tutorials.html", {"tutorial": c_sharp})
    else:
        return render(request, "tutorials.html", {"tutorials": tutorials})
    
def video_tutorials(request,language=None):
    video_tutorials = VideoTutorial.objects.all()

    python = video_tutorials[5]
    html = video_tutorials[0]
    css = video_tutorials[1]
    js = video_tutorials[2]
    c = video_tutorials[3]
    c_sharp = video_tutorials[4]

    if language == 'python':
        return render(request, "video_tutorials.html", {"video_tutorial": python})
    elif language == 'html':
        return render(request, "video_tutorials.html", {"video_tutorial": html})
    elif language == 'css':
        return render(request, "video_tutorials.html", {"video_tutorial": css})
    elif language == 'js':
        return render(request, "video_tutorials.html", {"video_tutorial": js})
    elif language == 'c':
        return render(request, "video_tutorials.html", {"video_tutorial": c})
    elif language == 'c_sharp':
        return render(request, "video_tutorials.html", {"video_tutorial": c_sharp})
    else:
        return render(request, "video_tutorials.html", {"video_tutorials": tutorials})
