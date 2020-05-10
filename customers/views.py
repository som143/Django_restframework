from django.shortcuts import render,redirect
from .models import customers
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializer import customerserializer
from rest_framework import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.
"""Start wokirng with classe based rest api view using APIView class in restframework"""
class customerAPiview(APIView):
    def get(self,request):
        customer = customers.objects.all()
        serializer = customerserializer(customer,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = customerserializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
        return Response(serializer.errors)

class customer_detail_api(APIView):
    def get_object(self,pk):
        try:
            customer=customers.objects.get(pk = pk)
            return customer
        except Exception :
            return None
    def get(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        if customer:
            serializer = customerserializer(customer)
            return Response(serializer.data,status=200) 
        else:
            return Response({"msg":"not found"})
    def put(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        serializer = customerserializer(customer,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"msg":"no update available"})
    def patch(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        serializer = customerserializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"msg":"data is not updated"})
    def delete(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        if customer:
            customer.delete()
            return Response({"msg":"data is deleted"})
        return Response({"msg":"no data found"})
"""END wokirng with classe based rest api view using APIView class in restframework"""

"""Start wokirng with classe based rest api view using Genericview and mixins restframework classes"""

class customer_List_genericAPIview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class =  customerserializer
    queryset = customers.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id = None):
        return self.list(request)
    def post(self,request,id = None):
        return self.create(request)

class customer_Detail_genericAPIview(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class =  customerserializer
    queryset = customers.objects.all()
    Lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        return self.retrieve(request,id)
    def put(self,request,id = None):
        return self.update(request,id)
    def delete(self,request,id = None):
        return self.destroy(request,id)
"""End wokirng with classe based rest api view using Genericview and mixins restframework classes"""



"""Working eith function based API"""
@csrf_exempt
def customer_functionAPI(request):
    if request.method == 'GET':
        customer = customers.objects.all()
        serializer = customerserializer(customer,many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = customerserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

@csrf_exempt
def customer_detail_API(request,pk = None):
    try:
        customer = customers.objects.get(pk = kwargs[pk])
        return customer
    except Exception:
        # return JsonResponse({"msg":"requested source is not available"})
        return  None
    if request.method == 'GET':
        serializer = customerserializer(customer)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = customerserializer(customer, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({"msg":"not a valid data"})

    if request.method =='PATCH':
        data = JSONParser().parse(request)
        serializer = customerserializer(customer, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({"msg":"patch is not found"})

    if request.method == "DELETE":
        customer.delete()
        return JsonResponse({"msg":"json data deleted successfully"})

"""End of working with API function view """


"""Start wokirng with functional base api View using api_view decorator"""
@api_view(['GET','POST'])
def customer_deco_api(request):
    if request.method == 'GET':
        customer = customers.objects.all()
        serializer = customerserializer(customer,many =True)
        return Response(serializer.data)
    else:
        if request.method =='POST':
            serializer =  customerserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,{"msg":"error found"})

@api_view(['GET','PUT','PATCH','DELETE'])
def customer_detail_deco_api(request,pk = None):
    try:

        customer = customers.objects.get(pk= pk)
    except Exception:
        return None
        
    if request.method == 'GET':
        serializer = customerserializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = customerserializer(customer,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,{"msg":"error occured"})

    elif request.method == 'PATCH':
        serializer =  customerserializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,{"msg":"not found"})

    elif request.method =='DELETE':
        customer.delete()
        return Response({"msg":"data deleted"} )


"""End of API using Decorator"""

"""END OF DOUBT IN API NOW YOU CAN ROCK IN API"""