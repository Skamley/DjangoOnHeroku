from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from first_app.models import  Topic, WebPage, Employee,Post
from .import forms
from first_app.forms import Employee_Login_From,UserForm,UserProfileInfoForm,PostingForm
from django.views.generic import  ListView

#Import following for REST
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from first_app.serializers import UserSerializer, GroupSerializer

#import for Login functionalities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
def index(request):
    return HttpResponse('Hello world!!!')
'''
def index(request):
    my_dict={'insert_me': "Hello I am from views.py !!!"}
    #return render(request, 'index.html', context=my_dict)
    return render(request, 'index.html')

def AppHomePage(request):
    topics = Topic.objects.all()
    #posts = Post.objects.all()
    users = User.objects.all()
    #This displays last 50 posts from the database in descending order of Date/Time of Creation
    posts = Post.objects.all().order_by("-created_at")[:50]
    # Context_Dir= {"Line1": "This site is undergoing development. Thanks for being patient.",
    #               "Line2": "This is a short note",
    #               }
    #return render(request,'first_app/LogoutView.html',Context_Dir)
    return render(request, 'first_app/AfterLoginView.html', {'all_topics': topics,
                                                                  'all_posts': posts,
                                                                  'all_users': users,
                                                              })

#View for Registration
def Registration(request):
    topics = Topic.objects.all()
    registered = False
    if request.method == "POST":
        print("Registration Request type is - Get")
        """
            Invoke both the forms 1.user_form  2.UserProfileInfoForm in the views
            from forms.py 
            1. UserForm is linked with django's default model User
            2. UserProfileInfoForm is linked with model UserProfileInfo which describes the two additional fields
        """
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            """
                The above line is actually relates to object reference 'user' defined in model.py by user = models.OneToOneField(User, on_delete='Cascade')
            """
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            #return HttpResponseRedirect(reverse(Registration))
        else:
            print("Form is invalid. Errors - " + user_form.errors + profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        print("Registration Request type is - Get")
    return render(request, 'first_app/Registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered,
                   'all_topics': topics,
                   })

#View for Posting Form
@login_required
def Posting(request):
    topics = Topic.objects.all()
    posts = Post.objects.all()
    users = User.objects.all()
    form = PostingForm
    if request.method == 'POST':
        print("Request type is post")
        form = PostingForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return AppHomePage(request)
            #HttpResponseRedirect is invoked to prevent the page from Resubmitting the form
            #So we have to Reverse the AppHomePage
            return HttpResponseRedirect(reverse(AppHomePage))
            # return render(request, 'first_app/AfterLoginView.html', {'all_topics': topics,
            #                                                          'all_posts': posts,
            #                                                          'all_users': users,
            #                                                          })
            #return render(request, 'first_app/Posting.html')
        else:
            print("Form is Invalid")
    else:
        print("Request type is GET")
    return render(request, 'first_app/Posting.html', {'form': form,'all_topics': topics})

#View of Login
def user_login(request):
    topics = Topic.objects.all()
    posts = Post.objects.all()
    users = User.objects.all()
    isValidCredential = True
    if request.method == 'POST':
        print("Login View - Request type is POST")
        username_entry = request.POST['username']
        #print(username_entry)
        password_entry = request.POST['password']
        user = authenticate(request,username=username_entry, password=password_entry)

        if user is not None:
            login(request, user)
            #return render(request, 'first_app/AfterLoginView.html')
            isValidCredential = True
            return HttpResponseRedirect(reverse(AppHomePage))
            # return render(request,'first_app/AfterLoginView.html',{'all_topics': topics,
            #                                                       'all_posts': posts,
            #                                                       'all_users': users,
            #                                                        'isValidCredential': isValidCredential,
            #                                                   })

            #return AppHomePage(request)
            #return HttpResponseRedirect(reverse('first_app/AppHomePage'))
        else:
            isValidCredential = False
            print("Login Failed-Invalid credentials supplied")
            print("Username entered: {} and Password entered:{}".format(username_entry, password_entry))
            return render(request, 'first_app/Login.html', {'all_topics': topics,
                                                                     'all_posts': posts,
                                                                     'all_users': users,
                                                                     'isValidCredential': isValidCredential,
                                                                     })

    else:
        print("Login View - Request type is GET")
        return render(request, 'first_app/Login.html', {'all_topics': topics,
                                                                     'all_posts': posts,
                                                                     'all_users': users,
                                                                     'isValidCredential': isValidCredential,
                                                                     })

#View for Logout
@login_required
def user_logout(request):
    logout(request)
    topics = Topic.objects.all()
    return render(request, 'first_app/LogoutView.html', {'all_topics': topics})
    #return HttpResponseRedirect(reverse('AppHomePage'))

#View for Contacts
def Contacts(request):
    #topics = get_object_or_404(Topic)
    #model = Topic
    topics = Topic.objects.all()
    #names = post.name.filter(active=True)
    return render(request, 'first_app/Contacts.html',{'all_topics': topics})


def rockUs(request):
    return render(request, 'first_app/rockTheWorld.html')

def DemoView(request):
    webpage_list= WebPage.objects.order_by('name')
    webpage_dict = {"WebPage_Records": webpage_list}



    return render(request, 'first_app/DemoView.html',context=webpage_dict)

# We have one class 'MyReg_Form' in forms.py. Now we have included forms.py, and we can
#create the instance of the class 'MyReg_Form' like in the below view method
def MyRegView(request):
    form_obj1 = forms.MyReg_Form(request.POST)
    if request.method == 'POST' and form_obj1.is_valid():

        print("Form is valid")
        print("Name Entered - "+form_obj1.cleaned_data['name'])
        print("Email Entered - "+form_obj1.cleaned_data['email'])
        print("Text input - "+form_obj1.cleaned_data['text'])


        '''
        #if form_obj.is_valid():
            #print("Form is valid")
            #if Form is valid do something
        '''

        '''
        print("Validation successful")
        print("Data entered by user - \n")
        print(form_obj.Cleaned_data['name'])
        print(form_obj.Cleaned_data['email'])
        print(form_obj.Cleaned_data['text'])    
        '''




    else:
        print("Request type is Get")
        form_obj1 = forms.MyReg_Form()


    return render(request,'first_app/MyReg.html',{"form_key1": form_obj1})

def EmployeeLogin(request):
    form = Employee_Login_From
    if request.method=='POST':
        print("Request type is post")
        form= Employee_Login_From(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form is Invalid")
    return render(request,'first_app/EmployeeLogin.html', {'form':form})



class BookListView(ListView):
    model = WebPage

    def head(self, *args, **kwargs):
        #allsites= self.get_queryset().all()
        #last_book = self.get_queryset().latest('publication_date')
        allsites=  self.get_queryset().all()

        response = HttpResponse()
        # RFC 1123 date format
        #response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

def PageOne(request):
    #topics = get_object_or_404(Topic)
    #model = Topic
    topics = Topic.objects.all()
    #names = post.name.filter(active=True)

    return render(request,'first_app/PageOne.html',{'posts':topics})

def PageTwo(request):

    return render(request,'first_app/PageTwo.html')









class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
