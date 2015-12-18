import time

class Person:

  def __init__(self, ident, name, last_date):
    self.ident     = ident
    self.name      = name
    self.last_date = last_date

  def __repr__(self):
    date_str = time.strftime("%m/%d/%Y", self.last_date)
    return "{0},{1},{2}".format(self.ident, self.name, date_str)

class Planner:

  def __init__(self, filename):
    self.filename = filename

  def load_recent_date(self):
    with open(self.filename) as f:
      lines = f.readlines()
    data = lines[1:len(lines)]
    people = map(self._csv_line_to_person, data)
    print(people)

  # private methods

  def _csv_line_to_person(self, data):
    parts = data.rstrip().split(StringUtils.COMMA)
    ident = int(parts[0])
    name  = parts[1]
    date  = time.strptime(parts[2], "%m/%d/%Y")
    return Person(ident, name, date)

class StringUtils:
  COMMA = ","

if __name__ == "__main__":
  planner = Planner("./recent_data.csv")
  planner.load_recent_date()
