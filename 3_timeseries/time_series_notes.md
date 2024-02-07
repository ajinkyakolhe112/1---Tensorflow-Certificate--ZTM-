What time series data `is` & `is not`
1. `is not`: Data captured at time intervals
2. `is`:     Data value dependent (directly or indirectly or related to) on the time

Consider following data
1. Electricity usage according to time
2. Share prize according to time
3. Heart rate according to time
4. Global temperature according to time

Share prize according to time
1. is this calculatable?

Terms
1. Nature of time series
   1. Trend
   2. Seasonality
   3. Auto-correlation -> future value depends on lagged & dampened value of past.
      1. TERM explaining meaning: lagged & dampened value of past. (auto correlation word doesn't explain its meaning. meaning should be encapsulated in term where we can identify it's meaning)
      2. (Random spikes) with (dampening attenuation)
      3. correlated with delayed & decayed copy of itself / lag
      4. Correlation vs. Autocorrelation -> Correlation measures the relationship between two variables, whereas autocorrelation measures the relationship of a variable with lagged values of itself.
   4. auto regression -> past values to predict future value
Think of
1. trend without seasonality
2. trend with seasonaility
3. seasonality without auto-correlation
4. seasonality with auto-correlation