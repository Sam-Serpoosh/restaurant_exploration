class Person:

  def __init__(self, ident, name, last_date):
    self.ident     = ident
    self.name      = name
    self.last_date = last_date

  def date_str(self):
    return self.last_date.strftime("%m/%d/%Y")

  def __eq__(self, other):
    return self.last_date == other.last_date

  def __lt__(self, other):
    return self.last_date < other.last_date

  def __gt__(self, other):
    return self.last_date > other.last_date

  def __repr__(self):
    return "{0},{1},{2}".format(self.ident, self.name, self.date_str())
