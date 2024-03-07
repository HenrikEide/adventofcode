import sys
lines = sys.stdin.read().split("\n")
points = []
for line in lines:
    x, y = line.split(" -> ")
    x1,y1 = [int(a) for a in x.split(",")]
    x2,y2 = [int(a) for a in y.split(",")]
    xs = list(range(min(x1, x2),max(x1,x2)+1))
    ys = list(range(min(y1, y2),max(y1,y2)+1))
    if len(xs)==1:
        xs = [x1 for _ in ys]
    elif len(ys)==1:
        ys = [y1 for _ in xs]
    for p in zip(xs,ys):
        points.append(p)
print(points[:100])
print(set(points[100]))
print(len(points)- len(set([str(v) for v in points])))