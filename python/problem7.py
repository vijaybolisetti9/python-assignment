print("Become the programmer you're meant to be!")
#calculation the pionts based on number of number of wins losses and draws while a win = 3 points and draw=1 point 
# wins , draws,losses

def foot_ball_points(wins,draws,losses):
    points=0
    points+=(  (int(wins)*3) +  (int(draws)*1) + (int(losses)*0)    )
    print(points)




wins,draws,losses=map(int,input().split())
match_points=foot_ball_points(wins,draws,losses)