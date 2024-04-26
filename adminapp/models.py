from django.db import models
from django.shortcuts import redirect, render


# Create your models here.
class  Admin(models.Model):
    id =models.AutoField(primary_key=True)
    username= models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
       db_table ="admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id= models.AutoField(primary_key=True)
    coursecode= models.CharField(max_length=50,blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)

    department=models.CharField(max_length=50, blank=False)
    department_choices = (("CSE", "CSE"), ("ECE", "ECE"), ("IOT", "IOT"))


    academicyear_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"), ("2021-22", "2021-22"))

    academicyear = models.CharField(max_length=20, blank=False,choices=academicyear_choices)

    semester_choices = (("ODD-semester", "ODD"), ("EVEN-semester", "EVEN"), ("Summer", "EVEN"))

    semester= models.CharField(blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)

    class Meta:
       db_table ="Course_table"

    def __str__(self):
        return self.coursecode



class Student(models.Model):
    objects = None
    id= models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100, blank=False)

    gender_choices = (("Female", "Female"), ("Male", "Male"), ("Others", "Others"))
    gender=models.CharField(max_length=200, blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department=models.CharField(max_length=50, blank=False,choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"),("M.Tech", "M.Tech"),("B.com", "B.com"))
    program=models.CharField(max_length=10, blank=False,choices=program_choices)

    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"), ("SUMMER", "SUMMER"))
    semester=models.CharField(max_length=20, blank=False,choices=semester_choices)

    year=models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact= models.CharField(max_length=10,blank=False,unique=True)

    class Meta:
       db_table ="Student_table"

    def __str__(self):
        return str(self.studentid)



class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gender_choices = (("Female", "Female"), ("Male", "Male"), ("Others", "Others"))
    gender = models.CharField(max_length=20, blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)

    qualification_choices=(("MD", "MD"), ("PHD", "PHD"), ("Dr.", "Dr."))
    qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)

    designation_choices = (("Prof.", "Professor"), ("Assoc. Prof", "Assoc Professor"), ("Asst. Prof", "Assistant professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "Faculty_table"

    def __str__(self):
        return str(self.facultyid)




def contactfunction(request):
    if request.method == 'POST':
        # If the form is submitted
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        country = request.POST.get('country')
        subject = request.POST.get('subject')

        # Create a new ContactForm object and save it to the database
        ContactForm.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            country=country,
            subject=subject
        )

        # Redirect to a success page or render a thank you message
        return redirect('success.html')  # You can replace 'success' with the name of your success page URL pattern
    else:
        # If it's a GET request, just render the contact form template
        return render(request, "contact.html")