def queue_time(costumers, n):
  queue = costumers
  time_estimate = 0
  tills = []
  for till in n:
    tills.append(0)
  for till in tills:
    for costumer in queue:
      if till == 0 and costumer != 0:
        till = costumer
  
