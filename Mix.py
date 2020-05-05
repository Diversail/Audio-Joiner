from pydub import AudioSegment
import easygui,time,os
z=[]
c=0
q=[]
v=[]
def Main():
    global c
    a=easygui.enterbox('How Many Music Tracks do you want to mix?' )
    a=int(a)
    for x in range(0,a):
        b=easygui.fileopenbox()
        while b==None:
            b=easygui.fileopenbox()
        print(b)
        p=os.path.getsize(b)
        if p>10000000:
            m=1
            print('File to large, try under 10 MB')
        else:
            z.append(b)
    so = sorted(z, key = os.path.getsize)
    so.reverse()
    print(so)
    for x in range(0,a):
        c+=a
        c=AudioSegment.from_mp3(so[x])
        q.append(c)
        print('%s is finished!'% so[x])
    output=q[0]
    print('Recoding %s'% q[0])
    for x in range(0,a-1):
        a-=1
        print('Recoding %s'% so[a])
        output = output.overlay(q[a], position=0)
    output.export("mixed_sounds.mp3", format="mp3")
Main()
print('Done!')
