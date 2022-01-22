def check_col(order, column, beam):
    if order[1]==0 or order[0:2] in [[b[0],b[1]+1] for b in column]:
        return 1
    elif order[0:2] in [[a[0]+1,a[1]] for a in beam] and order[0:1] not in [[a[0],a[1]] for a in beam]:
        return 1
    else:
        return 0
    
def check_beam(order, column, beam):
    if order[0:2] in [[b[0], b[1]+1] for b in column] or [order[0]+1,order[1]] in [[b[0], b[1]+1] for b in column]:
        return 1
    elif order[0:2] in [[a[0]+1,a[1]] for a in beam] and [order[0]+1,order[1]] in [[a[0],a[1]] for a in beam]:
        return 1
    else:
        return 0    

def solution(n, build_frame):
    column = []
    beam = []

    for i in build_frame:
        if i[3] == 0:
            if i[2] == 0:
                column.remove(i[0:3])
                for k in column:
                    if not check_col(k, column, beam):
                        column.append(i[0:3])
                    else:
                        continue
            else:
                beam.remove(i[0:3])
                for k in beam:
                    if not check_beam(k, column, beam):
                        beam.append(i[0:3])
                    else:
                        continue
        else:
            if i[2] == 0:
                if check_col(i, column, beam):
                    column.append(i[0:3])
            else:
                if check_beam(i, column, beam):
                    beam.append(i[0:3])

    answer = column + beam
    answer.sort()
    return answer
