def evaporator(content, evap_per_day, threshold):
  init = content
  while (content * threshold < init):
    init -= init * (float(init) / float(evap_per_day))
