import unittest
from datetime import datetime
from pack_web_static import do_pack


class DoPackTestCase(unittest.TestCase):
    def test_output_format(self):
        # Get the current datetime
        d_time = datetime.now()

        # Format the expected output string
        formatted_month = "{:02d}".format(d_time.month)
        formatted_day = "{:02d}".format(d_time.day)
        formatted_hour = "{:02d}".format(d_time.hour)
        formatted_minute = "{:02d}".format(d_time.minute)
        formatted_second = "{:02d}".format(d_time.second)
        expected_output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            d_time.year,
            formatted_month,
            formatted_day,
            formatted_hour,
            formatted_minute,
            formatted_second
        )

        # Call the do_pack function and get the actual output
        actual_output = do_pack()

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

