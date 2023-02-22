import openai
openai.api_key = ''
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="#convert this java code to flask python: \n@RestController \npublic class HelloController {\n@RequestMapping('\/hello'\)\npublic String hello(){ \nreturn '\Hello World'\;\n}\n}",
  temperature=0,
  max_tokens=68,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)