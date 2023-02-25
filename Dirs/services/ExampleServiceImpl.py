
class ExampleServiceImpl:
    def __init__(self, exampleRepository):
        self.exampleRepository = exampleRepository

    def getAllExamples(self):
        return self.exampleRepository.findAll()

    def saveExample(self, example):
        return self.exampleRepository.save(example)