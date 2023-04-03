import psutil
import utils.time_util as time_util


def get_cpu_percent(user_range, user_interval):
    percents = {}
    for i in range(user_range):
        per = psutil.cpu_percent(interval=user_interval)
        dtime = str(time_util.get_datetime())  # todo stringfy
        percents[dtime] = per
    return percents


def get_cpu_usage():
    cpu = psutil.cpu_times()
    return cpu


print(get_cpu_percent(5, 1))
