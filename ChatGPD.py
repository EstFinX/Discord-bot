def ChatGPD1(Запрос1):
  import g4f

  text = Запрос1

  response = g4f.ChatCompletion.create(
              model=g4f.models.gpt_4,
              provider=g4f.Provider.Bing,
              messages=[{"role": "user", "content": f"{text}"}],
          )
          
  print(response)