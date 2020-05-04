from pydub import AudioSegment
import easygui, time
a=easygui.enterbox('How Many Music Tracks do you want to mix?' )
a=int(a)
z=[]
c=0
q=[]
v=[]
for x in range(0,a):
    b=easygui.fileopenbox()
    print(b)
    if b==None:
        print('Error')
        a+=1
    else:
        z.append(b)
    time.sleep(.5)
for x in range(0,a):
    c+=a
    c=AudioSegment.from_mp3(z[x])
    q.append(c)
    print('%s is finished'% z[x])
output=q[0]
for x in range(0,a-1):
    print('Recoding %s'% z[x])
    a-=1
    output = output.overlay(q[a], position=0)
output.export("mixed_sounds.mp3", format="mp3")