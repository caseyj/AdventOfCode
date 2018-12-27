import unittest
import sleepTracking
import pandas as pd

class TestGuardCheckin(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame()
    
    def testOneCheckIn(self):
        df = sleepTracking.guard_checkin(self.df, 1, "11-30")
        self.assertEqual(60, len(df))
        self.assertEqual(1, df['Guard'].iloc[0])

class TestUpdateGuardSleep(unittest.TestCase):
    def setUp(self):
        df = sleepTracking.guard_checkin(pd.DataFrame(), 1, "11-30")
        df = sleepTracking.guard_checkin(df, 2, "10-31")
        self.df = df
    
    def test_GuardSleep2Min(self):
        sleepTracking.update_guard_sleep(self.df, "11-30", 30,31)
        sleeper = self.df.loc[self.df['Wake']==False]
        self.assertEqual(1,len(sleeper))
        self.assertEqual(1, sleeper['Guard'].iloc[0])

class TestGetDateTime(unittest.TestCase):

    def setUp(self):
        self.log_to_test0 = "[1518-11-01 00:00] Guard #10 begins shift"
        self.log_to_test1 = "[1518-11-01 00:05] falls asleep"
        self.log_to_test2 = "[1518-11-01 00:25] wakes up"
    
    def test_GetDateTime(self):
        self.assertEqual(("11-01", 0), sleepTracking.get_date_time(self.log_to_test0))
        self.assertEqual(("11-01", 5), sleepTracking.get_date_time(self.log_to_test1))
        self.assertEqual(("11-01", 25), sleepTracking.get_date_time(self.log_to_test2))

class testGetLogType(unittest.TestCase):
    def setUp(self):
        self.log_to_test0 = "[1518-11-01 00:00] Guard #10 begins shift"
        self.log_to_test1 = "[1518-11-01 00:05] falls asleep"
        self.log_to_test2 = "[1518-11-01 00:25] wakes up"
    
    def testGetLogType(self):
        self.assertEqual(sleepTracking.LogType.start_shift, sleepTracking.get_log_type(self.log_to_test0))
        self.assertEqual(sleepTracking.LogType.falls_asleep, sleepTracking.get_log_type(self.log_to_test1))
        self.assertEqual(sleepTracking.LogType.wakes_up, sleepTracking.get_log_type(self.log_to_test2))

class testGetGuardNo(unittest.TestCase):
    def setUp(self):
        self.log_to_test0 = "[1518-11-01 00:00] Guard #10 begins shift"
    
    def testGetGuardID(self):
        self.assertEqual(10, sleepTracking.get_guard_no(self.log_to_test0))

