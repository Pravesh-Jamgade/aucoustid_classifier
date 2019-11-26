
from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
import io
from rest_framework.parsers import JSONParser
import acoustid
import sys
import os
from boards.serializers import ServiceSerializer
from boards.models import ServiceData


# Create your views here.

class ServiceHandler(viewsets.ModelViewSet):
    queryset = ServiceData.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request):
        
        print('Start Serialization')
        s = ServiceSerializer(data=request.data)
        print('start')
        # retrieve data
        fileName = ""
        isTest = False

        # check validation
        if s.is_valid():
            print('valid')
            fileName = s.data['fileName']
            isTest = s.data['test']
            print(s.data['fileName'])
            print(s.data['test'])
       
        if not fileName:
            print('invalid')
            return Response({"failed"})

        if isTest:
            print('true')
            return self.ProcessTest(fileName)
        else :
            print('false')
            return self.Process(fileName)
        

    def ProcessTest(self, fileName):
        API_KEY = 'YC61VBBeNU'
        try:
            results = acoustid.match(API_KEY, fileName)
        except acoustid.NoBackendError:
            print("chromaprint library/tool not found", file=sys.stderr)
            return Response({"status":False, "Message": "Libraray not found!"})
        except acoustid.FingerprintGenerationError:
            print("fingerprint could not be calculated", file=sys.stderr)
            return Response({"status":False, "Message": "Fingerprint could not be calculates!"})
        except acoustid.WebServiceError as exc:
            print("web service request failed:", exc.message, file=sys.stderr)
            return Response({"status":False, "Message": "Web service request failed!"})

        first = True
        title = ""
        artist = ""
        for score, rid, title, artist in results:
            if first:
                first = False
            else:
                print()
            # print_('%s - %s' % (artist, title))
            title = title
            artist = artist
            # print_('http://musicbrainz.org/recording/%s' % rid)
            # print_('Score: %i%%' % (int(score * 100)))

        print(title, artist)
        serialized = {"status":True, "title": title, "artist": artist}
        return Response(serialized)
        
    def Process(self, fileName):
        API_KEY = 'YC61VBBeNU'
        print('Process')
        try:
            results = acoustid.match(API_KEY, fileName)
        except acoustid.NoBackendError:
            print("chromaprint library/tool not found", file=sys.stderr)
            return Response({"status":False, "Message": "Libraray not found!"})
        except acoustid.FingerprintGenerationError:
            print("fingerprint could not be calculated", file=sys.stderr)
            return Response({"status":False, "Message": "Fingerprint could not be calculates!"})
        except acoustid.WebServiceError as exc:
            print("web service request failed:", exc.message, file=sys.stderr)
            return Response({"status":False, "Message": "Web service request failed!"})

        first = True
        title = ""
        artist = ""
        for score, rid, title, artist in results:
            if first:
                first = False
            else:
                print()
            # print_('%s - %s' % (artist, title))
            title = title
            artist = artist
            # print_('http://musicbrainz.org/recording/%s' % rid)
            # print_('Score: %i%%' % (int(score * 100)))

        print('Process: '+ title+' '+ artist)
        serialized = {"status":True, "title": title, "artist": artist}
        return Response(serialized)  