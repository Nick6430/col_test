#Yee

def col(pl, obj):
    if pl.x + pl.w/2 > obj.x - obj.w/2 and pl.x - pl.w/2 < obj.x + obj.w/2:
        if pl.y + pl.h/2 > obj.y - obj.h/2 and pl.y - pl.h/2 < obj.y + obj.h/2:
            return True