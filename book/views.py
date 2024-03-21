from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def home(request):
    return render(request, "home.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the books page upon successful login
            return redirect('books')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')


def books(request):
    username = request.user.username
    query = request.GET.get('q', '')
    books = [
    {
        'title': 'Nineteen Eighty-Four',
        'author': 'George Orwell',
        'genre': 'Dystopian Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Mockingbird Chronicles',
        'author': 'Harper Lee',
        'genre': 'Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Magnificent Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'Classic Literature',
        'availability': 'Not Available'
    },
    {
        'title': 'Prejudice and Passion',
        'author': 'Jane Austen',
        'genre': 'Romance',
        'availability': 'Available'
    },
    {
        'title': 'Wizards and Wonders: The Enchanted Stone',
        'author': 'J.K. Rowling',
        'genre': 'Fantasy',
        'availability': 'Available'
    },
    {
        'title': 'The Rye Fields',
        'author': 'J.D. Salinger',
        'genre': 'Literary Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Hobbiton Adventure',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'availability': 'Available'
    },
    {
        'title': 'Animal Farmyard',
        'author': 'George Orwell',
        'genre': 'Political Satire',
        'availability': 'Available'
    },
    {
        'title': 'The Rings of Power',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'availability': 'Available'
    },
    {
        'title': 'New World Order',
        'author': 'Aldous Huxley',
        'genre': 'Dystopian Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Chronicles of the Magic Wardrobe',
        'author': 'C.S. Lewis',
        'genre': 'Fantasy',
        'availability': 'Available'
    },
    {
        'title': 'Whale Tale',
        'author': 'Herman Melville',
        'genre': 'Adventure',
        'availability': 'Available'
    },
    {
        'title': 'Dorians Portrait',
        'author': 'Oscar Wilde',
        'genre': 'Gothic Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Monster Within',
        'author': 'Mary Shelley',
        'genre': 'Gothic Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Heights of Wuthering',
        'author': 'Emily Bronte',
        'genre': 'Gothic Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Adventures of Huck Finn',
        'author': 'Mark Twain',
        'genre': 'Adventure','availability': 'Available'
    },
    {
        'title': 'The Epic Odyssey',
        'author': 'Homer',
        'genre': 'Epic Poetry',
        'availability': 'Available'
    },
    {
        'title': 'The Endless Road',
        'author': 'Cormac McCarthy',
        'genre': 'Post-Apocalyptic Fiction',
        'availability': 'Available'
    },
    {
        'title': 'The Haunted Hotel',
        'author': 'Stephen King',
        'genre': 'Horror',
        'availability': 'Available'
    }
  ]

    if query:
        books = [book for book in books if query.lower() in book['title'].lower()]

    return render(request, 'books.html', {'books': books, 'query': query, 'username': username})

def home1(request):
    return render(request, 'home1.html')
def cart(request):
    return render(request, 'cart.html')

def user_logout(request):
    logout(request)
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def cart_view(request):
    cart_items = [
        {'title': 'Book 1', 'price': 10.99, 'image_url': '/static/book1.jpg'},
        {'title': 'Book 2', 'price': 12.99, 'image_url': '/static/book2.jpg'},
        # Add more items as needed
    ]
    total_price = sum(item['price'] for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout_view(request: HttpRequest):
    # Retrieve book details from URL parameters
    title = request.GET.get('title')
    price = request.GET.get('price')

    # Render the checkout page with the selected book details
    return render(request, 'checkout.html', {'title': title, 'price': price})