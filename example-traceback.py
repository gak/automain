#!/usr/bin/env python

from automain import *


def test1():
    test2()

def test2():
    ()[0]
    print "You'll never see this printed ..."


@automain
def main():
    print 'works!'
    test1()

