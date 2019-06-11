from django.shortcuts import render
from django.views.generic import ListView, DetailView,\
    TemplateView, FormView
from .models import BlogPost
from .forms import PostForm


class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'


# User Post Form
class UserPostForm(FormView):
    form_class = PostForm
    template_name = 'blog/user_post_form.html'
    success_url = '/published-success/'

    def get_context_data(self, **kwargs):
        context = super(UserPostForm, self).get_context_data(**kwargs)
        # context["testing_out"] = "this is a new context var"
        return context

    def form_valid(self, form):
        form.save()
        return super(UserPostForm, self).form_valid(form)


class UserPostFormSuccess(TemplateView):
    template_name = 'blog/success_user_post_form.html'


# ************************************ Testing **********************************************************
# ************************************         **********************************************************
# PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )
#
#
# def get_client_ip(request):
#     """get the client ip from the request
#     """
#     remote_address = request.META.get('REMOTE_ADDR')
#     # set the default value of the ip to be the REMOTE_ADDR if available
#     # else None
#     ip = remote_address
#     # try to get the first non-proxy ip (not a private ip) from the
#     # HTTP_X_FORWARDED_FOR
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         proxies = x_forwarded_for.split(',')
#         # remove the private ips from the beginning
#         while (len(proxies) > 0 and
#                 proxies[0].startswith(PRIVATE_IPS_PREFIX)):
#             proxies.pop(0)
#         # take the first ip which is not a private one (of a proxy)
#         if len(proxies) > 0:
#             ip = proxies[0]
#
#     return render(request, 'testing/ip_check.html', {"ip": ip})

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return render(request, 'testing/ip_check.html', {"ip": ip})

'''
def get_ip_address_from_request(request):
    """ Makes the best attempt to get the client's real IP or return the loopback """
    PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', '127.')
    ip_address = ''
    # is_valid_ip = False
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if x_forwarded_for and ',' not in x_forwarded_for:
        if not x_forwarded_for.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(x_forwarded_for):
            ip_address = x_forwarded_for.strip()
    else:
        ips = [ip.strip() for ip in x_forwarded_for.split(',')]
        for ip in ips:
            if ip.startswith(PRIVATE_IPS_PREFIX):
                continue
            elif not is_valid_ip(ip):
                continue
            else:
                ip_address = ip
                break
    if not ip_address:
        x_real_ip = request.META.get('HTTP_X_REAL_IP', '')
        if x_real_ip:
            if not x_real_ip.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(x_real_ip):
                ip_address = x_real_ip.strip()
    if not ip_address:
        remote_addr = request.META.get('REMOTE_ADDR', '')
        if remote_addr:
            if not remote_addr.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(remote_addr):
                ip_address = remote_addr.strip()
    if not ip_address:
        ip_address = '127.0.0.1'
    return render(request, 'testing/ip_check.html', {"ip": ip_address})
    
'''

def get_ip(request):
    import socket
    import re
    import json
    from urllib.request import urlopen

    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    ip_addr = socket.gethostbyname(socket.gethostname())

    # ==========================
    # import os
    # import IP2Location
    #
    # database = IP2Location.IP2Location(os.path.join("data", "IPV4-COUNTRY.BIN"))
    #
    # rec = database.get_all(ip_addr)
    #
    # print(rec.country_short)
    # print(rec.country_long)
    # print(rec.region)
    # print(rec.city)
    # print(rec.isp)
    # print(rec.latitude)
    # print(rec.longitude)
    # print(rec.domain)
    # print(rec.zipcode)
    # print(rec.timezone)
    # print(rec.netspeed)
    # print(rec.idd_code)
    # print(rec.area_code)
    # print(rec.weather_code)
    # print(rec.weather_name)
    # print(rec.mcc)
    # print(rec.mnc)
    # print(rec.mobile_brand)
    # print(rec.elevation)
    # print(rec.usage_type)

    context = {
        "ip": IP,
        "ip_2": ip_addr,
        "org": org,
        "city": city,
        "country": country,
        "region": region,
    }
    return render(request, 'testing/ip_check.html', context)