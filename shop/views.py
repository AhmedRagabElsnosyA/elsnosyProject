from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Clients
from datetime import datetime
import os
from openpyxl import Workbook



def AddClient(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST['date']
        doctor = request.POST['doctor']
        # type_of_glass = request.POST['type_of_glass']
        # type_of_lenses = request.POST['type_of_lenses']
        # price =float( request.POST['price'])
        # paid_up = float(request.POST['paid_up'])
        # residual = price-paid_up
        right_sph = request.POST['right_sph']
        right_cyl = request.POST['right_cyl']
        right_axis = request.POST['right_axis']
        left_sph = request.POST['left_sph']
        left_cyl = request.POST['left_cyl']
        left_axis = request.POST['left_axis']
        addition = request.POST['addition']
        client = Clients.objects.create(
            name=name,
            phone=phone,
            address=address,
            date=date,
            doctor=doctor,
            # type_of_glass=type_of_glass,
            # type_of_lenses=type_of_lenses,
            # price=price,
            # paid_up=paid_up,
            # residual=residual,
            right_sph=right_sph,
            right_cyl=right_cyl,
            right_axis=right_axis,
            left_sph=left_sph,
            left_cyl=left_cyl,
            left_axis=left_axis,
            addition=addition

        )
        save_to_excel()
        # return redirect('ViewClient')
    return render(request,"index.html")


def save_to_excel():
    # Get the current working directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the path for the Excel file
    excel_file_path = os.path.join(
        base_dir, "F:\ShopProject\ShopProject\elsnosyshop\elsnosyshop\clients.xlsx")

    # Get all clients
    clients = Clients.objects.all()

    # Create a new Excel workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Define the header row
    header = ['Name', 'Phone', 'Address', 'Date', 'Doctor',  'Right Sph', 'Right Cyl', 'Right Axis', 'Left Sph', 'Left Cyl', 'Left Axis', 'Addition']

    # Write the header to the worksheet
    worksheet.append(header)

    # Loop through all clients and add their data to the worksheet
    for client in clients:
        client_data = [client.name, client.phone, client.address, client.date, client.doctor, client.right_sph,
                       client.right_cyl, client.right_axis, client.left_sph, client.left_cyl, client.left_axis,
                       client.addition]
        worksheet.append(client_data)

    # Save the workbook to the Excel file
    workbook.save(excel_file_path)


def ViewClient(request):
    clients = Clients.objects.all()

    context = {'clients':clients}
    return render(request, "ViewClient.html", context)


def deleteClient(request, client_id):
    client=Clients.objects.get(id=client_id)
    client.delete()
    return redirect("ViewClient")


def EditClient(request, client_id):
    client = get_object_or_404(Clients, id=client_id)

    if request.method == 'POST':
        # Update the client data with the new values
        client.name = request.POST['name']
        client.phone = request.POST['phone']
        client.address = request.POST['address']
        client.date = request.POST['date']
        client.doctor = request.POST['doctor']
        # client.type_of_glass = request.POST['type_of_glass']
        # client.type_of_lenses = request.POST['type_of_lenses']
        # client.price = float(request.POST['price'])
        # client.paid_up = float(request.POST['paid_up'])
        # client.residual = client.price - client.paid_up
        client.right_sph = request.POST['right_sph']
        client.right_cyl = request.POST['right_cyl']
        client.right_axis = request.POST['right_axis']
        client.left_sph = request.POST['left_sph']
        client.left_cyl = request.POST['left_cyl']
        client.left_axis = request.POST['left_axis']
        client.addition = request.POST['addition']

        client.save()  # Save the updated client data
        return redirect('ViewClient')  # Redirect to the view clients page

    return render(request, "EditData.html", {'client': client})

def ViewDetailsForCient(request, client_id):
    client=Clients.objects.get(id=client_id)
    context={'client':client}
    return render(request,"ViewDetailsForClient.html",context)


def ViewfilterClient(request):
    query = request.GET.get('q')
    clients = Clients.objects.all()

    if query:
        clients = clients.filter(
            Q(name__icontains=query) | Q(phone__icontains=query))

    context = {'clients': clients}
    return render(request, "ViewClient.html", context)
