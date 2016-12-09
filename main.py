
import io.input
import core
import config
from utils import log

if __name__ == "__main__":
	training_set = io.input.read(r'E:\test.csv')
	model = core.train_model(training_set)

	test_set = io.input.read(r'E:\test.csv')
	result = core.predict(model, test_set)
	#io.plot(result)

	print result
	log.e(config.use_spark)
