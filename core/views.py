from django.shortcuts import render,redirect
from django.views import View
from.models import Blog


# Create your views here.
def home(request):
    name = "wisam"
    context = {
        'name' : name,
        'email': "wisam@gmail.com",
        "age" : 20
        
    }
    return render(request, 'index.html', context)
class signupview(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, email, password)

        
        if email == 'wisam@gmail.com' and password == '55555':
            return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Invalid signup'})

class loginview(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        
        if username == 'wisam' and password == '55555':
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    
class DashboardView( View):
    def get(self, request):
        # Dummy data, actual me aapko apne model se lena hoga
        # users_list = [
        #     {'id': 1, 'name': 'Ali', 'age': 25},
        #     {'id': 2, 'name': 'Sara', 'age': 30},
        #     {'id': 3, 'name': 'Ahmed', 'age': 22},
        # ]
        blogs = Blog.objects.all() 
        print(blogs)
        context={
        'blogs': blogs
        }
        
        return render(request, 'dashboard.html', context)
    


# class Blogview(View):
#     def get(self, request):

#         return render(request,'blog.html')

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        print(id)


        blog = Blog.objects.filter(id=id).first()
        context = {
            'blog' : blog
        }
        return render(request, 'blogdetail.html', context)
    

class CreateBlogView(View):
        def get(self, request):

            return render(request, 'create_blog.html')
        
        def post(self, request):
            print("simple query")
            print(request.POST)
            titles = request.POST.get('title')
            descriptions = request.POST.get('description')
            blog_image = request.FILES.get('blog_image')


            print(titles, 123455654443)
            print(descriptions,5555555555333)
            print(blog_image, 453454365934)

            Blog.objects.create(
                title = titles,
                description = descriptions,
                blog_image = blog_image,
            )
            return redirect('dashboard')
            # return render(request, 'create_blog.html')
    


class EditBlogView(View):
  def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        blog = Blog.objects.filter(id=id).first()
        context = {
            'blog' : blog
        }
        return render(request, 'editblog.html', context)
  
  def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        blog_images = request.FILES.get('blog_image')
        print(blog_images)
        blog = Blog.objects.filter(id=id).first()
        blog.title = titles
        blog.description = descriptions
        if blog_images:
            blog.blog_image = blog_images
        blog.save()

        return redirect ('dashboard')


def delete_blog(request, *args, **kwargs):
    id = kwargs.get('id')
    blog = Blog.objects.filter(id=id).first()
    if blog:
        blog.delete()
        return redirect('dashboard')