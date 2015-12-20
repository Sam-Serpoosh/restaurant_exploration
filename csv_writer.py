class CsvWriter:

  def write(self, filename, header, data):
    with open(filename, "w") as f:
      f.write("{0}\n".format(header))
      for d in data:
        f.write("{0}\n".format(str(d)))
