# Task Midrand Speedster
# JHB Metro Police system
speed= int(input("speed in km/h: "))
speed_limit = int(input("average speed limit: "))
speed_limit_over = speed - speed_limit


if speed <= speed_limit:
    print("OK")
else:
      points = speed_limit_over/5
      points = int(points)
      print(points, "points")
      if points > 12:
          print("Time to goto jail!")


