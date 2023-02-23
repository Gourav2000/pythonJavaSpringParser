from find_classes_and_interfaces import zip_to_result
import os
import openai

def generateResponse(classes_interfaces):
  openai.api_key = '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'
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt='''convert this java code to python flask app: public class TransactionController {

        private ITransactionService transactionService;
        private IUserService userService;
        private IWealthService wealthService;

        @Autowired
        public TransactionController(ITransactionService transactionService, IUserService userService, IWealthService wealthService) {
                this.transactionService = transactionService;
                this.userService = userService;
                this.wealthService = wealthService;
        }

        @PostMapping("/create")
        public CreateTransactionResponse createTransaction(@RequestBody CreateTransactionRequest request) {

                if (request.getUsername() == null || request.getUsername().equals("")) {
                        throw new BadRequestException(Constants.MESSAGE_INVALIDUSERNAME);
                } else if (request.getCurrency() == null || request.getCurrency().equals("")) {
                        throw new BadRequestException(Constants.MESSAGE_INVALIDCURRENCY);
                } else if (request.getAmount() == null || request.getAmount().signum() == 0 || request.getAmount().signum() == -1) {
                        throw new BadRequestException(Constants.MESSAGE_INVALIDAMOUNT);
                } else if (request.getCurrency().equals(Constants.MAIN_CURRENCY)) {
                        throw new BadRequestException(Constants.MESSAGE_EXCHANGESWITHMAINCURRENCY);
                }

                User user = userService.findByUserName(request.getUsername());

                int last24HoursOperationCount = transactionService.getOperationCountFromLast24Hours(user.getId());
                if (last24HoursOperationCount >= 10) {
                        throw new DailyOperationLimitReachedException();
                }

                wealthService.makeWealthExchange(user.getId(), request.getCurrency(), request.getAmount(), request.isBuying());
                Transaction transaction = transactionService.createNewTransaction(user.getId(), request.isBuying(), request.getCurrency(), request.getAmount());

                CreateTransactionResponse response = new CreateTransactionResponse();
                response.setTransaction(transaction);
                return response;
        }

        @PostMapping("/find/all")
        public FindAllTransactionsByUserResponse findAll(@RequestBody FindAllTransactionsByUserRequest request) {

                if (request.getUsername() == null || request.getUsername().equals("")) {
                        throw new BadRequestException(Constants.MESSAGE_INVALIDUSERNAME);
                }

                User user = userService.findByUserName(request.getUsername());
                List<Transaction> transactionList = transactionService.findAllByUserId(user.getId());

                FindAllTransactionsByUserResponse response = new FindAllTransactionsByUserResponse();
                response.setTransactionList(transactionList);
                return response;
        }

}''',
    temperature=0,
    max_tokens=68,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  print(response)
  # res={}
  # for i in classes_interfaces:
  #   res[i]={}
  #   for j in classes_interfaces[i]:
  #     response = openai.Completion.create(
  #       model="text-davinci-003",
  #       prompt=f"convert this java code to flask python: {classes_interfaces[i][j]}",
  #       temperature=0,
  #       max_tokens=68,
  #       top_p=1.0,
  #       frequency_penalty=0.0,
  #       presence_penalty=0.0
  #     )
  #     res[i][j]=response.choices[0].text          
  # return res


if __name__=='__main__':
    classes_interfaces=zip_to_result(os.path.join(os.path.dirname(__file__),'Spring-Boot-Sample-Project.zip'))
    generateResponse(classes_interfaces)
    # print(json.loads(generateResponse(classes_interfaces)))

