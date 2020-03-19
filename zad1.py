import common
import median_min_max
import dominant
import correlation
import histogram

flowers = common.read_data_from_file()
median_min_max.execute(flowers)
dominant.execute(list(map(lambda f: f.flower_type, flowers)))
corr = correlation.execute(flowers)
histogram.execute(corr, flowers)
