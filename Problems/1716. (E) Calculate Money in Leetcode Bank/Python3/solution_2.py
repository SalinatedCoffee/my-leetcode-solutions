class Solution:
  def totalMoney(self, n: int) -> int:
    # math

    f_weeks = n // 7
    f_weeks_tot = (f_weeks * (f_weeks+1) // 2 * 7) + (f_weeks * 21)
    r_days = n % 7
    r_days_tot = r_days * (f_weeks) + r_days * (r_days+1) // 2

    return f_weeks_tot + r_days_tot

