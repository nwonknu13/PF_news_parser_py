import datetime

class Time_calc:

    def Set_seconds_limit(self, limit, now_):

        seconds_limit = 0

        if (limit == 'M'):
            a_month_ago = now_
            if (now_.month > 1):
                a_month_ago = datetime.datetime(now_.year, (now_.month - 1), now_.day, now_.hour, now_.minute,
                                                now_.second,
                                                now_.microsecond, now_.tzinfo)
            else:
                a_month_ago = datetime.datetime((now_.year - 1), 12, now_.day, now_.hour, now_.minute, now_.second,
                                                now_.microsecond, now_.tzinfo)

            seconds_in_month = (now_ - a_month_ago).total_seconds()
            seconds_limit = seconds_in_month
        else:
            seconds_limit = 3600 * 24 * int(limit)

        return seconds_limit


    def Create_datetime_story(self, meta_info):

        datetime_str = meta_info.find('time').get('datetime').split('T')
        date_ = [int(each) for each in datetime_str[0].split('-')]
        time_ = [int(each) for each in datetime_str[1].replace('Z', '').split(':')]
        datetime_story = datetime.datetime(date_[0], date_[1], date_[2], time_[0], time_[1], time_[2])
        return datetime_story


    def Limit_is_exceeded(self, now_, meta_info, seconds_limit):

        datetime_story = self.Create_datetime_story(meta_info)
        time_delta = now_ - datetime_story
        limit_is_exceeded = time_delta.total_seconds() > seconds_limit
        return limit_is_exceeded