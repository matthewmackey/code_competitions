#!/usr/bin/env python3

def LOG(msg):
  print(msg)

# Basic roll-your-own Logger
class AdventLogger:
  def __init__(self, level):
    self.level = level

  def log(self, msg, level="DEBUG"):
    LOG_LEVEL = self.level

    if LOG_LEVEL == "ERROR":
      if level == "ERROR":
        print(msg)

    if LOG_LEVEL == "WARN":
      if level == "ERROR" or level == "WARN":
        print(msg)

    if LOG_LEVEL == "INFO":
      if level == "ERROR" or level == "WARN" or level == "INFO":
        print(msg)

    if LOG_LEVEL == "DEBUG":
      if level == "ERROR" or level == "WARN" or level == "INFO" or level == "DEBUG":
        print(msg)

#-------------------------------------------------------------------------------
# Input File Parser:
#
# Parses over entire input file to convert the lines of input into "advent
# objects", where X number of input lines correspond to an object depending
# on the specifics of the daily challenge.
#-------------------------------------------------------------------------------
class AdventInputFileParser:

  ONE_LINE_PER_OBJ = 1000
  MULTI_LINE_PER_OBJ = 2000

  def __init__(self, line_parser, delimiter_type):
    self.delimiter_type = delimiter_type
    self.line_parser = line_parser

  def parse_file(self, input_file):
    parsed_objects = []

    with open(input_file) as input:

      if self.delimiter_type == self.ONE_LINE_PER_OBJ:
        for line in input:
          parsed_objects.append(self.line_parser.parse_line(line))

      elif self.delimiter_type == self.MULTI_LINE_PER_OBJ:
        line_data = ""
        for line in input:
          if line != "\n":
            line_data += line
          else:
            parsed_objects.append(self.line_parser.parse_line(line_data))
            line_data = ""
        parsed_objects.append(self.line_parser.parse_line(line_data))

    return parsed_objects

#-------------------------------------------------------------------------------
# Input Line Parser:
#
# A superclass whose parse_line() method is meant to parse one or more lines
# from a daily input file that represent a single "object", and then translate
# that into some sort of value that is being counted for that daily challenge.
#-------------------------------------------------------------------------------
class AdventLineParser:

  # @ToOverride
  # RETURN: should return the "value" for that day's line object
  def parse_line(self, line):
    LOG(f"IN AdventLineParser.parse_line() -> should have been OVERRIDDEN")

#-------------------------------------------------------------------------------
# Parsed Line Summarizer:
#
# A class used to get a final total count for the daily statistic from the
# parsed lines. This class provides a default implementation that seems to
# suffice for many days but can be extended for more advanced calculations.
#-------------------------------------------------------------------------------
class AdventParsedLineSummarizer:
  # @OptionallyOverride
  # This is a default implementation that does a basic sum
  def get_total(self, parsed_objects):
    return sum(parsed_objects)

