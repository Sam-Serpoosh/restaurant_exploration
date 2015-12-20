import datetime
from texter import Texter
from person import Person
from string_utils import StringUtils
from csv_writer import CsvWriter

class Planner:

  DAYS_PER_WEEK     = 7
  RECENT_CSV_HEADER = "id,name,date"

  def __init__(self, filename):
    self.filename = filename

  def who_is_next(self):
    people      = self._load_recent_dates()
    last_person = max(people)
    next_person = self._find_next_person(last_person.ident, people)
    next_person.last_date = self._weeks_later(last_person.last_date, 2)

    return (next_person, people)

  # private methods

  def _load_recent_dates(self):
    with open(self.filename) as f:
      lines = f.readlines()
    data = lines[1:len(lines)]
    people = map(self._csv_line_to_person, data)

    return people

  def _csv_line_to_person(self, data):
    parts = data.rstrip().split(StringUtils.COMMA)
    ident = int(parts[0])
    name  = parts[1]
    date  = datetime.datetime.strptime(parts[2], "%m/%d/%Y")
    return Person(ident, name, date)

  def _find_next_person(self, ident, people):
    if (ident == len(people)): return people[0]
    person = next(p for p in people if p.ident == ident + 1)
    return person

  def _weeks_later(self, date, num_of_weeks):
    days_count = num_of_weeks * Planner.DAYS_PER_WEEK
    return date + datetime.timedelta(days=days_count)

if __name__ == "__main__":
  filename   = "./recent_data.csv"
  planner    = Planner(filename)
  csv_writer = CsvWriter()
  texter     = Texter()

  next_person, people = planner.who_is_next()
  csv_writer.write(filename, Planner.RECENT_CSV_HEADER, people)
  #texter.text(next_person)
