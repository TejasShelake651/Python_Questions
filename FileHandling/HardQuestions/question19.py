# 19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.

file = open("attendance.txt","r")
lines = file.readlines()
file.close()

for line in lines:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    attended = int(data[2])
    total = int(data[3])

    percentage = (attended/total)*100

    print(name,"=",percentage,"%")

    if percentage < 75:
        print(name,"has attendance below 75%")
