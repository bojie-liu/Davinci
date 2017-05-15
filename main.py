
import io.input
import core
import config
import Davinci.utils.log

if __name__ == "__main__":
	log = Davinci.utils.log.get_logger('root')
	training_set = io.input.read(r'E:\test.csv')
	model = core.train_model(training_set)

	test_set = io.input.read(r'E:\test.csv')
	result = core.predict(model, test_set)
	#io.plot(result)

	log.info(config.use_spark)
