from video.models import Chat
from django.http.response import JsonResponse
# from video.models import Chat
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        command = request.POST['command']
        if (command == 'create'):
            room = request.POST['room']
            no_of_user = request.POST['users']
            check  = Chat.objects.filter(room_name=room)
            if check:
                return JsonResponse({
                    'command':'exist'
                })
            else:
                if(no_of_user == 'All'):
                    create = Chat.objects.create(room_name=room,allowed_users='All',total_users='All',no_of_users='All')
                    return JsonResponse({
                            'command':"created"
                        })
                else:
                    total_user = int(no_of_user) + 1
                    create = Chat.objects.create(room_name=room,allowed_users=no_of_user,total_users=str(total_user),no_of_users=1)
                    if create:
                        return JsonResponse({
                            'command':"created"
                        })
        else:
            print("joined")
            room = request.POST['room']
            print(room)
            check = Chat.objects.filter(room_name=room)
            if check:
                checked = check[0]
                total_user = checked.total_users
                allowed_users = checked.allowed_users
                no_of_users = checked.no_of_users
                if(allowed_users == 'All'):
                    return JsonResponse({
                        'command':'redirect'
                    })
                elif(total_user == no_of_users):
                    return JsonResponse({
                        'command':'full'
                    })
                else:
                    print('agya hun')
                    print(checked)
                    checked.no_of_users = int(no_of_users) + 1
                    checked.save()
                    return JsonResponse({
                        'command':'redirect'
                    })
            else:
                return JsonResponse({
                        'command':'not exist'
                    })



    # if request.method == 'POST':
    #     command = request.POST['command']
    #     if command == 'create':
    #         room = request.POST['room_name']
    #         users = request.POST['users']
    #         check = Chat.objects.filter(room_name=room)
    #         if check:
    #             return JsonResponse({
    #                 'command':"exist"
    #             })
    #         else:
    #             if(users == 'All'):
    #                 create = Chat.objects.create(room_name=room,allowed_users=users,total_users='All',no_of_users='All')
    #             else:
    #                 allowed_users = str(users)
    #                 total_user = int(users)+1
    #                 create = Chat.objects.create(room_name=room,allowed_users=allowed_users,total_users=total_user,no_of_users=1)
    #                 if create:
    #                     return JsonResponse({
    #                     'command':"created"
    #                     })
    #     elif command == 'join':
    #         room = request.POST['room_name']
    #         check = Chat.objects.filter(room_name=room)
    #         if check:
    #             checked = check[0]
    #             total_user = checked.total_users
    #             allowed_users = checked.allowed_users
    #             no_of_users = checked.no_of_users
    #             if(allowed_users == 'All'):
    #                 return JsonResponse({
    #                     'command':'redirect'
    #                 })
    #             elif(total_user == no_of_users):
    #                 return JsonResponse({
    #                     'command':'full'
    #                 })
    #             else:
    #                 checked.no_of_users = int(no_of_users) + 1
    #                 checked.save()
    #                 return JsonResponse({
    #                     'command':'redirect'
    #                 })

    #         else:
    #             return JsonResponse({
    #                 'command':'not exist'
    #             })
    return render(request,'index.html')

def chat(request,room):
    return render(request,'chat.html',{'roomname':room})