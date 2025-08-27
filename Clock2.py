from datetime import datetime, timedelta

now = datetime.now()
adjusted_time = now - timedelta(hours=4)

print(adjusted_time.strftime("%H:%M"))
