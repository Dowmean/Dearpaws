from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import PetForm
from .models import Pet

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # เปลี่ยน 'home' เป็นชื่อ path ของหน้าหลักของคุณ
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')



def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)  # รองรับไฟล์อัปโหลดด้วย request.FILES
        if form.is_valid():
            form.save()  # บันทึกข้อมูลสัตว์เลี้ยงและไฟล์รูปภาพลงในฐานข้อมูล
            return redirect('home')  # เปลี่ยนเส้นทางไปยังหน้า Home หลังจากเพิ่มข้อมูลเสร็จ
    else:
        form = PetForm()

    return render(request, 'pet_create.html', {'form': form})

def home_view(request):
    pets = Pet.objects.all().order_by('-created_at')  # ดึงข้อมูลสัตว์เลี้ยงเรียงตามวันที่สร้างใหม่ -> เก่า
    return render(request, 'home.html', {'pets': pets})
