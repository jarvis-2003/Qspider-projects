from django.shortcuts import render
from django.http import HttpResponse as R
# Create your views here.

def captain(request):
    return R("<h3>Captain of the Team is  Rajat Patidar</h3><p>The playing team members are : <ul><li>Openers: Virat Kohli, Phil Salt (WK)</li><li>Top/Middle Order: Devdutt Padikkal, Rajat Patidar (C), Tim David, Jitesh Sharma (WK)</li><li>All-rounders: Krunal Pandya, Romario Shepherd</li><li>Bowlers: Bhuvneshwar Kumar, Josh Hazlewood, Suyash Sharma</li><li>Impact Player Options: Rasikh Salam Dar, Jacob Duffy, Swapnil Singh</li></ul></p>")
