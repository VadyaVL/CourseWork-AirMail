# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.contrib import auth
from django.core.paginator import Paginator
from django.db.models import Q, F
from models import *

import forms,random

notLogin = "Для перегляду даної сторінки потрібно увійти до системи"
notLoginAtHomePage = "Для того, щоб відправляти повідомлення вам необхідно здійснити вхід."

def home(request):
    args = {}
    args['user'] = auth.get_user(request)
    if type(args['user']) != AnonymousUser:
        args['MessForm'] = forms.MessageForms()

        if request.method == 'POST' and args['user'] is not None:
            #print 'Post and User'
            mess_form = forms.MessageForms(request.POST)
            if mess_form.is_valid():
                #print 'Form is valid'
                dialogue = Dialogue(CountMess=1, ForReceiver=True)
                dialogue.Established = datetime.now()
                dialogue.Creator_id = args['user']
                dialogue.Receiver_id = args['user']
                dialogue.save()

                mess = mess_form.save(commit=False)
                mess.DateSent = datetime.now()
                mess.Dialogue_id = dialogue
                mess.User_id = args['user']
                mess_form.save()

                #отримуємо рандомне. тут і умову отримання пропишемо
                NewMessage = Dialogue.objects.filter(Q(CountMess=1) & ~Q(Creator_id=args['user']) &
                                                     Q(Receiver_id=F('Creator_id')))

                if len(NewMessage)!=0:
                    i = random.randint(0, len(NewMessage)-1)
                    NewMessage = NewMessage[i]
                    NewMessage.Receiver_id = args['user'];
                    NewMessage.save()
                    ##################################
                    args = {}
                    args['dialog'] = NewMessage
                    args['MessForm'] = forms.MessageForms()
                    args['user'] = auth.get_user(request)

                    messages = Message.objects.filter(Q(Dialogue_id=args['dialog']))
                    current_page = Paginator(messages, 10)
                    args['messages'] = current_page.page(current_page.num_pages)

                    return render(request, 'viewDialog.html', args)
                else:
                    return redirect('/')
            else:
                args['MessForm'] = mess_form
    else:
        args['mess'] = notLoginAtHomePage
    return render(request, 'home.html', args)

def view(request):
    args = {}
    args['user'] = auth.get_user(request)

    if type(args['user']) != AnonymousUser:
        args['list'] = Dialogue.objects.filter(~Q(Receiver_id=args['user']) & Q(Creator_id=args['user']) &
                                               Q(ForReceiver=False) |
        ~Q(Creator_id=args['user']) & Q(Receiver_id=args['user']) & Q(ForReceiver=True))
    #Вибірка лише моїх, лише для мене, лише не прочитаних.
        return render(request, 'view.html', args)
    else:
        args['mess'] = notLogin
        return render(request, 'info.html', args)

def getDialogue(request, dialogue_id, page_number=0):

    args = {}
    args['user'] = auth.get_user(request)
    if type(args['user']) != AnonymousUser:
        args['dialog'] = Dialogue.objects.get(id=dialogue_id)
        args['MessForm'] = forms.MessageForms()

        if request.method == 'POST':
            mess_form = forms.MessageForms(request.POST)
            if mess_form.is_valid():
                args['dialog'].CountMess += 1

                if args['dialog'].ForReceiver:
                    args['dialog'].ForReceiver = False
                else:
                    args['dialog'].ForReceiver = True

                args['dialog'].save()

                mess = mess_form.save(commit=False)
                mess.DateSent = datetime.now()
                mess.Dialogue_id = args['dialog']
                mess.User_id = auth.get_user(request)
                mess_form.save()

            else:
                args['MessForm'] = mess_form

        messages = Message.objects.filter(Q(Dialogue_id=args['dialog']))
        current_page = Paginator(messages, 10)

        if page_number == 0:
            page_number = current_page.num_pages

        args['messages'] = current_page.page(page_number)
        return render(request, 'viewDialog.html', args)
    else:
        args['mess'] = notLogin
        return render(request, 'info.html', args)

def about(request):

    return render(request, 'about.html')