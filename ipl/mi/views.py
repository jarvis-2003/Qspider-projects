from django.shortcuts import render
from django.http import HttpResponse as R
# Create your views here.

def captain(request):
    print(request.body)
    return R("<h3>Captain of the Team is hardik pandya</h3><p>The playing team members are : <ul><li>Openers: Rohit Sharma (Batter), Suryakumar Yadav (Batter)</li><li>Top/Middle Order:Ryan Rickelton (WK) / Quinton de Kock (WK)</li><li>All-rounders: Will Jacks, Naman dhir</li><li>Bowlers:Deepak Chahar, Jasprit Bumrah, Trent Boult (Pacer)</li><li>Impact Player Options: Shardul Thakur, Sherfane Rutherford, Swapnil Singh</li></ul></p>")
