task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ')
time_bound = input('Is it time-bound? (yes/no): ')
match priority:
  case "high":
    if time_bound == "yes":
      print(f'{task} is a high priority task that requires immediate attention today!')
    else:
      print(f"{task} is high priority task you should do it as soon as possible")
  case "medium":
    if time_bound == "yes":
      print(f"{task} is medium priority task. you have to do it befor the deadline after you finished your high priority tasks.")
    else:
      print(f'{task} is medium priority task consider doing it when you are free')
  case "low":
      if time_bound == "no":
        print(f'{task} is a low priority task. Consider completing it when you have free time.')
      else:
        print("You have to finish it before the time finishes")