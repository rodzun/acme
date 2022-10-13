import unittest
import constants

from acme_solution import ACME


def setUpModule():
    global acme 
    global persons 
    acme = ACME()
    with open('data.txt', 'r') as f:        
        persons = f.read().splitlines()
    

class TestAcmeClassMethods(unittest.TestCase):
    def test_name_days_splitter(self):
        person = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        name, days = acme.nameDaysSplitter(person)
        self.assertEqual('RENE',name)
        self.assertEqual('MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', days)

    def test_days_splitter(self):
        daysString = 'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00'
        daysList = ['MO10:00-12:00','TU10:00-12:00','TH01:00-03:00']
        self.assertEqual(acme.daysSplitter(daysString),daysList)

    def test_dayName_times_splitter(self):
        dayTime = 'MO10:00-12:00'
        day = 'MO'
        time = '10:00-12:00'
        self.assertEqual(day,acme.dayNameTimesSplitter(dayTime)[0])
        self.assertEqual(time,acme.dayNameTimesSplitter(dayTime)[1])

    def test_hours_splitter(self):
        time = '10:00-12:00'
        startHour = 10
        finishHour = 12
        self.assertEqual(acme.hoursSplitter(time)[0],startHour)
        self.assertEqual(acme.hoursSplitter(time)[1],finishHour)

    def test_person_payment(self):
        person = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        self.assertEqual('The amount to pay RENE is: 215 USD',acme.personPayment(person))
    

class TestStringDataIntegrity(unittest.TestCase):
    
    def test_each_person_string_contains_equal_sign(self):
        for person in persons:
            self.assertIn('=',person)
    
    def test_name_exists(self):
        for person in persons:
            self.assertNotEqual('',acme.nameDaysSplitter(person)[0])

    def test_days_exists(self):
        for person in persons:
            self.assertNotEqual('',acme.nameDaysSplitter(person)[1])

    def test_day_names_correct(self):
        daysNames = constants.regularDays + constants.weekends
        for person in persons:
            days = acme.nameDaysSplitter(person)[1]
            daysList = acme.daysSplitter(days)
            for day in daysList:    
                self.assertIn(acme.dayNameTimesSplitter(day)[0],daysNames)   
    
    def test_times_correct(self):
        for person in persons:
            days = acme.nameDaysSplitter(person)[1]
            daysList = acme.daysSplitter(days)
            for day in daysList:    
                times = acme.dayNameTimesSplitter(day)[1]
                startHour, finishHour = acme.hoursSplitter(times)
                self.assertIn(startHour, constants.feesRegular)
                self.assertIn(finishHour, constants.feesRegular)


if __name__ == '__main__':
    unittest.main()