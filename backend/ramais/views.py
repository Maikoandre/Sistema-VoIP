from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from asterisk.ami import AMIClient, SimpleAction
from .models import Extension
from .serializers import ExtensionSerializer
from django.shortcuts import render

class ExtensionViewSet(viewsets.ModelViewSet):
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer

class MakeCallView(APIView):
    def post(self, request, *args, **kwargs):
        caller = request.data.get('from')
        callee = request.data.get('to')

        if not caller or not callee:
            return Response(
                {'error': 'Both "from" and "to" fields are required.'}, 
                status=status.HTTP_400_BAD_REQUEST
                )
        
        try: 
            client = AMIClient(address='127.0.0.1', port=5038)
            client.login(username='admin', secret='password123')

            action = SimpleAction(
                'Originate',
                Channel=f'PJSIP/{callee}',
                Exten=caller,
                Context='from-internal',      
                Priority=1,
                CallerID=f'API Call <{callee}>'
            )

            client.send_action(action)
            client.logoff()

            return Response({'message': f'Call from {caller} to {callee} initiated successfully.'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        


def index(request):
    # Essa função apenas "renderiza" (mostra) o seu HTML
    return render(request, 'ramais/index.html')
