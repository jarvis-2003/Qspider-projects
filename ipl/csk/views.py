from django.shortcuts import render
from django.http import HttpResponse as R
# Create your views here.
def captain(request):
    return R("<h3>Captain of the Team is  Ruturaj Gaikwad</h3><p>The playing team members are : <ul><li>Top Order: Ruturaj Gaikwad (C), Sanju Samson (WK), Dewald Brevis</li><li>Middle Order: Shivam Dube, Urvil Patel/Ayush Mhatre, Kartik Sharma/Prashant Veer</li> <li>Finishers/All-rounders: MS Dhoni (WK), Jamie Overton</li><li>Bowlers: Akeal Hosein, Noor Ahmad, Khaleel Ahmed/Matt Henry</li><li>Key Impact Players: Mukesh Choudhary, Sarfaraz Khan</li></ul></p>")
