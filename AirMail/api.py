from tastypie.resources import ModelResource
from loginsys.models import Profile
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields
from django.contrib.auth.models import User
from django.db.models import Q

class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        excludes = ['email', 'password', 'is_superuser']
        always_return_data = True
        fields = ['username']

    def obj_get(self, bundle, **kwargs):
        user = None
        if 'pk' in kwargs:
            user = User.objects.get(Q(id=kwargs['pk']))
        elif 'id' in kwargs:
            user = User.objects.get(Q(id=kwargs['id']))

        return user

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_create(self, bundle, **kwargs):
        bundle = super(UserResource, self).obj_create(bundle, **kwargs)
        return bundle

class ProfileResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user', null=False)

    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        #fields = ['id', 'Messages', 'Established', 'CountMess']

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])

        return data_dict

    def obj_get(self, bundle, **kwargs):
        pr = None
        if 'pk' in kwargs:
            pr = Profile.objects.get(Q(id=kwargs['pk']) & Q(user=bundle.request.user))
        elif 'id' in kwargs:
            pr = Profile.objects.get(Q(id=kwargs['id']) & Q(user=bundle.request.user))

        return pr

    def obj_create(self, bundle, **kwargs):
        """
        Assign created notes to the current user
        """
        return super(ProfileResource, self).obj_create(bundle, user=bundle.request.user)


    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)