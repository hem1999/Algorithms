def draw_line(tick_length,tick_label = ""):
    line = '-'*tick_length
    if tick_label:
        line+=" "+tick_label
    print(line)

def draw_interval(center_length):
    if center_length>0:
        print(f"Calling draw_interval({center_length-1})")
        draw_interval(center_length-1)
        print(f"Calling draw_line({center_length})")
        draw_line(center_length)
        print(f"Calling draw_interval({center_length-1})")
        draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
    draw_line(major_length,tick_label = '0')
    for j in range(1,1+num_inches):
        print(f"Calling draw_interval({major_length-1})")
        draw_interval(major_length-1)
        print(f"Calling draw_line({major_length},{str(j)})")
        draw_line(major_length,str(j))

if __name__=="__main__":
    print("Please Note: Remove all the prints in draw_ruler and draw_interval functions to get output without recursion trace.!")
    print()
    print()
    draw_ruler(5,3)
