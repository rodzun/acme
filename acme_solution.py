from datetime import datetime
from time import time
import constants

class ACME:
    
    def nameDaysSplitter(self, personData: str) -> str:
        nameTime = personData.split('=')
        name = nameTime[0]
        days = nameTime[1]
        return name, days

    def daysSplitter(self, days: str) -> str:
        daysSplitted = days.split(',')
        return daysSplitted

    def dayNameTimesSplitter(self, dayTime: str) -> str:
        dayName = dayTime[0:2]
        hours = dayTime[2:]
        return dayName, hours

    def hoursSplitter(self, hours: str) -> int:
        formatString = "%H:%M"
        hoursSplitted = hours.split('-')
        startHour = datetime.strptime(hoursSplitted[0], formatString).time().hour    
        finishHour = datetime.strptime(hoursSplitted[1], formatString).time().hour 
        return startHour, finishHour

    def personPayment(self, personData: str):
        payment = 0
        name, days = self.nameDaysSplitter(personData)
        daysSplitted = self.daysSplitter(days)

        for day in daysSplitted:
            isRegularDay = False
            dayName, hours = self.dayNameTimesSplitter(day)
            startHour, finishHour = self.hoursSplitter(hours)

            if dayName in constants.regularDays:    
                isRegularDay = True

            if finishHour == 0:
                finishHour = 24

            for hour in range(startHour,finishHour):
                payment += (constants.feesRegular if isRegularDay else constants.feesWeekends)[hour]

        return f'The amount to pay {name} is: {payment} USD'

    def totalPayments(self, data):
        for person in data:
            print(self.personPayment(person))
            
            

def main():
    acme = ACME()
    with open('data.txt', 'r') as f:
        persons = f.read().splitlines()
        acme.totalPayments(persons)
        

if __name__ == "__main__":
    main()