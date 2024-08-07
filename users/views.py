from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser

import re

def is_valid_phone_number(phone_number):
    # Define a regex pattern for a valid phone number format
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    
    # Match the input phone number with the pattern
    if pattern.match(phone_number):
        return True
    else:
        return False
    
def is_valid_email(email):
    # Define a regex pattern for a valid email format
    pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    
    # Match the input email with the pattern
    return bool(pattern.match(email))


class UserRegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')

        # check if any field is missing
        if not username or not first_name or not last_name or not password or not password_confirm or not phone_number:
            return Response({'error': 'Please provide all required fields.'}, status=400)

        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=400)

        if password != password_confirm:
            return Response({'error': 'Passwords do not match.'}, status=400)

        if not is_valid_phone_number(phone_number):
            return Response({'error': 'Invalid phone number.'}, status=400)
        
        if email:
            if not is_valid_email(email):
                return Response({'error': 'Invalid email.'}, status=400)

        user = CustomUser.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.email = email
        user.save()

        return Response({'message': 'User created successfully.'}, status=201)

