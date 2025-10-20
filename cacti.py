def cacti_number(input_plot):
    plot = input_plot
    r = len(plot)

    if r == 0 :
        return 0
    
    c = len(plot[0]) 
    total = 0

    for row in range(r):
        for cell in range(c):
            if plot[row][cell] == 0:
                up = (row > 0 and plot[row-1][cell] == 1)
                down = (row < r - 1 and plot[row+1][cell] ==1)
                left = (cell > 0 and plot[row][cell-1] == 1)
                right = (cell < c - 1 and plot[row][cell+1] == 1)

                if not up and not down and not left and not right:
                    plot[row][cell] = 1 
                    total += 1

    return total
