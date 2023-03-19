from datetime import datetime
def tstamp():
  now = datetime.now()
  timestamp = datetime.timestamp(now)
  date_time = datetime.fromtimestamp(timestamp)
  rts_dr = date_time.strftime("%c")
  return rts_dr
