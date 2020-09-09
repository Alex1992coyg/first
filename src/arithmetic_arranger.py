def arithmetic_arranger(problems, answer= False):

  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    arranged_problems= []
    top_space        = ""
    end_space        = ""
    body_space       = ""
    dashes           = ""

  # Looping
    for i, problem in enumerate(problems):
      n       = problem.split()
      num1    = n[0]
      operand = n[1]
      num2    = n[2]
#first conditions
      if operand not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'."
      else:
        for digit in num1:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error:  Numbers must only contain digits."
          else:
            continue

        for digit in num2:
          if digit not in ["0","1","2","3","4","5","6","7","8","9"]:
            return "Error: Numbers must only contain digits."
          else:
            continue
        if len(num1) > 4 or len(num2) > 4:
          return 'Error: Numbers cannot be more than four digits.'
        else:
          if operand == "+":
            cal = int(num1) + int(num2)
          else:
            cal = int(num1) - int(num2)

          length     = max(len(num1), len(num2))   + 2
          top_space  = top_space    + str(num1.rjust(length))
          body_space = body_space   +  str(operand + num2.rjust(length-1))
          dashes     = dashes       + str("-" * length)
          end_space  = end_space    + str(cal).rjust(length)
    # Adding to the result
          if i < len(problems)-1:
            top_space  = top_space  + "    "
            body_space = body_space + "    "
            dashes     = dashes     + "    "
            end_space  = end_space  +  "    "

          if answer == True:
            arranged_problems = (top_space + "\n" + body_space + "\n" + dashes + "\n" + end_space)
          else:
            arranged_problems = (top_space + "\n" + body_space + "\n" + dashes)


    return arranged_problems
