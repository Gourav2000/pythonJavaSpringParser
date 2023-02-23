from find_classes_and_interfaces import zip_to_result
import os
import json
import openai

def generateResponse(classes_interfaces):
  openai.api_key = ''
  # response = openai.Completion.create(
  #   model="text-davinci-003",
  #   prompt="#convert this java code to flask python: \n@RestController \npublic class HelloController {\n@RequestMapping('\/hello'\)\npublic String hello(){ \nreturn '\Hello World'\;\n}\n}",
  #   temperature=0,
  #   max_tokens=68,
  #   top_p=1.0,
  #   frequency_penalty=0.0,
  #   presence_penalty=0.0
  # )
  res={}
  for i in classes_interfaces:
    res[i]={}
    for j in classes_interfaces[i]:
      cmd=""
      if i=='controllers':
         cmd="convert this java code to flask python :"
      elif i=="entities":
         cmd="convert this to python class :"
      elif i=="repositories":
         cmd= "convert this to python using sqlAlchemy :"
      elif i=="services":
         cmd= "convert this to python code :"
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{cmd} {classes_interfaces[i][j]}",
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
      )
      res[i][j]=response.choices[0].text          
  return res


if __name__=='__main__':
    classes_interfaces=zip_to_result(os.path.join(os.path.dirname(__file__),'Sample.zip'))
    print(json.dumps(generateResponse(classes_interfaces)))

