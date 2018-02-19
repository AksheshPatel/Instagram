# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from .models import User, Follow
from posts.models import Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form": form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/login/')
def followlist_view(request):
    if not request.user.is_authenticated:
        raise Http404
    users = User.objects.filter(~Q(id=request.user.id)).filter(~Q(id=1))
    print(users)
    followed_users = User.objects.all().filter(following__follower__id=request.user.id)
    users = set(users) - set(followed_users)
    # print(users)
    # print(User.objects.filter(id = request.user.id))
    return render(request, "followlist.html", {"users": users, "followed_users": followed_users})
    # return render(request, "followlist.html", {"users": users})


def unfollow_view(request, id=None):
    if not request.user.is_authenticated:
        raise Http404

    Follow.objects.all().filter(follower=request.user, following=User.objects.get(id=id)).delete()
    return redirect('/follow')


def follow_view(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    instance = Follow()
    instance.following = User.objects.get(id=id)
    instance.follower = request.user
    instance.save()
    return redirect('/follow')


def profile_follower(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    user = User.objects.get(id=id)
    follow1 = Follow.objects.filter(Q(following=user))
    return render(request, "list_followers.html", {"instance": follow1})


def profile_following(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    user = User.objects.get(id=id)
    followi = Follow.objects.filter(Q(follower=user))
    return render(request, "list_following.html", {"instance": followi})


@login_required(login_url='/login/')
def profile_view(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    instance = User.objects.get(id=id)
    # list = []
    # list.append(request.user)
    queryset = Post.objects.all().filter(user__in=id)
    return render(request, "profile.html", {"user": instance, "quesryset": queryset})


def search_view(request):
    if not request.user.is_authenticated:
        raise Http404
    query = request.GET.get("q")
    users = User.objects.filter(~Q(id=request.user.id)).filter(~Q(id=1))
    followed_users = User.objects.all().filter(following__follower__id=request.user.id)
    users2 = set(users) - set(followed_users)
    #curuser=User.objects.filter(id = request.user.id)
    if query:
        userlist = User.objects.all().filter(Q(name__icontains=query)
                                             | Q(username__icontains=query))
    #print userlist
    return render(request, "search.html", {"users": userlist,"followed_users":followed_users,"users2":users2})


def editprofile(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    instance = get_object_or_404(User, id=id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Profile Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, "editprofile.html", context)


def otherprofile(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    instance = User.objects.get(id=id)
    print(instance.id)
    queryset = Post.objects.all().filter(user__in=id)
    print(queryset)
    users = User.objects.filter(~Q(id=request.user.id)).filter(~Q(id=1))
    # instance2 = User.objects.filter(id=id)
    # print(instance2)
    # if instance:
    #     userlist = User.objects.all().filter(Q(name__icontains=instance)
    #                                          | Q(username__icontains=instance))

    followed_users = User.objects.all().filter(following__follower__id=request.user.id)
    users2 = set(users) - set(followed_users)
    return render(request, "other_profile.html", {"user": instance, "quesryset": queryset,"followed_users":followed_users,"users2":users2})
    #return render(request, "other_profile.html", {"user": instance, "quesryset": queryset})