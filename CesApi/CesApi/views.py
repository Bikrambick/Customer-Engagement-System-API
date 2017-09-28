from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    return Response({
    	'users': reverse('users_api:user_list', request=request, format=format),
        #'registration': reverse('rest-auth', request=request, format=format)
    })