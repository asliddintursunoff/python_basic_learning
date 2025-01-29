import unittest
def multiply(num):
    if (num != None):
        try:
            return  int(num)*5
        except ValueError as err:
            return err
    else:
        return "enter true number"

if __name__ == '__main__':
    unittest.main()
