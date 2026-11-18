import json,os,urllib.request as U
E=os.environ.get('MAKEFUN_ENV_URL')
N=-10;B=(-9,-11,11,9);R=(N,1,10,-1)
D={'P':(N,-20,-11,-9),'N':(-19,-21,-8,-12,12,8,21,19),'B':B,'R':R,'Q':B+R,'K':B+R}
M,L,Z=7e4,5e4,2e5;C={}
def tb(h):
 w=min(h,24)/24;T={}
 for i,p in enumerate('PNBRQK'):
  T[p]=t=[0]*120
  for s in range(64):
   r,f=s//8,s%8;c=min(f,7-f)+min(r,7-r);x=f in(3,4)
   m,e=((100+4*r+12*x*(r in(3,4))-12*x*(r==1),110+2*r*r),(300+7*c,290+5*c),(320+4*c,320+3*c),(480+20*(r>5)+6*x*(r<1),520+10*(r>5)),(940+2*c,960+4*c),(6e4+((20,30,10,0)[min(f,7-f)]if r<1 else-25*r),59970+10*c))[i]
   t[91-10*r+f]=int(e+(m-e)*w)
 return T
T=tb(24)
def rt(b):return b[::-1].swapcase()
def G(p):
 b,_,w,_,ep,k=p
 for i,c in enumerate(b):
  for d in D.get(c,()):
   j=i+d
   while 1:
    q=b[j]
    if q==' 'or q.isupper():break
    if c=='P'and(d in(N,-20)and q!='.'or d==-20 and(i<81 or b[i+N]!='.')or d in(-11,-9)and q=='.'and j!=ep and abs(j-k)>1):break
    yield i,j
    if c in'PNK'or q.islower():break
    if i==91 and b[j+1]=='K'and w[0]:yield j+1,j-1
    if i==98 and b[j-1]=='K'and w[1]:yield j-1,j+1
    j+=d
def V(p,m):
 b,_,_,_,ep,k=p;i,j=m;c=b[i];q=b[j];t=T[c];s=t[j]-t[i]
 if q.islower():s+=T[q.upper()][119-j]
 if abs(j-k)<2:s+=T['K'][119-j]
 if c=='K'and abs(j-i)==2:s+=T['R'][(i+j)//2]-T['R'][91 if j<i else 98]
 if c=='P':
  if j<29:s+=T['Q'][j]-t[j]
  if j==ep:s+=T['P'][109-j]
 return s
def X(p,m):
 b,s,w,o,ep,k=p;i,j=m;c=b[i];s+=V(p,m);b=list(b);e=n=0;b[j]=c;b[i]='.'
 w=w[0]*(i!=91),w[1]*(i!=98);o=o[0]*(j!=28),o[1]*(j!=21)
 if c=='K':
  w=(0,0)
  if abs(j-i)==2:n=(i+j)//2;b[91 if j<i else 98]='.';b[n]='R'
 if c=='P':
  if j<29:b[j]='Q'
  if j-i==-20:e=129-i
  if j==ep:b[j+10]='.'
 return rt(''.join(b)),-s,o,w,e,n and 119-n
def nl(p):return rt(p[0]),-p[1],p[3],p[2],0,0
def th(p,lg,h):
 n=[0];P=set(h);K={}
 def S(p,d,a,g,y):
  n[0]+=1
  if n[0]>Z:1/0
  if p[1]<=-L:return-M
  b=p[0]
  if y and b in P:return 0
  e=C.get(p);u=None
  if e:
   z,v,f,u=e
   if z>=d and(f<1 or f<2 and v>=g or f>1 and v<=a):return v
  q=d<=0;A=a
  if q:
   r=p[1]
   if r>=g:return r
   a=max(a,r);s=[m for m in G(p)if V(p,m)>50]
  else:
   r=-M
   if d<3 and p[1]-120*d>=g:return p[1]
   if d>2 and p[1]>=g and any(map(b.count,'NBRQ')):
    v=-S(nl(p),d-3,-g,1-g,y+1)
    if v>=g:return v
   s=list(y and G(p)or lg)
  l=K.get(y)
  s.sort(key=lambda m:-(2e5*(b[m[1]]!='.')+1e5*(m==l)+V(p,m)))
  if u in s:s.remove(u);s.insert(0,u)
  P.add(b);u=None;k=0;F=d==1 and p[1]+150<=a
  for m in s:
   if F and k and b[m[1]]=='.'and V(p,m)<100:r=max(r,p[1]);continue
   c=X(p,m)
   if q or k<1:v=-S(c,d-1,-g,-a,y+1)
   else:
    x=d>2 and k>3 and b[m[1]]=='.'
    v=-S(c,d-1-x,-a-1,-a,y+1)
    if v>a and(x or v<g):v=-S(c,d-1,-g,-a,y+1)
   k+=1
   if v>r:r=v;u=m
   if v>a:a=v
   if a>=g:
    if b[m[1]]=='.'and not q:K[y]=m
    break
  P.discard(b)
  if not q and r==-M:o=nl(p);r=-M+y if any(V(o,m)>=L for m in G(o))else 0
  if len(C)>3e5:C.clear()
  C[p]=d,r,1 if r>=g else 2 if r<=A else 0,u
  return r
 m=lg[0]
 try:
  for d in range(1,99*(len(lg)>1)):
   v=S(p,d,-M,M,0);m=C[p][3]
   if abs(v)>=L:break
 except:pass
 return m
def sq(s,f):i=ord(s[0])+4-10*int(s[1]);return f and 119-i or i
def nm(i,f):i=f and 119-i or i;return chr(i%10+96)+str(10-i//10)
def ps(g):
 global T
 f=g.split();b=' '*21
 for w in f[0].split('/'):
  for c in w:b+='.'*int(c)if c.isdigit()else c
  b+='  '
 b=b[:-1]+' '*20;k=f[2];x=f[1]=='b'
 T=tb(sum(map(b.lower().count,'nbrrqqqq')))
 w,o=('Q'in k,'K'in k),('k'in k,'q'in k)
 if x:b=rt(b);w,o=o,w
 F=lambda b:sum(T[c][i]for i,c in enumerate(b)if c in T)
 return(b,F(b)-F(rt(b)),w,o,f[3]>'-'and sq(f[3],x),0),x
def po(u,o):
 with U.urlopen(E+u,json.dumps(o).encode())as h:return json.load(h)
g0=0
while E:
 g=po('/game',{})
 if g['status']=='done':break
 if g['game']!=g0:g0=g['game'];h=set();C.clear()
 while g['status']=='your_move':
  p,x=ps(g['fen']);h.add(p[0])
  m=th(p,[(sq(u[:2],x),sq(u[2:4],x))for u in g['legal_moves']if len(u)<5 or'q'==u[4]],h);h.add(X(p,m)[0])
  g=po('/move',{'game':g['game'],'move':nm(m[0],x)+nm(m[1],x)+'q'*(p[0][m[0]]=='P'and m[1]<29)})
