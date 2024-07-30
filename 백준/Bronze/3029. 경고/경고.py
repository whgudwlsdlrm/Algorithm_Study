import sys
input = sys.stdin.readline

current = input()
current_hour = int(current[:2])
current_minute = int(current[3:5])
current_second = int(current[6:])

bomb = input()
bomb_hour = int(bomb[:2])
bomb_minute = int(bomb[3:5])
bomb_second = int(bomb[6:])

second = bomb_second - current_second
minute = bomb_minute - current_minute
hour = bomb_hour - current_hour

if second < 0:
  minute -= 1
  second += 60
second = str(second)
if len(second) == 1:
  second = '0'+second

if minute < 0:
  hour -= 1
  minute += 60
minute = str(minute)
if len(minute) == 1:
  minute = '0'+minute

if hour < 0:
  hour += 24
hour = str(hour)
if len(hour) == 1:
  hour = '0'+hour

if hour == '00' and minute == '00' and second == '00':
  print('24:00:00')
else:
  print(f"{hour}:{minute}:{second}")