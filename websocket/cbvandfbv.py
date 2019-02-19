# -*- coding: utf-8 -*-

from werkzeug.wrappers import Response,Request
from werkzeug.serving import run_simple
import json
@Request.application
def f1(request):
    return Response("hello,world")

class c1(object):
    def __call__(self, *args, **kwargs):
        return Response("hello,world")

if __name__ == "__main__":
    obj=c1()
    run_simple("localhost",9000,obj)




